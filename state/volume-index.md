# State index — the volume-level map, and what a phase must actually read

Created 30 September 2026, in the repair pass over `logs/batch-0005.review.log`, because `PHASE_SYSTEM.md` § *State Growth* requires a volume-level index once the state files grow too large to load whole, and they no longer are loadable at a useful budget:

| File | Size | Shape |
|---|---|---|
| `state/continuity.md` | 3.81 MB, 10,429 lines | newest section first, then every volume's batches, then the canon blocks |
| `state/chapter-summaries.md` | 1.85 MB, 3,063 lines | newest section first, then a per-batch index, then every batch in order |
| `state/current.md` | 1.75 MB, 3,458 lines | newest phase entry first, then one entry per phase, oldest at the bottom |
| `state/open-threads.md` | 1.61 MB, 3,806 lines | newest batch first, then every batch's threads, then the long-standing threads |

**THE RULE THAT FOLLOWS FROM THOSE FOUR NUMBERS IS THE ONLY THING THIS FILE IS FOR: A PHASE DOES NOT READ THESE FILES. A PHASE READS A SECTION OF ONE OF THEM, AND THIS FILE SAYS WHICH SECTION.**

## THE ACTIVE VOLUME. Volume 12, *The Single Voice*, Chapters 551 to 600. NOT YET WRITTEN. ITS OUTLINE IS ON DISK AND ITS FIRST BATCH IS QUEUED.

| What you need | File and lines | Note |
|---|---|---|
| **THE STATE OF THE WORLD YOU ARE WRITING INTO** | **`state/continuity.md` L1–57 — § *Volume 11 close and Volume 12 outline*, 30 September 2026. THIS IS THE ONE BINDING SECTION AND IT IS THE ONLY STATE SECTION A WRITER OF CHAPTERS 551 TO 560 NEEDS TO READ.** It carries the audit's counted figures, the one repair, the four items the repair pass left, the two departures, the whole starting state, and the length of the volume just closed | **Read this and nothing else in this file. It was written for exactly this phase** |
| **THE VOLUME'S OWN AUTHORITY** | **`outline/volume-12.md`, in full. Thirty-seven headed locks L1 to L37, the day table in L1, the four columns and their base and the Chapter 600 read-back in L2, the bag in L3, the fitting-out sheet and its base and its three dating forms in L4, the figure of money in L5, and its own eight numbered divergences** | **L2 is the leaf, L3 the bag, L4 the sheet, L5 the money, L37 the ending. L1 is the calendar and is printed in no other section of that file. The eight divergences at the end of the plan section govern, and item 3 is the one a writer is most likely to break without noticing: *orison* leaves the banned list for Volume 12 only** |
| **The volume that was just closed, and what the audit found** | `reviews/volume-11/volume-11-close.md`, in full, if you need the reasoning; **`state/continuity.md` L1–57 if you need the figures.** It is the authority on every decision Volume 11 deferred or flagged | **Do not read Chapters 501 to 550 to write Chapters 551 to 560. Read the audit's sections, not the chapters** |
| **The volume just closed, as it was written** | `state/continuity.md` L58–240 — § *Volume 11, Batch 0005 (Chapters 541–550) as written* — and L241–293 — § *The repair pass over Volume 11, Batch 0005* | **Read these two only if a chapter of 551 to 560 needs something the new section at L1 does not carry. The new section supersedes them for Volume 12 and the four earlier Volume 11 sections are superseded for every purpose except the record of what those ten chapters did** |
| Movement 4 of Volume 11, if a figure is wanted | `state/continuity.md` L10,281–10,429 — § *Volume 11, Batch 0004 (Chapters 531–540) as written* | the shipyard, the choice, the declared sea |
| Movement 3 of Volume 11, if a figure is wanted | `state/continuity.md` L493–720 — § *Volume 11, Batch 0003 (Chapters 521–530) as written* and its repair pass | the midpoint, the surrender of the buoys, the Chorus Diver stage taken once in Chapter 528 |
| Movements 1 and 2 of Volume 11 | `state/continuity.md` L373–492 and L721–824 | the proof in the refusal at about ten to three on the twenty-first |
| **The deep canon blocks** | `state/continuity.md` L997–1088 | canon status, fixed opening facts, institutions, the artifact custody, the relationship lock, the power lock, the ending lock, the reveal lock, the batch 0001 locks. **Read this once. It has not changed in eleven volumes** |
| The volume hand-off Volume 11 was written from | `state/continuity.md` L825–996 — § *Volume 10, Batch 0005 as written* and its repair pass | **You do not need this. The new section at L1 carries everything Volume 12 inherits** |

## Closed volumes. Do not read these to write. Read the audit section of the last one and nothing else.

| Volume | Chapters | Where its audit and its rulings live | Rulings a later phase may not break |
|---|---|---|---|
| 01 | 1–50 | `state/continuity.md` L1,504–1,558 | close accounting L1,504, rulings L1,514 |
| 02 | 51–100 | `state/continuity.md` L2,393–2,498 | close L2,393, rulings L2,401 |
| 03 | 101–150 | `state/continuity.md` L3,477–3,624 | the fourteen rulings L3,477, the forward rulings L3,494, the eleven mechanical repairs L3,501, the volume table L3,523 |
| 04 | 151–200 | `state/continuity.md` L4,649–4,802 | the close and its rulings L4,649, the close-phase repairs L4,719 |
| 05 | 201–250 | `state/continuity.md` L6,066–6,142 | **the twenty-one author-level rulings L6,066, which bind every later volume** |
| 06 | 251–300 | `state/continuity.md` L3,146–6,651 | per-batch repair sections; the third pass on Batch 0003 and the third pass on Batch 0005 are the last two of its six sections |
| 07 | 301–350 | `state/continuity.md` L7,456–7,511 | the close and its audit |
| 08 | 351–400 | `state/continuity.md` L8,198–8,385 | closed and audited. **`reviews/volume-08/` HOLDS NO AUDIT AND THE HOUSE'S OWN RECORD NAMES ONE. CARRIED AS A FLAG, NOT REPAIRED AND NOT INVENTED** |
| 09 | 401–450 | `reviews/volume-09/volume-09-close.md` | closed and audited; the model of what a close phase is |
| 10 | 451–500 | `state/continuity.md` L825–996 | the audited hand-over into Volume 11 |
| **11** | **501–550** | **`reviews/volume-11/volume-11-close.md`, and `state/continuity.md` L1–57 for its figures** | **the four columns, the money chain, the bag, the nine counters, the calendar, the wall's sense, the three dating forms, the two men of about fifty, the eleven counts that came back zero, and the two places the series file names that were not entered** |

**TWO AUDITS NAMED IN THE HOUSE'S OWN RECORD AND NOT IN THIS REPOSITORY: `reviews/volume-06/volume-06-close.md` AND `reviews/volume-08/volume-08-close.md`. NEITHER IS HERE. THIS INDEX DID NOT REPAIR EITHER, DID NOT INVENT EITHER, AND DID NOT AUDIT AROUND EITHER.**

## The three files, and what each one is for

- **`state/current.md` is a log, not a brief.** Newest entry first, one entry per phase, and the entries grow to hundreds of lines. **Read L1–8 only.** If a figure you want is not in the first fourteen lines, it belongs in a continuity section and not in this file.
- **`state/continuity.md` is the state of the world.** Newest section first. **Read L1–57 and `outline/volume-12.md`, and that is the whole of what a writer of Chapters 551 to 560 needs from state.** Read the canon blocks at L997–1088 once.
- **`state/open-threads.md` is what is owed.** Newest batch first, then every older batch's threads, and the long-standing threads from L415 onward. **Read the newest section at L1–38, and L415–490 once for the threads that cross volumes.**
- **`state/chapter-summaries.md` is for the voice and for the figures of a batch.** **For Volume 12 there is nothing to read, because no Volume 12 chapter exists. When one does, read that batch's section at the head of the file, and not the three thousand other lines.** The Volume 11 close section is at the head of the file and is the compact hand-over.

## What this index exists to stop

A phase that read all four files whole would spend most of a model context on Volumes 01 to 11, every one of which is closed, audited and ruled, and would arrive at the active volume with no budget left for the ten chapters it has to write. The repair pass over `logs/batch-0005.review.log` recorded that the previous phase wrote forty-three thousand and seven words for ten chapters and left roughly this much state behind, and that a large and growing share of a batch's output budget is being spent restating what earlier batches already said.

**THE FOUR FILES ARE NOT TRIMMED HERE, BECAUSE TRIMMING A STATE FILE IS AN AUTHOR-LEVEL DECISION AND NOT A REPAIR PASS'S. WHAT IS FIXED HERE IS THE ENTRY POINT: A PHASE THAT READS THIS FILE FIRST AND THEN ONE SECTION OF ONE STATE FILE HAS A BUDGET FOR ITS CHAPTERS.**

## THE ONE DEFECT THIS INDEX CANNOT FIX, RECORDED HERE BECAUSE IT IS THE HIGHEST-VALUE ACTION AVAILABLE ON THIS REPOSITORY

**`state/phase-ledger.json` READS `currentPhase: phase-000-bootstrap` WITH THAT PHASE AT `status: running` AND `volume-01-batch-0001` AT `planned` WITH `attempts: 0` AND `resultCommit: null`, AGAINST A MANUSCRIPT WRITTEN TO CHAPTER 550 WITH A CLOSED AND AUDITED VOLUME 11, A VOLUME 12 OUTLINE, AND A QUEUED WRITER PHASE. `PHASE_SYSTEM.md` MAKES THAT FILE THE SELECTOR'S ONLY INPUT. A WRITER, REPAIR OR AUDIT PHASE IS FORBIDDEN BY ITS OWN DISPATCH PROMPT FROM EDITING IT, AND THIS INDEX DID NOT EDIT IT. IT HAS NOW BEEN ESCALATED EIGHTEEN TIMES AND THE NEXT ESCALATION WILL BE THE SAME SENTENCE. THE CONTROLLER HAS TO.**
