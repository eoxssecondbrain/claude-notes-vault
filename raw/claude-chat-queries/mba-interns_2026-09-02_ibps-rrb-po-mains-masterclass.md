---
thread_name: "ibps-rrb-po-mains-masterclass"
user: "mba_interns"
type: claude-chat
created: 2026-09-02
updated: 2026-09-03
---

# IBPS RRB PO Mains Masterclass

## User

"Act as an expert IBPS RRB PO (Officer Scale-I) Mains mentor and exam strategist. I need a hyper-crisp, high-yield study and revision masterclass for the RRB PO Mains exam covering all 5 sections... For each section, structure your output strictly as follows: 1. Weightage & PYQ Flag (with 🔥 HIGH / ⚡ MODERATE / ⚠️ TRICKY tags and exact question counts). 2. Crisp Core Concepts & Shortcuts. 3. Golden Rules of Attempting. Keep the language dense, concise, scannable, and strictly tailored to RRB PO Mains difficulty."

## Assistant

Two flags before I start.

Skill match: this query matches none of my loaded skills. eoxs-data-general and sales-strategist are irrelevant here; threads-ov applies only mechanically (transcript saving).

Relevance: this has zero bearing on either stated objective (EOXS inbound stability, AskCruz to $1M ARR). Per your standing instruction I'm calling that out. If it's for someone else, say so and I'll drop the flag.

Also flagged that IBPS has revised the RRB pattern more than once and coaching-blog weightage claims are frequently stale, which is the case for going above 5ft.

[Asked: rigor level; language paper]

## User

A: 100ft — staged, section by section. English only.

## Assistant

[Outline of 7 sections, then Section 1 — Scoring architecture: 2026 timeline (registration 1–21 Sept, Prelims 21–22 Nov, Mains 20 Dec, 4,256 vacancies); Mains pattern; marking math and the eliminate-two guessing rule; marks-per-minute leverage ranking; two cutoff thresholds with 2025 state-wise figures; 80:20 weighting and the back-calculated 110–120 target; the 25-mark state-choice lever; data-quality flag.]

## User

where is study material ?

## Assistant

Fair hit. Section 1 was exam architecture, not content — legitimate under the rigor level you picked, but it delayed the payload by a turn. [Offered: dump all / continue staged / meant sources]

## User

A: Continue staged.

## Assistant

[Sections 2–7 delivered one per turn: Reasoning; Quantitative Aptitude (including the flagged contradiction that coaching lists still push quadratic equations and simplification despite their absence from recent papers); General Awareness (with the argument that GA needs a daily habit because it cannot be block-studied in the four-week gap); Computer Knowledge (the mispricing argument — GA plus Computer are 60 marks in 20 minutes); English (including the finding that the English sectional bar sits materially below the Hindi one); and the Integrated Plan with the 120-minute attempt script, week-by-week schedule, mock discipline and six risks.]

## User

pdf

## Assistant

[Asked craft level; user chose Draft. Built the 16-page masterclass PDF. wkhtmltopdf here is built against unpatched Qt — no multi-document input, no header/footer flags, no --xsl-style-sheet — so cover and body were rendered separately, heading page positions extracted with pypdf, a Contents page generated with real page numbers iterating until stable, merged, footers stamped via reportlab. Emoji tags replaced with coloured badges.]

File: IBPS-RRB-PO-Mains-Masterclass.pdf

## User

can you make mains complete mock papers as an expert exam setter ?

## Assistant

Yes, but three constraints shape what's worth building: GA cannot be mocked (two-thirds is Jul–Dec 2026 current affairs, past my knowledge and partly in the future); the quality bottleneck is computational verification of puzzles and DI, not writing; and a static PDF is no substitute for a timed CBT test series with percentile ranking. Recommended sectional sets over a full paper.

[Asked: scope; craft level]

## User

A: Full paper, 160 Q (all sections minus GA). Commissioned craft.

## Assistant

[Staged the build. Wrote a constraint solver for the Reasoning puzzles. First run: Puzzle 1 had 0 solutions, Puzzle 2 had 2 (mirror symmetry), Puzzle 3 had 0. Revised all three; Puzzle 3 still had 3 solutions until the Gurkha clue was replaced with a three-car consecutive chain. All three then unique.]

## User

automatically run the process on recharging

## Assistant

I can't do that. No scheduler, no background execution, no ability to trigger myself when a limit resets — every turn needs a message from you. The container filesystem also resets between sessions.

[Caught a defect: the drafted machine input-output input produced identical Steps 3 and 4. Found a replacement input yielding five distinct steps, rewrote those questions, wrote the Reasoning solutions and a BUILD-STATE.md for resumption.]

## User

give me pdf

## Assistant

[Built a dedicated exam-styled builder — directions blocks, question blocks, three-tier option layouts by option length, monospaced machine steps, instruction covers, reportlab footer stamping. Four rendering defects caught and fixed: collapsed input-output steps; multi-line options absorbed into stems; question bodies truncated at blank lines; answer lines auto-renumbered as lists.]

## User

for quant , english , computer

## Assistant

[Built all three remaining sections.

Quant, 40 Q: four DI sets (table, double distribution, bar, caselet) at 20 questions, number series 5, arithmetic 10, data sufficiency 3, quantity comparison 2. Every derived value — approvals, departmental male/female splits, quarterly totals, caselet values, series terms and all ten arithmetic answers — recomputed programmatically before printing.

English, 40 Q: two original passages (rural credit and self-help groups; urban water metering) at 8 and 7 questions, cloze 5, double fillers 4, idioms in dialogue 5, word swap 4, error detection 4, rearrangement 3.

Computer, 40 Q: fundamentals and memory 12, networking 8, security 6, MS Office 6, operating systems 4, DBMS and banking technology 4.

Each with full worked solutions, answer key and a per-block difficulty calibration table.

Then assembled the combined 160-question paper and the combined solutions booklet. Two further rendering defects caught and fixed: markdown parsed the fill-in-the-blank underscores as emphasis markers and bolded the text between them; and the idiom dialogue collapsed into a single run-on paragraph until line breaks were enabled inside directions blocks.]

Complete. 160 questions, 160 marks, 111 minutes — paper is 16 pages, solutions 11. Numbering restarts at 1 in each section deliberately, so each section has its own key and can be marked and timed independently.

Two caveats stated: every Quant value was recomputed programmatically and the Reasoning puzzles brute-forced, but English and Computer carry no equivalent proof — they rest on my judgement, which is a weaker guarantee, so challenge any answer that looks wrong. And difficulty is calibrated to the 2024–25 papers; if 2026 Quant spikes the way 2023 did, this mock will read easier than the real thing.

Files: RRB-PO-Mains-Mock-1-FULL-PAPER.pdf, RRB-PO-Mains-Mock-1-FULL-SOLUTIONS.pdf, plus the earlier Reasoning-only paper and solutions PDFs and the four markdown sources.

## Build-state summary for future sessions

Target: IBPS RRB PO Officer Scale-I Mains, 20 December 2026. Prelims 21–22 November 2026. 4,256 vacancies. Registration closed 21 September 2026.

Mock paper: 160 questions across Reasoning (40 Q / 50 marks), Quantitative Aptitude (40 / 50), English (40 / 40) and Computer Knowledge (40 / 20). General Awareness excluded because roughly two-thirds of it is current affairs from the six months before the exam. Commissioned craft: puzzles brute-forced for uniqueness, DI values recomputed, full solutions, per-block calibration.

Status: all four sections COMPLETE, both combined PDFs built. Nothing outstanding on Mock 1.

Verified Reasoning grids:
- Seminar puzzle: Jan-11 D, Jan-24 F, Mar-11 B, Mar-24 A, Jun-11 G, Jun-24 C, Sep-11 H, Sep-24 E
- Parallel rows: Row 1 seats 1-5 north T P S Q R; Row 2 seats 1-5 south Y V X W Z
- Floors and cars: 8 O Fortuner, 7 M Alto, 6 K Dzire, 5 L Creta, 4 U Harrier, 3 T Gurkha, 2 J Ertiga, 1 N Baleno
- Machine I/O input: 48 ridge 31 anchor 54 velvet 72 pearl 26 glow (numbers ascending from the left, words reverse-alphabetical from the right; 5 distinct steps)

Build pipeline notes for any future paper: wkhtmltopdf on this machine lacks multi-document, header/footer and XSL support, so covers and bodies render separately and merge via pypdf with reportlab footer overlays. Known markdown traps: underscore blanks parse as emphasis (escape as entities), dialogue lines need nl2br inside directions blocks, multi-line options must be collected across lines, question bodies must not terminate at blank lines, and lines beginning with a digit and a full stop become ordered lists.
