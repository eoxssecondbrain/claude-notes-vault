# Claude Notes Vault

A standalone scratchpad service for saving Claude chat transcripts and analysis
pages — fully isolated from the OV2 vault (`raj-wiki-vault`). Separate repo,
separate Render service, separate GitHub push target. Saving a note here never
touches OV2's code, data, or redeploy cycle, and vice versa.

## What it's for

Two write actions, exposed as MCP tools:

- **`save_chat_transcript(title, content)`** — saves a full Claude conversation
  transcript to `raw/claude-chat-queries/YYYY-MM-DD-<slug>.md`.
- **`save_analysis(title, content)`** — saves a synthesized write-up to
  `wiki/analyses/YYYY-MM-DD <Title>.md`.

Plus read-back tools so saved content is queryable later: `list_claude_chat_queries`,
`search_claude_chat_queries`, `get_claude_chat_query`, `list_analyses`,
`search_analyses`, `get_analysis`.

Every save commits and pushes directly to GitHub (`data` branch) — Render
auto-redeploys on every push, which just means the server always serves its
own latest content.

## Structure

```
claude-notes-vault/
├── mcp_server.py      ← the whole service
├── requirements.txt
├── render.yaml         ← single Render web service, no pipeline/cron
├── raw/
│   └── claude-chat-queries/   ← saved chat transcripts, one file per conversation
└── wiki/
    └── analyses/               ← saved analysis pages
```

## Running locally

```
pip install -r requirements.txt
set MCP_URL_SECRET=<random-value>
set GITHUB_TOKEN=<token-with-push-access>       # optional, saves stay local without it
python mcp_server.py
```

## Deploying

1. Create the GitHub repo `eoxssecondbrain/claude-notes-vault`, push this folder
   as the initial commit on a `data` branch (see `render.yaml` — that's the
   branch Render tracks).
2. Create a Render Blueprint from `render.yaml`, or a single web service
   manually with `buildCommand: pip install -r requirements.txt` and
   `startCommand: python mcp_server.py`.
3. Set `MCP_URL_SECRET` and `GITHUB_TOKEN` in the Render service's environment.
4. Add the deployed `https://<service>.onrender.com/<MCP_URL_SECRET>/sse`
   endpoint as a second MCP connector in Claude, alongside OV2.
