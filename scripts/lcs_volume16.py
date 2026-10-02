#!/usr/bin/env python3
"""Script 1: longest common contiguous word run between all ordered pairs
of files in chapters/volume-16/.

Tokenization: whitespace split.
Method: binary search over run length k; a common run of length k exists
iff the sets of k-grams (joined token tuples) of the two files intersect.
This is monotone in k, so binary search is exact. At the maximal k we
intersect the k-gram sets to enumerate EVERY distinct run of that length.
"""

import os
from itertools import combinations

DIR = "/home/runner/work/novel-glass-harbor/novel-glass-harbor/chapters/volume-16"


def tokens(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read().split()


def gram_set(toks, k):
    if k <= 0 or len(toks) < k:
        return set()
    return {tuple(toks[i:i + k]) for i in range(len(toks) - k + 1)}


def grams_with_pos(toks, k):
    out = {}
    if k <= 0 or len(toks) < k:
        return out
    for i in range(len(toks) - k + 1):
        g = tuple(toks[i:i + k])
        if g not in out:
            out[g] = i
    return out


def max_common_run(ta, tb):
    """Return (best_k, sorted list of (run_tuple, pos_a, pos_b))."""
    hi_bound = min(len(ta), len(tb))
    if hi_bound == 0:
        return 0, []

    # quick check for any shared token at all
    if not (set(ta) & set(tb)):
        return 0, []

    lo, hi = 1, hi_bound          # invariant: exists(l o) is monotonic
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if gram_set(ta, mid) & gram_set(tb, mid):
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1

    k = best
    if k == 0:
        return 0, []
    ga, gb = grams_with_pos(ta, k), grams_with_pos(tb, k)
    runs = []
    for g in ga:
        if g in gb:
            runs.append((g, ga[g], gb[g]))
    runs.sort(key=lambda r: (-r[0].__len__(), r[1]))
    return k, runs


def main():
    files = sorted(f for f in os.listdir(DIR) if f.endswith(".md"))
    tok = {f: tokens(os.path.join(DIR, f)) for f in files}

    print("=" * 78)
    print("FILE WORD COUNTS (whitespace tokens)")
    print("=" * 78)
    for f in files:
        print(f"{f:20s} {len(tok[f]):6d}")

    print()
    print("=" * 78)
    print(f"ALL DISTINCT PAIRS OF FILES ({len(files)} files -> {len(files)*(len(files)-1)//2} unordered pairs)")
    print("format: pair | run_len_words | run_text")
    print("=" * 78)
    rows = []
    for a, b in combinations(files, 2):
        k, runs = max_common_run(tok[a], tok[b])
        # one row per distinct max-length run
        if k == 0:
            rows.append((0, a, b, ""))
        else:
            for g, _, _ in runs:
                rows.append((k, a, b, " ".join(g)))

    rows.sort(key=lambda r: (-r[0], r[1], r[2]))
    for length, a, b, run in rows:
        print(f"{a} <-> {b} | len={length} | \"{run}\"")

    # per-pair summary: only the single best run per pair
    print()
    print("=" * 78)
    print("PER-PAIR BEST RUN (one line per pair, 780 pairs)")
    print("=" * 78)
    best_per_pair = {}
    for length, a, b, run in rows:
        key = (a, b)
        if key not in best_per_pair:
            best_per_pair[key] = (length, run)
    for (a, b) in sorted(best_per_pair):
        length, run = best_per_pair[(a, b)]
        print(f"{a} <-> {b} | len={length} | \"{run}\"")

    print()
    print("=" * 78)
    print("TARGETED PAIRS (a)-(d)")
    print("=" * 78)
    for label, a, b in [
        ("(a)", "chapter-0793.md", "chapter-0800.md"),
        ("(b)", "chapter-0797.md", "chapter-0800.md"),
        ("(c)", "chapter-0791.md", "chapter-0800.md"),
    ]:
        k, runs = max_common_run(tok[a], tok[b])
        print(f"{label} {a} vs {b}: longest common run = {k} word(s)")
        print(f"    all distinct maximal runs ({len(runs)}):")
        for g, pa, pb in runs:
            print(f"      run text : \"{' '.join(g)}\"")
            print(f"      as list  : {list(g)}")
            print(f"      token idx: {a}@{pa}   {b}@{pb}")
            print(f"      context A: {' '.join(tok[a][max(0,pa-12):pa+k+12])}")
            print(f"      context B: {' '.join(tok[b][max(0,pb-12):pb+k+12])}")
            print()

    print("=" * 78)
    print("(d) GLOBAL MAXIMUM ACROSS ALL 40 FILES")
    print("=" * 78)
    top_len = rows[0][0]
    print(f"global max run length (words) = {top_len}")
    winners = [r for r in rows if r[0] == top_len]
    print(f"rows (pair,run) achieving global max = {len(winners)}")
    for length, a, b, run in winners:
        print(f"  {a} <-> {b} | len={length} | \"{run}\"")

    print()
    print("--- distribution of best-per-pair run lengths ---")
    hist = {}
    for (length, run) in best_per_pair.values():
        hist[length] = hist.get(length, 0) + 1
    for k in sorted(hist, reverse=True):
        print(f"  len {k:3d}: {hist[k]:5d} pairs")

    print()
    print("--- top 25 (pair, run) by length ---")
    for length, a, b, run in rows[:25]:
        print(f"  len={length:3d}  {a} <-> {b}  \"{run}\"")


if __name__ == "__main__":
    main()
