---
thread_name: "discount-tag-10727-packing-lists"
user: "ron"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

User: I want you to use the Discount MCP and get me information of this tag and give me the names of all the packing list where this tag is added. Tag name is 10727.

Assistant: **Tag 10727** is a lot record (id 15579, product_id 648 — "6 BAR GATE" variant, 10 pcs, currently flagged `stock_status: in_packing_list`).

It appears on 2 packing lists:

| Packing List | State | Date | Origin |
|---|---|---|---|
| BPT/IN/00597 | Done | 2026-02-25 | P00374 (purchase receipt) |
| BPT/OUT/04714 | Waiting | 2026-08-20 | S06128 (sale order) |

So it was received in via P00374 and is currently staged to go out against sale order S06128, not yet completed.

Source: Discount MCP (live Odoo 13 DB) — stock_production_lot, stock_move_line, stock_picking.
