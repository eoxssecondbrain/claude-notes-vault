---
thread_name: "ppc-live-db-access-check"
user: "aryan-bakshi"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

User: Hi claude, can you tell me if you have the access to ppc live data base through connectors

Assistant: This doesn't match either skill I have set up (threads-ov covers transcript saving; eoxs-data-general covers EOXS emails/calls/wiki/tasks/tickets/invoices/CRM), and no connector here is for "PPC."

My current connectors are:

- Discount MCP (Odoo DB)
- Greer MCP (Odoo DB)
- Sabre Live (Odoo DB)
- Teams EOXS MCP (EOXS Team Live Odoo)
- EOXS Data General (curated second-brain: emails, calls, wiki, implementation tasks)
- Thread OV (chat transcript vault)

None of these is a PPC (pay-per-click / ad-platform) database. If you have a specific PPC data source in mind (Google Ads, Meta Ads, an internal PPC reporting DB, etc.), tell me which one and I can check `search_mcp_registry` for a connector, or if it's one of the Odoo instances above under a different name, point me to it and I'll query it directly.
