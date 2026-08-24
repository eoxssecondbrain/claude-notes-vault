---
thread_name: "local-backend-data-storage-check"
user: "nidhi"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

User: i have setup my backend server locally now how to see if data is stored or not

Assistant: Which backend are you referring to? A few local-storage projects are in flight and the check differs by which one:

1. **email-to-db-automation** — n8n workflow, Gmail → local Postgres (emails + email_attachments tables)
2. **email-filter-and-store** — spam/promo filter, non-spam stored in the same local Postgres pipeline
3. **gmail-double-ai-spam-filter** — two-stage AI spam detection, candidates staged in Google Sheets before Postgres
4. Something else entirely (askcruz email harvester, Cruz backend, a new server not yet in memory)

Tell me which one and I'll give you the exact check (psql query, table names, or wherever the data actually lands).
