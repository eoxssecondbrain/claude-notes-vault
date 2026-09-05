---
thread_name: "odoo-warning-text-extract"
user: "hashir"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

User: can you provide me the text part from this warning
[uploaded image: /mnt/user-data/uploads/1788618818135_image.png — Odoo error dialog screenshot]

Assistant: The warning text reads:

**Something went wrong !**

The operation cannot be completed:
- Create/update: a mandatory field is not set.
- Delete: another model requires the record being deleted. If possible, archive it instead.

Model: Manual Tag Reservation Line (sale.order.line.tag.reserve), Field: Reservation Warehouse (reservation_warehouse_id)

It's an Odoo validation error on the sale order line — the `reservation_warehouse_id` field on the Manual Tag Reservation Line model isn't populated.
