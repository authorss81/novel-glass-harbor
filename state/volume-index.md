# State index — the volume-level map, and what a phase must actually read

Created 30 September 2026, in the repair pass over `logs/batch-0005.review.log`, because `PHASE_SYSTEM.md` § *State Growth* requires a volume-level index once the state files grow too large to load whole, and they no longer are loadable at a useful budget:

| File | Size | Shape |
|---|---|---|
| `state/continuity.md` | 3.79 MB, 10373 lines | newest section first, then every volume's batches, then the canon blocks |
| `state/chapter-summaries.md` | 1.85 MB, 3023 lines | newest batch first, then a per-batch index, then every batch in order |
| `state/current.md` | 1.75 MB, 3451 lines | newest phase entry first, then one entry per phase, oldest at the bottom |
| `state/open-threads.md` | 1.60 MB, 3769 lines | newest batch first, then every batch's threads, then the long-standing threads |

**THE RULE THAT FOLLOWS FROM THOSE FOUR NUMBERS IS THE ONLY THING THIS FILE IS FOR: A PHASE DOES NOT READ THESE FILES. A PHASE READS A SECTION OF ONE OF THEM, AND THIS FILE SAYS WHICH SECTION.**

## The active volume. Volume 11, *The Cordon*, Chapters 501 to 550, WRITTEN AND NOT YET CLOSED.

| What you need | File and lines | Note |
|---|---|---|
| **The state of the world you are writing into** | `state/continuity.md` **L1–183** — § *Volume 11, Batch 0005 (Chapters 541–550) as written* — **and L184–236, § *The repair pass over Volume 11, Batch 0005*, which is binding on the same ground** | the two binding sections. Between them they carry the calendar, the night, the five elements, the sheet re-derived, the leaf, the nine counters, the checks, the thirteen things a later phase may not do, and the disposition of every finding in `logs/batch-0005.review.log` |
| The volume's own thirty-seven locks | `outline/volume-11.md` L166–361 | L1–L37. **L2 is the leaf, L3 the bag, L4 the fitting-out sheet, L5 the figure of money, L37 the ending. L209 is the read-back derivation, not L37** |
| The volume's own plan | `outline/volume-11.md` L1–165 | central pressure, starting state, locations, factions, escalation, costs, prohibitions, jurisdiction, midpoint, climax, resolution, the new question, six named divergences |
| Movement 4, the hand-off you inherit | `state/continuity.md` L10224–10372 | Nessa Pike's yard, the choice of 8 January, the declared sea |
| Movement 4's threads | `state/open-threads.md` L3723–3769 | |
| Movement 4's summary | `state/chapter-summaries.md` L44–88 | |
| Movement 3 | `state/continuity.md` L435–662 (as written L435–596, its repair pass L597–662), `state/open-threads.md` L42–87, `state/chapter-summaries.md` L88–130 | the midpoint, the surrender of the buoys, the Chorus Diver stage taken once in Chapter 528 |
| Movement 2 | `state/continuity.md` L291–434 (as written L291–382, its repair pass L283–290), `state/open-threads.md` L87–130, `state/chapter-summaries.md` L130–184 | the proof, in the refusal at about ten to three on the twenty-first |
| Movement 1 | `state/continuity.md` L237–290 and L663–766 (as written L663–766, its repair pass L237–290), `state/open-threads.md` L130–181, `state/chapter-summaries.md` L184–244 | |
| The deep canon blocks | `state/continuity.md` L940–1031 | canon status, fixed opening facts, institutions, the artifact custody, the relationship lock, the power lock, the ending lock, the reveal lock, the batch 0001 locks. **Read this once. It has not changed in ten volumes** |
| The volume handoff you are about to write | `state/continuity.md` L768–939 | Volume 10, Batch 0005, the audited hand-over into Volume 11 |

## Closed volumes. Do not read these to write. Read the audit section of the last one and nothing else.

| Volume | Chapters | Where its audit and its rulings live | Rulings a later phase may not break |
|---|---|---|---|
| 01 | 1–50 | `state/continuity.md` L1504–1558 | close accounting L1504, rulings L1514 |
| 02 | 51–100 | `state/continuity.md` L2393–2498 | close L2393, rulings L2401 |
| 03 | 101–150 | `state/continuity.md` L3477–3624 | the fourteen rulings L3477, the forward rulings L3494, the eleven mechanical repairs L3501, the volume table L3523 |
| 04 | 151–200 | `state/continuity.md` L4649–4802 | the close and its rulings L4649, the close-phase repairs L4719 |
| 05 | 201–250 | `state/continuity.md` L6066–6142 | **the twenty-one author-level rulings L6066, which bind every later volume** |
| 06 | 251–300 | `state/continuity.md` L3146–6651 | per-batch repair sections; the third pass on Batch 0003 and the third pass on Batch 0005 are the last two of its six sections |
| 07 | 301–350 | `state/continuity.md` L7456–7511 | the close and its audit |
| 08 | 351–400 | `state/continuity.md` L8198–8385 | closed and audited |
| 09 | 401–450 | `state/continuity.md` L9391–9491 | closed and audited |
| 10 | 451–500 | `state/continuity.md` L768–939 | the audited hand-over into Volume 11 |

## The three files, and what each one is for

- **`state/current.md` is a log, not a brief.** Newest entry first, one entry per phase, and the entries grow to hundreds of lines. **Read L1–8 only.** If a figure you want is not in the first fourteen lines, it belongs in a continuity section and not in this file.
- **`state/continuity.md` is the state of the world.** Newest section first. Read the one section named at the top of the batch prompt, and the canon blocks once.
- **`state/open-threads.md` is what is owed.** Newest batch first, then every older batch's threads, and the long-standing threads from L377 onward. **Read the newest section, and L377–452 once for the threads that cross volumes.**
- **`state/chapter-summaries.md` is for the voice and for the figures of a batch.** Read the newest batch, or the per-batch index at L351, and not the other three thousand lines.

## What this index exists to stop

A phase that read all four files whole would spend most of a model context on Volumes 01 to 10, every one of which is closed, audited and ruled, and would arrive at the active volume with no budget left for the ten chapters it has to write. The repair pass over `logs/batch-0005.review.log` recorded that the previous phase wrote forty-three thousand and seven words for ten chapters and left roughly this much state behind, and that a large and growing share of a batch's output budget is being spent restating what earlier batches already said.

**THE FOUR FILES ARE NOT TRIMMED HERE, BECAUSE TRIMMING A STATE FILE IS AN AUTHOR-LEVEL DECISION AND NOT A REPAIR PASS'S. WHAT IS FIXED HERE IS THE ENTRY POINT: A PHASE THAT READS THIS FILE FIRST AND THEN ONE SECTION OF ONE STATE FILE HAS A BUDGET FOR ITS CHAPTERS.**
