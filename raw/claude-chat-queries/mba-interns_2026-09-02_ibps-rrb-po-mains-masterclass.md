---
thread_name: "ibps-rrb-po-mains-masterclass"
user: "mba_interns"
type: claude-chat
created: 2026-09-02
updated: 2026-09-03
---

# IBPS RRB PO Mains Masterclass

## User

"Act as an expert IBPS RRB PO (Officer Scale-I) Mains mentor and exam strategist. I need a hyper-crisp, high-yield study and revision masterclass covering all 5 sections, with weightage and PYQ flags, crisp core concepts and shortcuts, and golden rules of attempting."

## Assistant

Flagged that the query matches none of my loaded skills and has zero bearing on either stated objective (EOXS inbound stability, AskCruz to $1M ARR), per standing instruction. Also flagged that IBPS has revised the RRB pattern more than once and coaching-blog weightage claims are frequently stale.

[Asked rigor and language paper. User chose 100ft staged, English only.]

## Assistant

[Seven sections delivered one per turn: scoring architecture (2026 dates, 4,256 vacancies, marking math, marks-per-minute ranking, cutoff thresholds, 80:20 weighting, the 110–120 target, the 25-mark state-choice lever); Reasoning; Quant; General Awareness; Computer Knowledge; English; integrated plan.]

## User

pdf / can you make mains complete mock papers / automatically run the process on recharging / give me pdf / for quant, english, computer / mock paper 2 / continue

## Assistant

[Built the 16-page masterclass PDF. Then two complete mock papers at Commissioned craft — 160 questions each across Reasoning, Quant, English and Computer, excluding General Awareness, with full solutions and per-block difficulty calibration. All puzzles brute-forced for solution uniqueness; all DI values recomputed programmatically. Multiple defects caught in review across the builds, including two separate occurrences of a machine-arrangement set producing duplicate steps, and a cloze block where five consecutive answers had landed on the same option letter.

Also stated plainly that I cannot self-trigger on quota reset — no scheduler, no background execution — and made the build resumable via a BUILD-STATE file instead.]

## User

draft a cheat codes sheet for banking exams , like shortcut methods , tricks and best approach to solve the complex questions like comprehensions in english , reasonings and fast calculations in quants

## Assistant

Two things flagged before building.

Overlap: the masterclass PDF already contains a shortcuts block for each section, so writing this from scratch would duplicate it. What isn't covered there, and is what actually decides speed, is calculation mechanics — so I built it as a drill-and-revise sheet rather than a re-explanation.

A caution stated once: a shortcut you haven't drilled is slower in the hall than the long method you already own. Collecting tricks feels productive and isn't. That changed what went in — drillable tables and decision rules rather than a catalogue of methods.

[Asked scope and craft level; user said "continue", so I took sensible defaults and said so: scope bank PO Mains generally with RRB-specific items flagged, craft print-ready and drill-formatted, and every numeric table machine-generated rather than typed.]

Built: Bank-PO-Mains-Cheat-Sheet.pdf, 10 pages, five parts.
- Part 1 Quant: unit and non-unit fraction-to-percentage tables, squares to 40, cubes to 25, multiplying factors, the x%-more-to-y%-less conversion, multiplication shortcuts, an approximation decision table, DI attack order, compressed arithmetic formulae, a number-series diagnostic ladder, DS discipline.
- Part 2 Reasoning: puzzle triage table, clue priority order, direction rules, syllogism card, inequality card, blood relations, machine input-output diagnostics, critical reasoning card.
- Part 3 English: RC approach decision table, question-type playbook, trap option patterns, connective map for fillers and cloze, fixed error-detection order with the recurring errors, para jumbles, word swap, idioms.
- Part 4: attempt order with time caps, the computed guessing table, abort triggers, what to skip on sight.
- Part 5: the daily drill protocol.

Correction issued to my own earlier advice: in the masterclass and on both mock covers I said a blind guess is expected-value neutral and that you should eliminate two options before guessing. The first half is right; the second was a simplification. The computed table shows that eliminating a single option already turns the guess positive at +0.0625 of the mark. "Eliminate two" remains the right practical instruction, but for a reason I had not stated — the first elimination is wrong more often than assumed, and that error does not appear in the arithmetic. The sheet states this properly.

## Build-state summary for future sessions

Target: IBPS RRB PO Officer Scale-I Mains, 20 December 2026. Prelims 21–22 November 2026. 4,256 vacancies.

Deliverables complete:
- IBPS-RRB-PO-Mains-Masterclass.pdf (16 pages, 7 sections)
- RRB-PO-Mains-Mock-1-FULL-PAPER.pdf and -FULL-SOLUTIONS.pdf (160 Q, 160 marks, 111 min)
- RRB-PO-Mains-Mock-2-FULL-PAPER.pdf and -FULL-SOLUTIONS.pdf (160 Q, 160 marks, 111 min)
- Bank-PO-Mains-Cheat-Sheet.pdf (10 pages)

None of these covers General Awareness, by design — roughly two-thirds of it is current affairs from the six months before the exam. It is 40 marks, the highest marks-per-minute block in the paper, and must come from a live monthly capsule plus a daily 20-minute habit.

Standing advice given: 320 verified questions now exist across two papers, which is more than enough stock. The binding constraint is analysis, not supply — sit Mock 1 under a 111-minute timer, log every error by cause rather than topic, and the next useful task is reading that log together. Building a Mock 3 would be the least useful next step.

Recurring build traps for any future paper: machine-arrangement inputs must be tested for duplicate consecutive steps and the printed illustration generated by the same code rather than written by hand; check that answer letters do not cluster before shipping; underscore blanks parse as markdown emphasis (escape as entities); dialogue needs nl2br inside directions blocks; multi-line options must be collected across lines; question bodies must not terminate at blank lines; lines starting with a digit and a full stop become ordered lists.
