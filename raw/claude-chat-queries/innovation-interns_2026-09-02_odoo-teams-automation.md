---
thread_name: "odoo-teams-automation"
user: "innovation_interns"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

User asked about automating an Odoo (teams.askcruz.com, Module 13 / Odoo 13) board. Clarified requirements: daily end-of-day email report showing which team members logged a note on assigned tasks vs who didn't, scope = all assigned tasks across team, "logged" = specific log note field, action = auto-reminder to non-loggers, timing = 6PM EST / 4AM IST.

Claude checked EOXS-TEAMS-MCP (read-only SQL to EOXS Team Live Odoo 13 DB) and confirmed feasibility:
- project_task table has user_id (assignee) field.
- mail_message table has model/res_id/create_date, allowing filtering for log notes on project.task records by date.
- base_automation table exists, confirming Automated Actions module is installed.

Proposed build: Scheduled Action (ir.cron) at 4AM IST -> server action Python code checks each assigned task for a same-day log note in mail_message -> splits assignees into logged/not-logged -> sends summary email + individual reminder emails to non-loggers.

Caveat given to user: MCP DB access is read-only (SELECT only), so Claude can verify data/query logic but cannot create the Automated Action/cron/email templates in Odoo itself — needs admin/Studio access or a developer.

Open question asked to user: do they have Odoo admin/Studio access themselves, or does someone else need to build it.
