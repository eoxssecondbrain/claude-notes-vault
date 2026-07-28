---
thread_name: "brannon-steel-project-overview"
user: "ayan"
type: claude-chat
created: 2026-07-28
updated: 2026-07-28
---

# Thread: Brannon Steel — Project Overview

**User:** Tell me everything on very high level on brannon project

**Assistant:**

## Brannon Steel — high level

**Who they are:** A prime steel service center in Brampton, Ontario — EOXS's first Canadian client and first AI-only (non-ERP) engagement. Won January 20, 2026 by Scott Begin and Rajat Jain, after Raj met owner David Brannon at the SMU Steel Summit in Sep 2025.

**What they bought:** Not the full EOXS ERP — just MTR AI, which digitizes Mill Test Report PDFs into a structured chemistry/mechanical database with an NLP search layer ("find heats with 0.12C, 0.31Si"). Brannon still runs Microsoft Business Central as their core ERP and a ~20-year-old shop-floor system (SFA).

**Deal terms:** $14,400 CAD implementation + $1,240 CAD/month flat (not per-seat) — though the CRM record vs. a Dec 2025 call transcript disagree on whether the term is 3 years or 1 year at $1,000 USD/month.

**Key people:**
- David Brannon (owner, warm but delegated to team)
- Manish Trivedi (Head of Ops, main technical driver)
- Ranim/Raneem Fallaha (APQP Manager, ex-Gerdau, primary UAT tester — thorough and engaged)
- On EOXS's side: Ayaan (implementation lead) and, more recently, Jaskeerat Singh (QA/data validation)

**Progress:** Went live Jan 2026, Phase 1 (MTR digitization) confirmed complete Mar 12. By working through a large historical backlog (~4,777 unique MTRs) and a string of extraction bugs (grade misreads, impact-test logic, batch-number-missing PDFs, scan-rotation errors), the tool reached ~90% MTR upload by end of April and has a working chatbot answering real inventory queries by late May. Weekly implementation huddles ran continuously Feb–June.

**Open issues:**
- Multi-month AR backlog — several invoices (implementation HST, May/June/July subscription) were overdue as of July 22, 2026, despite this account's generally low-risk profile.
- Contract-term contradiction (1yr vs. 3yr) unresolved.
- A pricing/scope tension: the flat monthly fee was implicitly scoped to ~200–300 MTRs/month, but Brannon's actual historical backlog is far larger — this got renegotiated rather than fully reconciled.
- An unresolved naming oddity: Brannon's Odoo alias signs off as "Steel America," the same branding used by a separate, identity-unresolved account (Velox Steel) — flagged but not explained.

**Overall risk:** LOW — engaged client, concrete bug list being worked through, no churn signals, just some billing/paperwork loose ends.

Source: OV2 wiki page [[Brannon Steel]] (wiki/entities/clients/Brannon Steel.md)

---

**User:** tell me about Ranim

**Assistant:**

## Ranim Fallaha (aka "Raneem Fallaha")

**Role:** APQP Manager / Materials Engineer at Brannon Steel, Brampton, Ontario. Ex-Gerdau — that industry background is one of the trust signals EOXS's sales team leaned on during the pitch.

**Two emails, one person:** CRM lists her as ranim.fallaha@brannonsteel.com, but her actual working email (used on calls and in the task threads) is rfallaha@brannonsteel.com.

**Her role in the deal:** Not the primary account contact (that's Manish Trivedi) — she's the primary hands-on tester of MTR AI. She was formally appointed Brannon-side project lead on Dec 22, 2025, and has been Brannon's consistent presence across all 14 weekly implementation huddles from March through June 2026.

**What she's actually been doing:**
- Back in Feb 2026, she was one of two people (with Manish) EOXS asked to supply 200–300 sample MTRs to train/validate the AI's extraction.
- She sized the real scope of the job April 7 by reporting Brannon has 4,777 unique MTR numbers on file (2024–2026) — which then triggered a pricing/scope negotiation, since the flat monthly fee assumed a much smaller ongoing volume.
- She owns the manual workflow for batch-number mapping and pushed to get it made editable.
- She's the one who's been catching the AI's real accuracy failures — grade misreads, a missed manganese-too-high failure, missing carbon equivalency, and impact-test results shown with a qualitative "Excellent" label but no actual numbers behind it.
- She's technically sharp — she understands MTR chemistry, grade specs, and CVN (Charpy V-notch) test logic well enough to spot when the AI's compliance logic is wrong, not just when it's broken.
- She's also expressed interest in Phase 2 (replacing Brannon's aging shop-floor system).

**Vault flags of note:** one open, unresolved thread ties her to a "Steel America" affiliation via her Odoo notification alias — the same branding that shows up on a separate, identity-unclear account (Velox Steel). Nothing in the wiki explains whether that's a real corporate link, a shared reseller instance, or just a naming coincidence.

**Overall picture:** she's the most engaged, technically credible person on the Brannon side — thorough, constructive, and central to why this account's risk is rated LOW despite a real backlog of bugs.

Sources: OV2 wiki pages [[Ranim Fallaha]] (wiki/entities/contacts/brannon-steel/Ranim Fallaha.md), [[Brannon Steel]]
