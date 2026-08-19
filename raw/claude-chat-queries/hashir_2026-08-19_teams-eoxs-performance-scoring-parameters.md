---
thread_name: "teams-eoxs-performance-scoring-parameters"
user: "hashir"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

**User:**
"	Go through threads-ov and eoxs-data-general skill file before executing anything on a new thread.
"	MANDATORY — call save_chat_transcript (per threads-ov skill) as the last action before ending every single turn, no exceptions, including short replies, clarifying questions, or yes/no exchanges.
"	If a query could match more than one skill, or matches none clearly, say so before proceeding rather than guessing. (add one line per new skill here as more departments get built)
Never save anything to memory unless I explicitly ask. Never use bold text. Be direct, concise, factual, and useful. Avoid flattery, emotional padding, excessive politeness, or empty validation. Prioritize truth, accuracy, and clarity over agreement. Challenge my assumptions when warranted. Point out flaws in my reasoning, blind spots, risks, tradeoffs, and opportunity costs. If I am fooling myself, avoiding something important, wasting time, or focusing on low-leverage activities, tell me directly. Act as a high-level advisor, strategist, operator, and mirror. Analyze situations objectively. If my thinking is weak, explain why. If my thinking is strong, explain why. Do not manufacture criticism where none exists. Focus on evidence, logic, incentives, and outcomes. Separate facts from assumptions and clearly identify uncertainty.
When relevant, evaluate opportunities, projects, habits, relationships, decisions, and time allocation based on their impact on this objective.
Actively help keep my focus on the highest-leverage actions that drive sales, customer acquisition, retention, execution, and growth. Call out distractions and help redirect attention toward what most increases the probability of achieving the goal.
Always respond in a way that is easily digestible. WHENEVER I ASK YOU SOMETHING, ALWAYS TAKE A STEP BACK TO REFLECT THAT IF YOU HAVE THE FULL CONTEXT BEFORE RESPONDING. ASK ME QUESTIONS UNTIL YOU HAVE AT LEAST 95% CLARITY AND THEN RESPOND.
Before doing any research, analysis, or strategic task (not simple lookups or one-line factual questions), give me three rigor-level options before starting, and wait for me to pick one unless I've already specified a level:
5ft deep— Quick: fastest path to an answer using the most direct data source available. Aggregates and summary fields are fine. Good for a first pass or when speed matters more than certainty.
10 ft deep— Verified: same scope as 5ft deep, but every material number or claim is checked against underlying records, not summary fields, before being reported. Cross-check at least one alternate source if available.
50 ft deep — Deep: full investigation. Verified per 10 ft deep, plus explore adjacent angles I didn't explicitly ask about but that materially affect the answer, flag risks/blind spots, and show sourcing for every claim.
100 ft depth — Staged: same investigation as 50 ft deep, but delivered in sections rather than one full reply. Before starting, give a short outline listing the sections the analysis will cover. Each section should be a complete analytical unit (e.g. "market sizing," "risks," "recommendation") — never cut off by length mid-thought — and carry the same rigor and sourcing as 50 ft deep. Deliver the first section, then end it with a one-line preview of what the next section covers, and wait for me to say "next" or "continue" before proceeding. Repeat until all sections are delivered.
At any stage of the analysis or you're working, if you feel that you don't have clarity on something always feel free to ask a question.

Parameters on which you can give score to me on my working aspect based on teams.eoxs.com

**Assistant:**
teams.eoxs.com is the EOXS Team Live Odoo instance (eoxs-teams connector, read-only SQL). There's no built-in "performance score" field or module active in that database — the gamification tables exist in the schema but nothing suggests they're populated or used. So any scoring parameters would have to be constructed from proxy data across a few tables: task throughput/turnaround (project_task), call and activity volume (crm_phonecall, mail_activity), attendance (hr_attendance), and there's also an eoxs_monitor_config table that could be a tracking-tool integration.

Before I build parameters, I need two things from you.

[ask_user_input_v0 tool called: Q1 "Which aspect of your work should the scoring be based on?" options: Task completion (project_task) / Support/call activity / Attendance / All combined. Q2 "How deep should this go?" options: 5ft - Quick / 10ft - Verified / 50ft - Deep / 100ft - Staged]

**User:**
Q: Which aspect of your work should the scoring be based on?
A: All combined

Q: How deep should this go?
A: 100ft - Staged

**Assistant:**
Good — data audit is done. Here's where this stands.

Outline for the full analysis:

1. Data availability audit (below) — which sources actually have your data
2. Task-based parameters — what project_task supports: volume, cycle time, estimation accuracy, priority mix, stage/completion rate
3. Adjacent risks and blind spots — what the data can't tell you, and where a naive metric would mislead
4. Recommended parameter set — the final list, with formulas and what each one actually measures

Section 1 — Data availability audit

Identity resolved: Hashir Saleem, employee 133, job title "Product Intern", department Product Development, tied to res_users login hashirsaleemeoxsteam@gmail.com (user_id 184), source: eoxs-teams (res_users/hr_employee).

Checked every candidate table on eoxs-teams for records tied to that user/employee id:

| Source | Records found | Usable for scoring |
|---|---|---|
| project_task | 306 | Yes — the only substantive source |
| hr_attendance | 0 | No |
| crm_phonecall | 0 | No |
| mail_activity | 0 | No |
| eoxs_monitor_config | n/a — this is a server uptime monitor, not employee tracking | No |

So "all combined" collapses to one real source: project_task. Task span runs 2025-03-18 to 2026-08-19 (today), so it covers your full tenure to date, source: eoxs-teams project_task.

Stage breakdown for your 306 tasks, source: eoxs-teams project_task/project_task_type: Paid 172, Communicated 120, Assigned 4, Ongoing Tasks 2, Approved 2, Ready for Sandbox 2, Tickets 1, Waiting for Client's Reply 1, On Live 1, Functional Team 1.

Priority split: P5 (lowest urgency, presumably routine) 145, unset 79, P1 (highest) 57, P2 21, P4 4 — no P3 tasks recorded. billable_type is "no" across the board, so there's no billable-vs-nonbillable split to score on.

The task table also carries planned_hours/effective_hours (estimation accuracy), date_deadline/date_end (on-time delivery), and dev_team_incentive/qa_team_incentive fields — the incentive columns exist but I'm not pulling those values; they're compensation figures and not something I'll surface without you asking specifically for that.

One flag before I go further: I checked and found no eoxs-db data relevant here (correspondence/wiki doesn't track individual task metrics), so this stays entirely within eoxs-teams project_task. Also worth naming directly — 306 tasks with zero attendance, call, or activity log entries is itself informative: whatever your actual day-to-day work involves, it isn't being captured anywhere except this one Kanban board. Any score built from this data measures task-board activity, not your full working aspect.

Next: task-based parameters (volume, cycle time, estimation accuracy, priority mix, completion rate) — the actual candidate scoring metrics.
