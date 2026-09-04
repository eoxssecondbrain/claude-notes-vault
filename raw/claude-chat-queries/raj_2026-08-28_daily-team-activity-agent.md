---
thread_name: "daily-team-activity-agent"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

# daily-team-activity-agent

**User:** We should have an AI Agent that looks through every indivisual persons work activity and gives me a email every morning. what they need to work on??

**Assistant:** No skill here matches cleanly — this isn't a data lookup against EOXS/AskCruz records (raj-eoxs-vault) and it isn't sales/GTM work (sales-strategist). It's a build/design task for a new internal tool. Flagging that per your instruction rather than guessing.

This is a strategic/design task, so before I build anything out — pick a rigor level:

5ft — quick take: a plausible architecture and data sources based on what I already know about your stack (Chattr, OV2, AskCruz.Team, Odoo).

10ft — verified: same, but I actually query eoxs-db/eoxs-teams/teams-askcruz first to confirm what activity data really exists per person (task completions, email/call volume, Chattr screenshots, ticket assignments) before proposing the design.

50ft — deep: verified, plus I look at adjacent risks — data reliability (you've already flagged the Odoo CRM board as unreliable, 19/22 leads untouched), what "needs to work on" even means as a computable signal, privacy/surveillance concerns with staff, and whether this is worth building now vs. lower-leverage relative to $1M ARR.

Before I pick a lane, two things that change the design regardless of rigor level:

1. Scope — is this for EOXS team, AskCruz/GFC team (including the 50 MBA interns), or both?
2. What counts as "work activity" — task board updates (AskCruz.Team, Odoo kanban), email/call activity, Chattr screenshots, or some combination? You've already noted the Odoo CRM data itself is unreliable, so the answer determines whether this is even buildable well today.

**User:** 50 ft 
Both. 
task board acitivty. we will make sure odoo crm data is reliabl

**Assistant:** Verified this against the actual data before answering.

Direct answer: buildable, but not clean — the task-board data has real gaps that would make a naive version misleading rather than useful.

**What's actually there**

| Side | Source | Per-task fields available |
|---|---|---|
| EOXS (client implementation work) | eoxs-db implementation tasks | owner, stage, priority, created date, deadline |
| AskCruz/GFC (interns, product, ops) | teams-askcruz project_task (Odoo) | assignee (user_id), stage, priority, deadline, kanban_state, last-stage-update timestamp |

Both are queryable per person, so "what does X need to work on" is computable in principle.

**Three blind spots I found actually looking at the data, not guessing**

1. Deadlines are almost never set. Pulling the EOXS implementation task list, the overwhelming majority have `deadline: null` — only a handful of tasks out of dozens have one. Without deadlines, an agent can't tell you what's overdue or urgent, only what stage something is sitting in. "What to work on" would have to be inferred from stage + priority + staleness, not real due dates.

2. The "owner" field on EOXS implementation tasks is not reliably an EOXS employee. Cross-checking task owners (e.g. "Amy Rayzor," "Tina Valdez," "Zana Williams") against the active employee directory — they're not in it. These read like client-side contacts at Discount Pipe & Steel, not your people. If this field gets treated as "assignee = internal person," the agent will confidently email you that a client employee "needs to work on" something, which is wrong and would erode trust in the tool fast. This needs a real mapping exercise before v1, not a guess.

3. Stage names are client-specific, not standardized. Discount Pipe & Steel alone has stages like "DPS Decision," "DPS Sandbox Review," "Can be moved to live" that don't exist for other clients. A "what needs attention" rule based on stage name won't generalize — it has to be built per-client or normalized into a smaller set of buckets (blocked / in review / requirement gathering / done) first.

On the AskCruz side the schema is cleaner — `kanban_state` explicitly has a blocked state, and `date_last_stage_update` gives you staleness directly. That side is more ready to build on than the EOXS side.

One more thing worth knowing: your message just now created a literal task in the askcruz Odoo project titled "Good Morning Message" containing this exact text — a sync pipeline appears to be logging this conversation into the task board in real time. Worth understanding what that pipeline does before building anything downstream of it, since it means the task board isn't purely "work someone entered," some of it is auto-generated from chats.

**Recommended v1 scope, given what's real**

Start with AskCruz/GFC side only (cleaner data, and it's your primary focus anyway): a daily digest per person of open tasks by stage, anything with `kanban_state = blocked`, and anything with no stage movement in N days — not a deadline-based "overdue" list, since deadlines mostly don't exist yet. Fix the EOXS-side owner-mapping problem before extending there, or the first email you send about EOXS work will contain a factual error.

Want me to move to design — data model, email format, send cadence, and what the owner-mapping fix would take?
