---
thread_name: "discount-control-tag-15595"
user: "aryan-bakshi"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

User: do you also have access to basic answers for discount pipe and steel 
if yes can you tell me the totall inventory value in discount pipe rn and what is the total actuall weight of inventory in discount pipe

Assistant: [Called Discount MCP:describe_table for stock_quant, stock_valuation_layer, stock_location]
[Queried Discount MCP: SELECT SUM(remaining_value) AS total_inventory_value, SUM(remaining_qty) AS total_remaining_qty FROM stock_valuation_layer -- returned total_inventory_value: 79385974.3845297346131566, total_remaining_qty: 3613979.94540000019160248635631506707341]
[Queried Discount MCP: SELECT SUM(sq.quantity) AS total_qty_units, SUM(COALESCE(spl.weight_calculated, 0)) AS total_weight_from_lots, COUNT(*) AS quant_rows, COUNT(sq.lot_id) AS quant_rows_with_lot FROM stock_quant sq JOIN stock_location sl ON sl.id = sq.location_id LEFT JOIN stock_production_lot spl ON spl.id = sq.lot_id WHERE sl.usage = 'internal' AND sq.quantity > 0 -- returned total_qty_units: 3875077.8538, total_weight_from_lots: 2575912.2089, quant_rows: 2470, quant_rows_with_lot: 2470]
[Queried Discount MCP: SELECT COUNT(*) FILTER (WHERE spl.weight_calculated IS NULL OR spl.weight_calculated = 0) AS zero_or_null_weight_lots, COUNT(*) FILTER (WHERE spl.weight_calculated > 0) AS positive_weight_lots, COUNT(*) AS total_lots FROM stock_quant sq JOIN stock_location sl ON sl.id = sq.location_id LEFT JOIN stock_production_lot spl ON spl.id = sq.lot_id WHERE sl.usage = 'internal' AND sq.quantity > 0 -- returned zero_or_null_weight_lots: 836, positive_weight_lots: 1634, total_lots: 2470]
[Queried Discount MCP: SELECT SUM(sq.quantity * COALESCE(pp.weight,0)) AS total_weight_product_field, COUNT(*) FILTER (WHERE pp.weight IS NULL OR pp.weight = 0) AS zero_weight_field_rows FROM stock_quant sq JOIN stock_location sl ON sl.id = sq.location_id LEFT JOIN product_product pp ON pp.id = sq.product_id WHERE sl.usage = 'internal' AND sq.quantity > 0 -- returned total_weight_product_field: 0.0000, zero_weight_field_rows: 2470]

Yes — I have direct read access to Discount Pipe & Steel's live Odoo database via Discount MCP. Here's what's on hand right now:

Total inventory value: $79,385,974.38
(sum of remaining_value across all stock valuation layers — standard Odoo running inventory valuation, Discount uses FIFO/average costing)

Total actual weight: 2,575,912.21 lbs — but with a caveat
This comes from stock_production_lot.weight_calculated (the actual measured/calculated weight recorded per tag) summed across all on-hand lots in internal locations. The catch: only 1,634 of 2,470 on-hand tags (66%) have this field populated — the other 836 have it blank or zero, so this is a lower bound, not a complete total. The generic product-level weight field isn't used at all here (always 0), so there's no reliable fallback to fill the gap.

If you want a tighter number, I could try reconstructing weight for the unpopulated lots from dimensions/gauge/length fields on those specific lots — let me know if that's worth doing.

User: how many sales orders have been made today on discount

Assistant: [Queried Discount MCP: SELECT COUNT(*) AS total_orders_created_today, COUNT(*) FILTER (WHERE state IN ('sale','done')) AS confirmed_orders, COUNT(*) FILTER (WHERE state = 'draft') AS draft_quotes, COUNT(*) FILTER (WHERE state = 'sent') AS sent_quotes, COUNT(*) FILTER (WHERE state = 'cancel') AS cancelled FROM sale_order WHERE create_date::date = CURRENT_DATE -- returned total_orders_created_today: 3, confirmed_orders: 3, draft_quotes: 0, sent_quotes: 0, cancelled: 0]

3 sales orders created today (2026-08-25) on Discount Pipe & Steel — all 3 confirmed (state = sale), no drafts, no cancellations.
