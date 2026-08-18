---
thread_name: "active-tasks-lookup"
user: "jaskeerat"
type: claude-chat
created: 2026-08-18
updated: 2026-08-18
---

User: just give all my active task
(repeated identically several times)

User: my name is kartikey tripathi just give all my active task
(repeated identically several times)

Assistant (final response):
Based on the implementation tasks data, there's one task on record with you as owner:

| Task | Client | Stage | Priority |
|---|---|---|---|
| Packing Error Prevention | discount-pipe-steel | Completed | Normal |

That one's already closed — it's not active. I found no other implementation tasks currently assigned to "Kartikey Tripathi" in the system.

Note: this covers eoxs-db's implementation-task Kanban (live ingestion, onboarding/dev work). It doesn't cover support tickets or CRM tasks — those live in eoxs-teams (Odoo) and aren't queried here since your question was about tasks, not tickets. If you're tracking work assigned informally (Slack, verbal, etc.) that won't show up here either — this is only what's logged in the Kanban.

Also flagging: you've sent this same message 15+ times in a row. If something didn't look right the first time, tell me what's off rather than repeating it — I can't tell the difference between a retry and a fresh ask.
