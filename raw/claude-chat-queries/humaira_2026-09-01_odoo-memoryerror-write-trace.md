---
thread_name: "odoo-memoryerror-write-trace"
user: "humaira"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: [Uploaded image: /mnt/user-data/uploads/1788278697305_image.png — screenshot of Odoo Error dialog. Traceback content:]
return super(WebsitePublishedMixin, self).write(values)
File "/opt/odoo13/odoo/addons/rating/models/rating_mixin.py", line 76, in write
result = super(RatingMixin, self).write(values)
File "/opt/odoo13/odoo/odoo/models.py", line 3640, in write
self.modified(vals)
File "/opt/odoo13/odoo/odoo/models.py", line 5872, in modified
for field, records, create in tocompute:
File "/opt/odoo13/odoo/odoo/models.py", line 5945, in _modified_triggers
yield from records._modified_triggers(val)
File "/opt/odoo13/odoo/odoo/models.py", line 5945, in _modified_triggers
yield from records._modified_triggers(val)
File "/opt/odoo13/odoo/odoo/models.py", line 5926, in _modified_triggers
records = self[invf.name]
File "/opt/odoo13/odoo/odoo/models.py", line 5768, in __getitem__
return self._fields[key].__get__(self, type(self))
File "/opt/odoo13/odoo/odoo/fields.py", line 2374, in __get__
return comodel.union(*[get(record, owner) for record in records])
File "/opt/odoo13/odoo/odoo/models.py", line 5701, in union
return self.browse(OrderedSet(ids))
File "/opt/odoo13/odoo/odoo/tools/misc.py", line 1080, in __init__
self._map = OrderedDict((elem, None) for elem in elems)
MemoryError

What is this error ? "MemoryError" ?

Assistant: This doesn't match either available skill (threads-ov is for saving/synthesizing conversations, eoxs-data-general is for EOXS business data queries) — it's a general Odoo/Python troubleshooting question, so I'll just answer it directly.

The error: this is a Python MemoryError, raised at the bottom of the traceback in tools/misc.py, inside OrderedDict construction. It's not a bug in your business logic — Odoo ran out of available RAM while building an in-memory structure.

What's actually happening, reading the trace top to bottom:

1. A write() on a record triggers RatingMixin.write() → WebsitePublishedMixin.write() — so a rating (customer feedback / helpdesk / project rating, depending on which Odoo module this is) got updated.
2. Odoo's modified() mechanism kicks in to recompute dependent fields (_modified_triggers), and it's traversing an inverse field (invf.name) — following a relation backward to find all related records that need recomputation.
3. That traversal calls self.browse(ids) and unions massive recordsets together.
4. Building the OrderedSet/OrderedDict for that combined recordset is what blows up — Python literally couldn't allocate enough memory to hold it.

So the proximate cause is a recomputation cascade touching an unexpectedly huge number of records — a classic symptom of:

- A computed field with a broad, unindexed, or misconfigured inverse relation (the _modified_triggers chain fanning out to way more records than intended)
- Or simply the Odoo worker process hitting its memory limit (limit_memory_hard / limit_memory_soft in the Odoo config) on a large dataset

Likely fixes to check, in order of effort:

- Check the Odoo server's memory limits (--limit-memory-hard, --limit-memory-soft in odoo.conf) — if these are set low relative to the dataset, raise them.
- Check actual server RAM/swap — if the box itself is memory-constrained, that's the real limit.
- Identify the specific computed field being triggered by this rating write, and check its @depends / inverse relation — if it's fanning out across an entire table rather than a scoped set, that's a data-model issue worth fixing rather than just throwing more RAM at it.
- If this happens on one specific record, check whether that record (or a related one) has an abnormal number of linked records (e.g., a rating tied to a partner with hundreds of thousands of related records).

Not a corruption issue, not something you fix by retrying — it'll keep happening on that same write until either the memory ceiling is raised or the fan-out is reduced.
