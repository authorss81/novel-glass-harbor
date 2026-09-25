#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
mkdir -p logs

PRIMARY="${NOVEL_MODEL:-opencode/space-bunny-free}"
FALLBACKS="${NOVEL_FALLBACK_MODELS:-opencode/muse-spark-1.3-contributor-free,opencode/muse-spark-1.2-contributor-free,opencode/nemotron-3-ultra-free,opencode/nemotron-3.5-lightning-free,opencode/mimo-v2.6-flash-free,opencode/ling-3.0-flash-fin-free}"
MAX_MODELS="${MAX_MODELS:-3}"
MAX_ATTEMPTS="${MAX_ATTEMPTS:-3}"
PLANNING_TIMEOUT_SECONDS="${PLANNING_TIMEOUT_SECONDS:-2700}"
BATCH_TIMEOUT_SECONDS="${BATCH_TIMEOUT_SECONDS:-7200}"
REVIEW_TIMEOUT_SECONDS="${REVIEW_TIMEOUT_SECONDS:-900}"
FIX_TIMEOUT_SECONDS="${FIX_TIMEOUT_SECONDS:-3600}"
CHECKPOINT_INTERVAL_SECONDS="${CHECKPOINT_INTERVAL_SECONDS:-300}"
LEASE_SECONDS="${LEASE_SECONDS:-14400}"
RETRY_DELAY_SECONDS="${RETRY_DELAY_SECONDS:-1800}"
LEDGER_FILE="${NOVEL_LEDGER_FILE:-state/phase-ledger.json}"
SELECT_ONLY="${NOVEL_SELECT_ONLY:-0}"
export LEASE_SECONDS RETRY_DELAY_SECONDS

phase_field() {
  local phase_id="$1"
  local field="$2"
  python3 - "$LEDGER_FILE" "$phase_id" "$field" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    data = json.load(handle)
for phase in data.get("phases", []):
    if phase.get("id") == sys.argv[2]:
        value = phase.get(sys.argv[3])
        if value is not None:
            print(value)
        break
PY
}

phase_attempts() {
  local phase_id="$1"
  python3 - "$LEDGER_FILE" "$phase_id" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    data = json.load(handle)
for phase in data.get("phases", []):
    if phase.get("id") == sys.argv[2]:
        print(int(phase.get("attempts") or 0))
        break
PY
}

next_phase_id() {
  python3 - "$LEDGER_FILE" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    data = json.load(handle)
for phase in data.get("phases", []):
    if phase.get("status") == "done":
        continue
    if phase.get("status") == "planned":
        print(phase.get("id", ""))
    break
PY
}

ledger_update() {
  local action="$1"
  local phase_id="$2"
  local model="${3:-}"
  local fallback_used="${4:-false}"
  local reason="${5:-}"
  local result_commit="${6:-}"

  python3 - "$LEDGER_FILE" "$action" "$phase_id" "$model" "$fallback_used" "$reason" "$result_commit" <<'PY'
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone

path, action, phase_id, model, fallback_used, reason, result_commit = sys.argv[1:]
with open(path, encoding="utf-8") as handle:
    data = json.load(handle)

phase = next((item for item in data.get("phases", []) if item.get("id") == phase_id), None)
if phase is None:
    raise SystemExit(f"Phase not found in ledger: {phase_id}")

now = datetime.now(timezone.utc)
if action == "claim":
    status = phase.get("status")
    lease = phase.get("leaseExpiry")
    lease_expired = True
    if lease:
        try:
            lease_expired = datetime.fromisoformat(lease.replace("Z", "+00:00")) <= now
        except ValueError:
            lease_expired = True
    if status not in {"planned", "deferred"} and not (status == "running" and lease_expired):
        raise SystemExit(f"Phase is no longer claimable: {phase_id} ({status})")
    phase["attempts"] = int(phase.get("attempts") or 0) + 1
    phase["status"] = "running"
    phase["baseCommit"] = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    phase["leaseExpiry"] = (now + timedelta(seconds=int(os.environ.get("LEASE_SECONDS", "1800")))).isoformat().replace("+00:00", "Z")
    phase["actualModel"] = None
    phase["fallbackUsed"] = False
    phase["nextRetryTime"] = None
    phase["lastError"] = None
    data["currentPhase"] = phase_id
elif action == "metadata":
    phase["actualModel"] = model or None
    phase["fallbackUsed"] = fallback_used.lower() == "true"
elif action == "defer":
    phase["status"] = "deferred"
    phase["leaseExpiry"] = None
    phase["nextRetryTime"] = (now + timedelta(minutes=max(1, int(os.environ.get("RETRY_DELAY_SECONDS", "1800")) // 60))).isoformat().replace("+00:00", "Z")
    phase["lastError"] = reason or "deferred"
    data["currentPhase"] = phase_id
elif action == "block":
    phase["status"] = "blocked"
    phase["leaseExpiry"] = None
    phase["nextRetryTime"] = None
    phase["lastError"] = reason or "blocked"
elif action == "done":
    phase["status"] = "done"
    phase["leaseExpiry"] = None
    phase["nextRetryTime"] = None
    phase["resultCommit"] = result_commit or None
    phase["lastError"] = None
    remaining = [item for item in data.get("phases", []) if item.get("status") == "planned"]
    data["currentPhase"] = remaining[0].get("id") if remaining else None
else:
    raise SystemExit(f"Unknown ledger action: {action}")

tmp = f"{path}.tmp"
with open(tmp, "w", encoding="utf-8") as handle:
    json.dump(data, handle, indent=2)
    handle.write("\n")
os.replace(tmp, path)
PY
}

select_phase() {
  python3 - "$LEDGER_FILE" "$MAX_ATTEMPTS" <<'PY'
import json
import sys
from datetime import datetime, timezone

path, max_attempts_text = sys.argv[1:]
max_attempts = int(max_attempts_text)
now = datetime.now(timezone.utc)
with open(path, encoding="utf-8") as handle:
    data = json.load(handle)

for phase in data.get("phases", []):
    status = phase.get("status")
    if status == "blocked":
        # A blocked predecessor halts all later work until a controller resolves it.
        raise SystemExit(0)
    if status not in {"planned", "deferred", "running"}:
        continue
    timestamp = phase.get("nextRetryTime" if status == "deferred" else "leaseExpiry")
    ready_at = None
    if timestamp:
        try:
            ready_at = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except ValueError:
            ready_at = datetime.min.replace(tzinfo=timezone.utc)
    if ready_at is not None and ready_at > now:
        # Phases are sequential. A waiting current phase blocks later planned work.
        raise SystemExit(0)
    action = "BLOCK" if int(phase.get("attempts") or 0) >= max_attempts else "RUN"
    prompt = phase.get("prompt")
    if not prompt:
        raise SystemExit(f"Ledgered phase has no prompt path: {phase.get('id')}")
    print("\t".join((action, phase.get("id", ""), prompt)))
    break
else:
    raise SystemExit(0)
PY
}

if [ -z "${OPENCODE_API_KEY:-}" ] && [ "$SELECT_ONLY" != "1" ]; then
  echo "OPENCODE_API_KEY is missing" >&2
  exit 2
fi

selection="$(select_phase)"
if [ -z "$selection" ]; then
  echo "No ready incomplete phase found"
  exit 0
fi

IFS=$'\t' read -r selection_action phase_id prompt_rel <<< "$selection"
phase_dir="$(dirname "$prompt_rel")"
prompt_file="$prompt_rel"
if [ ! -f "$prompt_file" ]; then
  echo "Ledgered prompt is missing: $prompt_file" >&2
  exit 1
fi

if [ "$SELECT_ONLY" = "1" ]; then
  printf '%s\t%s\t%s\n' "$selection_action" "$phase_id" "$prompt_rel"
  exit 0
fi

if [ -f "$phase_dir/.done" ] || [ -f "$phase_dir/.blocked" ]; then
  echo "Ledger/marker conflict for $phase_id; refusing duplicate execution" >&2
  exit 1
fi

log_file="logs/${phase_id}.log"
review_log="logs/${phase_id}.review.log"
review_after_fix_log="logs/${phase_id}.review-after-fix.log"
fix_log="logs/${phase_id}.fix.log"
wip_branch="novel-wip/${phase_id}"
checkpoint_pid=""

case "$(phase_field "$phase_id" kind)" in
  planning) phase_timeout="$PLANNING_TIMEOUT_SECONDS" ;;
  *) phase_timeout="$BATCH_TIMEOUT_SECONDS" ;;
esac

printf '%s\n' "Running $phase_id with timeout ${phase_timeout}s" | tee "$log_file"

start_checkpoint_loop() {
  checkpoint_loop &
  checkpoint_pid=$!
}

stop_checkpoint_loop() {
  if [ -n "$checkpoint_pid" ]; then
    kill "$checkpoint_pid" 2>/dev/null || true
    wait "$checkpoint_pid" 2>/dev/null || true
    checkpoint_pid=""
  fi
}

worktree_has_changes() {
  local status_line
  local changed_path
  while IFS= read -r status_line; do
    changed_path="${status_line:3}"
    case "$changed_path" in
      logs|logs/*) continue ;;
    esac
    return 0
  done < <(git status --porcelain --untracked-files=all 2>/dev/null)
  return 1
}

checkpoint_wip() {
  if ! worktree_has_changes; then
    return 0
  fi
  local tree commit base temp_index
  base="$(git rev-parse HEAD 2>/dev/null || echo HEAD)"
  temp_index="$(mktemp "${TMPDIR:-/tmp}/novel-phase-index.XXXXXX")" || return 1
  rm -f "$temp_index"
  if ! GIT_INDEX_FILE="$temp_index" git read-tree "$base" ||
     ! GIT_INDEX_FILE="$temp_index" git add -A ||
     ! tree="$(GIT_INDEX_FILE="$temp_index" git write-tree 2>/dev/null)" ||
     ! commit="$(git commit-tree "$tree" -p "$base" -m "novel: checkpoint $phase_id $(date -u +%s)" 2>/dev/null)"; then
    rm -f "$temp_index"
    return 1
  fi
  rm -f "$temp_index"
  if git push origin "$commit:refs/heads/$wip_branch" --force 2>/dev/null; then
    echo "Checkpoint pushed to $wip_branch"
    return 0
  fi
  echo "Checkpoint could not be pushed to $wip_branch"
  return 1
}

clear_checkpointed_worktree() {
  # This runs only after the writer/fixer process has stopped. The snapshot has
  # already been pushed, so restoring the active checkout cannot erase the only copy.
  if checkpoint_wip; then
    git reset --hard HEAD >/dev/null 2>&1 || true
    git clean -fd >/dev/null 2>&1 || true
    return 0
  fi
  return 1
}

checkpoint_loop() {
  while true; do
    sleep "$CHECKPOINT_INTERVAL_SECONDS"
    checkpoint_wip || true
  done
}

resume_wip() {
  if git ls-remote --exit-code origin "refs/heads/$wip_branch" >/dev/null 2>&1; then
    echo "Resuming checkpoint from $wip_branch"
    git fetch origin "$wip_branch" 2>/dev/null || true
    git merge --no-edit FETCH_HEAD
    touch "$phase_dir/.checkpoint"
    rm -f "$phase_dir/.deferred"
  fi
}

clear_wip() {
  git push origin --delete "$wip_branch" 2>/dev/null || true
  rm -f "$phase_dir/.checkpoint"
}

commit_changes() {
  local message="$1"
  git config user.name "novel-fleet-bot"
  git config user.email "novel-fleet-bot@users.noreply.github.com"
  git add -A
  if git diff --cached --quiet; then
    return 1
  fi
  git commit -m "$message"
  git push origin HEAD
  return 0
}

commit_controller_state() {
  local message="$1"
  local marker
  git config user.name "novel-fleet-bot"
  git config user.email "novel-fleet-bot@users.noreply.github.com"
  git add -- "$LEDGER_FILE"
  for marker in .checkpoint .deferred .blocked .done; do
    if [ -e "$phase_dir/$marker" ]; then
      git add -- "$phase_dir/$marker"
    fi
  done
  if git diff --cached --quiet; then
    return 1
  fi
  git commit -m "$message"
  git push origin HEAD
  return 0
}

defer_phase() {
  local reason="$1"
  stop_checkpoint_loop
  if ! clear_checkpointed_worktree; then
    echo "Could not persist WIP checkpoint; leaving $phase_id running for a later retry" >&2
    exit 1
  fi
  touch "$phase_dir/.checkpoint" "$phase_dir/.deferred"
  ledger_update defer "$phase_id" "" false "$reason"
  if ! commit_controller_state "novel: defer $phase_id"; then
    echo "Could not persist deferred phase state: $phase_id" >&2
    exit 1
  fi
  echo "Phase deferred: $phase_id ($reason)"
  exit 0
}

fail_work_phase() {
  local reason="$1"
  local attempts
  stop_checkpoint_loop
  if ! clear_checkpointed_worktree; then
    echo "Could not persist WIP checkpoint; leaving $phase_id running for a later retry" >&2
    exit 1
  fi
  attempts="$(phase_attempts "$phase_id")"
  if [ "$attempts" -ge "$MAX_ATTEMPTS" ]; then
    touch "$phase_dir/.blocked"
    ledger_update block "$phase_id" "" false "$reason"
    if ! commit_controller_state "novel: block $phase_id"; then
      echo "Could not persist blocked phase state: $phase_id" >&2
    fi
    echo "Phase blocked after $attempts attempts: $phase_id ($reason)" >&2
    exit 1
  fi
  touch "$phase_dir/.checkpoint" "$phase_dir/.deferred"
  ledger_update defer "$phase_id" "" false "$reason"
  if ! commit_controller_state "novel: defer $phase_id"; then
    echo "Could not persist deferred phase state: $phase_id" >&2
    exit 1
  fi
  echo "Phase deferred after $attempts attempts: $phase_id ($reason)"
  exit 0
}

review_status() {
  local log_path="$1"
  python3 - "$log_path" <<'PY'
import re
import sys

ansi = re.compile(r"\x1b\[[0-9;]*m")
status = ""
try:
    with open(sys.argv[1], encoding="utf-8", errors="replace") as handle:
        for line in handle:
            clean = ansi.sub("", line).strip()
            if clean in {"NOVEL_REVIEW_RESULT: PASS", "NOVEL_REVIEW_RESULT: FIX"}:
                status = clean
except FileNotFoundError:
    pass
print(status)
PY
}

if [ "$selection_action" = "BLOCK" ]; then
  touch "$phase_dir/.blocked"
  ledger_update block "$phase_id" "" false "maximum attempts reached"
  commit_changes "novel: block $phase_id" || true
  echo "Phase blocked after maximum attempts: $phase_id" >&2
  exit 1
fi

# Resume any pushed work before claiming the phase, then record the claim in the
# authoritative ledger. A second event sees status=running and cannot duplicate it.
resume_wip
ledger_update claim "$phase_id"
if ! commit_changes "novel: claim $phase_id"; then
  echo "Could not persist phase claim: $phase_id" >&2
  exit 1
fi

model_list=("$PRIMARY")
IFS=',' read -r -a fallback_list <<< "$FALLBACKS"
for model in "${fallback_list[@]}"; do
  [ -n "$model" ] && model_list+=("$model")
done
if [ "${#model_list[@]}" -gt "$MAX_MODELS" ]; then
  model_list=("${model_list[@]:0:$MAX_MODELS}")
fi

prompt_text="$(cat "$prompt_file")"
if [ -f "$phase_dir/.checkpoint" ]; then
  prompt_text="A checkpoint exists for this phase. Continue from the existing files and state. Do not restart completed work. $prompt_text"
fi

start_checkpoint_loop
writer_ok=false
writer_model=""
attempted=0
for model in "${model_list[@]}"; do
  attempted=$((attempted + 1))
  printf 'Trying writer model %s\n' "$model" | tee -a "$log_file"
  set +e
  timeout --signal=TERM --kill-after=30s "$phase_timeout" opencode run --model "$model" --agent novel-writer "$prompt_text" >>"$log_file" 2>&1
  code=$?
  set -e
  if [ "$code" -eq 0 ]; then
    printf 'Writer model used: %s\n' "$model" | tee -a "$log_file"
    writer_ok=true
    writer_model="$model"
    break
  fi
  if [ "$code" -eq 124 ] || [ "$code" -eq 143 ]; then
    defer_phase "writer timeout"
  fi
  if grep -qiE '429|rate limit|too many requests|quota|timeout|timed out|502|503|504|model not found|unavailable' "$log_file"; then
    printf 'Writer model unavailable or rate limited: %s\n' "$model" | tee -a "$log_file"
    if [ "$attempted" -ge "$MAX_MODELS" ]; then
      defer_phase "all writer models unavailable"
    fi
    continue
  fi
  fail_work_phase "writer work error"
done
stop_checkpoint_loop

if [ "$writer_ok" != true ]; then
  defer_phase "no writer model succeeded"
fi

fallback_used=false
if [ "$attempted" -gt 1 ]; then
  fallback_used=true
fi
if ! worktree_has_changes; then
  fail_work_phase "writer produced no file changes"
fi
ledger_update metadata "$phase_id" "$writer_model" "$fallback_used"
if ! commit_changes "novel: save writer work $phase_id"; then
  fail_work_phase "could not commit writer work"
fi
content_commit="$(git rev-parse HEAD)"

start_checkpoint_loop
set +e
timeout --signal=TERM --kill-after=20s "$REVIEW_TIMEOUT_SECONDS" opencode run --model "$PRIMARY" --agent novel-reviewer "Review the current phase changes. Do not edit files. Return concrete findings and finish promptly. End with exactly one status line: NOVEL_REVIEW_RESULT: PASS or NOVEL_REVIEW_RESULT: FIX." >"$review_log" 2>&1
review_code=$?
set -e
stop_checkpoint_loop

if [ "$review_code" -ne 0 ]; then
  fail_work_phase "reviewer failed or timed out"
fi
review_result="$(review_status "$review_log")"
if [ "$review_result" != "PASS" ] && [ "$review_result" != "FIX" ]; then
  fail_work_phase "reviewer returned no usable status"
fi

if [ "$review_result" = "FIX" ]; then
  start_checkpoint_loop
  set +e
  timeout --signal=TERM --kill-after=20s "$FIX_TIMEOUT_SECONDS" opencode run --model "$PRIMARY" --agent novel-writer "Read the reviewer findings in $review_log. Apply necessary fixes to the current phase and state files. Preserve good prose, do not restart the batch, and do not change the planned plot. Do not mark the current phase done or blocked." >"$fix_log" 2>&1
  fix_code=$?
  set -e
  stop_checkpoint_loop
  if [ "$fix_code" -ne 0 ]; then
    fail_work_phase "review fixer failed or timed out"
  fi
  if ! worktree_has_changes; then
    fail_work_phase "review fixer produced no file changes"
  fi
  ledger_update metadata "$phase_id" "$writer_model" "$fallback_used"
  if ! commit_changes "novel: save review fixes $phase_id"; then
    fail_work_phase "could not commit review fixes"
  fi
  content_commit="$(git rev-parse HEAD)"

  start_checkpoint_loop
  set +e
  timeout --signal=TERM --kill-after=20s "$REVIEW_TIMEOUT_SECONDS" opencode run --model "$PRIMARY" --agent novel-reviewer "Re-review the current phase after fixes. Verify that the prior findings in $review_log are resolved and report only remaining actionable findings. Do not edit files. End with exactly one status line: NOVEL_REVIEW_RESULT: PASS or NOVEL_REVIEW_RESULT: FIX." >"$review_after_fix_log" 2>&1
  re_review_code=$?
  set -e
  stop_checkpoint_loop
  if [ "$re_review_code" -ne 0 ] || [ "$(review_status "$review_after_fix_log")" != "PASS" ]; then
    fail_work_phase "post-fix review still has findings"
  fi
fi

# The controller alone changes the phase to done. The result commit points to
# the committed content that passed review; the following commit records closure.
ledger_update "done" "$phase_id" "" false "" "$content_commit"
touch "$phase_dir/.done"
rm -f "$phase_dir/.deferred" "$phase_dir/.blocked" "$phase_dir/.checkpoint"
if ! commit_changes "novel: complete $phase_id"; then
  echo "Completion marker produced no commit" >&2
  exit 1
fi
clear_wip

next_phase="$(next_phase_id)"
if [ -n "$next_phase" ] && [ -n "${GH_TOKEN:-}" ]; then
  gh api -X POST \
    -H "Accept: application/vnd.github+json" \
    "repos/${GITHUB_REPOSITORY}/dispatches" \
    -f event_type=novel_tick \
    -f "client_payload[phase]=${next_phase}" \
    -f "client_payload[completedPhase]=${phase_id}" \
    -f "client_payload[run_id]=${GITHUB_RUN_ID:-local}"
fi

echo "Completed $phase_id"
