---
thread_name: "biodiversity-wiki-mcp-corrections"
user: "ai_interns1"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

User: i am Pragya Kumari working as intern at Eoxs . i am building a Wiki connecting it to mcp server and  . the exact task is: Structure your own LLM wiki from repo into a postgres db and create a deployed MCP link that can be connected to claude front end to run queries.

i have built some part of this project do the corrections wherever it is needed

Assistant: Reviewed your biodiversity wiki project (folder: C:\Users\hp\Desktop\biodiversity wiki — README.md, schema.sql, server.py, requirements.txt, .env, seed.sql, ingest_kaggle_data.py) and made the following corrections directly in the files:

1. Render deployment would silently fail. server.py only switched to SSE/HTTP mode when `--sse` was in argv or `TRANSPORT=sse` was set, but the README's Start Command (`python server.py`) and env var list never set either. On Render this would run in stdio mode, never bind to a port, and the web service would fail health checks. Fixed: server.py now also auto-detects Render's own `PORT`/`RENDER` env vars and switches to SSE mode automatically, so it works even if the Start Command is left as `python server.py`.

2. No access control on the deployed endpoint. Tier 3 responses print a "SECURITY LEVEL: RESTRICTED/CONFIDENTIAL/SECRET" label but nothing enforced it — once deployed on Render, the /sse endpoint would be public, and anyone with the URL could query poaching-risk scores and protected breeding zone data for every species, undermining the point of a "restricted" tier. Fixed: added optional API-key middleware (`MCP_API_KEY` env var + `x-api-key` header). Updated README's env var and Claude Desktop config instructions accordingly. This is off by default (so local stdio testing with Claude Desktop still works unauthenticated) but should be turned on before deploying since this pattern models real access-controlled data.

3. .env with a live database password had no .gitignore, and the README instructed pushing the whole repo to GitHub, which would have committed the plaintext Postgres password. Added a .gitignore (.env, venv/, __pycache__/, *.pyc, .qodo/) and a note in the README not to push .env.

4. requirements.txt didn't pin the `mcp` SDK version at all (`mcp[cli]` unpinned) — risk of a future `pip install` pulling a version that changes/removes `sse_app()`. Pinned to `mcp[cli]>=1.6.0`.

5. server.py had a dead/misleading import: it tried `from mcp.server import MCPServer as FastMCP` first (that class doesn't exist in the installed SDK) and silently fell back to the real `from mcp.server.fastmcp import FastMCP`. Removed the dead branch.

Files corrected and written back to the connected folder: server.py, requirements.txt, .gitignore (new), README.md.

Not yet reviewed in depth: ingest_kaggle_data.py logic (spot-checked, no bugs found), export_to_obsidian.py, seed.sql vs ingest_kaggle_data.py overlap (there appear to be two separate ways to populate the DB — worth clarifying which one is canonical), and the obsidian_vault output itself. Can go deeper on any of those on request.
