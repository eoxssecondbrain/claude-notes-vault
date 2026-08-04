---
title: "Sabre Alloys — Full Client Profile (DB-Only Sources)"
type: analysis
created: 2026-08-04
updated: 2026-08-04
---

## Question
Compile all available information on Sabre Alloys: contacts, relationship history, contract/commercial terms, support activity, and current status — using only the eoxs-db (database) tool set.

## Client Record
- Slug: `sabre-alloys` | Odoo instance: https://sabre.eoxs.com | Domain: sabrealloys.com | Client ID 1 (first client in registry — one of EOXS's oldest accounts)
- No wiki page exists for Sabre Alloys in the DB wiki index (0 wiki pages total in DB currently).

## Key Contacts (from emails, tickets, calls)
| Name | Role/Context |
|---|---|
| **Michael Mercadante** | CEO/Owner, Sabre Alloys. Sent detailed "Using Claude" AI requirements doc (see below). Direct: (346) 355-0823 |
| **Juan Deshon** | Primary day-to-day contact for support/accounting issues (income statement, bank reports). juan@sabrealloys.com |
| **Tye Webb, Jesus Rios** | CC'd on Michael's AI requirements email — likely operations/finance staff |
| **David Underwood** | External (dmgunderwood@gmail.com) — CC'd on AI requirements thread |
| **Christi** | Client-side contact who EOXS support repeatedly escalated to for "Demanded PCS field" confirmation (referenced only by first name in internal tickets) |
| **Charles, Ernie** | Referenced in internal call/ticket notes re: inventory/toll processing training and historical decisions — appear to be Sabre operational staff EOXS has trained over time |
| **James** | Referenced multiple times in Fathom call re: inventory cost-per-pound discrepancy investigation |
| **Austin** | Approved a QuickBooks reconciliation module charge |

**EOXS-side owners:** Ron Jain (primary account lead/support escalation point), Rajat Jain (CEO, handles Sabre relationship personally — explicitly told a new sales hire "Do not name Sabre Alloys... has history I'll handle personally"), Humaira Zainab, Hashir Saleem, Aryan Bakshi, Talal, G. Nijamuddin, Siddhant Pathak (dev/support staff who've touched Sabre tickets).

## Relationship History & Commercial Status
- **Long-term client** — internal email (Rajat, June 2026) states "Sabre has been a customer for several years."
- **Implementation**: 827 implementation tasks exist system-wide; Sabre Alloys has an extensive "Soft Launch" project with 100+ tasks dated April–June 2024 covering ERP build-out (control tags, processing, freight/landed cost, buyout flows, MTR functionality, payment terms, inventory control, etc.) — most marked "Completed/Released," several still "Need discussion" or "Backlog."
- **Revenue scale**: Internal email calls Sabre a "$10k MRR account" — used by Rajat as a benchmark ("four accounts the size of Sabre Alloys" = major growth goal for next 12 months), signaling Sabre is one of EOXS's largest accounts.
- **Two dedicated servers**: A ticket (T06868, Apr 2026) shows EOXS committed to running **two live servers ("taxis")** for Sabre — a primary always-on + a daily-synced backup — reflecting Sabre's outsized importance/reliability requirements. This task was severely delayed (idle 50+ days, escalated repeatedly, eventually done on a new "Hetzner" server per internal notes).

## ⚠️ Major Incident: February Cybersecurity Breach & Dispute (2026)
This is the most significant event in the relationship, detailed in a private email thread ("Need Help...", Rajat Jain to an external advisor, June–Aug 2026):
- **Feb 11, 2026**: Sabre's EOXS environment suffered a cybersecurity incident. Sales order processing restored within ~2 days; full recovery took ~1–2 more weeks of round-the-clock EOXS effort (backup restoration, data rebuild/validation, manual data entry, new reporting tools).
- **Dispute emerged** after recovery: Sabre asserted a **damages claim of ~$80,000** for business disruption.
- Sabre also had **~$43,000 in unpaid invoices** outstanding at the time.
- EOXS's first settlement offer was **$25,000**; Sabre rejected it.
- Rajat brought in an external advisor (Robert Dunn) to mediate.
- **Resolution (reported July 31, 2026)**: EOXS gave Sabre a **$25,000 credit against outstanding invoices**, plus **another $25,000 to be paid out over 25 months**. Rajat confirmed the dispute was resolved and the relationship preserved.
- Follow-on email (June 22, 2026, "Using Claude" thread) shows Rajat explicitly linking resolution of this **"February resolution and outstanding account balance"** as a precondition before EOXS would begin new IRIS/AI development work for Sabre — i.e., commercial leverage tied the AI project to settling the dispute first.

## "Sabre IRIS" — AI/Analytics Project
- Michael Mercadante sent an extremely detailed requirements email (June 16, 2026, "Using Claude") asking EOXS to configure/train the Claude-based AI agent already built into the ERP to answer operating questions across: Cash/AR, open orders/shipment risk, inventory, quotes/sales activity, margin/pricing, purchasing/vendors, customer profitability, certs/documentation, and a "daily management briefing." Rajat called it "Gold fucking mine."
- Rajat's reply (June 22): agreed to review requirements but said new IRIS work would only proceed **after** the Feb incident/account balance was resolved — existing support, stability work, and current IRIS access would continue in the meantime.
- Internal Fathom call (July 2, 2026, Ron J + team) confirms:
  - The tool ("Sabre IRIS") connects **Claude via MCP to the Sabre server**.
  - EOXS pays for Claude Pro membership + usage credits on Sabre's behalf — actual bills cited: ~$32 (May 5), ~$21 (May 13), ~$48 extra usage (June).
  - Ron discusses proposed pricing: **$1,000/month** for "IRIS Pro," to be approved by Sabre before invoicing, and considers separating usage into per-person accounts.
  - Weekly recurring calls with Juan (paused, then resumed late June 2026) — team debated whether to start charging for these calls.
  - Rajat/Ron followed up "ready to show" IRIS demo (July 31, 2026) — Sabre had not yet responded as of Aug 3 email ("??").

## Support Ticket History (Odoo, client_id=1)
| Ticket | Date | Subject | Status | Notes |
|---|---|---|---|---|
| T07534 | 2026-07-31 | B/IN/03618 (cancel receiving) | Communicated | Resolved same day |
| T07513 | 2026-07-27 | Re: INCOME STATEMENT | Paid | Long thread w/ Juan Deshon re: bank report Excel export, inventory ageing report, quarterly statement formatting bugs — repeated delays acknowledged by EOXS support |
| T06868 | 2026-04-15 | Setting up 2 taxis for Sabre Alloys | Assigned | Dual-server infra; task stalled 50+ days despite repeated critical escalations to Ron/Talal |
| T06519 | 2026-03-09 (closed 2026-08-01) | Order parts showing in plate assignment (High priority) | Paid | ~5 months to resolve; incentive dispute over missed deadline, ultimately paid Aug 1 |
| T06359 | 2026-02-09 (closed 2026-08-01) | Add Vendor Delivery field (Change Request) | Paid | ~6 months to resolve; same incentive/deadline dispute as above |
| T04432 | 2025-07-24 | SO-13853 Sulzer Pump Services (PO cost issue) | Paid | |
| T04430 | 2025-07-24 | SO-12779 Hydro-Blade Waterjets (tag cost reassignment) | Paid | |
| T04418 | 2025-07-22 | SO-13447 Southern Heat Exchanger Serv. | Paid | |

**Pattern across tickets**: Several show extended idle periods (30–75+ days) triggering automated "CRITICAL" escalation nudges to Ron Jain/Rajat Jain/dev team — a recurring theme of slow internal follow-through on Sabre requests despite the account's size and importance. Internal notes also reference a dedicated support "Demanded PCS Field" ticket where the client contact "Christi" went unanswered for 10–14+ days on confirmation, compounded by conflicting internal reports (Ron said feature was live; Aryan Bakshi said "Not on live").

## Sales/Culture Signals
- In an internal sales-onboarding script (Aug 2026), Rajat explicitly instructs a new cold-caller: **"Do not name Sabre Alloys, Discount Pipe & Steel or PPC Metals [as references]. Each has history I'll handle personally."** — confirms Sabre is treated as a sensitive/high-touch account not to be used as a casual reference.
- Sabre is simultaneously used internally as a positive benchmark for account size/value ("four accounts the size of Sabre Alloys" as a growth target).

## Sources
- eoxs-db_list_clients, eoxs-db_search_tickets/get_ticket (T07534, T07513, T06868, T06519, T06359, T04432, T04430, T04418)
- eoxs-db_list_implementation_tasks (client=sabre-alloys, "Soft Launch" project, ~100 tasks)
- eoxs-db_search_emails/get_email: "Team growth plan" (id 255), "Sales person onboarding" (id 275), "Re: Add Demanded PCS Field" (id 72), "Using Claude" (id 16, Michael Mercadante → Rajat), "Need Help..." (id 2, Rajat → Robert Dunn re: cybersecurity dispute/settlement), "Re: INCOME STATEMENT" (ticket T07513 embedded thread)
- eoxs-db_search_calls/get_call: Fathom call "Impromptu Zoom Meeting" 2026-07-02 (Ron J + team, Sabre IRIS pricing/MCP/Claude billing discussion)
