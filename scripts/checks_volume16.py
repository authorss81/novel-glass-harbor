#!/usr/bin/env python3
"""Script 2: style / lint checks on chapters/volume-16/.

Runs detailed per-check reporting on chapter-0800.md, then
corpus-wide aggregates across all 40 files.
"""

import os
import re
from collections import Counter

DIR = "/home/runner/work/novel-glass-harbor/novel-glass-harbor/chapters/volume-16"
TARGET = "chapter-0800.md"

SECOND_PERSON = ["you", "your", "yours", "yourself", "yourselves"]
FIRST_PERSON = ["i", "me", "my", "mine", "myself", "we", "us", "our", "ours", "ourselves"]

L23_PROHIBITED = [
    "stage", "prototype", "openhand", "anchor", "chorus", "fleet", "network",
    "committee", "singular", "keelwright", "tide-ear", "faultreader",
    "storm-reader", "cache", "chamber", "minister", "plate",
    "four feet", "twenty-two fathoms",
]

BOOK_STRUCTURE = [
    "in nine volumes", "two volumes", "volumes back", "an earlier volume",
    "this chapter", "this volume", "this book", "this series", "the sea below",
]

CURRENCY_SYMBOLS = list("$€£¥₹₽₩₪₺₴₦฿₫₦")


def load(name):
    with open(os.path.join(DIR, name), "r", encoding="utf-8") as fh:
        return fh.read()


def lines_of(text):
    return text.split("\n")


def is_quote_line(line):
    """A line containing at least one double-quote character."""
    return '"' in line


def occurrences(pattern, line):
    return [(m.start() + 1, m.group(0)) for m in re.finditer(pattern, line)]


def word_hits(words, line):
    """Whole-word, case-insensitive matches of any word in `words`."""
    pat = r"\b(?:%s)\b" % "|".join(re.escape(w) for w in words)
    return [(m.start() + 1, m.group(0)) for m in re.finditer(pat, line, re.IGNORECASE)]


def hr(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def main():
    files = sorted(f for f in os.listdir(DIR) if f.endswith(".md"))
    corpus = {f: load(f) for f in files}
    ll = {f: lines_of(corpus[f]) for f in files}

    # ------------------------------------------------------------------
    hr("SECTION 1 -- DETAIL PER-CHECK FOR %s" % TARGET)
    # ------------------------------------------------------------------
    t = TARGET
    tl = ll[t]

    print("file: %s   lines: %d   chars: %d" % (t, len(tl), len(corpus[t])))

    print()
    print("--- 1.1 question marks ---")
    qm = [(i, line.count("?"), line.strip()) for i, line in enumerate(tl, 1) if "?" in line]
    print("total '?' count: %d" % corpus[t].count("?"))
    print("lines containing '?': %d" % len(qm))
    for i, c, txt in qm:
        print("  L%-5d x%d  %s" % (i, c, txt))

    print()
    print("--- 1.2 second-person words (you/your/yours/yourself/yourselves), case-insensitive ---")
    sp_rows = []
    for i, line in enumerate(tl, 1):
        for col, w in word_hits(SECOND_PERSON, line):
            sp_rows.append((i, col, w, line.strip()))
    print("total: %d" % len(sp_rows))
    by_word = Counter(w.lower() for _, _, w, _ in sp_rows)
    print("breakdown: %s" % dict(sorted(by_word.items())))
    for i, col, w, txt in sp_rows:
        print("  L%-5d col%-4d %-8s | %s" % (i, col, w, txt))

    print()
    print("--- 1.3 first-person words: ALL lines vs OUTSIDE quotation lines ---")
    print("    (quotation line = a line containing at least one '\"')")
    fp_all, fp_out = [], []
    for i, line in enumerate(tl, 1):
        for col, w in word_hits(FIRST_PERSON, line):
            fp_all.append((i, col, w, line, is_quote_line(line)))
            if not is_quote_line(line):
                fp_out.append((i, col, w, line))
    print("total first-person occurrences (all lines): %d" % len(fp_all))
    print("  breakdown: %s" % dict(sorted(Counter(w.lower() for _, _, w, _ in fp_all).items())))
    print("quotation lines in file: %d of %d" % (sum(1 for l in tl if is_quote_line(l)), len(tl)))
    print("first-person occurrences OUTSIDE quotation lines: %d" % len(fp_out))
    print("  breakdown: %s" % dict(sorted(Counter(w.lower() for _, _, w, _ in fp_out).items())))
    print("first-person occurrences ON quotation lines: %d" % (len(fp_all) - len(fp_out)))
    print("  breakdown: %s" % dict(sorted(Counter(w.lower() for i, c, w, l, q in fp_all if q).items())))
    if fp_out:
        print("  OUTSIDE-quotation-line detail:")
        for i, col, w, txt in fp_out:
            print("    L%-5d col%-4d %-8s | %s" % (i, col, w, txt.strip()))
    else:
        print("  OUTSIDE-quotation-line detail: (none)")

    print()
    print("--- 1.4 'thank' / 'thanked' ---")
    tk = []
    pat = re.compile(r"\bthank\w*\b", re.IGNORECASE)
    for i, line in enumerate(tl, 1):
        for m in pat.finditer(line):
            tk.append((i, m.start() + 1, m.group(0), line.strip()))
    print("total: %d  breakdown: %s" % (len(tk), dict(Counter(x[2].lower() for x in tk))))
    for i, col, w, txt in tk:
        print("  L%-5d col%-4d %-8s | %s" % (i, col, w, txt))
    if not tk:
        print("  (no matches)")

    print()
    print("--- 1.5 L23 prohibited words, case-insensitive ---")
    tot = 0
    for w in L23_PROHIBITED:
        pat = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(w), re.IGNORECASE)
        hits = []
        for i, line in enumerate(tl, 1):
            for m in pat.finditer(line):
                hits.append((i, m.start() + 1, m.group(0), line.strip()))
        tot += len(hits)
        print()
        print("  [%s]  occurrences in %s: %d" % (w, t, len(hits)))
        for i, col, mm, txt in hits:
            print("    L%-5d col%-4d %-18s | %s" % (i, col, mm, txt))
        if not hits:
            print("    (none)")
    print()
    print("  TOTAL L23 prohibited-word occurrences in %s: %d" % (t, tot))

    print()
    print("--- 1.6 book-structure forms ---")
    for form in BOOK_STRUCTURE:
        pat = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(form), re.IGNORECASE)
        hits = []
        for i, line in enumerate(tl, 1):
            for m in pat.finditer(line):
                hits.append((i, m.start() + 1, m.group(0), line.strip()))
        print()
        print("  [%s]  occurrences: %d" % (form, len(hits)))
        for i, col, mm, txt in hits:
            print("    L%-5d col%-4d %-20s | %s" % (i, col, mm, txt))
        if not hits:
            print("    (none)")

    print()
    print("--- 1.7 four-digit years ---")
    yr = []
    for i, line in enumerate(tl, 1):
        for m in re.finditer(r"(?<!\d)\d{4}(?!\d)", line):
            yr.append((i, m.start() + 1, m.group(0), line.strip()))
    print("total: %d  distinct: %s" % (len(yr), sorted({x[2] for x in yr})))
    for i, col, mm, txt in yr:
        print("  L%-5d col%-4d %-6s | %s" % (i, col, mm, txt))
    if not yr:
        print("  (none)")

    print()
    print("--- 1.8 currency symbols / money in digits ---")
    cur = []
    for i, line in enumerate(tl, 1):
        for s in CURRENCY_SYMBOLS:
            if s in line:
                cur.append((i, s, line.strip()))
    money = []
    for i, line in enumerate(tl, 1):
        for m in re.finditer(r"[£$€¥]\s?[\d,]+|\b\d[\d,]*\.\d{2}\b", line):
            money.append((i, m.start() + 1, m.group(0), line.strip()))
    print("currency SYMBOL occurrences: %d" % len(cur))
    for i, s, txt in cur:
        print("  L%-5d [%s] | %s" % (i, s, txt))
    if not cur:
        print("  (none)")
    print("money-in-digits patterns ([symbol]N or N.NN): %d" % len(money))
    for i, col, mm, txt in money:
        print("  L%-5d col%-4d %-10s | %s" % (i, col, mm, txt))
    if not money:
        print("  (none)")
    print("note: prose money is spelled out (pence/marks/shillings), not digits.")

    print()
    print("--- 1.9 quote and bold character parity ---")
    print('  count of \'"\': %d   (even=%s)' % (corpus[t].count('"'), corpus[t].count('"') % 2 == 0))
    print("  count of '*': %d   (even=%s)" % (corpus[t].count("*"), corpus[t].count("*") % 2 == 0))
    print("  count of '**' occurrences: %d" % corpus[t].count("**"))
    print("  lines with odd number of '\"': %s" % [
        i for i, line in enumerate(tl, 1) if line.count('"') % 2 == 1])
    print("  lines with odd number of '*': %s" % [
        i for i, line in enumerate(tl, 1) if line.count("*") % 2 == 1])
    print("  total lines: %d" % len(tl))

    # ------------------------------------------------------------------
    hr("SECTION 2 -- CORPUS AGGREGATES, ALL %d FILES" % len(files))
    # ------------------------------------------------------------------

    print()
    print("--- 2.1 question marks per file ---")
    tot_q = 0
    for f in files:
        c = corpus[f].count("?")
        tot_q += c
        print("  %-20s %d" % (f, c))
    print("  %-20s %d" % ("TOTAL", tot_q))

    print()
    print("--- 2.2 second-person words per file (total / by word) ---")
    tot_sp = 0
    corpus_sp_by_word = Counter()
    for f in files:
        cnt = 0
        by = Counter()
        for i, line in enumerate(ll[f], 1):
            for col, w in word_hits(SECOND_PERSON, line):
                cnt += 1
                by[w.lower()] += 1
        tot_sp += cnt
        corpus_sp_by_word.update(by)
        print("  %-20s %4d   %s" % (f, cnt, dict(sorted(by.items()))))
    print("  %-20s %4d   %s" % ("TOTAL", tot_sp, dict(sorted(corpus_sp_by_word.items()))))

    print()
    print("--- 2.3 first-person words per file (all lines / outside quotation lines) ---")
    tot_fa, tot_fo = 0, 0
    corpus_fo_by_word = Counter()
    for f in files:
        a = o = 0
        byo = Counter()
        for i, line in enumerate(ll[f], 1):
            for col, w in word_hits(FIRST_PERSON, line):
                a += 1
                if not is_quote_line(line):
                    o += 1
                    byo[w.lower()] += 1
        tot_fa += a
        tot_fo += o
        corpus_fo_by_word.update(byo)
        print("  %-20s all=%4d  outside_quote_lines=%4d  %s" % (f, a, o, dict(sorted(byo.items()))))
    print("  %-20s all=%4d  outside_quote_lines=%4d  %s" % ("TOTAL", tot_fa, tot_fo, dict(sorted(corpus_fo_by_word.items()))))

    print()
    print("--- 2.4 'thank' / 'thanked' per file ---")
    tot_tk = 0
    corpus_tk_by_word = Counter()
    pat = re.compile(r"\bthank\w*\b", re.IGNORECASE)
    for f in files:
        hits = []
        for i, line in enumerate(ll[f], 1):
            for m in pat.finditer(line):
                hits.append((i, m.group(0), line.strip()))
        tot_tk += len(hits)
        corpus_tk_by_word.update(m.lower() for _, m, _ in hits)
        print("  %-20s %d" % (f, len(hits)))
        for i, m, txt in hits:
            print("      L%-5d %-8s | %s" % (i, m, txt))
    print("  %-20s %d   %s" % ("TOTAL", tot_tk, dict(sorted(corpus_tk_by_word.items()))))

    print()
    print("--- 2.5 L23 prohibited words across all 40 files (with line numbers) ---")
    grand = 0
    for w in L23_PROHIBITED:
        pat = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(w), re.IGNORECASE)
        hits = []
        for f in files:
            for i, line in enumerate(ll[f], 1):
                for m in pat.finditer(line):
                    hits.append((f, i, m.group(0), line.strip()))
        grand += len(hits)
        print()
        print("  [%s]  TOTAL occurrences: %d" % (w, len(hits)))
        for f, i, mm, txt in hits:
            print("    %-20s L%-5d %-18s | %s" % (f, i, mm, txt))
        if not hits:
            print("    (none)")
    print()
    print("  GRAND TOTAL L23 prohibited-word occurrences across all 40 files: %d" % grand)

    print()
    print("--- 2.6 book-structure forms across all 40 files ---")
    for form in BOOK_STRUCTURE:
        pat = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(form), re.IGNORECASE)
        hits = []
        for f in files:
            for i, line in enumerate(ll[f], 1):
                for m in pat.finditer(line):
                    hits.append((f, i, m.group(0), line.strip()))
        print()
        print("  [%s]  TOTAL occurrences: %d" % (form, len(hits)))
        for f, i, mm, txt in hits:
            print("    %-20s L%-5d %-20s | %s" % (f, i, mm, txt))
        if not hits:
            print("    (none)")

    print()
    print("--- 2.7 four-digit years per file ---")
    grand_y = 0
    all_years = Counter()
    for f in files:
        hits = []
        for i, line in enumerate(ll[f], 1):
            for m in re.finditer(r"(?<!\d)\d{4}(?!\d)", line):
                hits.append((i, m.start() + 1, m.group(0), line.strip()))
        grand_y += len(hits)
        all_years.update(m for _, _, m, _ in hits)
        print("  %-20s %d" % (f, len(hits)))
        for i, col, mm, txt in hits:
            print("      L%-5d col%-4d %-6s | %s" % (i, col, mm, txt))
    print("  %-20s %d" % ("TOTAL", grand_y))
    print("  distinct four-digit numbers seen: %s" % dict(sorted(all_years.items())))

    print()
    print("--- 2.8 currency symbols / money in digits per file ---")
    grand_c = 0
    for f in files:
        cur, money = [], []
        for i, line in enumerate(ll[f], 1):
            for s in CURRENCY_SYMBOLS:
                if s in line:
                    cur.append((i, s, line.strip()))
            for m in re.finditer(r"[£$€¥]\s?[\d,]+|\b\d[\d,]*\.\d{2}\b", line):
                money.append((i, m.start() + 1, m.group(0), line.strip()))
        grand_c += len(cur) + len(money)
        print("  %-20s symbols=%d  money_digits=%d" % (f, len(cur), len(money)))
        for i, s, txt in cur:
            print("      L%-5d [%s] | %s" % (i, s, txt))
        for i, col, mm, txt in money:
            print("      L%-5d col%-4d %-10s | %s" % (i, col, mm, txt))
    print("  %-20s symbols+money_digits=%d" % ("TOTAL", grand_c))

    print()
    print("--- 2.9 quote / bold parity per file ---")
    print("  %-20s %8s %8s %8s %8s  %s" % ("file", '"count', "even?", "*count", "even?", "odd-*-lines"))
    bad_q, bad_s = [], []
    for f in files:
        q = corpus[f].count('"')
        s = corpus[f].count("*")
        odd_s = [i for i, line in enumerate(ll[f], 1) if line.count("*") % 2 == 1]
        odd_q = [i for i, line in enumerate(ll[f], 1) if line.count('"') % 2 == 1]
        if q % 2: bad_q.append((f, odd_q))
        if s % 2: bad_s.append((f, odd_s))
        print("  %-20s %8d %8s %8d %8s  %s" % (
            f, q, q % 2 == 0, s, s % 2 == 0, odd_s if odd_s else "-"))
    print("  FILES WITH ODD '\"' COUNT: %s" % ([f for f, _ in bad_q] or "none"))
    for f, lines_ in bad_q:
        print("    %-20s odd lines: %s" % (f, lines_))
    print("  FILES WITH ODD '*' COUNT: %s" % ([f for f, _ in bad_s] or "none"))
    for f, lines_ in bad_s:
        print("    %-20s odd lines: %s" % (f, lines_))
    tot_q_ch = sum(corpus[f].count('"') for f in files)
    tot_s_ch = sum(corpus[f].count("*") for f in files)
    print("  corpus total '\"' = %d (even=%s)" % (tot_q_ch, tot_q_ch % 2 == 0))
    print("  corpus total '*' = %d (even=%s)" % (tot_s_ch, tot_s_ch % 2 == 0))


if __name__ == "__main__":
    main()
