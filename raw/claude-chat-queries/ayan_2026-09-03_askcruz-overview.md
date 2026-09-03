---
thread_name: "askcruz-overview"
user: "ayan"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

User: tell me about AskCruz.

Assistant: AskCruz is a live Odoo 13 (Community) instance — a separate connector from the main EOXS second-brain data. It's HR + Project + Training focused; the sale/purchase/accounting apps aren't installed, so no orders, invoices, or products live here.

Current state (2026-09-03):

- 63 active employees across 5 departments (includes HR, Product, Product Intern, and others)
- 11 active projects, 304 active tasks in `project_project`/`project_task`
- Custom training-management addon (`emp_training_*` tables) exists in schema but has zero rows currently — unused so far
- `res_partner` mixes contacts, clients, and employee-linked records; no customer/vendor activity since sale/purchase apps aren't installed

Access here is via `teams-askcruz` — raw SQL (read) plus 4 write tools (`create_task`, `update_task`, `move_task_stage`, `add_task_note`) that require a two-phase confirm before anything is written.

What do you want to look at — task backlog, a specific project's status, or headcount by department?
