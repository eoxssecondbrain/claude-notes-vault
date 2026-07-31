---
thread_name: "2026-revenue-monthly-lookup"
user: "raj"
type: claude-chat
created: 2026-07-31
updated: 2026-07-31
---

User: tell me my reveunue from 2026. monthly.

Assistant: 2026 EOXS revenue (posted customer invoices, net of credit notes), monthly:

| Month | Posted invoices | Net revenue |
|---|---|---|
| Jan | 13 | $74,491.10 |
| Feb | 2 | $20,160.00 |
| Mar | 8 | $45,244.00 |
| Apr | 3 (1 credit note) | $6,606.00 |
| May | 9 | $55,898.35 |
| Jun | 8 (2 credit notes) | $11,170.00 |
| Jul | 6 | $29,511.35 |

Total Jan–Jul 2026: $243,080.80

Notes:
- Source: account_move in EOXS Teams Live, type = out_invoice/out_refund, state = posted, invoice_date in 2026.
- Excluded: 3 canceled invoices in Jan ($15,110), 2 canceled + 1 draft in May ($38,921.15) — not real revenue.
- June's number is low because $26,560 in credit notes landed that month, likely offsetting an earlier invoice.
- No invoices in this DB for Aug 2026 onward yet (today is Jul 31).
- This is EOXS's own Teams Live instance only — doesn't include GFC/Krinox revenue, which is a separate entity and not yet invoicing.

$243K over 7 months is ~$35K/month average, against a $1M ARR / 12-month goal ($83K/month needed). You're running at roughly 42% of the monthly pace the goal requires, and April/June show real volatility, not just growth noise.

User: put it on a graph

Assistant: [Rendered a bar chart via the Visualizer showing net posted revenue by month, Jan-Jul 2026: Jan $74,491.10, Feb $20,160.00, Mar $45,244.00, Apr $6,606.00, May $55,898.35, Jun $11,170.00, Jul $29,511.35]

Jan and May are your two strong months; April and June are the weak points, both dragged down by credit notes rather than just low invoicing.
