---
thread_name: "ibps-rrb-po-mains-masterclass"
user: "mba_interns"
type: claude-chat
created: 2026-09-02
updated: 2026-09-03
---

# IBPS RRB PO Mains Masterclass

## User

"Act as an expert IBPS RRB PO (Officer Scale-I) Mains mentor and exam strategist. I need a hyper-crisp, high-yield study and revision masterclass for the RRB PO Mains exam covering all 5 sections... For each section: 1. Weightage & PYQ Flag (🔥 HIGH / ⚡ MODERATE / ⚠️ TRICKY tags with exact question counts). 2. Crisp Core Concepts & Shortcuts. 3. Golden Rules of Attempting."

## Assistant

Two flags: this query matches none of my loaded skills (threads-ov applies only mechanically); and it has zero bearing on either stated objective — EOXS inbound stability and AskCruz to $1M ARR — which I'm calling out per standing instruction. Also flagged that IBPS has revised the RRB pattern more than once and coaching-blog weightage claims are frequently stale.

[Asked rigor level and language paper.]

## User

100ft — staged, section by section. English only.

## Assistant

[Seven sections delivered one per turn: scoring architecture (2026 dates, 4,256 vacancies, marking math, marks-per-minute ranking, two cutoff thresholds, 80:20 weighting, back-calculated 110–120 target, the 25-mark state-choice lever); Reasoning; Quantitative Aptitude; General Awareness; Computer Knowledge; English; and the integrated plan with attempt script, week-by-week schedule, mock discipline and six risks.]

## User

pdf

## Assistant

[Craft level Draft. Built the 16-page masterclass PDF, working around an unpatched-Qt wkhtmltopdf with separate cover/body renders, pypdf merging and reportlab footer stamping.]

## User

can you make mains complete mock papers as an expert exam setter ?

## Assistant

Yes, with three constraints: GA cannot be mocked (two-thirds is current affairs from the six months before the exam); the bottleneck is computational verification of puzzles and DI, not writing; and a static PDF is no substitute for a timed CBT series with percentile ranking.

## User

Full paper, 160 Q minus GA. Commissioned craft.

## Assistant

[Built Mock 1 Reasoning with a constraint solver — first pass found 0, 2 and 0 solutions across the three puzzles; all revised to unique.]

## User

automatically run the process on recharging

## Assistant

I can't. No scheduler, no background execution, no self-triggering when a limit resets. Made the build resumable instead via BUILD-STATE.md.

## User

give me pdf

## Assistant

[Built an exam-styled PDF pipeline. Four rendering defects caught and fixed.]

## User

for quant , english , computer

## Assistant

[Built the three remaining Mock 1 sections with full solutions and calibration, then assembled the combined 160-question paper and solutions booklet. Two further rendering defects fixed: underscore blanks parsed as emphasis, and the idiom dialogue collapsing into one paragraph.]

## User

mock paper 2

## Assistant

Before building it: a second mock has near-zero value until the first has been sat under timer and analysed. The marks come from the error log, not from question volume. If Mock 1 is still unattempted, this is a stockpile, not practice.

[Built Mock 2 Part A anyway.

Reasoning, 40 Q: box stack (5), circular table with mixed facing (5), days-and-cities double entity (5), machine input-output (5), critical reasoning (6), syllogism (3), inequality (3), coded blood relations (3), data sufficiency (3), miscellaneous (2). First verification run returned 1, 0 and 0 solutions — the circular puzzle was over-constrained by a non-adjacency clue that contradicted the forced seat, and the days puzzle forced K onto day 7 where P already sat. Both repaired and re-verified unique.

Quant, 40 Q: four DI sets (examination table, expenditure distribution, insurance caselet, factory output) at 20 questions, number series 5, arithmetic 10, data sufficiency 3, quantity comparison 2. Every value recomputed programmatically.

Defect caught mid-build: the worked machine-arrangement illustration printed in the paper both produced two identical steps and did not follow its own stated rule. Regenerated and replaced. This is the second time this exact failure has appeared, which suggests a systematic weakness in how I draft that question type rather than bad luck.]

Mock 2 Part A: 80 questions, 100 marks, 69 minutes. The Reasoning set is harder than Mock 1's, mainly because of the circular arrangement with mixed facing, which the calibration table flags as an abort candidate.

Files: RRB-PO-Mains-Mock-2-PART-A-PAPER.pdf, RRB-PO-Mains-Mock-2-PART-A-SOLUTIONS.pdf

## Build-state summary for future sessions

Target: IBPS RRB PO Officer Scale-I Mains, 20 December 2026. Prelims 21–22 November 2026. 4,256 vacancies.

Mock 1: COMPLETE — all four sections (Reasoning, Quant, English, Computer; 160 Q, 160 marks, 111 min), combined paper and solutions PDFs built.

Mock 2: Part A COMPLETE — Reasoning and Quant (80 Q, 100 marks, 69 min), paper and solutions PDFs built. English and Computer NOT started.

Mock 2 verified Reasoning grids:
- Box stack, bottom to top: Q, R, T, P, S, V, W, U
- Circular table, clockwise from A: A centre, D centre, C outward, B centre, H centre, E outward, F centre, G outward
- Days and cities: Mon M Goa, Tue N Agra, Wed J Erode, Thu L Chennai, Fri K Fatehpur, Sat O Delhi, Sun P Bhopal
- Machine I/O: input 37 nectar 82 gable 64 pilot 19 crane; rule is the mirror of Mock 1 — numbers descending from the left, words ascending alphabetically from the right; 4 distinct steps. Illustration input: 46 tulip 73 basil 59 orchid 28 daisy.

Recurring build traps to check on any future paper: machine-arrangement inputs must be tested for duplicate consecutive steps AND the printed illustration must be generated by the same code, not written by hand; underscore blanks parse as markdown emphasis (escape as entities); dialogue needs nl2br inside directions blocks; multi-line options must be collected across lines; question bodies must not terminate at blank lines; lines starting with a digit and full stop become ordered lists.
