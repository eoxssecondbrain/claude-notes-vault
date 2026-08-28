---
thread_name: "dps-eoxs-relationship-status"
user: "aryan-bakshi"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

USER: tell me how is the relationship between eoxs and discount pipe and steel rn
and what problems are they facing

ASSISTANT: I have a solid picture. Here's the state of the EOXS ↔ Discount Pipe & Steel (DPS) relationship as of late August 2026.

**Relationship status: strained, active churn risk.**

- On 2026-08-17, a DPS complaint reached Ron J and Rajat Jain secondhand — via Ryan Capinski at Eastern States Steel — that Amy Rayzor was "very frustrated," "about at their wits end," and actively researching other EOXS clients to compare experiences as due-diligence toward possibly switching systems, specifically over the reservation/double-selling bug.
- On 2026-08-18, in a direct check-in call, Amy Rayzor raised the ROI question outright — whether continued investment is justified given core functions "not working completely." This echoes the same complaint from an April 2026 call. Ron separately proposed shifting more responsibility to DPS's own team ("delegation"); Amy's response was "that's fair," read as receptive rather than resistant.
- Wiki tags on the reservation escalation page include churn-risk and payment-dispute.

**Concrete problems, in rough order of severity:**

1. Reservation / double-selling bug — the headline issue. Long-running, recurring across the reservation function; triggered emergency live-push prioritization for DPS ahead of PPC Metals, Sabre Alloys, and Greer Steel the week of Aug 17. One fix was reportedly lost to an accidental staging-server deletion during a pivot to fix a packing list issue (unverified detail from the call).
2. Packing list / control-tag issues — a large, recurring cluster: quantity discrepancies, duplicate lines, wrong SO-line matching against tags, confirmation failures. This is the single largest category of open wiki pages for DPS.
3. Billing dispute — DPS's accounting team disputed a "Bank Reconciliation Module" line item on the Aug invoice, saying it was never approved for activation. EOXS (Ron) held firm citing a Dec 2025 approval thread, and per the Aug 14 update, the matter appears to have moved toward collections without confirmed client sign-off — an open sore alongside the technical complaints.
4. Stalled onboarding deliverables — Aircall video, Stripe video, and DPS functional training videos flagged by an internal stall-detection bot as stagnant for 3–8+ weeks, with prior escalations to Rajat going unanswered.
5. Operations access request pending — as of Aug 26–28, DPS (Austin Rayzor) asked for write access to the DPS environment via an MCP connector so their own external load-check tool could bypass EOXS's tag-matching errors. Ron escalated internally to Raj and asked for an effort estimate before deciding — unresolved as of the latest data.
6. Accounting/reporting gaps — separate open pages note discrepancies vs. QuickBooks and unresolved reporting filter-persistence issues, one of which was marked "Done" then contradicted.

**Net read:** this is EOXS's client with the largest concentration of open bug/gap pages in the wiki, and it's now producing direct sentiment/ROI pushback and one live billing dispute simultaneously — not just a technical backlog. The emergency reservation push and Ron's delegation proposal look like retention moves in response.

Sources: EOXS Data General wiki pages (client:discount-pipe-steel tag cluster), fathom call 2398 (Aug 18 check-in), email threads 66482/66483/66499/66500/66610/66616/66617/65996/66137 (Aug reservation escalation), email 60912 (billing dispute), email thread 67473 (Aug 26–28 ops blockers).
