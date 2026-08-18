---
thread_name: "eoxs-day-one-employee-overview"
user: "jaskeerat"
type: claude-chat
created: 2026-08-18
updated: 2026-08-18
---

# EOXS Day-One Employee Overview + Company History + Current Clients Query

**User:** tell me 2 lines i need to know about eoxs from an employee perspective who has joined today itself

**Assistant:** (used EOXS Data General integration — search_wiki/list_assets, 2 files viewed)
Two things worth knowing on day one:
1. EOXS (legally Prata Inc.) is a vertical SaaS + AI company building an ERP exclusively for the steel and metals industry — modules cover accounting/inventory (Books), CRM, HR/payroll (People), e-commerce (Shop), and reporting, plus a separate suite of 12+ task-specific "AI Worker" co-pilots (SmartQuote, Steel Brain, Iris, etc.) that can run standalone or alongside competitor ERPs like SAP or Epicor.
2. The core pitch to customers is domain depth, not generic software — the founder/team come from the steel industry itself, and the argument against SAP/NetSuite/Epicor is that they don't handle steel-specific costing, batch/continuous production, and grade-variation logistics; Gerdau is the one named enterprise reference client.

**User:** don't use connectors but do you think response is fine?

**Assistant:** Not fully — flagged 3 gaps: ambiguous "employee perspective" (no role asked), thin sourcing (wiki synthesis not primary asset docs), and inability to re-verify with connectors off.

**User:** and if ask you again the same question what would be your response?

**Assistant:** Would ask which role/team first, then pull from primary asset docs with citation instead of repeating the same answer.

**User:** [asked same question again]

**Assistant:** Asked clarifying question: which team/role is the new hire joining? Options: Sales/Customer-facing, Engineering/Product, Operations/Implementation, Other/General.

**User:** Operations / Implementation

**Assistant:** Pulled primary asset doc "EOXS Client Implementation and Go-Live SOP" (tier2_confidential). Two lines given:
1. The client project board is the single source of truth — every requirement, decision, task, approval, testing result, and open item must be written on it; calls/transcripts are only supporting evidence.
2. Nothing is "delivered" just because it's built — a task is only complete once tested, client-approved where required, deployed, validated live, client informed, and tracker updated.
Cited: EOXS Client Implementation and Go-Live SOP, Sections 3 and 25.

**User:** i wants to know about company, it's history, evolution

**Assistant:** Flagged that rigor levels should have been offered first (self-correction). Gave first-pass (~5-10ft depth) findings:
- Public version (EOXS Company Overview asset): legal name Prata Inc trading as EOXS, website active since ~2021, founding date not publicly disclosed, founder steel background (30 combined years claimed), HQ New Rochelle NY. Evolution: ERP-only to adding a second product line — 12+ "AI Worker" co-pilots, ERP-agnostic.
- Internal wiki (tier2_confidential), with caveats: Rajat Jain (account owner/founder-adjacent figure) has steel-distribution background to the 1980s, ran a company under "Stock Alloys Ireland" pre-EOXS. Legal entity confirmed Prata Inc, Delaware C-Corp (vault previously mistakenly treated as separate entity; corrected by 2025 source). Earliest documented internal activity: 2021 "founding-era" email archive batch; rajat@prata.ca usage confirmed from 2022-04-26. Earliest confirmed live production client: 3GM Steel, went live 2022-07-18. Gerdau named enterprise reference client.
- Flagged: vault has an open, unresolved internal contradiction about exact entity history/dates. get_wiki_page tool malfunctioned twice on "Rajat Jain" entity page — founder-background detail sourced from search snippet only. Offered 50ft/100ft rigor to resolve properly.

**User:** who are the current clients of EOXS?

**Assistant:** list_clients returned 8 registry entries: Sabre Alloys, 3GM Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, Ohio Strip Steel (formerly Greer Steel), RW Conklin Steel, Brannon Steel. Flagged that RW Conklin and Brannon had no odoo_base_url on file (status unverified) and that Morgan-Hauser Steel Inc. appeared in earlier searches with a termination history but wasn't in the registry. Offered a 10ft verification pass.

**User:** do it

**Assistant:** Ran verification via get_client_profile and wiki searches:
- Confirmed current/active (live Odoo instance, recent activity, no cancellation found): Sabre Alloys, 3GM Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, Ohio Strip Steel.
- Brannon Steel: confirmed active — calls as recent as 2026-08-18 (today), mid-implementation on MTR AI module specifically.
- RW Conklin Steel: ambiguous, flagged not confirmed either way. Deeper record ("Contract Dispute & Near-Cancellation" wiki page, tier2_confidential) shows: usage stalled post-go-live, client attempted cancellation Aug 2025 citing financial distress, a 12-month "readoption or revert" trial was negotiated but never formally signed by the client side, a clean-break termination settlement was then offered, but invoicing continued unchanged through Dec 2025 (billed Jan 2026) — the source page itself states status is unresolved as of the last recovered thread. Recommended checking raw/invoices/ (Odoo) directly to settle it.
- Morgan-Hauser Steel Inc.: confirmed churned Feb 23, 2024 (unresolved implementation backlog) — correctly excluded from the registry, not a current client.
- Conclusion: 7 of 8 registry entries are solid current clients; RW Conklin is a genuine open question in the underlying data, not a data-entry gap.
