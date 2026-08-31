---
thread_name: "askcruz-pm-top5-priorities"
user: "ai_interns1"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

**User:** if you were the product manager for ask cruz what are the top 5 improvements you would prioritize and why? [50ft/Deep rigor selected]

**Assistant:** [Re-ran with verification against Eoxs-Data-general records rather than reusing the earlier unverified answer.]

1. Resolve the Cruz-frontend trust gap exposed by the 3GM deal (verified): 3GM's Company Brain deal closed (Travis confirmed Aug 19, reduced to 2-user scope), but the team's own Aug 17 decision was to run it on Claude's interface, not AskCruz's own Cruz frontend, for the client-facing side. Source: internal analysis of the 3GM proposal email thread + Aug 12 call transcript (id 2388).

2. Resolve the internal positioning contradiction (new finding, verified): AskCruz's own three reference docs disagree — product feature file says steel-vertical-specific, PMF guide says industry-agnostic and warns against vertical positioning, client-facing catalog is neutral. Flagged internally as an unresolved contradiction. Matters directly for the 3GM/Sabre joint GTM push already underway.

3. Fix the shared-password onboarding pattern (verified, repeat offense): 43 people onboarded onto askcruz.com mailboxes via one shared plaintext password, mirroring an identical earlier failure on the Cattr rollout.

4. Build the daily cash-risk/overdue-invoice/order-risk briefing as an owned, routed deliverable, not a broadcast alert (verified): EOXS's internal escalation-bot pattern is systemic (30-332+ day idle tasks, up to 70 ignored nudges, across multiple clients) — proof broadcast alerts without an owner don't work. The digest itself is a real, documented ask tied to Sabre Alloys' post-crisis recovery (AI Workers wiki page).

5. Retrieval-quality ("search context layer" noise) and multi-tenant isolation/prompt-injection testing gaps: explicitly flagged as UNVERIFIED this pass — no corroborating record surfaced under multiple search phrasings, unlike the prior (pre-compaction) answer which stated these as settled facts. Recommended a direct check with engineering instead of treating as confirmed.

Explicitly corrected the record: told the user the 3GM story was reframed with more accurate detail, and that two claims from the earlier answer in this same conversation could not be re-verified and should not have been asserted as fact.
