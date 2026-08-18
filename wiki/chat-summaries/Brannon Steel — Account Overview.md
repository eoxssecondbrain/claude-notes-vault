---
title: "Brannon Steel — Account Overview"
type: chat-summary
sources: [raw/claude-chat-queries/raj_2026-07-27_brannon-latest-calls.md, raw/claude-chat-queries/ayan_2026-07-28_brannon-steel-project-overview.md]
created: 2026-07-27
updated: 2026-07-28
---

# Brannon Steel — Account Overview

_One-sentence description of what this cluster of conversations covers._

Two Claude conversations — one pulling Brannon Steel's call history, one giving a high-level project/people overview — together cover the account's deal shape, implementation progress, open risk items, and its most engaged contact, Ranim Fallaha.

## Summary

Brannon Steel is a prime steel service center in Brampton, Ontario — EOXS's first Canadian client and first AI-only (non-ERP) engagement. The deal was won January 20, 2026 by Scott Begin and Rajat Jain, after Raj met owner David Brannon at the SMU Steel Summit in September 2025. Brannon bought MTR AI only (not the full ERP): a tool that digitizes Mill Test Report PDFs into a structured chemistry/mechanical database with an NLP search layer. Brannon continues to run Microsoft Business Central as its core ERP plus a roughly 20-year-old shop-floor system (SFA).

Deal terms are $14,400 CAD implementation plus $1,240 CAD/month flat (not per-seat) — though the CRM record and a December 2025 call transcript disagree on whether the term is 3 years or 1 year at $1,000 USD/month; this contradiction is unresolved as of 2026-07-28.

Progress: went live January 2026; Phase 1 (MTR digitization) was confirmed complete March 12, 2026. The team worked through a large historical backlog (~4,777 unique MTR numbers, 2024–2026) and a string of extraction bugs (grade misreads, impact-test logic, batch-number-missing PDFs, scan-rotation errors), reaching ~90% MTR upload by end of April and a working inventory-query chatbot by late May. Weekly "Implementation Huddle" calls ran continuously February–June 2026, same 5-person roster (Rajat, Ayan Dutta, Manish Trivedi, Ranim Fallaha, Ron) — 14 calls logged, roughly weekly, ~11 minutes each. As of the 2026-07-27 query, the vault has no huddle call ingested since 2026-06-23 — no July call on record.

Note on call data quality: 13 of the 14 logged huddle calls have no Fireflies transcript body at all (metadata only); the one exception (3/17) has a single garbled line. Substantive content for these calls instead comes from recovered email threads (Phase 1 completion 3/12, an MTR volume/pricing dispute 3/31–4/9, ~90% MTRs uploaded by 4/30), documented on the separate "Implementation Huddles Jun 2026" wiki page.

Open issues as of late July 2026: a multi-month AR backlog (implementation HST plus May/June/July subscription invoices overdue as of July 22, 2026, despite the account's generally low-risk profile); the unresolved 1-year-vs-3-year contract term contradiction; a pricing/scope tension where the flat monthly fee was implicitly scoped to ~200–300 MTRs/month but Brannon's actual historical backlog (4,777 unique MTRs) is far larger, which was renegotiated but not fully reconciled; and an unexplained naming oddity where Brannon's Odoo alias signs off as "Steel America," the same branding used by a separate, identity-unresolved account (Velox Steel). Overall account risk is rated LOW — engaged client, a concrete bug list being worked through, no churn signals, just billing/paperwork loose ends.

Ranim Fallaha (also seen as "Raneem Fallaha") is Brannon's APQP Manager / Materials Engineer, ex-Gerdau, and the account's most engaged technical contact. She was formally appointed Brannon-side project lead on December 22, 2025, and has attended all 14 weekly huddles March–June 2026. She is not the primary account contact (that's Manish Trivedi, Head of Ops) but is the primary hands-on UAT tester of MTR AI. She reported on April 7, 2026 that Brannon has 4,777 unique MTR numbers on file, which triggered the pricing/scope renegotiation described above. She owns the manual batch-number-mapping workflow and pushed to get it made editable. She has caught several real AI accuracy failures — grade misreads, a missed manganese-too-high failure, missing carbon equivalency, and impact-test results shown with a qualitative "Excellent" label but no supporting numbers. She has also expressed interest in a Phase 2 engagement (replacing Brannon's aging shop-floor system).

## Tribal Knowledge Extracted
- **CRM/working-email mismatch for Ranim Fallaha** — CRM lists her as `ranim.fallaha@brannonsteel.com`, but her actual working email (used on calls and in task threads) is `rfallaha@brannonsteel.com`. Anyone emailing the CRM address risks reaching the wrong inbox — this discrepancy exists only in this conversation's synthesis, not in any single written record. (source: raw/claude-chat-queries/ayan_2026-07-28_brannon-steel-project-overview.md)
- **"Steel America" Odoo alias oddity** — Brannon's Odoo notification alias signs off as "Steel America," the same branding used by a separate, identity-unresolved account (Velox Steel). Flagged as an open unexplained naming overlap — not a documented corporate relationship, just an observed coincidence nobody has run down. (source: raw/claude-chat-queries/ayan_2026-07-28_brannon-steel-project-overview.md)
- **Flat-fee-vs-actual-volume workaround** — the $1,240 CAD/month flat fee was implicitly scoped around an assumed ~200–300 MTRs/month, but Brannon's real backlog (4,777 unique MTRs) blew past that assumption once Ranim surfaced the true number on April 7. The response was an informal renegotiation rather than a formal contract amendment — described as "renegotiated but not fully reconciled," i.e. there's no clean written resolution of this scope mismatch. (source: raw/claude-chat-queries/ayan_2026-07-28_brannon-steel-project-overview.md)
- **Call-log data gap workaround** — because 13 of 14 logged "Implementation Huddle" calls have no real Fireflies transcript (metadata only), the team's practice has been to reconstruct substantive call content from recovered email threads instead, tracked on a separate "Implementation Huddles Jun 2026" wiki page rather than from the call transcripts themselves. (source: raw/claude-chat-queries/raj_2026-07-27_brannon-latest-calls.md)

## Key Points
- Deal won 2026-01-20 by Scott Begin and Rajat Jain; sourced from a Sept 2025 SMU Steel Summit meeting between Raj and owner David Brannon.
- Product sold: MTR AI only, not full EOXS ERP; Brannon runs Microsoft Business Central plus a ~20-year-old shop-floor system (SFA).
- Terms: $14,400 CAD implementation + $1,240 CAD/month flat — contradicted by a Dec 2025 call transcript suggesting 1 year at $1,000 USD/month vs. CRM's 3-year term; unresolved as of 2026-07-28.
- Phase 1 (MTR digitization) completed 2026-03-12; ~90% of MTRs uploaded by end of April 2026; working chatbot answering inventory queries by late May 2026.
- Historical MTR backlog: 4,777 unique MTR numbers (2024–2026), reported by Ranim Fallaha on 2026-04-07.
- 14 weekly "Implementation Huddle" calls logged Feb–June 2026 (same roster: Rajat, Ayan Dutta, Manish Trivedi, Ranim Fallaha, Ron); most recent on record is 2026-06-23; no July 2026 call ingested as of the 2026-07-27 query.
- AR backlog as of 2026-07-22: implementation HST plus May/June/July subscription invoices overdue.
- Ranim Fallaha appointed Brannon-side project lead 2026-12-22 [sic, per source: appointed Dec 22, 2025].
- Overall account risk rating: LOW.

## Sources
- raw/claude-chat-queries/raj_2026-07-27_brannon-latest-calls.md — Raj's query for Brannon's latest call history; surfaces the 14-call huddle series, the metadata-only transcript gap, and that no call has been logged since 2026-06-23.
- raw/claude-chat-queries/ayan_2026-07-28_brannon-steel-project-overview.md — Ayan's high-level project overview plus a deep-dive on contact Ranim Fallaha, covering deal terms, implementation progress, open issues, and her role.

## Candidate OV2 Cross-References
- Brannon Steel (wiki/entities/clients/Brannon Steel.md) — both threads cite this page directly as their source; the CRM-vs-working-email mismatch and the flat-fee/actual-volume renegotiation detail could sharpen the existing OV2 entry if not already captured there.
- Ranim Fallaha (wiki/entities/contacts/brannon-steel/Ranim Fallaha.md) — the CRM/working-email discrepancy is a concrete, checkable fact that may be worth verifying against and correcting on this existing contact page.
