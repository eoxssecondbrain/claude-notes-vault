---
thread_name: "eoxs-kanban-pending-tasks-kartikey"
user: "Kartikey"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

User: So go through my all the task and tell me all my pending tasks  and tell me which task are pending and is there any task that i should give priority first

Assistant: [Asked clarifying question via ask_user_input_v0]: By "my tasks" do you mean your assigned items in the EOXS Odoo Implementation Kanban (across all 8 clients), or something else (e.g. AskCruz build tasks, a personal to-do list)?
Options: EOXS Odoo Implementation Kanban tasks assigned to me | AskCruz-related tasks | Something else — let me clarify

User selected: EOXS Odoo Implementation Kanban tasks assigned to me

Assistant: One pending task assigned to you in the Odoo Implementation Kanban across all 8 clients:

**Eastern States Steel — "Turn Off CRM Card Auto-Creation from Sales Orders"** (task 30360)
Stage: Code QA. Priority: Normal. No deadline.
Assigned to you Feb 10, 2026. You moved it to Code QA on Feb 17, 2026. No stage movement since — it's been sitting in Code QA for over 6 months.
Scope: disable the automation that auto-creates a CRM pipeline card from Sales Orders/Quotes, and remove the related automation that pushes that card to "Won."

Completed (for reference, not pending): "Packing Error Prevention" for Discount Pipe & Steel (task 30542).

That's the full set — I checked all 8 clients (3GM Steel, Brannon Steel, Discount Pipe & Steel, Eastern States Steel, Ohio Strip Steel, PPC Metals, RW Conklin Steel, Sabre Alloys) and only these two tasks have you as owner.

Priority call: there's only one candidate, so priority isn't really a decision — it's whether it's actually stuck or just forgotten in QA. A task sitting 6 months in Code QA with no chatter since Feb 17 either means it's blocked on someone else (QA reviewer, deployment) or it fell off everyone's radar. Worth a 2-minute check with whoever owns Code QA review before you assume it needs your action.

Caveat: this only covers tasks tracked in the Odoo Implementation Kanban with you as the named owner. If you have dev work assigned informally (Slack, direct requests from Dhrup, verbal) it won't show up here — that system tracks client-facing implementation items, not internal engineering backlog.

Assistant: The Threads OV save tool isn't exposed among available connector tools right now (only EOXS Data General, EOXS Team Live, and claude-in-chrome are), so I can't call save_chat_transcript this turn — the Threads OV MCP connector isn't currently connected/loaded in this conversation, unlike what your preferences assume. I'm flagging that rather than silently skipping it.

User: okay and can you tell me in which task i worked a day before

Assistant: Based on what I can see in the Odoo Implementation Kanban, nothing — no task activity from you on Aug 19, 2026.

The only task assigned to you in the system (30360 — Turn Off CRM Card Auto-Creation, Eastern States Steel) hasn't had any chatter or stage change since Feb 17, 2026. A search of call transcripts for "Kartikey" also turns up nothing from yesterday — the closest match is a call from May 2026, and it's actually a different person (Kartikey Sharma).

Caveat: I can only search task chatter by name/description text and owner field, not "who commented on this task" across the whole system. If you worked on something informally — Slack, a task where someone else is listed as nominal owner, or work not logged in Odoo at all — it won't surface here. If you can point me to a client or task name, I can pull that specific record directly.
