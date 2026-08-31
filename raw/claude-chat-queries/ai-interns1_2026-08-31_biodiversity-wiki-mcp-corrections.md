---
thread_name: "biodiversity-wiki-mcp-corrections"
user: "ai_interns1"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

[... earlier turns already saved ...]

User: now how to deploy on render

Assistant: Assuming you haven't pushed to GitHub yet, here's the full path from your local folder to a live Render URL.

1. Push to GitHub (from the project folder):
git init
git add server.py ingest_kaggle_data.py export_to_obsidian.py requirements.txt schema.sql seed.sql README.md .gitignore
git commit -m "Biodiversity wiki MCP server"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
Check git status before the add — confirm .env and venv/ do not show up as tracked/staged.

2. Get a hosted Postgres database (Render Postgres, Neon, or Supabase) and copy its connection string.

3. Load data into that hosted database once from your machine before/after deploying:
set DATABASE_URL=<hosted-connection-string>
python ingest_kaggle_data.py

4. On render.com: New → Web Service → connect the GitHub repo.

5. Service settings: Name biodiversity-mcp-server, Runtime Python 3, Build Command "pip install -r requirements.txt", Start Command "python server.py", Free instance type to start.

6. Environment variables: DATABASE_URL (hosted connection string), MCP_API_KEY_TIER1/TIER2/TIER3 (three different secret strings you generate — leave unset only if you want it fully open). Don't set PORT manually — Render injects it and server.py auto-detects.

7. Deploy and watch build logs for "PostgreSQL Database Connection Pool initialized successfully." and "Starting MCP SSE Server on port <n>...".

8. Endpoints: https://<your-app-name>.onrender.com/sse and /messages.

9. Point Claude Desktop at it using the JSON block in the README, x-api-key set to whichever tier key matches the desired access level for that connection.

Noted the free-tier gotcha: service spins down after 15 min idle, ~30-50s cold start on next request — not a code bug.

Asked if the user wants Claude in Chrome to drive the actual Render dashboard clicks, or if they're doing the deploy themselves.
