---
thread_name: "eoxs-ov-vault-schema-mcp-demo"
user: "ayan"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

# EOXS OV Vault Schema — MCP Demo for Dev

**User:** Ayan Dutta
**Context:** Ayan asked Claude for the schema of the "Eoxs ov" vault (EOXS second-brain MCP server) to show a developer how MCP works.

---

**User:** give me the schema of our vault eoxs ov. Need to show a dev on how mcp works

**Assistant:** Called `Eoxs ov:get_index` and returned the following schema/index:

**Top-level collections (`get_index`)**

| Collection | Count |
|---|---|
| Wiki pages | 1,800 |
| Email threads | 34,503 |
| Fireflies call transcripts | 2,270 |
| Fathom call transcripts | 133 |
| Clients | 8 |
| Implementation tasks (Odoo Kanban) | 828 |

**Wiki pages broken down by type**

| Page type | Count |
|---|---|
| entity | 721 |
| source | 308 |
| analysis | 554 |
| concept | 163 |
| overview | 20 |
| prospect | 34 |

**Tool mapping explained for the dev:**
- `get_index` → row-count summary (schema overview, no args)
- `list_wiki_pages` / `search_wiki` / `get_wiki_page` → the 1,800 wiki pages
- `list_emails` / `search_emails` / `get_email` → the 34,503 email threads
- `list_calls` / `search_calls` / `get_call` → the 2,270 Fireflies + 133 Fathom calls
- `list_clients` / `list_contacts` / `get_client_profile` → the 8 clients
- `list_implementation_tasks` / `search_implementation_tasks` / `get_implementation_task` → the 828 Odoo tasks
- `get_attachment_text` / `get_client_file` → pull raw content by ID or source path
- `list_employees` / `search_employees` / `get_employee` (+ create/update/deactivate) → HR side
- `list_assets` / `search_assets` / `get_asset` (+ create/update) → curated internal docs (SOPs, ICP, etc.)

Noted as a good example for the dev: `get_index` exposes semantic list/search/get tools rather than raw SQL — contrasted with Ask Cruz MCP, which exposes `list_tables` / `describe_table` / `query` directly against Odoo/Postgres.

---

**User:** save this thread into out vault

**Assistant:** Saved this transcript into Thread Vault (Threads OV) per the threads-ov skill.
