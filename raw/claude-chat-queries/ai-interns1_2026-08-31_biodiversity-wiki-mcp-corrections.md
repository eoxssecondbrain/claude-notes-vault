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

User: how to run it locally and deploy it on render . what every tier is doing and how they are connected

Assistant: Local run

1. Create the Postgres database and load the schema.
   - Install Postgres locally (or use one already running).
   - `createdb biodiversity` (or `psql -c "CREATE DATABASE biodiversity;"`)
   - Your `.env` already has `DATABASE_URL="postgresql://postgres:Kumar123@localhost:5432/biodiversity"` — matches this.

2. Set up Python.
   - `cd` into the project folder, create/activate a venv (you already have `venv/`), then `pip install -r requirements.txt`.

3. Populate the database. You have two paths right now — pick one, don't run both against the same DB:
   - `python ingest_kaggle_data.py` — this is the one your README documents. With no dataset downloaded it auto-generates `dummy_wildlife_dataset` and ingests that, applying `schema.sql` itself first, then truncating and filling all 4 tables (species, sightings, ecological_interactions/corridors, conservation_intelligence).
   - `seed.sql` looks like a second, static way to seed data directly via `psql $DATABASE_URL -f seed.sql`. Since `ingest_kaggle_data.py` already runs schema.sql and generates its own data, seed.sql is redundant unless you built it for a different purpose (e.g. a smaller fixed dataset for demos). Tell me which one you actually want as canonical and I'll delete or reconcile the other — right now a new user reading the README has no idea seed.sql exists at all.

4. Build the Obsidian vault (optional, for the graph view): `python export_to_obsidian.py`.

5. Run the MCP server for Claude Desktop (stdio mode, the default): `python server.py`. Then add it to `claude_desktop_config.json` as a stdio server, not the SSE block in the README (that one's for the deployed version):
```json
{
  "mcpServers": {
    "biodiversity-wiki": {
      "command": "C:\\Users\\hp\\Desktop\\biodiversity wiki\\venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\hp\\Desktop\\biodiversity wiki\\server.py"]
    }
  }
}
```
Restart Claude Desktop, and the three tools (`get_tier1_sightings`, `get_tier2_interactions`, `get_tier3_risk_intelligence`) should show up.

Deploy on Render

1. Push the repo to GitHub — `.gitignore` now keeps `.env`, `venv/`, `__pycache__/` out of it.
2. On Render: New → Web Service → connect the repo. Runtime: Python. Build Command: `pip install -r requirements.txt`. Start Command: `python server.py` (the auto-detect fix means it'll switch to SSE mode on its own because Render injects `PORT`).
3. Environment variables: `DATABASE_URL` (point this at a real hosted Postgres — Neon/Supabase/Render Postgres, not localhost) and `MCP_API_KEY` (a secret string you make up — required or the endpoint is open to anyone with the URL).
4. Once it deploys, run the ingestion step once against the production DB (`DATABASE_URL=<render-db-url> python ingest_kaggle_data.py` from your machine, or a Render one-off job) since Render's Start Command only runs the server, not the ingestion.
5. Update `claude_desktop_config.json` to the SSE block from the README, pointing at `https://<your-app>.onrender.com/sse` with the `x-api-key` header set to your `MCP_API_KEY`.

What the tiers are and how they connect

Tier 1 — raw observation/telemetry (`sightings` table): individual sighting events per species — timestamp, lat/long, sensor ID, battery, temperature, image path. This is the "what was seen, where, when" layer, generated from the YOLO annotation files (each detected bounding box in a label file becomes one row).

Tier 2 — relational/ecological network (`ecological_interactions`, `corridors`, `species_corridors`): how species relate to each other (predation, mutualism) and which geographic corridors they share. This is the graph layer — it's what makes the Obsidian export non-linear, since a species note links out to its predators/prey and its corridors as wikilinks.

Tier 3 — conservation intelligence (`conservation_intelligence`): the sensitive/summary layer per species — IUCN status, poaching risk score, protected breeding zone, patrol frequency. One row per species, not per event.

They connect through `species.id`, the master table every other table foreign-keys into:
- `sightings.species_id` → which species Tier 1 events belong to.
- `ecological_interactions.species_a_id / species_b_id` → which two species a Tier 2 relationship links.
- `species_corridors` → junction table between species and corridors (many-to-many).
- `conservation_intelligence.species_id` → the one Tier 3 record per species.

So a query like "find the highest poaching-risk species, then show its recent sightings" is: look up in Tier 3 → get `species_id` → join into Tier 1 via that same `species_id`. That's exactly what your README's test prompts are exercising — each one deliberately walks from one tier to another through the shared `species_id` foreign key, which is the whole point of exposing them as three separate MCP tools instead of one flat query.
