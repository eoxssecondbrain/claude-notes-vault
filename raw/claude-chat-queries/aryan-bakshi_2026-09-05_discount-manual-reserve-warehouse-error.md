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
