# Current State

## Phase position

The planning baseline for Volume 01 is established, and **Volume 01, Batches 0001–0002, Chapters 1–20 are now written and complete in `chapters/volume-01/`.** This file does not set phase status, completion markers, or the queued next phase; those belong to `state/phase-ledger.json` and the controller.

- Current volume: 1 — *The First Bell*, Chapters 1–50
- Last completed chapter: 20
- Chapters written: `chapter-0001.md` through `chapter-0020.md`
- Next writing phase: Volume 01, Batch 0003, Chapters 21–30 (Movement 3, *the ordered chain*). Its prompt is `workspace/volume-01/batch-0003/PROMPT.md`.
- Last batch summary: below.

## Batch 0002 summary

**Batch goal, achieved.** Movement 2, *the leash*: Calder funds weather-exposed ordinary work inside the harbor line, holds the crew through a poor month, proves value in a hearing where his Marr name is used against him, faces a rival Free Keel claim on the freed shoal iron, wins a narrow twenty-day extension with a bond of twelve marks plus held gear and a harbor eighth off any future raising, and ends tending rather than diving, with the naval claim still closed over the shoal. No dive past the four-hundred-yard limit, no second echo entry, no glass returned, no compartment proved.

**Conflicts found and how they were resolved:**

1. Calendar: Batch 0001 ran Tue 11th–Fri 14th. Batch 0002 runs Sat 15th–Tue 25th (11: Sat poor week; 12: Sun gale; 13: Mon 17th; 14: Tue 18th; 15: Wed 19th; 16: Thu 20th; 17: Fri 21st; 18: Sat 22nd; 19: Mon 24th sitting; 20: Tue 25th). Sunday 23rd is an unwritten rest day; no events placed there.
2. The twelve-day defense entered Fri 14th would lapse ~27th; the Mon 24th sitting extends it twenty days further on new terms rather than renewing the same twelve days. Recorded as extension, not second window.
3. Ordinary diving while under echo aftercare: Ch12 and Ch16 dives are ordinary harbor work inside the line under the Morrow Quay charter, not echo entries. Ch12 is a short surge dive that reopens the burn and triggers Nessa's standing shutdown; Ch16 puts Bevin on the bottom with Calder tending. No bell entry occurs; the two-clean-daylight-looks rule for echo work is never lifted.

**Interface compliance:** no panels, stat blocks, sheets, floating text, prompts, trees, level-ups, or software vocabulary. Message-like objects only: labor log, crew's book, reeve's slates, hearing-room slate wall, harbor notices, Registry memorandum and certificate, custody record references, lead-line tag and rag float (harbor lift), buoy bell and working bells, printed duplicate copies. None tells Calder what to do next. Standing bans observed: no "System," "stats," "skills/skill," "mastery," "status panel," "notification," "quest," "level up," "true memory." No Nine Harbors, Quietening, or Crown Seal named. Ilya Serr appears only as name/seal of a senior Registry examiner.

## Batch 0001 summary

**Batch goal, achieved.** Calder's ordinary salvage life and the Gannet debt are established; the first transparent hull is uncovered through a legitimate paid job and a two-date work permit; Calder and Mara are forced into a bounded cooperation neither wanted; the tide-ear procedure is assembled in the yard and used once, at physical cost; both pieces of glass leave the deck in one witnessed surrender; the provenance record, the freed shoal iron, and the numbers survive; and the *Vigil* arrives as paperwork and berth. The batch ends on Calder's own spoken decision, not on a threat.

**Actual word count:** approximately 34,300 words across ten chapters, against a 25,000–29,000 batch guide in `outline/batches/volume-01-batch-0001.md`. The honest per-chapter position, measured after the Batch 0001 review repairs: **eight of the ten chapters run past their own card's ceiling** (1: ~3,373 against 3,000; 2: ~3,366 against 2,800; 3: ~3,639 against 2,800; 5: ~4,180 against 2,800; 6: ~3,372 against 3,200; 8: ~3,722 against 2,800; 9: ~3,741 against 2,800; 10: ~3,871 against 3,000), Chapter 5 is the largest single overrun at about 1,380 words past its ceiling, and **no chapter meets its card's range exactly**; Chapters 4 (~2,721 against a 3,000 ceiling) and 7 (~2,335 against 2,800) are the only two under. Five chapters carry three or more required discrete beats that could not be cut without dropping a cost the crew pays; Chapters 2, 3, 8, 9, and 10 are over because a document has to be read aloud, a specification has to be laid on a bench, and a surrender has to be signed line by line. The prose was trimmed twice, the review removed repetition, and the overrun is recorded here rather than resolved by deleting a cost. No beat listed in the batch outline was dropped.

**Conflicts found and how they were resolved:**

1. The batch outline's day labels (Chapter 4 as "the first working day," Chapter 10 as "the second working day") do not fit a calendar in which Kest sends Calder to the office "tomorrow" at the end of Chapter 1. Resolution: Chapter 1 is a market day on Tuesday the 11th, Chapters 2–4 are Wednesday the 12th, Chapter 5 is Thursday the 13th, Chapters 6–8 are that night into the small hours of Friday the 14th, and Chapters 9–10 are Friday the 14th. Nothing in the prose contradicts any card, and the full calendar is locked in `state/continuity.md`.
2. The Chapter 5 card requires a physical anchor for the Chapter 6 entry, and no Gannet-associated object exists in the cast. Resolution: Calder supplies Oren's brass rigger's hand bell, a private keepsake from before the ferry, and Mara records it as family property with the association to the site **not established** and Calder's own statement that he does not know where it was at the time of the scene. This is a new personal object, not a new world rule, and it is the first thing Calder has ever told anyone he owns.
3. Tobias Wren's account of the old Veyr bell entries was first drafted with inconsistent dates (thirty-one years / forty-five years). Corrected to thirty-one years throughout, with "secondhand" added.
4. Alden was first drafted making a joke about Bevin Rook's name being in the Marr family line, which risked implying a relation to Magistrate Halven Rook. Replaced with a reference to Calder's grandmother, which keeps the family joke and removes the surname implication.

## Batch 0001 review repairs (recorded, not hidden)

The review of Batch 0001 returned FIX. Nine canon and continuity faults and three state-file faults were repaired in the chapters and the state, without restarting the batch and without changing the plot, and the full list is in `reviews/volume-01/batch-0001.md`. The items a later batch would otherwise have inherited wrong:

- **A date collapse.** The Chapter 3 repairer's mark was dated three incompatible ways at once, including to a year of the Serein Accord that is roughly two and a half centuries back. It is now a shop mark of **eleven years back, the middle of the Gannet decade, in plain reckoning**, which is the only date that lets the card's "a shop hand of that decade" and Calder's private suspicion about Oren's notation both stand. The Bible and the card are unchanged; the chapter was wrong.
- **Orison's depth.** Chapter 10 said a hundred and thirty fathoms. It is **seventy fathoms**, per `bible/world.md` and `bible/terminology.md`, and every state file that had absorbed 130 has been corrected.
- **The Chapter 4 dive clock.** The first clamp was written as fitted before the diver was in the water, and the window arithmetic did not close. The dive now runs: bell over 5:10, slack water 5:20, set given as 6:15, first clamp 5:25, silt curtain at 6:00 for four minutes, second clamp off 6:05, current 6:15, up at 6:20, five minutes past what Nessa allowed. Chapter 5's reading of the slate matches it.
- **Depths.** The drifted mole anchor has **one** depth, about eight feet, in every chapter that names it. The freed shoal iron and the *Alder Reach*'s frames are at eight fathoms, with a hole off her quarter at twenty-two.
- **The shard's flange.** The Chapter 9 match depended on a flange that no chapter had ever established on the shard, and collided with the plate's bolted flange. The shard's **ground band** is now planted in Chapter 2 in Mara's own examination, entered as a measurement with *purpose not stated* under it, carried into the Chapter 8 duplicate, and identified in Chapter 9. The two flanges are now visibly different objects' features and are never described in one clause.
- **Shoal geometry.** The four-hundred-yard limit, the outer marks, and the pale run now sit in one fixed set of distances, locked in `state/continuity.md`, because the limit is a live constraint in Batch 0002.
- **The shard's claim window** closed when the courier took the box down the slip, not at dark on a later day, and the three-day courier transit and the two mislocated memories of Chapter 2 and Chapter 9's slip were corrected.
- **The Chapter 2 card compliance.** Calder now hands over the day sheet, the position mark, and the three Free Keel names that the card requires him to submit, which is also what `state/open-threads.md` had been claiming happened.
- **One deviation from the bible is flagged, not applied.** `bible/power-system.md` lists shaking hands as a first-entry cost and Chapters 6 and 7 invert it deliberately. The prose stands; the deviation is recorded in `state/open-threads.md` and `state/continuity.md` for an outline phase to ratify, and no later volume may treat the shake as owed.

**Interface compliance:** the batch contains no panels, stat blocks, character sheets, status messages, floating text, quest text, skill trees, level-ups, or software vocabulary. The only message-like objects used are a lead-line tag and a rag float mark, a crew's book entry, Kest's notice, Registry book entries, a reeve's slate, Mara's separate condition sheet, a written anchor description, the work permit, the custody numbers, and the spoken cutoff word. None of them tells Calder what to do next.

## Story state at the end of Chapter 20

Calder Marr is thirty-two, tending rather than diving until his reopened forearm takes a glove, hearing still double with a third-of-a-second shadow, bound by a twenty-day defense from the 24th, a twelve-mark bond paid plus yard gear held to eighteen, a harbor eighth off any future raising, slip tides given to the Free Keel through November, the *Kittiwake*'s cradle deferred to spring, forty marks owed to Mara after food, and a third of any fair-price shoal-iron sale entered to the *Low Lantern*. He has no glass, no shoal access, no echo permission, and a crew that compensates for his ears by speaking numbers back.

Oren Marr remains thirteen years lost. The compartment contradiction is still available but unproved; the bearing west-southwest and Orison at seventy fathoms remain a direction only.

## Active pressures going into Chapter 21

- **Legal and economic:** twenty-day defense from 24th, lapsing without a further sitting; naval claim still closed within four hundred yards of the outer marks; pump and spare gear held against bond; chandler's note at twelve weeks into six; air pot partly rebuilt from buoy money; *Kittiwake* beached on the hard through winter.
- **Evidence:** shard and plate remain in circuit custody under two numbers; crew holds labor log, measurements, three repair-seam records, scaled plate drawing with eleven keys, anchor-bearing sheet (witnessed as method, never certified as provenance), crew's book, public duplicate on market wall plus ten crew-only printed copies without Mara's name; unverified memory note still separate with its one false line; Oren mark still untold to Mara.
- **Bodily:** reopened rope-burn on right forearm; continuous tinnitus with late second sound; hearing confusion compensated by crew call-backs; Nessa holds standing shutdown on any echo work; Bevin logs any claimed voice with hour and water state, unseen by Calder first.
- **Approach:** broad west-southwest bearing only; harbor-lifted mole anchor now municipal and up; outer water untouched.

## Current relationship pressure

Calder and Mara are an auditor and a suspect who have ended up as witnesses to each other. She holds the Registry's original custody log; he holds only a marked public copy. She has certified his measurements, his hours, and his contamination, and has refused to certify his motive. He has given her everything except the one thing that would let her check his resonance against Oren's notation, and she has told him in writing what that costs. There is no romance, no rescue, and no professional subordination in either direction; she corrects him, he follows the plate, and both of those things are true at once.

Nessa Pike now holds standing authority over any bell entry Calder attempts, written on a slate both of them signed, and Calder has given her the shutdown in front of the crew. Bevin Rook has the logbook job of recording anything Calder calls a voice in a keel-line, which is the first time anyone has been given authority over Calder's perception rather than over his hands. Tobias Wren has said out loud that he has never been able to guess at Calder and that it has cost this yard a great deal.

## Current power state

**Line Diver, and the beginnings of an unstable tide-ear capacity.** One supervised anchored entry, eleven minutes forty inside, surfaced on the tender's word rather than his own judgment. He carries a limited practice trace (the body's memory of a heavy case carried low, a tagged keel-line at deck level, and a frame that has a rail in it), a fresh rope-burn reenactment, tinnitus with a recorded bell under it, and emotional residue strong enough that he answered Nessa in Oren's call mark without deciding to. **His hands do not shake**, which surprised him more than the burn did, and the cost of the entry is not in his hands. He cannot rewind the scene, cannot judge whether any of it is true, cannot read a second echo while carrying this one, and cannot enter a bell until two clean daylight looks have happened with a conservator or a tender present. He is not yet a faultreader and has not claimed to read seams; Mara has used the word *seam* about the doubled edge, and he has written down only what he saw.

## Canon sources

`bible/premise.md`, `bible/world.md`, `bible/characters.md`, `bible/power-system.md`, `bible/themes.md`, and `bible/terminology.md` are canon. `outline/series.md` and `outline/ending.md` are canon for the mystery, antagonist ladder, power stages, and final resolution. `outline/volume-01.md` is canon for the first volume. `outline/batches/volume-01-batch-0001.md` is canon for Chapters 1–10, and Chapters 1–10 as written are now the authority on what happened in them. Where a draft conflicts with a planning file, the planning files win and the conflict is recorded in `state/open-threads.md`.

## Volume index

- **Volume 01, *The First Bell*, Chapters 1–50:** the first transparent recovery, the claim, the seizure, and a one-season provisional working charter. Resolution: the crew keeps its salvage share and a defensible provenance record; the reason for the seizure stays hidden. Next question: why do the transparent vessels form a route toward Orison? **Chapters 1–10 complete.**
- **Volume 02, *The License Sea*, Chapters 51–100:** weather, debt, and a forged coast road; the charter becomes a leash. Resolution: a provisional writ with a reporting clause.
- **Volume 03, *The Unmapped Fleet*, Chapters 101–150:** the fleet resolves into a civic chain linking nine communities. Resolution: the fleet's formation is public; Calder becomes a faultreader and loses a bell-archive to save a crew.
- **Volume 04, *The Keeper's Ledger*, Chapters 151–200:** the registry inquiry and the missing Gannet page. Resolution: the manifest discrepancy is acknowledged, Mara leaves the Registry, and Calder loses Second Bell eligibility.
- **Volume 05, *The Nine Harbors*, Chapters 201–250:** the compact is confirmed as an agreement about custody. Resolution: an informal Nine Harbor Assembly and shared rescue obligations.
- **Volume 06, *The Quietening*, Chapters 251–300:** the descent proves a forced-consensus cascade and a collective scuttling. Resolution: Ilya's seal appears on the old evidence chain.
- **Volume 07, *The Closed Sea*, Chapters 301–350:** blockade and a remembered storm route. Resolution: the blockade is broken at a real cost in boats and responsibility.
- **Volume 08, *The Admiral's Bell*, Chapters 351–400:** amnesty refused, convoy truth exposed, Vey defeated. Resolution: Ilya is promoted to minister at the close of the volume.
- **Volume 09, *A Thousand Small Voices*, Chapters 401–450:** a planted claim panics the public archive. Resolution: the Open Keel Assembly is chartered and the Oren route copy is authorized under mixed custodians.
- **Volume 10, *The Sea Below*, Chapters 451–500:** the Unlit Keel and the testimony-stripping tool. Resolution: proof that Ilya's office rebuilt the Crown Seal and signed the Gannet transfer.
- **Volume 11, *The Cordon*, Chapters 501–550:** close-sea cordon and three broken points. Resolution: independent routes move people and supplies; Calder surrenders accumulated authority.
- **Volume 12, *The Single Voice*, Chapters 551–600:** the Crown Keel begins activating and a technically credible offer of single authority. Resolution: the counter-plan of permitted testimonies and visible gaps.
- **Volume 13, *The Last Witness*, Chapters 601–650:** consent negotiation and a manufactured glass storm. Resolution: the sealed remainder is identified, Calder holds an unexercised family claim, and Ilya admits the Gannet lie.
- **Volume 14, *The Nine Roads*, Chapters 651–700:** the routes hold only with each community's own limits. Resolution: the Crown's monopoly fails; the Crown Keel turns toward Orison.
- **Volume 15, *The Open Sea*, Chapters 701–760:** the Ninth Bell, the released claim, the distributed braid. Resolution: no empire owns the surviving memory network.

## Required updates after each batch

A writer phase that completes a batch updates these same files and does not set phase status:

- `state/chapter-summaries.md`: one entry per chapter, two to five sentences each, plus the compact volume index.
- `state/continuity.md`: new canon facts, changed relationships, power costs and gains, discovered world rules, and any proposed canon change.
- `state/open-threads.md`: promises opened, promises closed, and threads carried forward.
- `state/current.md`: the story state at the end of the batch, so the next batch starts from the right place, plus the batch summary.
