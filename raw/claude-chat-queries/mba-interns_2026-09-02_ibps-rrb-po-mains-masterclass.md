---
thread_name: "ibps-rrb-po-mains-masterclass"
user: "mba_interns"
type: claude-chat
created: 2026-09-02
updated: 2026-09-03
---

# IBPS RRB PO Mains Masterclass

## User

"Act as an expert IBPS RRB PO (Officer Scale-I) Mains mentor and exam strategist. I need a hyper-crisp, high-yield study and revision masterclass covering all 5 sections. For each section: 1. Weightage & PYQ Flag (🔥 HIGH / ⚡ MODERATE / ⚠️ TRICKY tags with exact question counts). 2. Crisp Core Concepts & Shortcuts. 3. Golden Rules of Attempting."

## Assistant

Two flags: the query matches none of my loaded skills, and it has zero bearing on either stated objective — EOXS inbound stability and AskCruz to $1M ARR — which I'm calling out per standing instruction. Also flagged that IBPS has revised the RRB pattern more than once and coaching-blog weightage claims are frequently stale.

[Asked rigor level and language paper.]

## User

100ft — staged. English only.

## Assistant

[Seven sections delivered one per turn: scoring architecture (2026 dates, 4,256 vacancies, marking math, marks-per-minute ranking, two cutoff thresholds, 80:20 weighting, back-calculated 110–120 target, the 25-mark state-choice lever); Reasoning; Quant; General Awareness; Computer Knowledge; English; and the integrated plan.]

## User

where is study material ? / pdf

## Assistant

[Acknowledged that Section 1 was architecture rather than content. Later built the 16-page masterclass PDF at Draft craft, working around an unpatched-Qt wkhtmltopdf.]

## User

can you make mains complete mock papers as an expert exam setter ?

## Assistant

Yes, with three constraints: GA cannot be mocked; the bottleneck is computational verification of puzzles and DI, not writing; and a static PDF is no substitute for a timed CBT series. Recommended sectional sets; user chose a full 160-question paper at Commissioned craft.

## User

automatically run the process on recharging

## Assistant

I can't. No scheduler, no background execution, no self-triggering when a limit resets. Made the build resumable via BUILD-STATE.md instead.

## User

[Mock 1 build across several turns: give me pdf / for quant, english, computer]

## Assistant

[Mock 1 completed: all four sections, 160 Q, 160 marks, 111 min. Constraint solver caught 0, 2 and 0 solutions on the first pass of the three puzzles; all repaired. Six rendering defects caught and fixed across two build turns.]

## User

mock paper 2

## Assistant

Flagged first that a second mock has near-zero value until the first has been sat under timer and analysed. Built it anyway.

[Mock 2 Part A: Reasoning and Quant. First verification run returned 1, 0 and 0 solutions — the circular puzzle was over-constrained by a non-adjacency clue contradicting the forced seat, and the days puzzle forced K onto a day P already occupied. Both repaired. Separately, the printed machine-arrangement illustration both produced duplicate steps and did not follow its own stated rule; regenerated. Noted this was the second occurrence of that exact failure, indicating a systematic weakness in how I draft that question type rather than bad luck.]

## User

continue

## Assistant

[Mock 2 English and Computer built, then the complete Mock 2 assembled.

English, 40 Q: two original passages — weather-index crop insurance and municipal waste segregation — at 8 and 7 questions, cloze 5, double fillers 4, idioms in dialogue 5, word swap 4, error detection 4, rearrangement 3. Caught during checking that five consecutive cloze answers had all landed on option (b); reordered the option sets across eight questions to spread the key.

Computer, 40 Q: fundamentals and hardware 12, networking 8, security 6, MS Office 6, operating systems 4, DBMS and banking technology 4.]

Mock 2 complete: 160 questions, 16-page paper, 10-page solutions. The Part A PDFs are superseded.

Closing advice given: 320 verified questions now exist across two papers, which is more than enough stock, and building a Mock 3 would be the least useful next step. The binding constraint is analysis, not supply — sit Mock 1 under a 111-minute timer, log errors by cause rather than topic, and the next useful task is reading that log together. The one gap neither paper closes is General Awareness, 40 marks and the highest marks-per-minute block in the real exam, which must come from a live monthly capsule.

## Build-state summary for future sessions

Target: IBPS RRB PO Officer Scale-I Mains, 20 December 2026. Prelims 21–22 November 2026. 4,256 vacancies.

Mock 1: COMPLETE — 160 Q, 160 marks, 111 min. Files: RRB-PO-Mains-Mock-1-FULL-PAPER.pdf, RRB-PO-Mains-Mock-1-FULL-SOLUTIONS.pdf.
Mock 2: COMPLETE — 160 Q, 160 marks, 111 min. Files: RRB-PO-Mains-Mock-2-FULL-PAPER.pdf, RRB-PO-Mains-Mock-2-FULL-SOLUTIONS.pdf.
Neither includes General Awareness.

Mock 2 verified Reasoning grids:
- Box stack, bottom to top: Q, R, T, P, S, V, W, U
- Circular table, clockwise from A: A centre, D centre, C outward, B centre, H centre, E outward, F centre, G outward
- Days and cities: Mon M Goa, Tue N Agra, Wed J Erode, Thu L Chennai, Fri K Fatehpur, Sat O Delhi, Sun P Bhopal
- Machine I/O: input 37 nectar 82 gable 64 pilot 19 crane; numbers descending from the left, words ascending alphabetically from the right; 4 distinct steps. Illustration input: 46 tulip 73 basil 59 orchid 28 daisy.

Difficulty relationship between the papers: Mock 2 Reasoning is slightly harder than Mock 1 (circular set with mixed facing); Mock 2 Quant is slightly easier; English and Computer are comparable, with Mock 2 adding a dangling-participle item and a binary conversion. Compare block by block, never section totals.

Recurring build traps: machine-arrangement inputs must be tested for duplicate consecutive steps and the printed illustration must be generated by the same code rather than written by hand; check that answer letters do not cluster before shipping; underscore blanks parse as markdown emphasis (escape as entities); dialogue needs nl2br inside directions blocks; multi-line options must be collected across lines; question bodies must not terminate at blank lines; lines starting with a digit and full stop become ordered lists.
