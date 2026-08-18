---
title: "Sabre Alloys — Account History, Payment Discipline & AskCruz Proposal"
type: chat-summary
sources: [raw/claude-chat-queries/raj_2026-07-27_sabre-alloys-mrr-lookup.md, raw/claude-chat-queries/raj_2026-07-28_sabre-alloys-complete-info.md, raw/claude-chat-queries/raj_2026-07-29_sabre-alloys-contacts.md, raw/claude-chat-queries/raj_2026-08-04_sabre-alloys-payment-delay.md, raw/claude-chat-queries/raj_2026-07-31_sabre-alloys-dispute-time-headspace.md, raw/claude-chat-queries/ron_2026-08-18_sabre-alloys-askcruz-proposal.md]
created: 2026-07-27
updated: 2026-08-18
---

# Sabre Alloys — Account History, Payment Discipline & AskCruz Proposal

_Six Claude conversations (Jul 27 – Aug 18, 2026) tracking Sabre Alloys as EOXS's largest account: MRR and contacts, chronic late payment and Raj's personal script to Juan, the time/headspace cost of the Feb 2026 outage claim dispute, and the newly-pitched AskCruz AI Transformation proposal._

## Summary

Sabre Alloys is EOXS's single largest client: $10,970/month MRR (28 users, up from $4,080/month at 12 users), ~$342K total revenue since Jan 2024, contracted to a December 2026 renewal. Contact structure centers on three actively-engaged people — Tye Webb (Ops/COO, primary contact, 477 threads), Michael Mercadante (CEO), and Juan Deshon (fractional CFO, finance) — with Charles White (management, executive dashboard user, main Fireflies call contact) more operationally involved than his title implies, and Christi Deaton (Accounting, 231 threads) the contact who triggered a Sep 2024 AR crisis.

Payment has been chronically late — invoices routinely require multiple reminders, one was still unpaid at 171 days past due as of Jul 22, and two invoices were already 58 and 28 days overdue on Mar 31, 2026, predating the Feb 2026 outage dispute entirely. This recurring lateness surfaces in Raj's own investor board meetings; investors pushed him to adopt a 7-day-late-service-stop policy, which he refused. On Aug 4, Raj asked Claude to help him raise this "softly" with Juan Deshon — notably clarified mid-conversation that Juan is an operations contact, not AP, so the ask was reframed from "pay faster" to "get me the AP owner's name and the monthly cutoff date."

Separately, a Feb 11 – Jun 22, 2026 server-outage dispute consumed an estimated 20-28 hours of Raj's direct personal time: an $80K claim from Sabre against EOXS, negotiated down to a $25K + $1,000/month (25 months) settlement liability owed BY EOXS to Sabre. This escalated to board-level mediation (Robert Dunn) — a level of personal exposure not used for any other Sabre crisis (not the $883K balance sheet mismatch, not the $600K valuation gap) — and included a self-inflicted second outage (8-9 days, invoice delivery via Grexo) caused by the rushed security-hardening fix that followed the first incident.

Most recently, Raj pitched a 6-week AskCruz "AI Transformation" proposal to Sabre (call held Aug 13, 2026; not yet signed) covering all 15 Sabre users at $34,500 one-time + $3,900/month, alongside a separately-floated $1,000/month "IRIS Pro" AI add-on (proposed Jul 2, 2026, still pending approval as of the MRR lookup) — these are two distinct AI upsell tracks and should not be conflated.

## Tribal Knowledge Extracted
- **"IRIS Pro" AI add-on ($1,000/month) is NOT the same thing as the AskCruz AI Transformation proposal ($3,900/month + $34,500 one-time).** Two separate AI upsell efforts floated to Sabre roughly six weeks apart — IRIS Pro (proposed Jul 2, still pending as of Jul 27) is smaller-scope and predates AskCruz (pitched Aug 13). Neither transcript cross-references the other; this distinction exists only by piecing the two threads together. (source: raj_2026-07-27_sabre-alloys-mrr-lookup.md; ron_2026-08-18_sabre-alloys-askcruz-proposal.md)
- **The Aug 14 proposal email to Sabre had zero attachments — the only correctly-attached copy of the AskCruz proposal was sent by Ron to Raj's own inbox, never to Michael or Tye.** As of Aug 18 it is unverified whether Sabre's decision-makers have ever actually seen the proposal document, despite a call having already been held to "walk through" it. This is an open, unresolved gap, not a resolved fact. (source: ron_2026-08-18_sabre-alloys-askcruz-proposal.md)
- **Juan Deshon cannot approve or release Sabre's payments** — he's a fractional-CFO/operations contact on cash forecasting, not AP. Any late-payment conversation with him needs to be framed as "get me a name and a cutoff date," not "please pay faster," or it produces a friendly conversation with zero mechanism change. This distinction came from Claude flagging it before drafting Raj's script, not from any written record of Sabre's org chart. (source: raj_2026-08-04_sabre-alloys-payment-delay.md)
- **Sabre's Feb 2026 server incident was never resolved internally as either "infrastructure issue" or "breach" — Raj used both terms at different points and it was never reconciled to one characterization.** Flagged as a live risk: if Sabre or another client asks directly later, there's no single internal answer on record. (source: raj_2026-07-31_sabre-alloys-dispute-time-headspace.md)
- **Odoo's actual "closed" ticket indicator is the `fold=true` marker on `project_task_type`, not guessing from stage names like "Paid"/"Approved."** A general Odoo-querying convention surfaced while pulling PPC Metals ticket counts in the same thread as the Sabre MRR lookup — not Sabre-specific, but worth capturing since it's an unwritten rule about how to query this system correctly. (source: raj_2026-07-27_sabre-alloys-mrr-lookup.md)
- **The $1,000/month settlement Sabre is owed (25 months, from the Feb 2026 outage) is a liability EOXS owes TO Sabre — the inverse direction of the $10,970 MRR Sabre owes EOXS.** Conflating the two when reporting "Sabre revenue" would overstate the account's net economics. (source: raj_2026-07-27_sabre-alloys-mrr-lookup.md; raj_2026-07-31_sabre-alloys-dispute-time-headspace.md)

## Key Points
- MRR: $10,970/month, 28 users (up from $4,080/month at 12 users); source OV2 entity page updated 2026-07-22, corroborated by a Feb 2026 outage-settlement internal batch note citing $10K MRR.
- Billing has slipped to 30+ days in arrears as a standing pattern (noted Jul 27, 2026).
- Settlement liability: $25K + $1,000/month for 25 months, owed BY EOXS to Sabre, from the Feb 2026 outage claim (Sabre's original ask was $80K).
- Total revenue since Jan 2024: ~$342K; renewal window December 2026.
- Charles White (cwhite@sabrealloys.com): 117 total interactions (109 email threads + 8 calls); recurring voice behind escalating packing-list-to-invoice quantity-mismatch complaints; involved in server migration/processing-speed escalations.
- Primary contact triad: Tye Webb (Ops/COO, 477 threads), Michael Mercadante (CEO, submitted 20-category AI requirements Jun 2026), Juan Deshon (fractional CFO, built cash-forecasting framework).
- Christi Deaton (Accounting, 231 threads) triggered an AR crisis in Sep 2024.
- One invoice was still unpaid at 171 days past due as of 2026-07-22; two others were 58 and 28 days overdue as of 2026-03-31 — predating the Feb 2026 outage dispute.
- Investor pressure: in the week before Aug 4, 2026, Raj's investors demanded a 7-day-late-service-stop policy for Sabre; Raj refused.
- Claim dispute estimated time cost: 20-28 hours of Raj's direct personal time over Feb 11 – Jun 22, 2026, concentrated in three bursts (crisis week, itemized-update period, negotiation period).
- $150K inventory valuation discrepancy analysis authored by Raj, Apr 12, 2026, as part of the dispute.
- Board-level mediation used: Robert Dunn (board member) brought in as outside mediator, Jun 2, 2026 — a level of escalation not used for any other Sabre or EOXS crisis on record.
- Second, self-inflicted outage: 8-9 days, invoice delivery via Grexo affected, caused by the rushed post-incident security-hardening fix.
- AskCruz AI Transformation proposal: pitch call held 2026-08-13 (Zoom, 3:00-3:30pm ET, Raj hosting); $34,500 one-time + $3,900/month for all 15 Sabre users; 6-week rollout; 12-month initial term (3-year going forward), up to 8% annual renewal increase, Net 7 billing, 50% due at kickoff.
- A parallel AskCruz proposal was pitched to 3GM Steel the same day (Aug 13, 2026) — both proposal emails reference an attachment with no attachment text captured in records.
- IRIS Pro AI add-on ($1,000/month) proposed 2026-07-02, still pending Sabre approval as of the Jul 27 MRR lookup — separate from the AskCruz proposal.

## Sources
- raw/claude-chat-queries/raj_2026-07-27_sabre-alloys-mrr-lookup.md — MRR figure ($10,970/mo), Charles White profile, plus unrelated lookups (PPC ticket count, 3GM's Jessica Worley, DPS invoice, Greer ticket cadence, Brannon Steel contract value) in the same multi-question thread.
- raw/claude-chat-queries/raj_2026-07-28_sabre-alloys-complete-info.md — Thin thread: user requested "complete info" on Sabre; assistant offered rigor-level options (5ft/10ft/50ft) and flagged billing slippage + Dec 2026 renewal as context, but no data pull is recorded in this file.
- raw/claude-chat-queries/raj_2026-07-29_sabre-alloys-contacts.md — Full Sabre contact roster (12 named contacts with roles/notes) pulled from the OV2 entity page; also notes an assistant error (accidental save_analysis placeholder file) unrelated to Sabre content itself.
- raw/claude-chat-queries/raj_2026-08-04_sabre-alloys-payment-delay.md — Raj requests a script to raise chronic late payment with Juan Deshon "softly"; assistant clarifies Juan isn't AP and reframes the ask around getting an AP owner's name and cutoff date.
- raw/claude-chat-queries/raj_2026-07-31_sabre-alloys-dispute-time-headspace.md — Full time/headspace accounting of the Feb-Jun 2026 outage claim dispute (20-28 hrs estimate) plus a follow-up equating that cost to Sabre's account size and EOXS's $1M ARR goal.
- raw/claude-chat-queries/ron_2026-08-18_sabre-alloys-askcruz-proposal.md — AskCruz AI Transformation proposal timeline, pricing table, and terms; flags that the proposal email sent to Sabre had no attachment.

## Candidate OV2 Cross-References
- Sabre Alloys (entity page) — the AskCruz proposal's unresolved "did Sabre actually receive the document" gap and the 171-day-past-due invoice status are both operationally live facts that may warrant a pointer update if OV2's entity page doesn't already reflect them.
- Juan Deshon (contact) — the "not an AP contact, can't release payments" distinction is a role clarification that could sharpen an existing OV2 contact note if one exists.
