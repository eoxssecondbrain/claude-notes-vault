---
thread_name: "work-activity-digest-agent"
user: "kriti-jain"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

[User, initial message, with attached screenshot showing a message from Raj]:
"We should have an AI Agent that looks through every indivisual persons work activity and give me a email every morning. what they need to work on??

Pick up the conversation from here.

https://claude.ai/share/759e4537-22ee-40d5-b394-90650df1fb49"

Followed by: "this is what raj wants me to build. lets start. but first we will see how this can be done, what all is needed. and a full plan"

[Claude]: Attempted to fetch the shared claude.ai link for prior context — it returned only page metadata, no actual conversation content (likely requires an authenticated session to render). Asked the user three clarifying questions via AskUserQuestion:
1. How to proceed given the share link didn't load — paste key points vs proceed fresh.
2. Rigor level per standing preference (5ft/10ft/50ft/100ft).
3. Which systems count as the source of truth for "work activity" (Ask Cruz, EOXS Teams DB, Slack, other) — multi-select.

[User answers]: "Proceed fresh" / "50ft — Deep (recommended)" / "Ask Cruz (AskCruz CRM/tasks), EOXS Teams DB / EOXS data"

[Claude]: Ran a 50ft-deep data audit before building the plan:
- Pulled AskCruz's business schema (Odoo 13, HR + Project + Training focused; sale/purchase/account apps not installed).
- Pulled EOXS general connector's index: 1,453 wiki pages, 30,474 email threads (only 3 shared inboxes — raj_gmail, ron_gmail, remya_gmail, plus support_zoho — not per-employee), 2,201 Fireflies + 140 Fathom calls, 8 clients, 824 implementation tasks.
- Described project_task, mail_activity, and hr_employee tables in AskCruz — confirmed project_task has user_id, stage_id, write_date, date_deadline (real per-person staleness/overdue signal).
- Pulled EOXS list_implementation_tasks — confirmed owner, stage, priority, deadline, created-date per task across 8 clients, but no last-updated timestamp exposed and some owners are "Dev team" rather than a person.
- Ran a live query against AskCruz project_task joined to hr_employee: 63 active employees; sample per-assignee breakdown of open/stale(>3d)/overdue tasks, e.g. Ayan Dutta 146 open / 106 stale / 25 overdue, 79 tasks unassigned, Nidhi Rana 24/20/3, Isha Bisht 18/12/0, Jaskeerat Singh 11/5/0.

Then built and published an HTML plan artifact ("Work Activity Digest", https://claude.ai/code/artifact/2588c715-1203-4b1e-a9f1-395812058e28) covering:
1. The ask, precisely — restated Raj's request, flagged two decisions that change the shape of the system: who receives the email (manager digest to Kriti vs. per-person nudges — very different trust/privacy profile), and what "needs to work on" means (no field says this directly — has to be inferred from proxies). Assumption made to keep moving: manager digest to Kriti only (flagged as decision D1).
2. Data audit — table of AskCruz vs EOXS implementation tasks vs EOXS email/calls vs Slack, rated per-person availability, signal quality, and gaps for each; included the real sample per-assignee stats above.
3. Signal model — three proxy signals (Overdue, Stale >Nd, High-priority idle) with definitions, what each catches, and false-positive risk; flagged that "stale" is the weakest signal but doing most of the work in the sample data, and needs a "blocked/waiting on client" escape hatch or it will misfire constantly.
4. Architecture — table mapping each pipeline step (cron trigger via create_trigger, DB pulls via Ask_cruz_mcp/EOXS_data_genaral, scoring, email composition, delivery) to what's already available vs. missing; flagged that outbound email sending is not a confirmed-connected capability and is the one real dependency gap.
5. Risks — surveillance-shaped tool if rolled out without care; data quality (79 unassigned AskCruz tasks, "Dev team" as an EOXS owner) undercutting credibility; stale ≠ blocked; no ID join between AskCruz's hr_employee and EOXS's free-text owner field (name-string match only).
6. Open decisions needed before Phase 2 — D1 (who receives it), D2 (which teams in scope for v1 — recommended starting with AskCruz only), D3 (staleness threshold — recommend per-stage, not one flat number), D4 (delivery channel for the pilot given the email gap — Slack or a saved doc as an immediate fallback).
7. Phased build order — Phase 0 data audit (done), Phase 1 manual MVP against AskCruz only (no new tools needed), Phase 2 automate pull+compose via scheduled task delivering to Slack/doc, Phase 3 turn on email once a connector exists, Phase 4 fix data problems the pilot exposes, Phase 5 expand sources (Slack activity, per-person email/call) later and optionally.

Final message to user: summarized that the plan artifact is published, restated the core open decision (who receives it — Kriti-only manager digest assumed) and the one real blocker (no confirmed email-send connector), and that Phase 1 (a manual run against AskCruz data) can start immediately with zero new tooling.
