---
thread_name: "ov2-write-access-scoping"
user: "ayan"
type: claude-chat
created: 2026-07-28
updated: 2026-07-28
---

# Thread: OV2 Write Access Scoping for EOXS Teams Live

## User message 1
User is setting up write access (create/assign/update tasks) on the EOXS Teams Live MCP module for OV2's Support AI. Devop sent 9 scoping questions before granting write access. User asked Claude to answer them after inspecting the MCP link.

Devop's questions:
1. Use case - auto-create tasks from tickets? move stages? edit details? comments only?
2. Which project board(s) - specific or multiple?
3. Create new tasks or only update existing?
4. Which fields need write access (name, description, stage, deadline, assignee, tags, priority)?
5. Any fields that trigger webhooks/sync/notifications on their side?
6. Expected write volume/frequency (rate limits)?
7. Auto-commit writes or preview/confirmation step first?
8. Notification (Telegram/email) per write, or log sufficient?
9. Test against live EOXS Teams data or staging/mirror first?

## Claude's investigation
- Checked current EOXS Team Live MCP tools: only read-only tools exist currently (list_tables, describe_table, get_business_schema, query - SELECT only, capped 1000 rows, 30s timeout). No write tools exist yet.
- Attempted describe_table('project_task') and list_tables() - both returned "No approval received" errors, so could not pull live schema in this session.
- Per raj-eoxs-vault skill (Section on "Two different things live under client data"): project_task table filtered by partner is EOXS's own internal dev/support Kanban - bug fixes, feature requests, staffing status ("Need Developer"), QA/sandbox/live stages. This is the live, ongoing dev-task tracker (distinct from OV2's historical Implementation Kanban snapshots and distinct from each client's own operational Odoo).

## Claude's response
Provided draft answers to relay to the devop, based on current read-only-only access and the project_task table's known structure, while flagging which answers are Raj's judgment calls (volume, confirmation-step preference, notification channel, staging vs live) rather than technical facts Claude can determine unilaterally.
