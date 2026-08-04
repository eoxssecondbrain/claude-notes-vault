---
thread_name: "brannon-steel-full-picture"
user: "jaskeerat"
type: claude-chat
created: 2026-08-04
updated: 2026-08-04
---

# Brannon Steel — Full Picture

## User Question
"What information do you have about Brannon steel. Give me the full picture"

## Assistant Response Summary

**Who they are:** Prime steel service center in Brampton, Ontario, Canada. EOXS's first Canadian client and first AI-only (non-ERP) engagement. Runs Microsoft Business Central as core ERP + ~20yr old SFA shop-floor app. EOXS sold standalone MTR AI product only, not full ERP.

**Product: MTR AI** — reads Mill Test Report PDFs, extracts chemistry/mechanical data, builds searchable heat-number-keyed database, joins to inventory, enables NLP material search. This is EOXS's flagship case study, referenced in pitches to Jamie Vilcheck, Lawrence, Rob Coppens, and Collier Metals.

### Timeline
- Sep 2025: Raj met David Brannon (owner) at SMU Steel Summit
- Oct 15, 2025: In-person meeting in Brampton
- Nov 11, 2025: Technical scoping call, pricing sent ($14,400 CAD impl + $1,240 CAD/mo)
- Jan 20, 2026: Deal WON (Scott Begin salesperson, Rajat Jain account owner)
- Jan 21, 2026: Kickoff, instance at brannon.eoxs.com
- Feb–Jun 2026: Weekly Implementation Huddles; Ayan Dutta EOXS project lead (Feb 24); Ranim/Raneem Fallaha primary UAT tester
- Mar 12, 2026: Phase 1 complete
- Apr 2026: Bulk-backlog pricing negotiation resolved; ~90% MTRs uploaded by Apr 30
- May 2026: Monthly subscription billing begins
- Jun–Jul 2026: Ongoing bug fixes; new contact Jaskeerat Singh joins

### Key Contacts
- David Brannon — Owner, warm, delegated technical eval
- Manish Trivedi — Head of Operations, drove evaluation, signed contract
- Ranim/Raneem Fallaha — APQP Manager/Materials Engineer, ex-Gerdau, primary UAT tester
- Kevin Brannon — VP

### Commercial Terms (SOW signed Jan 7, 2026)
- Implementation: $14,400 CAD one-time
- Monthly: $1,240 CAD flat (invoiced at $1,200 base/$1,356 w/ tax — ~3% discrepancy)
- Governing law: Ontario; liability capped at 12 months' fees
- Contract term conflict: CRM says 3-year; Dec 22 2025 call transcript says 1-year at $1,000 USD/mo — unresolved

### Billing (Odoo, as of late July 2026)
| Order | Date | Amount CAD | Item | Status |
|---|---|---|---|---|
| S00155 | 2026-01-07 | $4,320 | Implementation Kick-Off | Paid 2026-01-21 |
| S00174 | 2026-03-12 | $10,080 | Implementation Due | Cancelled, superseded |
| S00189 | 2026-05-20 | $4,881.60 | Implementation Kick-Off (reissue) | Unpaid |
| S00196 | 2026-05-21 | $11,390.40 | Implementation Due (reissue) | Unpaid |
| S00203 | 2026-07-22 | $1,356.00 | Monthly Subscription July 2026 | Unpaid (+$3,051 additional dev invoice) |

Overdue payment concern flagged 2026-07-22/07-28 (~CAD 7,119 outstanding); partial payment (CAD 2,712, May+June subs) received Aug 1, 2026. July subscription + $3,051 dev charge remain outstanding.

### Technical Issues
Grade misreads, carbon-equivalency omissions, impact-test temp-direction errors, false compliance approvals (e.g. heat LW0940), batch-number-missing MTRs, scan-rotation extraction errors. ~5-6/14 flagged issues resolved by mid-June 2026. Ticket T06332 (MTR Inventory Module) sat idle in QA-Passed for ~2 months with unanswered daily escalation bot nudges.

### Risk Assessment
Low-to-moderate. Engaged tester, no churn signal, but: (1) pricing under-scoped for actual MTR volume (200-300/mo cap vs 3,500-4,777 backlog), (2) first AR backlog issue emerged July 2026.

### Unresolved oddity
Overlap between Brannon's info.brannon@gmail.com Odoo alias and "Steel America" (steelamerica.net) branding also used by separate client Velox Steel — not resolved in vault sources.

## Sources Used
- wiki/entities/clients/Brannon Steel.md
- wiki/concepts/products/MTR AI.md
- raw/invoices/2026-01-S00155.md, 2026-03-S00174.md, 2026-05-S00189.md, 2026-05-S00196.md, 2026-07-S00203.md
- raw/tickets/2026-02-04-T06332-MTR-Inventory-Module.md and others
- Multiple call transcripts (raw/clients/brannon-steel/calls/)
- Multiple emails (raj_gmail, ron_gmail 2025-09 through 2026-07)
