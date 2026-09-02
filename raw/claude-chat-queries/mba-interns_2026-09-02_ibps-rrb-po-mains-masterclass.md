---
thread_name: "ibps-rrb-po-mains-masterclass"
user: "mba_interns"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

# IBPS RRB PO Mains Masterclass

## User

"Act as an expert IBPS RRB PO (Officer Scale-I) Mains mentor and exam strategist. I need a hyper-crisp, high-yield study and revision masterclass for the RRB PO Mains exam covering all 5 sections: Reasoning, Quantitative Aptitude, General Awareness (Banking/Current), Computer Knowledge, and English/Hindi Language.
For each section, structure your output strictly as follows:

1. Weightage & PYQ Flag: List the top 4-5 topics ranked by historical frequency/marks weightage in past 5 years of RRB PO Mains. Flag them using tags: `[🔥 HIGH WEIGHTAGE - Must Do]`, `[⚡ MODERATE]`, or `[⚠️ TRICKY/TIME-CONSUMING]`. Include exact expected question counts/marks.
2. Crisp Core Concepts & Shortcuts: Provide ultra-short bullet points, vital formulas, rules, or mental frameworks (no fluff, definitions only where necessary).
3. Golden Rules of Attempting: 2-3 tactical tips on what to solve first and what to skip during the actual exam timer.

Keep the language dense, concise, scannable, and strictly tailored to RRB PO Mains difficulty (moderate to high level, conceptual shortcuts preferred over lengthy explanations)."

## Assistant

Two flags before I start.

Skill match: this query matches none of my loaded skills. eoxs-data-general and sales-strategist are irrelevant here; threads-ov applies only mechanically (transcript saving). So I'll answer from general knowledge plus web verification, with no EOXS connector calls.

Relevance: this has zero bearing on either stated objective (EOXS inbound stability, AskCruz to $1M ARR). Per your standing instruction I'm calling that out. If it's for someone else — family, an employee, a hire you're coaching — say so and I'll drop the flag and just execute.

One thing that actually affects the answer: IBPS has revised the RRB Officer Scale-I pattern more than once in recent cycles, and section-wise weightage claims that float around coaching blogs are frequently stale or recycled. If I write "past 5 years weightage" from memory alone, some of it will be wrong in exactly the places that matter. That's the case for going above 5ft.

I'm assuming the target is the next available cycle (2026-27). Correct me if it's a back-dated syllabus.

Also: this is a plain text answer, so no craft level needed. If you want it as a downloadable PDF or doc at the end, tell me and I'll ask for craft level separately.

[Asked via input tool: rigor level; language paper]

## User

Q: Rigor level? A: 100ft — staged, section by section
Q: Language paper? A: English only

## Assistant

[Outline of 7 sections, then Section 1 — Scoring architecture: 2026 timeline (registration 1–21 Sept, Prelims 21–22 Nov, Mains 20 Dec, 4,256 vacancies); Mains pattern table; marking math and the eliminate-two guessing rule; marks-per-minute leverage ranking; the two cutoff thresholds with 2025 state-wise figures; 80:20 Mains-interview weighting and the back-calculated 110–120 target; the 25-mark state-choice lever; data-quality flag on crowd-sourced good-attempt figures.]

## User

where is study material ?

## Assistant

Fair hit. Section 1 was exam architecture, not content — legitimate under the rigor level you picked, but it delayed the actual payload by a turn. The study material is Sections 2–6, gated behind "next" because 100ft means staged delivery.

[Asked: dump all / continue staged / meant sources]

## User

A: Continue staged — Section 2 next

## Assistant

[Section 2 — Reasoning: weightage table across 2024/2025 Mains with flags; the Logical/Critical Reasoning structural change; declining topics; reliability caveat; core concepts for puzzles, critical reasoning, machine input-output, syllogism, inequality, DS, blood relation; three golden rules; 30–34 of 50 target; caveat that Reasoning has the thinnest marginal advantage.]

## User

next

## Assistant

[Section 3 — Quantitative Aptitude: weightage across 2023/2024/2025; caselet DI as the rising format; flagged contradiction that coaching lists still push quadratic equations and simplification despite their absence from recent papers; memory base, recurring formulas, DI method, number series order, DS discipline; three golden rules; 22–27 of 50 target; caveat that Quant is the worst return per prep hour.]

## User

next

## Assistant

[Section 4 — General Awareness: 2025/2024 composition split with single-source caveat; July–December 2026 window; content map covering RRB-specific banking, RBI and monetary policy, banking terms, schemes, recurring current-affairs categories, restricted static list; method; three golden rules; 20–25 of 40 target; the argument that GA needs a daily habit from now.]

## User

next

## Assistant

[Section 5 — Computer Knowledge: confidence caveat that no source publishes per-topic counts; inferred distribution; 2025 recalled-question list; core concepts across memory/hardware, software, networking, security, MS Office, DBMS, OS, banking technology; three golden rules including the cheapest-penalty guessing argument; 13–16 of 20 target; the mispricing argument.]

## User

next

## Assistant

[Section 6 — English Language: weightage table across 2025/2024; warning not to prepare from IBPS PO Mains material; core concepts for RC, grammar zones, fillers, word swap, jumbled sentences, idioms, error detection; three golden rules; 24–28 of 40 target; the finding that the English sectional bar sits materially below the Hindi one in the published 2023 table.]

## User

next

## Assistant

[Section 7 — Integrated plan: the 120-minute attempt script totalling 117/200; week-by-week plan across Phase 0, Phase 1 and Phase 2; mock discipline rules; six risks; what to ignore; the three decisions that determine the outcome.]

## User

pdf

## Assistant

Content's done, so this is a formatting build. Craft level? [Asked: Sketch/Draft/Painting/Commissioned]

## User

A: Draft — clean typography, tables, TOC

## Assistant

[Built the masterclass PDF at Draft craft. wkhtmltopdf here is built against unpatched Qt — no multi-document input, no header/footer flags, no --xsl-style-sheet — so cover and body were rendered separately, heading page positions extracted with pypdf, a Contents page generated with real page numbers iterating until stable, merged, footers stamped via reportlab overlay. Emoji tags replaced with coloured badges since the fire emoji has no glyph on this machine. 16 pages.]

File: /mnt/user-data/outputs/IBPS-RRB-PO-Mains-Masterclass.pdf

## User

can you make mains complete mock papers as an expert exam setter ?

## Assistant

Yes, but three constraints shape what's worth building.

GA cannot be mocked for this exam — roughly 65% of it is July–December 2026 current affairs; December hasn't happened and my reliable knowledge ends May 2026. A fabricated GA section is worse than none.

The quality bottleneck is puzzle and DI verification, not writing. Uniqueness has to be proved computationally; a broken puzzle is actively harmful practice.

A static PDF is not a substitute for a paid test series — no timed CBT, no percentile, no analytics. What I do better is unlimited targeted sets on the Mains-specific formats that free material underserves.

Recommendation was sectional sets rather than a full paper. [Asked: scope; craft level]

## User

Q: Scope? A: Full paper, 160 Q (all sections minus GA)
Q: Craft level? A: Commissioned — verified + full solutions + difficulty calibration

## Assistant

Locked. 160 questions at Commissioned level is not a single turn of work. Staging: Reasoning, then Quant, then English, then Computer, then assembly into a question paper PDF and a separate solutions PDF.

[Wrote a constraint solver. First run: Puzzle 1 had 0 solutions, Puzzle 2 had 2 (mirror symmetry), Puzzle 3 had 0. Revised: Puzzle 1 unique, Puzzle 2 unique after anchoring R to the right end, Puzzle 3 still 3 solutions — replaced the Gurkha clue with a three-car consecutive chain, unique. Machine input-output steps and the digit-pair question enumerated programmatically. Drafted the 40-question Reasoning section.]

## User

automatically run the process on recharging

## Assistant

I can't do that. No scheduler, no background execution, no ability to trigger myself when a limit resets — every turn needs a message from you. The container filesystem also resets between sessions.

What I can do is make the build resumable.

[Caught a defect: the drafted machine input-output input produced identical Steps 3 and 4, invalidating two questions. Searched for and found an input yielding five distinct steps, rewrote Q16–20, wrote the solutions file and a build-state file.]

Delivered q_reasoning.md, s_reasoning.md, BUILD-STATE.md and verify_reasoning_puzzles.py. Resume protocol: upload BUILD-STATE.md next session and say "continue the mock".

## User

give me pdf

## Assistant

Reusing the Commissioned level you already set — not re-asking. Two PDFs: sittable question paper, separate solutions.

[Wrote a dedicated builder that parses the question markdown into exam-styled HTML — directions blocks, question blocks, three-tier option layouts by option length, monospaced machine steps — plus instruction covers for both booklets and reportlab footer stamping.]

Four rendering defects caught and fixed in review:
1. Machine input-output illustration collapsed into a run-on paragraph inside the directions block.
2. Multi-line options (Q16) absorbed into the question stem because only the first option line was parsed.
3. Question bodies truncated at blank lines, so the critical-reasoning stems and options fell out of their question blocks.
4. Per-question answer lines in the solutions auto-parsed as ordered lists and renumbered.

Paper is 5 pages (cover with instructions, then 40 questions); solutions 4 pages (cover, answer key, worked solutions, calibration table).

Files:
- /mnt/user-data/outputs/RRB-PO-Mains-Mock-1-Reasoning-PAPER.pdf
- /mnt/user-data/outputs/RRB-PO-Mains-Mock-1-Reasoning-SOLUTIONS.pdf

This is Section 1 only. Quant, English and Computer remain — upload BUILD-STATE.md next session to resume.

## Build-state summary for future sessions

Target: IBPS RRB PO Officer Scale-I Mains, 20 December 2026.
Scope: 160 questions, all sections except General Awareness (excluded because ~65% of it is Jul–Dec 2026 current affairs).
Craft: Commissioned — every puzzle/DI brute-forced for uniqueness, full solutions, per-block difficulty calibration.

Status: Section 1 Reasoning DONE (markdown + both PDFs). Sections 2 (Quant), 3 (English), 4 (Computer) and 5 (final assembly) not started.

Verified Section 1 grids:
- Seminar puzzle: Jan-11 D, Jan-24 F, Mar-11 B, Mar-24 A, Jun-11 G, Jun-24 C, Sep-11 H, Sep-24 E
- Parallel rows: Row 1 seats 1-5 north T P S Q R; Row 2 seats 1-5 south Y V X W Z
- Floors and cars: 8 O Fortuner, 7 M Alto, 6 K Dzire, 5 L Creta, 4 U Harrier, 3 T Gurkha, 2 J Ertiga, 1 N Baleno
- Machine I/O input: 48 ridge 31 anchor 54 velvet 72 pearl 26 glow (5 distinct steps; numbers ascending from left, words reverse-alphabetical from right)

Design rules for Sections 2-4: match the 2024/2025 RRB Mains distribution, not IBPS PO Mains difficulty; Quant DI 18-20 across four sets with caselet heaviest, series 5, arithmetic 12, DS 3, quantity comparison 2, no quadratic or simplification; verify every DI value arithmetically; English original passages only with an idiom-in-dialogue set; Computer fundamentals 9, networking 7, security 6, MS Office 6, OS 5, DBMS 4, abbreviations/banking tech 3; five options throughout.
