---
thread_name: "discount-pipe-inventory-valuation-3-screens"
user: "hashir"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

User: I want to go through the 3 screens of the live database for discount pipe and then we need to create an md file through that in that md file i want to get all the informations related to inventory valuation so for the three screens the first is the inventory lot/serial screen which provide us the data of the available inventory if we put the company as the group by then it shows us the total value for the inventory valuation for all the tags available in the inventory, Then the second screen is the accounting screen from the balance sheet we get the information of the inventory valuation total and then the last screen would be inside the inventory module we have the reporting section in that we  have inventory valuation screen again by putting the group by of company we get the total valuation of the inventory and through this you can create an md file which i can provide to cowork for scheduling this task every 8:30AM EST at humaira@eoxsteam.com

Assistant: Pulled all three sources from DPS LIVE. Key finding, and it's the important one: your assumption that Screen 1 (Lot/Serial grouped by company) independently gives a dollar valuation doesn't hold in this schema — `stock_quant` has no value column in Odoo 13. Whatever number that screen shows is Odoo computing it live from the same costing engine behind Screen 3, not a separately stored figure. I documented the on-hand qty/lot/product counts from that screen instead of a fabricated value, so the md file doesn't claim a number that doesn't actually exist at that table level.

Numbers as of today:
- Screen 2 (Balance Sheet, Stock Valuation acct 110100): $1,087,475.62
- Screen 3 (Inventory Valuation report, `SUM(stock_valuation_layer.value)`): $1,101,787.95
- Gap: $14,312.33 (~1.3%) — plausible from unposted/in-transit moves, worth watching if it grows.

One thing you should know before this runs unattended: `stock_valuation_layer.remaining_value` is broken in this database — 527 fully-consumed layers still carry nonzero remaining_value, so `SUM(remaining_value)` returns ~$79M, nowhere near reality. I used `SUM(value)` instead, which reconciles with the balance sheet. If anyone else queries this table later without knowing that, they'll get garbage and might not notice.

The md file has the exact SQL for all three sources, the reconciliation logic, and the email format for the 8:30 AM EST send to humaira@eoxsteam.com.

[File created and presented: inventory_valuation_daily_check.md — full content:]

# Daily Inventory Valuation Check — Discount Pipe & Steel

## Schedule
- Run daily at 8:30 AM EST
- Send output to: humaira@eoxsteam.com

## Purpose
Pull the inventory valuation total from three separate screens/sources in the DPS LIVE (Discount Pipe & Steel, Odoo 13) database and confirm they reconcile. Flag any mismatch beyond a small tolerance.

## Data source
Connector: **DPS LIVE** (read-only Postgres, Odoo 13 schema for Discount Pipe & Steel). Single company: `Discount Pipe & Steel` (company_id = 1).

---

## Screen 1 — Inventory > Inventory Control > Lot/Serial Numbers (grouped by Company)
Shows on-hand quantity across lots/serials. There is no stored per-lot monetary value in this Odoo version (`stock_quant` has no `value` column), so the valuation total on this screen is Odoo's live-computed figure from the same costing engine as Screen 3. Use this query to reproduce the on-hand quantity base and cross-check against Screen 3's total:

```sql
SELECT sq.company_id, c.name AS company_name,
       SUM(sq.quantity) AS total_on_hand_qty,
       COUNT(DISTINCT sq.lot_id) AS distinct_lots,
       COUNT(DISTINCT sq.product_id) AS distinct_products
FROM stock_quant sq
JOIN res_company c ON c.id = sq.company_id
JOIN stock_location sl ON sl.id = sq.location_id
WHERE sl.usage = 'internal' AND sq.quantity <> 0
GROUP BY sq.company_id, c.name;
```

Note: `usage = 'internal'` restricts to real warehouse locations. Without this filter, quantities go deeply negative because customer/vendor virtual locations are included.

---

## Screen 2 — Accounting > Balance Sheet (Inventory Valuation line)
The balance sheet inventory figure is the posted balance of the **Stock Valuation** account (code `110100`, account_id = 3).

```sql
SELECT aml.company_id, c.name AS company_name,
       SUM(aml.debit - aml.credit) AS balance_sheet_inventory_value
FROM account_move_line aml
JOIN account_move am ON am.id = aml.move_id
JOIN res_company c ON c.id = aml.company_id
WHERE aml.account_id = 3 AND am.state = 'posted'
GROUP BY aml.company_id, c.name;
```

Last pulled value (2026-09-05): **$1,087,475.62**

---

## Screen 3 — Inventory > Reporting > Valuation (grouped by Company)
Sourced from `stock_valuation_layer`.

```sql
SELECT svl.company_id, c.name AS company_name,
       SUM(svl.value) AS total_valuation
FROM stock_valuation_layer svl
JOIN res_company c ON c.id = svl.company_id
GROUP BY svl.company_id, c.name;
```

Last pulled value (2026-09-05): **$1,101,787.95**

Important — use `SUM(value)`, not `SUM(remaining_value)`. On this database, `remaining_value` does not net down correctly on fully-consumed layers (527 layers with `remaining_qty = 0` still carry non-zero `remaining_value`), which inflates a naive `SUM(remaining_value)` to roughly $79M — nowhere close to the actual balance sheet figure. `SUM(value)` is the column that reconciles with the Stock Valuation account.

---

## Reconciliation logic for each run
1. Run all three queries.
2. Compare Screen 2 (balance sheet) total to Screen 3 (`SUM(value)`) total.
   - These should be close. A gap is expected only from unposted/in-transit stock moves not yet journaled.
   - Last observed gap: $1,101,787.95 − $1,087,475.62 = **$14,312.33**.
   - Flag if the gap exceeds ~2% of the balance sheet total, or has grown materially versus the prior run.
3. Report Screen 1's on-hand quantity/lot/product counts as supporting context, not as an independent dollar figure (no separate value column exists at the quant level in this schema).

## Email output format (to humaira@eoxsteam.com)
Subject: Daily Inventory Valuation Check — Discount Pipe & Steel — {date}

Body:
- Balance Sheet Inventory Valuation (Stock Valuation acct 110100): $X
- Inventory Valuation Report total (stock_valuation_layer, SUM(value)): $Y
- Variance: $Y − $X
- On-hand quantity (internal locations): Z, across N lots / M products
- Flag: OK / REVIEW (variance threshold breached or grew vs. last run)
