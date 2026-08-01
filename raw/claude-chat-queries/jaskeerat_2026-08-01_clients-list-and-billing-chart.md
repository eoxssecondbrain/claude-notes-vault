---
thread_name: "clients-list-and-billing-chart"
user: "jaskeerat"
type: claude-chat
created: 2026-08-01
updated: 2026-08-01
---

# Clients List and Billing Chart

## User Question 1
"Give me all the clients we have right now"

## Response 1
Listed 8 clients from raw/clients/ vault folder:
1. 3GM Steel
2. Brannon Steel
3. Discount Pipe & Steel
4. Eastern States Steel
5. Greer Steel
6. PPC Metals
7. RW Conklin Steel
8. Sabre Alloys

## User Question 2
"Make a graph of this according to whatever we are charging them"

## Response 2
Researched invoices/sales orders for each client via eoxs-vault_search_invoices and eoxs-vault_get_invoice tools. Found:

- **Sabre Alloys**: ~$7,820/mo license charges (23 users × $425, 20% disc) — last invoice found S00057, dated 2024-10-02. No 2025/2026 invoices found in search.
- **3GM Steel**: Proposal states $4,759/mo contracted rate (15 users × $423, 25% sign-up disc, 3-yr term). Last actual invoice found was 2023-05 (S00024) at $4,488.75/mo (15 users × $399, 25% disc). No invoices found post-2023.
- **Discount Pipe & Steel**: $3,120/mo licensing (8 users × $390) + $2,500/mo implementation installment. Latest: S00150, 2025-12-26.
- **Eastern Steel Sales** (= Eastern States Steel in invoicing system): $2,340/mo (6 users × $390). Latest: S00182, 2026-05-02.
- **PPC Speciality Metals** (= PPC Metals): $2,200/mo (5 users × $550, 20% disc). Latest: S00201/S00191, 2026-06.
- **R W Conklin Steel**: $1,800/mo (4 users × $450). Latest: S00154, 2026-01-06.
- **Greer Steel Company**: ~$1,150/mo avg (10-11 users × $160, 30% disc). Latest: S00074, 2025-05-06.
- **Brannon Steel**: $1,200 CAD/mo (MTR AI subscription, new product) + one-time $10,080 CAD implementation charge (May 2026). Latest: S00203, 2026-07-22.

Built an HTML bar chart comparing monthly recurring billing across all 8 clients, flagged stale data for Sabre Alloys and 3GM Steel (recommended direct Odoo verification).

## Key Sources
- raw/invoices/ (various S0000X sales order files)
- raw/clients/3gm-steel/account/PROPOSAL_3GM_Steel.md (contract terms)
- raw/clients/sabre-alloys/ (searched but no recent invoices found)
