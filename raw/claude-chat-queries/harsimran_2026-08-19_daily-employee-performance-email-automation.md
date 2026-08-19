---
thread_name: "daily-employee-performance-email-automation"
user: "Harsimran"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

## Session: Daily Employee Performance Email Automation (continued)

**User:** Asked whether the AskCruz teams Odoo instance is now connected.

**Assistant:** Verified three ways — no. The SQL connector still points at `Eoxteams_12Feb24` (EOXS Team Live); searching `project_project` for AskCruz / MBA / Idea Board / Hiring Funnels returned 0 of 61 projects; the connector registry showed no new installs. Offered two routes to connect it: (A) a read-only Postgres connector for `teams-askcruz`, matching how eoxs-teams is already wired, or (B) Odoo external API via XML-RPC needing instance URL, database name, and an Odoo API key (not an account password). Noted that since the existing scrum-report automation demonstrably reads `teams-askcruz` live, access already exists somewhere and tracing that wiring may be faster than building a new path.

**User:** "ok create a report from what ever data you have"

**User (mid-turn):** "also add a parameter of catter weekly timing of employees"

**Assistant:** Built the report from EOXS Team Live and investigated Cattr before answering.

### Cattr finding
Cattr is confirmed as the time-tracking tool behind EOXS working-hours figures, but it is separate SaaS — an `information_schema` sweep for `%cattr%`/`%track%`/`%attendance%`/`%timesheet%`/`%screenshot%` tables found no Cattr table in Odoo. Per-employee hours are not readable on this connection. Odoo cannot substitute: `hr_attendance` has 3 rows total (latest Aug 2024) and every task's `effective_hours` is 0.0.

Two structural facts surfaced that change the request:
- **A weekly Cattr report already reaches Raj.** Isha Bisht (`isha@eoxsteam.com`) sends an automated "EOXS HR Automation — Weekly Team Report" most Mondays covering Sun–Sat, per-employee worked hours for ~29 employees; most recent covers 2026-08-10 to 2026-08-16. Adding hours would duplicate an existing automation.
- **Cattr reliability is documented as poor.** Tracking has malfunctioned for at least five employees — Humaira Zainab six times across six weeks through 2026-08-13, plus Chandvi Gupta, Harsimran Singh and Vithal.

Both were written into the report so the omission is not read as an oversight.

### Report produced
`employee-quality-report-2026-08-20.html` — window 13–20 Aug 2026, 33 active employees with linked user accounts, 805 open tasks across 12 boards. Delivered as a local HTML file (not published externally, given confidentiality).

Deliberate design choice: no ranking by task count, and no single collapsed per-person score. Volume on these boards is an assignment artifact (EOXS Support auto-assigns in bulk), so a throughput ranking would reward proximity to the intake queue.

### Headline finding
**Of 278 human log notes written this week on these employees' tasks, only 112 (40%) were written by the task's own owner.** The other 166 came from someone else chasing status. This directly addresses Raj's own 2026-08-17 objection that the prior report was "measuring your nagging activity, not team engagement" — and it is exactly what a task-count report hides.

### Where quantity and quality diverge
- **Kartikey Tripathi** — closed 9 tasks, most on the team, but owns 4 of 7 open dev failures and 6 of 11 overdue items (four P1). Only 3 of 20 notes on his tasks are his. First on throughput, last on durability.
- **Aryan Bakshi** — 13 stage moves looks busy, but 28 of 32 notes on his tasks were authored by others (worst ratio on team), own average 71 chars, 29 tasks never once commented on, 17 open P1/P2.
- **G. Nijamuddin** — weak on volume (20 open, 3 done) but deepest notes on the team by a wide margin (468 chars avg). Different, more coachable problem: work comes back — 2 dev fails, 1 QA fail, 2 overdue.
- **Dhrup Kumar Singh** (senior developer) — zero self-authored notes against 7 by others, no stage moves, QA failure sitting 72 days. Most significant gap in the report.
- **Isha Bisht** — 100% ownership (11 self notes, zero chased), 6 completions, nothing stale or silent.
- **Vithal / Rohit Chand / Vaibhav Jain** — strong ownership (59–70%) and note depth (257–297 chars) at small load.

### Flagged as data problems, not people problems
- Sheenam Rawat (173 open) and Ron (72 open) carry stale backlog — 236-day and 322-day average staleness, oldest untouched item 904 days, Ron with 48 silent tasks. Reading these counts as workload would be wrong; recommended backlog purge before any performance judgement.
- **Seven active employees hold zero tasks** on this instance (Adefolabi, Aditya Kumar Yadav, Arpita, Danish Lari, Jaskeerat Singh, Priyanshu Sinha, Ryan) — likely working on `teams-askcruz`. An assignment-process gap, not a performance finding.

### Report contents
Team signal tiles (21 completions, 40% self-authored, 136 silent open tasks = 17% of board, 22 open quality exceptions); per-person quality read grouped into Strong / Mixed / Concern / Light load / No tasks; a 22-row open quality-exceptions register naming each failed, blocked or overdue task with stage, priority and days since last move; a "what this report cannot see" section covering Cattr and the AskCruz board; and a method section documenting the ownership ratio, the depth proxy's weakness, and what was deliberately excluded.

**Open question to user:** whether to now turn this into the scheduled daily job, or adjust the rubric first. Still unresolved from earlier: Raj's 2026-08-17 shutdown request, and the email delivery mechanism.
