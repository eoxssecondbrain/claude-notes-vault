# Claude Notes Vault ("Threads OV")

A standalone scratchpad service for saving Claude chat transcripts and mining them
for tribal knowledge — fully isolated from the OV2 vault (`raj-wiki-vault`).
Separate repo, separate Render service, separate GitHub push target. Saving a
note here never touches OV2's code, data, or redeploy cycle, and vice versa.

See `CLAUDE.md` for the governing rules and `SKILL.md` for the full tool
reference and step-by-step SYNTHESIZE/CROSS-LINK workflows.

## What it's for

- **`save_chat_transcript(thread_name, content)`** — saves/updates a conversation
  transcript. Called automatically after every assistant response (see SKILL.md
  Section 0) — never waits to be asked. Overwrites the same file across a whole
  conversation rather than creating one file per message. Filename:
  `raw/claude-chat-queries/<user>_<created-date>_<thread_name>.md`, where `<user>`
  is resolved server-side from which connector URL the request came in on (see
  "Multi-user setup" below) — never supplied by the model.
- **`save_analysis(title, content)`** — saves a one-off synthesized write-up to
  `wiki/analyses/`. Still requires explicit user confirmation before each save.
- A **SYNTHESIZE** workflow (agent-driven, not a single tool call) clusters raw
  transcripts by topic into `wiki/chat-summaries/` pages, explicitly hunting for
  tribal knowledge — undocumented terms, rules, and workarounds that exist only
  in that conversation.
- A **CROSS-LINK** workflow proposes short 1-2 line pointers into OV2's own wiki
  when a chat-summary is genuinely relevant, via a stage-then-approve-then-apply
  flow (`propose_ov2_xref` → user review → `apply_ov2_xref`).

Plus read-back tools: `list_claude_chat_queries`, `search_claude_chat_queries`
(both take an optional `user` filter), `get_claude_chat_query`, `list_analyses`,
`search_analyses`, `get_analysis`, `list_chat_summaries`, `search_chat_summaries`,
`get_chat_summary`, `search_ov2_wiki`, `list_staged_ov2_xrefs`.

Every save/apply commits and pushes directly to GitHub — Render auto-redeploys
on every push, which just means the server always serves its own latest content.

## Structure

```
claude-notes-vault/
├── CLAUDE.md            ← governing rules (read this first)
├── SKILL.md              ← tool reference + workflows
├── mcp_server.py          ← the whole service
├── requirements.txt
├── render.yaml             ← single Render web service, no pipeline/cron
├── raw/
│   └── claude-chat-queries/   ← saved chat transcripts, <user>_<date>_<thread>.md
├── wiki/
│   ├── chat-summaries/          ← synthesized, tribal-knowledge-mined pages
│   └── analyses/                 ← one-off saved analyses
├── .ov2-clone/                  ← LOCAL ONLY, gitignored — working copy of OV2's repo
└── .ov2-xref-staging/            ← LOCAL ONLY, gitignored — proposed cross-references
```

## Multi-user setup

One service serves everyone — adding a user is a config edit, not a new
deployment. `CLAUDE_OV_USERS` is a single JSON object mapping each person's own
long random secret to their username:

```json
{"9f8a...longrandom...": "raj", "3e7c...longrandom...": "ayan"}
```

Give each person their own connector URL using their own secret:
`https://<host>/<their-secret>/sse`. The server resolves identity from the URL
itself (see `_IdentityMiddleware` in `mcp_server.py`) before any tool call
runs — this is enforced by the server, not inferred by the model.

Generate a secret per user with:
```
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## Running locally

```
pip install -r requirements.txt
set CLAUDE_OV_USERS={"<random-secret>": "yourname"}
set GITHUB_TOKEN=<token-with-push-access>       # optional, saves stay local without it
set OV2_GITHUB_TOKEN=<separate-token-scoped-to-raj-wiki-vault>   # optional, only needed for cross-link tools
python mcp_server.py
```

## Deploying

1. Create the GitHub repo `eoxssecondbrain/claude-notes-vault`, push this folder
   as the initial commit on a `data` branch (see `render.yaml` — that's the
   branch Render tracks).
2. Create a Render Blueprint from `render.yaml`, or a single web service
   manually with `buildCommand: pip install -r requirements.txt` and
   `startCommand: python mcp_server.py`.
3. Set these in the Render service's environment: `CLAUDE_OV_USERS`,
   `GITHUB_TOKEN`, `OV2_GITHUB_TOKEN` (a separate fine-grained token scoped
   only to `eoxssecondbrain/raj-wiki-vault` with Contents: Read and write).
4. Each user adds their own `https://<service>.onrender.com/<their-secret>/sse`
   endpoint as an MCP connector in their own Claude account, alongside OV2.
