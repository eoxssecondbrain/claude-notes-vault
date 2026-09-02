---
thread_name: "eoxs-task-scheduler-thread-automation"
user: "aryan-bakshi"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

User: with the current mcps and connectors you have is it possible to create a scheduling  skill/program in calude which sees all the tasks in my name that just updated today or within the last hour and it creates a new thread with the task and what to do in that task

Assistant: Short answer: buildable, but it's an assembly of three separate pieces, and one of them only partly fits what you described.

**1. The trigger ("within the last hour")**
This chat can't run itself on a timer. The real mechanism is a Claude Cowork scheduled task — hourly is a supported cadence, each firing gets its own session, and it can use the same connectors you have here. So the "hourly check" part is a Cowork setup task, not something built inside a conversation.

**2. The data source ("tasks in my name that just updated") — verified, not assumed**
I checked the actual schema rather than guessing. Teams EOXS MCP (EOXS Team Live Odoo) has a real `project_task` table with `user_id` (assignee), `write_date` (last update), `stage_id`, `name`, `description`, `project_id`. That means a query like:

```sql
SELECT id, name, description, stage_id, write_date
FROM project_task
WHERE user_id = <your odoo user id>
  AND write_date >= now() - interval '1 hour'
  AND active;
```

genuinely answers "my tasks updated in the last hour." This is solid.

What does *not* work for this: EOXS Data General's `list_implementation_tasks`/`search_implementation_tasks` (the client-onboarding Kanban) only filters by `client` and `stage` — no assignee filter, no update-timestamp filter, per its own tool spec. If "tasks in my name" means that Kanban rather than internal EOXS Team project tasks, this can't be done cleanly — you'd be pulling everything per client and diffing yourself, which is not a real "last hour" check.

So the first open question: which system is "my tasks" — EOXS Team's internal `project_task`, or the client implementation Kanban?

**3. The output ("creates a new thread with the task and what to do")**
Nothing in this environment lets a process autonomously spawn N new separate chat windows. What's actually available — and it's the same pattern already used by the morning-brief setup here — is: one scheduled run produces one item per newly-updated task, each with a short work order and a link that opens a fresh, pre-loaded thread when you tap it. That's "new thread per task" in the only form that's real: launchable, not auto-opened. If you instead want a standing written record rather than something to click into, each task could be logged as a saved entry instead — history, not an actionable thread.

What I need to lock this down:
- Which task source counts as "my tasks" (internal project_task vs. client Kanban)
- Whether you want a clickable launch-item per task (opens a fresh thread on tap) or a saved log entry per task
