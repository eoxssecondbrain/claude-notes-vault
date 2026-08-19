---
thread_name: "daily-employee-performance-email-automation"
user: "Harsimran"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

ction, and any credential the user pasted has been redacted deliberately.

**User:** Requested an automation that emails Raj daily about every employee's performance — time worked, productivity, performance, tasks performed — so Raj can evaluate them. Explicitly asked that performance be measured by **quality of work, not quantity**. Data to be retrieved from the project management tools of Ask Cruz and EOXS.

**User (mid-turn):** Supplied the sending mailbox `harsimran@askcruz.com` together with an account password. *(Credential redacted — not recorded, not used.)*

**Assistant:** Investigated both reachable data sources before building anything, then reported findings and asked four blocking questions.

### Credential handling
Declined to use the supplied account password. Recommended immediate rotation, since it was pasted in plaintext into a chat log. Noted that an account password is the wrong mechanism for automated sending in any case — `askcruz.com` runs on mailcow, which supports **app passwords scoped to SMTP only**. Nothing was stored.

### Findings

**1. The automation already exists, and Raj shut it down two days prior.**
A "Weekly AskCruz Board Scrum Report" already produced per-person scorecards, gap lists and anomalies from live Odoo data (10-point rubric: Ack / Movement / Completions / Depth / Scope). On **2026-08-17 15:17 UTC, Rajat Jain replied "Shut this automation down, please."** A new report nevertheless self-generated on 2026-08-18 with expanded scope (6 boards instead of 1); the wiki records this as an unexplained contradiction.

Raj's own report had flagged the design flaw: every board update that day was authored by Raj himself chasing non-responsive assignees, so the report stated the scores were *"measuring your nagging activity, not team engagement."*

**2. The Ask Cruz board is not reachable.**
It lives in a separate Odoo instance (`teams-askcruz`, project_id 6, ~39 active tasks). The available SQL connector reaches only **EOXS Team Live** (`Eoxteams_12Feb24`). Confirmed by querying `project_project` — no AskCruz project exists in the reachable DB.

**3. Hours worked does not exist in any reachable system.**
- `hr_attendance` — 3 rows total, latest 2024-08-27
- `project_task.effective_hours` — 0.0 for every assignee
- `account_analytic_line` — 878 rows, uniform 8.0-hour monthly accrual entries, not tracked work
- `hr_timesheet_sheet_sheet` — 1 row
- `eoxs_monitor_config` — a URL uptime monitor, unrelated to employees

**4. Quality signals that do exist in EOXS Team Live** (`project_task`):
`fail_state='failed1'` (dev failure), the "QA Failed" stage, `kanban_state='blocked'`, `priority_level` P1–P5 (weight of work taken on), `date_deadline` vs actual, stage regression (rework), and chatter note depth via `mail_message` on model `project.task`.

### Verification against real data
A 7-day quality query was run and produced a ranking that inverts a pure volume ranking:

| Person | Stage moves | Dev/QA fails | Avg note length | Reading |
|---|---|---|---|---|
| Aryan Bakshi | 11 | 0 | 33 chars | High volume, near-zero documented substance |
| G. Nijamuddin | 4 | 1 + 1 | 392 chars | Low volume, deep notes, but quality failures |
| Humaira Zainab | 7 | 0 | 39 chars | 175 notes across 84 tasks — breadth, thin depth |
| Hashir Saleem | 13 | 0 | 251 chars | Volume and substance together |

This confirms the quality-over-quantity approach the user asked for is achievable on the reachable data.

### Four questions put to the user
1. **Raj's shutdown request** — proceed anyway, route to Harsimran for review first, switch to weekly, or build as originally asked?
2. **Ask Cruz data** — EOXS only for now, arrange a read-only connector for `teams-askcruz`, or use Odoo's external API with an API key?
3. **Time worked** — drop hours in favour of cycle-time signals, connect the real tracking tool, or use the sparse timesheet data labelled as incomplete?
4. **Email delivery** — mailcow SMTP app password, generate a file for manual forwarding, or send via Odoo's existing outgoing mail server?

**Outcome:** The user dismissed all four questions without answering. No automation was created, no scheduled task registered, no email sent, no credential stored. Work is paused pending further instruction.
