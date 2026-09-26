Read AGENTS.md, NOVEL_SPEC.md, the complete bible, `outline/series.md`, `outline/ending.md`, `outline/volume-01.md`, `outline/batches/volume-01-batch-0001.md`, all current state files, and this prompt. This is the first batch, so no previous chapters exist; use the bible, outlines, and rolling state as long-term memory.

## Where the chapters go

Create `chapters/volume-01/` if it does not exist and write one file per chapter, in order:

```text
chapters/volume-01/chapter-0001.md
chapters/volume-01/chapter-0002.md
...
chapters/volume-01/chapter-0010.md
```

Each file holds that chapter's prose only, with a `# Chapter N` heading. No batch notes, summaries, or status blocks go in a chapter file.

## What to write

Write Chapters 1–10 in order as complete, finished scenes. Follow every chapter card and preserve the batch goal, midpoint, climax, aftermath, and exact continuity facts. Each chapter must have a clear immediate goal, real resistance, a changed situation, an emotional or practical consequence, and a complete ending beat.

Calder remains an ordinary line diver whose first tide-ear attempt is physical, dangerous, limited, and costly; do not grant him instant mastery. Mara is an independent conservator whose expertise must affect events without becoming Calder's assistant. Do not introduce a new canon rule, a new final enemy, or a new institution.

**This world's bible forbids any game-style interface outright.** There are no panels, stat blocks, character sheets, status messages, floating text, quest text, skill trees, level-ups, or software vocabulary anywhere in the prose. This is unconditional for this novel and is not a matter of taste or degree: `bible/power-system.md`, `bible/premise.md`, `bible/terminology.md`, `AGENTS.md`, and batch hard rule 1 all forbid it. The only message-like elements permitted are world-native physical things: claim seals, Registry notations, bell marks, written limits, gauge readings, and physical warnings. None of them may tell Calder what to do next. If you find yourself reaching for a system-like presentation, render the information as one of those physical things instead.

## If you run out of room

The batch targets roughly 25,000–29,000 words in a single run, and that is a guide rather than a quota. If you approach the output limit, **stop at a chapter boundary.** Never restart, rewrite, or re-emit a chapter you have already finished. Then:

1. Save every completed chapter file and the state files exactly as they stand.
2. Update `state/current.md` with the last chapter you actually finished.
3. In `state/chapter-summaries.md`, summarize only the completed chapters and record the next unfinished chapter number.
4. Note in the batch prompt directory that the batch is resumable, naming the first unfinished chapter, so the next run continues instead of starting over.

A shorter, complete batch of finished scenes is a success. A batch that restarts finished chapters is a failure.

## After the ten chapters

Update the rolling state: batch summary, chapter summaries, continuity, open threads, current state, and relevant character/world state. Keep summaries compact. Record the batch's actual events, not the plan's, and flag any conflict you had to resolve rather than resolving it silently.

Then create exactly one next phase:

- If Volume 01 has chapters after Chapter 10, create exactly one next batch directory under `workspace/volume-01/` with a detailed prompt for Chapters 11–20.
- If the volume is complete, create exactly one volume-close prompt.

Create nothing beyond that single next phase. Do not create speculative batch files, extra chapter cards, or parallel prompts.

## What you must not touch

Phase status, completion markers, and the queued phase list belong to the controller. Do not mark the current phase done, blocked, or running, and **do not edit `state/phase-ledger.json`** or any file under `scripts/`, `.github/workflows/`, or `.opencode/agent/`, and do not edit `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, or `opencode.json`.
