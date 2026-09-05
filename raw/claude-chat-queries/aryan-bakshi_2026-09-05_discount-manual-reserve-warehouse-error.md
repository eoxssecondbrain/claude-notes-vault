---
thread_name: "discount-manual-reserve-warehouse-error"
user: "aryan-bakshi"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

User: The operation cannot be completed: - Create/update: a mandatory field is not set. - Delete: another model requires the record being deleted. If possible, archive it instead.  Model: Manual Tag Reservation Line (sale.order.line.tag.reserve), Field: Reservation Warehouse (reservation_warehouse_id)

getting this error on discount pipe live server when trying to save a quote with manual reserve line.
this error only comes on manual reserve line and not on auto reserve

Assistant: No dedicated skill matches this — it's a raw Odoo schema/config investigation on the Discount MCP live server, not covered by threads-ov, eoxs-data-general, or any of the listed plugins. Proceeding with the general query/describe_table tools (read-only, per your Discount/Greer/Sabre rule).

This is a diagnostic investigation, not a one-line lookup, so pick a rigor level:

- **5ft** — pull the `sale.order.line.tag.reserve` model definition and check why `reservation_warehouse_id` is required on manual vs not on auto (likely a conditional `required` attribute tied to a reserve-type field). Fast, single-source.
- **10ft** — same, but cross-check the required-field logic against actual live rows (are auto-created lines populating that field silently, or is it just not required for them?) before concluding.
- **50ft** — full trace: model field definition, view-level `attrs`/`required` conditions, any server-side `_compute`/`create()` override that sets it for auto but not manual, and whether this is a recent break (compare against a working record if one exists) or a validation rule that's always required manual input.

Which one?

User: 50ft

Assistant: Root cause: the "Manual Tag Reservation Line" model (sale_order_line_tag_reserve) has reservation_warehouse_id defined as related="sale_line_id.reservation_warehouse_id", required=True, stored — meaning its value isn't entered directly on that line, it's inherited from the "Reservation Warehouse" field on the parent sale order line itself.

Why manual fails and auto doesn't:
- The order-line form view shows reservation_warehouse_id as a plain field on the line (no conditional attrs), and separately shows a tag_reserve_lines one2many grid (the "Manual Tag Reservation" table) that only exposes tag_id and reserved_pcs as columns — reservation_warehouse_id is never entered there.
- That grid only renders when reserve_mode = manual. For reserve_mode = auto, tag_reserve_lines is invisible entirely, so no sale_order_line_tag_reserve child records get created through the UI at all — the required-related-field check on that model is never triggered for auto lines.
- So the failure is specific to manual: if you add rows to the Manual Tag Reservation grid before the "Reservation Warehouse" field on the sale order line itself is populated, the related field on the child record has nothing to inherit, comes through as null, and hits the NOT NULL/required constraint — exactly the error text you got.

Confirmed against live data: all 1,476 existing sale_order_line_tag_reserve rows have reservation_warehouse_id populated — no exceptions — consistent with this being a hard required field that simply isn't being satisfied yet on your in-progress quote.

Fix: on the sale order line, set "Reservation Warehouse" (the field above the reserve_mode/tag grid, not inside the grid) before or while filling in the manual reserve tag rows. Once that line-level field has a value, the manual reserve lines should save.

One thing I can't verify from schema/view alone (would need the module's Python, which isn't queryable here): whether there's supposed to be an onchange that auto-populates reservation_warehouse_id when reserve_mode is switched to manual, and it's silently failing to fire for you. If setting the warehouse field manually fixes the save, that's a workaround, not a guarantee the onchange is working as designed — worth a one-line check with dev if this keeps recurring.
