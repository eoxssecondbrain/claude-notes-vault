---
thread_name: "erp-build-team-project-task-fields"
user: "raj"
type: claude-chat
created: 2026-08-05
updated: 2026-08-05
---

User: Go to ERP and go into the project module. You can go into any project. Maybe you can go into the Build Team project. Open any task and understand all the headers and the sections in a task, like available hours, tags, all that stuff.

Assistant: Pulled this straight from EOXS Teams Live (project_project / project_task tables) rather than clicking through the UI — same data, faster.

## Build Team project (id 75)
Internal EOXS dev/build project. 1,062 active tasks. Timesheets enabled. No fixed start/end date — it's an ongoing pipeline, not a dated project.

## The kanban pipeline (17 stages)
Intake → Raj questions → Tabled → Task Pool → Assigned → Code QA/AI Review → Ready for Sandbox → On Sandbox/Functional QA → QA Failed → Revert code/Update Gitlab → QA Passed → Can be released → On Live → Email to be sent → Communicated → Approved → Paid (folded/archived)

This is the real dev lifecycle EOXS tracks build work through — not a generic to-do/doing/done board. Note there's a dedicated QA Failed → Revert code loop built into the stages themselves.

## Task-level fields, grouped

Identity
- name — task title
- description — rich text; often the actual spec (e.g. one task's description is a log-note thread naming exactly who gets dashboard access)
- parent_id — set if it's a subtask

Workflow / status
- stage_id — one of the 17 stages above
- kanban_state — normal / blocked / done, labeled per-stage via legend_normal / legend_blocked / legend_done (typically "In Progress" / "Blocked" / "Ready for Next Stage")
- priority — 0/1 star flag (996 unstarred vs 66 starred, Build Team-wide)
- priority_level — separate custom field, P1–P6. P1 is most common (411 tasks), P5 next (244), 207 tasks have none set
- fail_state / fail_state_qa — dev-side and QA-side revision tracking: developing / failed1 / failed2 on dev, QA / failed1 on QA side. This is how a task gets kicked back after failing QA instead of just sitting in a stage

People
- user_id — single assignee field, frequently null
- project_task_res_users_rel — the actual multi-assignee join table; a task can have more people on it than just user_id
- partner_id — the client the task is attributed to. Notably, internal Build Team tasks still carry a client (e.g. the example below is tagged to Sabre Alloys) — that's how internal dev work gets traced back to who it's for
- create_uid / write_uid — created by / last touched by

Hours and effort
- planned_hours, remaining_hours, effective_hours, total_hours_spent, subtask_effective_hours (rolled up from children), progress (%)
- date_deadline, date_assign, date_last_stage_update
- working_hours_open/close, working_days_open/close — Odoo's auto-tracked aging fields since the task opened

Tags (many-to-many via project_tags)
Used for three different things at once, no separate fields for each:
- Module area: Sales Module (77 tasks), Processing Module (32), Purchase Module (30), Inventory Management (23), Finance and Accounting (22), CRM (13), Core Product (12), Product and Product Variant (5), IT & Security (4), Shipping & Receiving (3), Contact Management (3), Advanced Analytics & Reporting (2)
- Skill level: Junior (58), Intern (23), Senior (15)
- Ad hoc priority/ownership: Priority 1/2/3, Super Urgent, Jesus Req, Raj

Example: task "Fix Sales Return Functionality" carries Sales Module, Core Product, Junior, and Priority 2 all at once.

Money
- dev_team_incentive, qa_team_incentive — per-task bonus in USD. One task has $3,000 dev / $600 QA attached — this reads like a bounty/piece-rate layer on top of salary, not standard Odoo
- currency_id

Billing
- billable / billable_type — both "no" on effectively every Build Team task (1,062 of 1,062). Confirms this project is pure internal cost, never billed out, even though tasks carry a partner_id
- sale_order_id / sale_line_id — null here; these would link a task to a sales order on a billable project

Dead weight
- custom_application_id, custom_subject_id, custom_application_line_id, custom_training_start_date/end_date, custom_training_employee_id, custom_is_application_task — these columns exist on every task row, but the tables they'd point to don't exist in this database. Looks like leftover fields from an HR recruitment/application customization bolted onto the task model and never cleaned up. Dead weight on a 1,000+ row table — worth a note to whoever owns the schema.

## Worked example — task 5044, "MTD Scorecard (Dashboard)"
- Stage: Tabled
- user_id: none, but Ron is on it via the multi-assignee table
- Client: Sabre Alloys
- Hours: 2 planned, 2 remaining, 0 effective — estimated, not started
- Deadline: 2026-01-16 — that's already past due as of today
- Incentive: $3,000 dev / $600 QA
- fail_state: developing
- Created by Ron, last touched by Hashir Saleem
- Description: a log-note thread restricting dashboard access to Tye, Jesus, Dave, Michael

Want me to pull the full field list for a different project (e.g. a client-facing implementation project) to see how billable/sale_order_id actually populate when a project is client-billed, versus Build Team's internal-only pattern?
