---
thread_name: "dps-s06119-taxcloud-100k-qty-error"
user: "jaskeerat"
type: claude-chat
created: 2026-08-04
updated: 2026-08-04
---

# Discount Pipe & Steel — S06119 Sale Order Confirmation Error (TaxCloud / 100,000 qty threshold)

## User's situation
User is handling a ticket from Discount Pipe & Steel (Austin, from Austin site) where a sale order (S06119, ticket T07533 "Values making no sense") could not be confirmed — stuck in quotation state with a warning related to tax/text. User diagnosed on staging: SO had 3 lines; line 1 had quantity >100,000 (footage). Reproduced on staging server: replica SO with qty >100,000 threw the same error; reducing qty below 100,000 let it confirm successfully. Previous SOs for same customer never hit this because no line ever exceeded 100,000. User asked: should they share these findings with the customer now, say they're still investigating, or something else?

## Assistant's research and answer
Searched tickets, implementation tasks, wiki for Discount Pipe & Steel. Found:
- Ticket T07533 "S06119" (2026-07-31, status "Need Developer," desc "Values making no sense") — matches user's ticket.
- Wiki (Discount Pipe & Steel entity page, and Post-Go-Live Operations page) already documents, added 2026-07-09: "a 100,000-per-order-line error on Oklahoma-taxed addresses that Austin [Rayzor] could not tell apart from a genuine TaxCloud threshold feature."
- This is the SAME symptom: SO line quantity crossing 100,000 on tax-integrated (TaxCloud) address triggers a hard confirmation-blocking error.
- TaxCloud is DPS's sales-tax integration, documented elsewhere as chronically fragile (e.g., T07285/S05493 June 2026 `sale_account_taxcloud` module crash: `ValueError: Invalid field 'name' on model 'stock.move.line'`).
- Root cause of the >100k threshold itself (genuine TaxCloud API limit vs EOXS-side bug in quantity/amount serialization before calling TaxCloud) was NOT resolved as of 2026-07-09 per the wiki — Austin's question was left open.

## Recommendation given to user
1. Don't present this as a final "root cause" to the customer — it's a confirmed reproducible trigger (qty >100,000 per SO line breaks tax calc/confirmation), not yet a diagnosed root cause (unclear if TaxCloud API limit or EOXS-side bug).
2. Reply to customer: confirm the trigger condition found; give workaround (split the line into two lines each under 100,000 so they can confirm the order now); tell them it's escalated to dev team to determine if hard TaxCloud limit or bug, will follow up.
3. Internally: link ticket T07533 to the pre-existing 2026-07-09 TaxCloud/100k finding on the wiki so dev doesn't re-diagnose from scratch; confirm with Austin Rayzor/dev whether the open question (bug vs. TaxCloud threshold) was ever answered.

## Sources cited
- Ticket T07533 (S06119, Discount Pipe & Steel, 2026-07-31, "Need Developer")
- Wiki: "Discount Pipe & Steel" entity page (100,000-per-order-line / Oklahoma-taxed addresses TaxCloud note, added 2026-07-09)
- Wiki: "Discount Pipe & Steel — Post-Go-Live Operations"
- Ticket T07285 (S05493 - J&I Manufacturing, 2026-06-16) — TaxCloud module crash traceback (`sale_account_taxcloud`)
- Implementation task 30605 "Sales Order Status Not Updating" (unrelated quote-number display bug, reviewed but not directly relevant)
