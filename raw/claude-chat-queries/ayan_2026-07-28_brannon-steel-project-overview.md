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
