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
