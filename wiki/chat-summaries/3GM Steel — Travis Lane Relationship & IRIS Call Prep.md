---
title: "3GM Steel — Travis Lane Relationship & IRIS Call Prep"
type: chat-summary
sources: [raw/claude-chat-queries/raj_2026-07-29_travis-lane-3gm-relationship-research.md, raw/claude-chat-queries/raj_2026-07-30_travis-lane-3gm-iris-call-prep.md]
created: 2026-07-29
updated: 2026-07-30
---

# 3GM Steel — Travis Lane Relationship & IRIS Call Prep

_A deep-research relationship history on Travis Lane (CCO, 3GM Steel) followed one day later by prep, execution review, and follow-up drafting for the IRIS demo call that resulted from his dashboard/deal-desk requirements email._

## Summary

On 2026-07-29 Raj requested a full relationship history on Travis Lane of 3GM Steel. Travis first ran 3GM's original 2022 sales cycle as General Manager, left, returned in a BD role by Sept 2023, made a one-off introduction in Sept 2025, then re-entered in March 2026 as Chief Commercial Officer. His CCO dashboard request stalled for roughly five months (March–July 2026) due to undefined KPIs, before he broke silence on 2026-07-20 with a detailed two-part spec: a CCO executive dashboard plus a new, previously-undiscussed Deal Desk approval-workflow request, accompanied by a working HTML prototype with a live margin calculator he'd built himself. Raj replied 2026-07-21 pitching something "well beyond a static dashboard" and proposing a live demo.

On 2026-07-30, following the actual call (held 2026-07-29, 37 minutes, Fireflies-recorded), Raj reviewed the transcript and drafted a follow-up email. Raj ran a version of a pre-built call script largely from memory: named both requirements, deferred deal desk to a written follow-up, and ran a live IRIS demo against 3GM's real ERP data — including an unplanned live demo of EOXS's email-integrated "second brain" layer using non-3GM relationship data. Travis reacted well overall but flagged a data-context problem: the AI's margin output labeled Southeastern Outdoor Products and TMP Mac Metal Sales as loss accounts, when in fact one is an intentional scrap-dump account and the other an intercompany entity. Three action items were committed on the call (trial access, two pricing tiers, implementation timeline) and drafted into a single follow-up email in this session, with credentials and dollar figures left as placeholders. A previously scheduled "next Tuesday" call had by this point moved to Wednesday and had not yet occurred as of session end.

## Tribal Knowledge Extracted
- **The 2022-04-18 verbal 13.2% renewal discount offer** — Raj verbally offered Travis a 13.2% renewal discount for signing that week during the original 2022 deal, but the signed contract only reflects the standard 6% annual renewal-increase cap. This was never reconciled and exists only as a spoken promise — if Travis ever raises it, there's no written backup for either side. (source: raw/claude-chat-queries/raj_2026-07-29_travis-lane-3gm-relationship-research.md)
- **Ticket "Paid" stage ≠ deal status** — Ticket T07471 closing same-day as "Paid" is explicitly called out as an Odoo stage-routing artifact, not a real signal about where a deal stands. Anyone reading ticket history for this account needs to know not to infer deal progress from that field. (source: raw/claude-chat-queries/raj_2026-07-29_travis-lane-3gm-relationship-research.md)
- **Access-parity gap never confirmed closed** — Jessica Worley requested system-access parity for Travis on 2026-03-05 when he became CCO, but there is no record this was ever completed. This is a live, unresolved gap that could surface mid-pitch (e.g., the CCO dashboard needing module visibility he doesn't actually have) if not checked proactively. (source: raw/claude-chat-queries/raj_2026-07-29_travis-lane-3gm-relationship-research.md)
- **"Biggest loser" account flags can be misleading without business context** — the IRIS/AI margin analysis flagged Southeastern Outdoor Products and TMP Mac Metal Sales as loss accounts for 3GM. Southeastern is actually an intentional scrap/excess-inventory dump account (a client using it as a planned write-down channel, not a failing account), and TMP Mac Metal Sales is an intercompany entity, not a genuine external customer loss. The underlying numbers are correct but lack the qualitative business context a new user needs — this is a known interpretation trap for this account's data going forward, not a one-off glitch. (source: raw/claude-chat-queries/raj_2026-07-30_travis-lane-3gm-iris-call-prep.md)
- **3GM is creating a "VP of Trading Operations" role** — specifically to own a deal-desk function and stop deals "falling through the cracks." This is unwritten organizational context relevant to how the deferred deal-desk conversation should eventually be scoped and who it should ultimately be sold to/through. (source: raw/claude-chat-queries/raj_2026-07-30_travis-lane-3gm-iris-call-prep.md)
- **3GM ownership is "wary of investments in tech"** — Travis's own characterization of his ownership group, meaning any proposal to this account needs to lead with ROI/time-saved framing rather than a feature list. This shapes not just this deal but the tone EOXS should default to with 3GM generally. (source: raw/claude-chat-queries/raj_2026-07-30_travis-lane-3gm-iris-call-prep.md)
- **Why Travis went dark for months, twice** — his "still getting acclimated to the role" refrain (used on Ron's March/April follow-ups) and the 5-month dashboard stall trace to a real cause not visible from tickets alone: both the prior COO (Brittany) and prior sales manager (Cole) resigned earlier in 2026, forcing Travis into a combined CCO/de-facto-sales-manager role with heavy travel. Pattern-reading his silence as disengagement would be wrong — it's understaffing, and he tends to return with unusually well-prepared asks (a built prototype, not just a wish list). (source: raw/claude-chat-queries/raj_2026-07-30_travis-lane-3gm-iris-call-prep.md)
- **The "second brain" is not exclusive to 3GM, and Raj said so on the call** — during the live demo Raj stated outright that the email-integrated second-brain layer is already used by other customers and by EOXS itself. This forecloses any later "you'd be our first steel service center" exclusivity pitch — future messaging to Travis must stay consistent with what was actually said on the July 29 call. (source: raw/claude-chat-queries/raj_2026-07-30_travis-lane-3gm-iris-call-prep.md)

## Key Points
- 2022-03-25: First contact — discovery call with Travis as 3GM's GM; he ran the full Mar–Apr 2022 sales cycle himself.
- 2022-04-19: Original contract signed — $299/user net (15 users), $58,240 net implementation, 3-year term, 6% annual renewal-increase cap.
- 2023-09: Travis returned to 3GM in a BD role after time away.
- 2025-09-16: Travis made an introduction (Scott Begin → Lee Tyler, Priefert Manufacturing) but didn't join the call — connector, not participant.
- 2025-07-31 (per the 07-30 thread): 3GM signed a fresh 3-year contract, $4,759/month, 15 office users, 6% max renewal increase, locked through ~2028 — not a renewal-window account; current activity is a pure expansion sale.
- 2026-03-04: Travis re-entered as CCO, requested full system access and a custom CCO dashboard.
- 2026-03-05: Jessica Worley requested access parity for Travis (status unconfirmed — see Tribal Knowledge).
- 2026-03-25 to 2026-05-06: Dashboard request stalled; Ron and PM Humaira followed up without a real spec; Raj pitched AI capabilities May 6 with no response.
- 2026-07-20: Travis broke a four-month silence with a full two-part spec (CCO dashboard + new Deal Desk approval-workflow request, two scenarios, sample deal-ticket forms) plus a working HTML prototype with a live margin calculator.
- 2026-07-21: Raj replied proposing a live demo instead of email scoping, called the deal desk "very doable."
- 2026-07-29: The actual IRIS demo call happened (37 min, Fireflies-recorded, rajat@eoxs.com / travis@3gmsteel.com) — dashboard demoed live against 3GM's real ERP data, deal desk deferred to email, second-brain layer demoed live (non-3GM data).
- On the call, Raj referenced a case study: a Houston client replaced a planned $180K/year sales director hire with a $40K "AI sales director" deployment — landed well ("Wow" — Travis).
- Travis wants two separate pricing proposals: executive-team-only access and full sales team, as a deliberate phased-adoption approach for his tech-wary ownership.
- Travis agreed to 15-day trial access to the IRIS/Claude account for his own data cuts.
- Travis asked Raj for referrals for young BD hires in the steel industry — a personal/relationship ask, separate from the commercial track.
- Committed action items from the call: (1) send trial access credentials, (2) send two pricing proposals, (3) send an implementation timeline — all drafted into one follow-up email this session, with credentials and $ figures left as placeholders pending Raj's input.
- As of session end: the follow-up call originally slated "next Tuesday" had moved to Wednesday and had not yet occurred; deal desk remains fully deferred/unscoped, CFO not yet looped in.

## Sources
- raw/claude-chat-queries/raj_2026-07-29_travis-lane-3gm-relationship-research.md — Deep-research relationship timeline on Travis Lane/3GM Steel, sourced from OV2 wiki and tickets, plus strategic read on his negotiating pattern and the deal-desk expansion opportunity.
- raw/claude-chat-queries/raj_2026-07-30_travis-lane-3gm-iris-call-prep.md — Call-script planning, review of the actual 2026-07-29 IRIS demo call transcript, data-quality issue Travis flagged, and drafting of the three-item follow-up email.

## Candidate OV2 Cross-References
- Travis Lane (3GM Steel) contact page — the data-context caveat (Southeastern Outdoor Products / TMP Mac Metal Sales misread as losses) and the VP of Trading Operations role are durable account facts an OV2 contact/account page would likely want a pointer to.
- 3GM Steel — Ongoing Operations — the deferred Deal Desk workflow request and the two-tier pricing/phased-adoption plan are new expansion-sale developments beyond what OV2's existing account page likely reflects as of the March 2026 access-parity note.
