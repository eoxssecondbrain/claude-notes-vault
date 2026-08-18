---
thread_name: "eoxs-day-one-employee-overview"
user: "jaskeerat"
type: claude-chat
created: 2026-08-18
updated: 2026-08-18
---

# EOXS Day-One Employee Overview + Company History Query

**User:** tell me 2 lines i need to know about eoxs from an employee perspective who has joined today itself

**Assistant:** (used EOXS Data General integration — search_wiki/list_assets, 2 files viewed)
Two things worth knowing on day one:
1. EOXS (legally Prata Inc.) is a vertical SaaS + AI company building an ERP exclusively for the steel and metals industry — modules cover accounting/inventory (Books), CRM, HR/payroll (People), e-commerce (Shop), and reporting, plus a separate suite of 12+ task-specific "AI Worker" co-pilots (SmartQuote, Steel Brain, Iris, etc.) that can run standalone or alongside competitor ERPs like SAP or Epicor.
2. The core pitch to customers is domain depth, not generic software — the founder/team come from the steel industry itself, and the argument against SAP/NetSuite/Epicor is that they don't handle steel-specific costing, batch/continuous production, and grade-variation logistics; Gerdau is the one named enterprise reference client.

**User:** don't use connectors but do you think response is fine?

**Assistant:** Not fully — flagged 3 gaps:
1. "Employee perspective" was ambiguous (role/team not specified) — defaulted to generic company positioning instead of asking, contrary to stated clarity-before-answering preference.
2. Source tier was thin — pulled from synthesized wiki pages, not cross-checked against a primary asset doc. Legal entity name and Gerdau-as-reference-client claims should be verified against a source doc, not just wiki synthesis.
3. Since connectors were off that turn, couldn't re-verify — flagged both lines as unverified until checked against a primary source.

**User:** and if ask you again the same question what would be your response?

**Assistant:** Would not repeat the same answer. Would first ask which role/team the new hire is joining, since "employee perspective" is ambiguous. Would then pull the two lines from a primary asset doc (not wiki synthesis) and cite the source — clarifying question first, sourced answer second.

**User:** [asked same question again]

**Assistant:** Asked clarifying question via ask_user_input_v0: which team/role is the new hire joining? Options: Sales/Customer-facing, Engineering/Product, Operations/Implementation, Other/General.

**User:** Operations / Implementation

**Assistant:** Pulled primary asset doc "EOXS Client Implementation and Go-Live SOP" (tier2_confidential). Two lines given:
1. The client project board is the single source of truth — every requirement, decision, task, approval, testing result, and open item must be written on it; calls/transcripts are only supporting evidence.
2. Nothing is "delivered" just because it's built — a task is only complete once tested, client-approved where required, deployed, validated live, client informed, and tracker updated.
Cited: EOXS Client Implementation and Go-Live SOP, Sections 3 and 25.

**User:** i wants to know about company, it's history, evolution

**Assistant:** Flagged that this is a research task and rigor levels should have been offered first (self-correction, didn't ask before starting). Gave first-pass (~5-10ft depth) findings:
- Public version (EOXS Company Overview asset, tier2, sourced eoxs.com June 2026): legal name Prata Inc trading as EOXS, website active since ~2021, founding date not publicly disclosed, founder steel background (30 combined years claimed), HQ New Rochelle NY. Evolution: ERP-only (Books/CRM/People/Shop/Report Builder) to adding a second product line — 12+ "AI Worker" co-pilots, positioned ERP-agnostic (works with SAP/Epicor/Invera/Stratix too).
- Internal wiki (tier2_confidential), with caveats: Rajat Jain (account owner/founder-adjacent figure) has steel-distribution background to the 1980s, ran a company under "Stock Alloys Ireland" pre-EOXS. Legal entity confirmed Prata Inc, Delaware C-Corp (previously the vault mistakenly treated Prata Inc as a possibly-separate entity from EOXS; corrected by a 2025 source). Earliest documented internal activity: 2021 "founding-era" email archive batch; rajat@prata.ca usage confirmed from 2022-04-26. Earliest confirmed live production client: 3GM Steel, went live 2022-07-18 (longest-tenured client). Gerdau named as enterprise reference client; Steel Brain AI built on a Gerdau metallurgist's knowledge.
- Flagged: vault has an open, unresolved internal contradiction about exact entity history/dates — not smoothed over. get_wiki_page tool malfunctioned twice returning wrong page for "Rajat Jain" entity — founder-background detail sourced from a search snippet only, not the full record. Offered to go to 50ft/100ft rigor to resolve properly if wanted.
