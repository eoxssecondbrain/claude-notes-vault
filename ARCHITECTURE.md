# Architecture — Threads OV (Claude Notes Vault)

This document is a complete technical reference for how this system is built, hosted, and operated: tech stack, runtime architecture, data flow, identity model, git-based persistence, and every tool/endpoint exposed. It complements (does not replace) `CLAUDE.md` (governing rules) and `SKILL.md` (agent-facing workflow instructions) — this file describes *how the machine works*, those describe *how the agent should behave*.

---

## 1. What this system is

Threads OV is a single-process **MCP (Model Context Protocol) server** that gives Claude a persistent memory for chat transcripts. It has no database, no queue, no ingestion pipeline, and no scheduled jobs — its only backing store is a **git repository**, and its only "ingestion" mechanism is Claude itself calling tools during a live conversation.

It exists to solve one problem: keep Claude-chat bookkeeping (raw transcripts, synthesized summaries, mined "tribal knowledge") completely out of **OV2** (`raj-wiki-vault`), the main EOXS second-brain vault, while still allowing a short, human-approved pointer line to cross over when something is genuinely relevant to OV2.

---

## 2. Tech stack

| Layer | Technology | Notes |
|---|---|---|
| Language | Python 3 | Single file: [mcp_server.py](mcp_server.py) (~880 lines), no other modules |
| Protocol | MCP (Model Context Protocol) via `mcp.server.fastmcp.FastMCP` | SSE transport (`mcp<2.0.0`) |
| ASGI server | `uvicorn` | Runs the raw ASGI app directly (`uvicorn.run(app, ...)`), not via `mcp.run()` |
| Web framework | `starlette` | Only used for `PlainTextResponse`/`JSONResponse` inside custom middleware and the health route |
| Persistence | **Git** (no database) | The vault's own files ARE the database; every write is a `git add / commit / push` |
| Hosting | **Render** (render.yaml, `runtime: python`, `plan: starter`) | One web service, auto-deploys on push to the `data` branch |
| Source control | Two separate GitHub repos | `eoxssecondbrain/claude-notes-vault` (this vault) and `eoxssecondbrain/raj-wiki-vault` (OV2, written to only via a separate credential) |
| Content format | Markdown with YAML frontmatter | Every saved file — transcripts, summaries, analyses — is a `.md` file |
| Dependencies | `mcp<2.0.0`, `starlette`, `uvicorn>=0.30.0` | See [requirements.txt](requirements.txt) — deliberately minimal, no ORM, no HTTP client library beyond what `mcp`/`starlette` bring |

There is no frontend, no build step, no compiled assets, no client-side code of any kind. The "client" is Claude itself, connecting as an MCP client over SSE.

---

## 3. Hosting & deployment

- **Platform**: Render, `type: web`, `runtime: python`, `plan: starter` (see [render.yaml](render.yaml)).
- **Build**: `pip install -r requirements.txt`
- **Start**: `python mcp_server.py`
- **Branch tracked**: `data` (both code and content live on the same branch — there is no separate `main`; unlike OV2, this vault has no long-running multi-account pipeline that needs to avoid a mid-run redeploy, so keeping code+content on one branch is an accepted simplification).
- **Auto-redeploy**: Render redeploys on every push to `data`. Since every save is a single small markdown file commit, a self-triggered redeploy per save is an accepted tradeoff (same pattern as OV2's own server) rather than something engineered around.
- **Persistent disk**: none. The Render service's local working copy of the git repo is the only "storage," and it's ephemeral relative to GitHub — GitHub is the actual durable store. `OV2_CLONE_DIR` defaults to `/tmp/ov2-clone`, explicitly non-persistent.
- **Port**: `PORT` env var, default `8000`.

### Environment variables (all set on the Render service, not in code)

| Var | Purpose | Required? |
|---|---|---|
| `CLAUDE_OV_USERS` | JSON map of `secret → username` — the entire identity system | **Required** — server refuses to start without it |
| `GITHUB_TOKEN` | Push credential for this vault's own repo | Optional — without it, saves stay local-only, no push |
| `GITHUB_REPO_URL` | Defaults to `https://github.com/eoxssecondbrain/claude-notes-vault.git` | Has default |
| `GIT_BRANCH` | Defaults to `data` | Has default |
| `OV2_GITHUB_TOKEN` | **Separate** fine-grained token scoped only to `raj-wiki-vault` (Contents: Read/write) | Optional — without it, `search_ov2_wiki`/`apply_ov2_xref` fail with an explicit error |
| `OV2_REPO_URL` | Defaults to `https://github.com/eoxssecondbrain/raj-wiki-vault.git` | Has default |
| `OV2_BRANCH` | Defaults to `data` | Has default |
| `OV2_CLONE_DIR` | Defaults to `/tmp/ov2-clone` on Render | Has default |
| `PORT` | Server port | Defaults to `8000` |

**Why two tokens**: a bug in this server's own-repo write path can never accidentally touch OV2, and vice versa — enforced by using structurally separate credentials, not by application-level permission checks.

---

## 4. Runtime architecture

```
                         ┌─────────────────────────────────────────┐
                         │              Render (data branch)         │
                         │                                             │
   Claude (MCP client)   │   uvicorn.run(app)                          │
   connects via SSE to   │     app = _IdentityMiddleware(mcp.sse_app())│
   https://<host>/       │                                             │
   <secret>/sse    ─────▶│   ┌───────────────────────────────────┐     │
                         │   │  _IdentityMiddleware (raw ASGI)   │     │
                         │   │  - resolves <secret> → username    │     │
                         │   │  - rewrites path to internal SSE   │     │
                         │   │  - tracks session_id → username    │     │
                         │   │  - exposes POST /<secret>/api/save │     │
                         │   └───────────────┬─────────────────────┘   │
                         │                   │ (path rewritten)         │
                         │   ┌───────────────▼─────────────────────┐   │
                         │   │   FastMCP  (mcp.sse_app())          │    │
                         │   │   sse_path = /_internal/sse          │   │
                         │   │   message_path = /_internal/messages/│   │
                         │   │   tools registered via @mcp.tool()   │   │
                         │   └───────────────┬─────────────────────┘   │
                         │                   │                          │
                         │   ┌───────────────▼─────────────────────┐   │
                         │   │  Tool functions (mcp_server.py)      │   │
                         │   │  read/write local .md files under    │   │
                         │   │  raw/ and wiki/, then git commit+push │  │
                         │   └───────────────┬─────────────────────┘   │
                         └───────────────────┼──────────────────────────┘
                                              │ git push (token in URL)
                                   ┌──────────▼───────────┐      ┌────────────────────┐
                                   │ GitHub:                │      │ GitHub:              │
                                   │ claude-notes-vault      │      │ raj-wiki-vault (OV2) │
                                   │ (GITHUB_TOKEN)          │      │ (OV2_GITHUB_TOKEN)   │
                                   │ branch: data             │      │ branch: data          │
                                   └─────────────────────────┘      └──────────────────────┘
```

### 4.1 The identity middleware (`_IdentityMiddleware`)

This is the most structurally important piece of custom code in the system, because **FastMCP only supports one fixed `sse_path` per instance**, but this service needs to support N different users each with their own connector URL. The middleware sits in front of FastMCP's ASGI app and does per-request routing/identity resolution that FastMCP itself has no hook for.

MCP's SSE transport is a **two-leg protocol**:

1. **Leg 1 — handshake**: client does `GET /<secret>/sse`. The middleware:
   - Splits the path, looks up `secret` in `CLAUDE_OV_USERS`. Unknown secret → `404`.
   - Rewrites `scope["path"]` to the fixed internal path (`/_internal/sse`) before handing off to FastMCP.
   - Sets a Python `contextvars.ContextVar` (`_current_user`) for the duration of this request.
   - **Snoops the outgoing SSE response body** for the `endpoint` event FastMCP emits (`data: /_internal/messages/?session_id=<id>`), extracts `session_id`, and records `_session_users[session_id] = username`. This is necessary because leg 2 requests carry no secret at all.

2. **Leg 2 — tool-call POSTs**: client POSTs to `/_internal/messages/?session_id=<id>` (a URL FastMCP itself generated, with no secret in it). The middleware looks up `session_id` in the in-memory `_session_users` dict to recover the username, sets the contextvar, and passes the request through.

`_session_users` is **in-memory only** — it resets on redeploy, which is fine because SSE sessions don't survive a redeploy anyway.

There's also a **third path** the middleware handles directly, bypassing MCP/SSE entirely:

3. **`POST /<secret>/api/save`** — a plain HTTP JSON endpoint (`{"thread_name": ..., "new_messages": ...}`) that calls `save_chat_transcript` directly. This exists for a deterministic **Stop hook** (a Claude Code / client-side hook that fires when a turn ends) to save transcripts without needing a live MCP tool-call round trip — same contract, different transport.

A bare `GET /` is a public, unauthenticated health check (`PlainTextResponse("ok")`) — no secret, no vault data, used by Render for liveness probing.

### 4.2 `current_user()` — the identity contract

```python
def current_user() -> str:
    return _current_user.get()
```

This is the **only** source of truth for whose thread a save belongs to. It is resolved entirely server-side, before any tool function runs, from the secret embedded in the connector URL. No tool accepts a `user` argument that affects a filename or a save — where a `user` parameter exists (on read tools), it is explicitly documented as a filter convenience only, never an identity claim. This closes off an entire class of bug/misuse where a model could be prompted into mislabeling whose conversation something is.

### 4.3 Auto-save reminder injection (`_patch_tools_with_reminder`)

Because "remember to call this tool" is not something the system can enforce at the protocol level, the server hedges by **monkey-patching every registered tool's function** (except `save_chat_transcript` itself) so that any string result it returns has a reminder banner appended:

```
⚠️ SYSTEM REMINDER: You MUST call `save_chat_transcript` before ending this turn...
```

This runs once at startup (`_patch_tools_with_reminder()`, called from `__main__`), wraps `mcp._tool_manager._tools[...].fn` for every tool. Combined with the FastMCP server's own `instructions` string (also a mandatory-auto-save directive shown to the model at connection time), this gives **two independent nudge mechanisms** — but both are explicitly documented as best-effort, not system-enforced. Nothing server-side actually blocks a turn from ending without a save; SKILL.md Section 0 is candid about this being a per-turn instruction-following exercise, not a guarantee.

---

## 5. Data model & storage layout

There is no database schema — the schema *is* the folder structure and frontmatter convention.

```
claude-notes-vault/
├── CLAUDE.md                  ← governing rules for the agent
├── SKILL.md                   ← tool reference + step-by-step workflows
├── README.md                  ← setup/deploy instructions
├── ARCHITECTURE.md            ← this file
├── mcp_server.py               ← the entire service (single file)
├── render.yaml                  ← Render deployment config
├── requirements.txt
├── index.md                     ← flat index of chat-summaries + analyses
├── raw/
│   └── claude-chat-queries/     ← Layer 1: full transcripts, one file per conversation
│         <user>_<created-date>_<thread_name>.md
├── wiki/
│   ├── chat-summaries/           ← Layer 2: topic/entity-clustered synthesis pages
│   └── analyses/                  ← separate concern: one-off "save this" pages
├── .ov2-clone/                    ← LOCAL ONLY, gitignored — working copy of OV2's repo
└── .ov2-xref-staging/              ← LOCAL ONLY, gitignored — proposed OV2 cross-refs
```

### 5.1 Three layers of compression

1. **`raw/claude-chat-queries/`** — full verbatim transcripts. One file per conversation thread, **overwritten in place** on every turn (not append-only, not one-file-per-message). This is the only layer written automatically/unattended.
2. **`wiki/chat-summaries/`** — topic-clustered synthesis, written by an agent following the SYNTHESIZE workflow (no dedicated "save" tool — the agent uses ordinary file-write tools, then commits/pushes the same way `save_analysis` does). This is where "tribal knowledge" extraction happens.
3. **A pointer line on an OV2 page** — 1-2 sentences, written only through the CROSS-LINK workflow's stage → approve → apply pipeline.

`wiki/analyses/` is a parallel, independent concern — one-off explicit-ask write-ups, not part of the transcript→summary pipeline.

### 5.2 Filename conventions

- **Raw transcripts**: `raw/claude-chat-queries/<user>_<created-date>_<thread_name>.md`
  - `<user>` — slugified `current_user()`, **never** model-supplied.
  - `<created-date>` — ISO date, fixed at the thread's *first* save; later saves on later days do not change it (`_chat_transcript_path` finds the existing file by `user_*_slug` glob, ignoring the date segment).
  - `<thread_name>` — slugified, chosen once by the agent and reused for the life of the conversation. Changing it mid-conversation orphans the old file and starts a new one — this is a documented failure mode, not a supported behavior.
- **Analyses**: `wiki/analyses/<today> <Title>.md`, with `(2)`, `(3)` suffixes on same-day title collisions.
- **Chat summaries**: `wiki/chat-summaries/<Descriptive Title>.md`, Title Case, matching OV2's own naming convention for consistency (even though the two vaults' filenames never need to cross-match programmatically).
- **OV2 xref staging**: `.ov2-xref-staging/<date>-<slugified-chat-summary-title>.md`, numeric suffix on collision.

### 5.3 Frontmatter shapes

Every file gets YAML frontmatter written by the tool that created it:

```yaml
# raw/claude-chat-queries/*.md — written by save_chat_transcript
thread_name: "..."
user: "..."
type: claude-chat
created: YYYY-MM-DD
updated: YYYY-MM-DD
```

```yaml
# wiki/analyses/*.md — written by save_analysis
title: "..."
type: analysis
created: YYYY-MM-DD
updated: YYYY-MM-DD
```

```yaml
# wiki/chat-summaries/*.md — written by hand (agent) per SKILL.md's template
title: "..."
type: chat-summary
sources: [raw/claude-chat-queries/..., ...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
```

```yaml
# .ov2-xref-staging/*.md — written by propose_ov2_xref
ov2_page_path: "..."
chat_summary_title: "..."
status: pending
created: YYYY-MM-DD
```

---

## 6. Data flow / "ingestion" pipeline

There is no traditional ingestion pipeline (no webhooks, no polling, no cron, no queue). All data enters the system through **live MCP tool calls made by Claude during a conversation**. The full lifecycle:

### 6.1 Turn-by-turn auto-save (the only automatic path)

```
User sends message
   → Claude composes a reply
   → Claude calls save_chat_transcript(thread_name, content=<verbatim full transcript>)
        → _chat_transcript_path() resolves/creates the target file path
        → frontmatter built (created date preserved across overwrites)
        → file written to raw/claude-chat-queries/
        → _git_commit_and_push() : add, commit, fetch, rebase-or-recover, push
   → Claude ends its turn
```

This repeats **every single turn** — the content passed is the full transcript so far (not a diff), so each save fully overwrites the file. This is deliberately unconditional per SKILL.md Section 0 — there is no length/triviality exception, and the content must be verbatim, not a narrated summary of the turn.

An equivalent path exists outside MCP entirely: a **Stop hook** can `POST /<secret>/api/save` with `{thread_name, new_messages}` directly, bypassing the SSE tool-call round trip — same underlying `save_chat_transcript` function, invoked directly by `_IdentityMiddleware`.

### 6.2 SYNTHESIZE (on-demand, human-triggered — "sync claude threads")

Not scheduled, not automatic. An agent runs this only when asked:

1. `list_claude_chat_queries()` → find raw transcripts not yet cited in any chat-summary's `sources` frontmatter list (i.e. "unprocessed").
2. Cluster unprocessed transcripts by **topic/entity** (client name, recurring issue, project) — explicitly not by date.
3. **Hunt for tribal knowledge** before writing anything else — informal terms, undocumented business rules, workarounds that exist nowhere else in writing. This is called out as the step most likely to be skipped under time pressure and the one that most justifies the vault's existence.
4. Write/update a `wiki/chat-summaries/<Title>.md` page (agent uses file-write tools directly — there is no `save_chat_summary` MCP tool).
5. Commit + push (same git helper as the save tools, invoked by the agent's own file-write + a manual git flow, or reusing `_git_commit_and_push`-equivalent steps).
6. Update `index.md`.

### 6.3 CROSS-LINK (on-demand, always human-approved)

The only path that can ever cause a write into **OV2's** repository. Runs after SYNTHESIZE, using that pass's "Candidate OV2 Cross-References":

1. **Verify** — `search_ov2_wiki(query)` clones/pulls a read-only local copy of OV2 (`.ov2-clone/`, via `OV2_GITHUB_TOKEN`) and greps it, to confirm the target page exists and the chat-summary adds something genuinely new (not OV2's own `search_wiki` — that's preferred if that connector is separately available in-session, this is the fallback).
2. **Draft** a single-sentence pointer line.
3. **Stage** — `propose_ov2_xref(ov2_page_path, pointer_line, chat_summary_title)` writes **only** to `.ov2-xref-staging/` in this vault's own repo. OV2 is untouched at this point.
4. **Present** the full staged batch to the user; approval must be itemized, never inferred from silence or a blanket "apply all."
5. **Apply** — `apply_ov2_xref(staged_id)`, once per approved item:
   - `_ensure_ov2_clone()` clones or hard-resets `.ov2-clone/` against `origin/<OV2_BRANCH>`.
   - Appends the pointer line under a `## Related Claude Threads` heading on the target page (creating the heading if absent).
   - Commits (`git config user.email/name = claude-ov-xref@eoxs.com / "Threads OV Cross-Reference"`) and pushes directly to OV2's `data` branch using `OV2_GITHUB_TOKEN`.
   - Deletes the local staging file on success.

### 6.4 What is explicitly *not* ingested

No emails, calls, tickets, invoices, or CRM data flow into this vault — that's OV2's domain, accessed via entirely separate MCP tools (`mcp__eoxs-wiki-db__*`) that this vault's server has no knowledge of or dependency on. This vault's only inputs are (a) live Claude conversation turns and (b) explicit "save this analysis" requests.

---

## 7. Git persistence mechanics

Since there is no database, the git layer *is* the durability and consistency mechanism, and it has to handle concurrent writers safely. `_git_commit_and_push()` (shared by `save_chat_transcript` and `save_analysis`) does the following, every single call:

1. Re-adds `origin` with the token embedded in the URL (`https://<TOKEN>@github.com/...`) — done fresh each call rather than assumed to persist, since the remote config can't be trusted to survive across the server's lifetime reliably.
2. Sets local git identity (`notes-mcp-server@eoxs.com` / `"Claude Notes MCP Server"`).
3. `git add <file>` + `git commit` — if nothing changed, returns early with "Nothing to commit."
4. **Fetch + rebase onto `origin/<branch>` before every push** — because this process's local clone only ever advances via its own commits (it never proactively re-pulls), it *will* drift behind if anything else pushes to the branch (a manual push, or a genuinely concurrent request in another process/thread). A bare push would then fail non-fast-forward *forever*, silently stranding all future saves as "committed locally, never reached GitHub" until the process restarts against a fresh clone.
5. **If the rebase itself fails** (branch has diverged onto unrelated/far-behind history — a real observed failure mode, not hypothetical) the recovery path is:
   - Abort the rebase.
   - Diff current `HEAD` against `origin/<branch>` to capture every locally-stranded commit's content as a patch (this preserves not just the current file but any other saves stranded by the same earlier failure).
   - Hard-reset the local branch to `origin/<branch>`.
   - Re-apply the captured patch (`git apply --3way`).
   - Commit and push again.
   - Every failure branch of this recovery returns a descriptive error string rather than failing silently, explicitly naming the stranded commit hash so manual recovery is possible if automated recovery itself fails.
6. **Push race retry**: if a plain push fails (someone else pushed between this process's fetch and its push), retry the fetch+rebase+push cycle exactly once more before giving up with an explicit error.

This entire mechanism exists because this is a **multi-user system with no locking** — Raj, Ayan, and others can save concurrently through the same process (or Render could theoretically run more than one instance), so the git layer has to self-heal from divergence rather than assume serialized access. This was a real incident (see recent commit history: `fix: self-heal git push when local branch diverges from origin`, and `chat: recover transcripts stranded by broken rebase`) — not a speculative design.

The same commit/push shape is reused (independently implemented as `_ov2_git`/`_ensure_ov2_clone`) for the OV2 cross-reference path, but that path only ever fetch+hard-resets before writing (no local-commit divergence to recover, since staging happens locally and `apply_ov2_xref` is the only writer to that clone).

---

## 8. Complete tool/endpoint inventory

### 8.1 MCP tools (all in [mcp_server.py](mcp_server.py), via `@mcp.tool()`)

| Tool | Purpose | Writes? |
|---|---|---|
| `save_chat_transcript(thread_name, content)` | Overwrite the current thread's transcript file, commit+push | Yes — automatic, every turn |
| `search_claude_chat_queries(query, user="")` | Grep raw transcripts, optional user filter | No |
| `list_claude_chat_queries(user="")` | List raw transcripts, newest first (cap 150 shown) | No |
| `get_claude_chat_query(file_path)` | Return one transcript's full content | No |
| `save_analysis(title, content)` | Write a one-off analysis page, commit+push | Yes — explicit-ask only |
| `search_analyses(query)` | Grep `wiki/analyses/` | No |
| `list_analyses()` | List analyses, newest first | No |
| `get_analysis(file_path)` | Return one analysis's full content | No |
| `search_chat_summaries(query)` | Grep `wiki/chat-summaries/` | No |
| `list_chat_summaries()` | List chat-summary pages | No |
| `get_chat_summary(file_path)` | Return one chat-summary's full content | No |
| `search_ov2_wiki(query)` | Grep a local read-only clone of OV2's wiki | No (to this vault); clones OV2 locally |
| `propose_ov2_xref(ov2_page_path, pointer_line, chat_summary_title)` | Stage a proposed OV2 pointer locally | Yes — local staging only |
| `list_staged_ov2_xrefs()` | List staged, not-yet-applied proposals | No |
| `apply_ov2_xref(staged_id)` | Push an approved pointer line into OV2's actual repo | **Yes — the only tool that writes to OV2** |

### 8.2 HTTP endpoints (outside the MCP tool-call protocol, handled by `_IdentityMiddleware` directly)

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Health check (`"ok"`), no auth, no secret |
| `/<secret>/sse` | GET | MCP SSE handshake (leg 1) — identity resolved from `<secret>` |
| `/_internal/messages/?session_id=...` (externally reached only via the `/<secret>/...` rewrite path internally — actual client traffic goes through leg 1/leg 2 as described in §4.1) | POST | MCP tool-call payloads (leg 2) — identity resolved from `session_id` |
| `/<secret>/api/save` | POST | Direct JSON save endpoint for Stop hooks: `{"thread_name": ..., "new_messages": ...}` → calls `save_chat_transcript` |

---

## 9. Multi-user / identity model summary

- **One process, one deployment** serves every user — Raj, Ayan, and anyone else added later.
- Each person gets **their own secret** and thus their own full connector URL (`https://<host>/<their-secret>/sse`), configured as a separate MCP connector in their own Claude account.
- `CLAUDE_OV_USERS` (a single JSON env var) is the entire user directory: `{secret: username}`.
- **Adding a user** = generate a secret (`python -c "import secrets; print(secrets.token_urlsafe(32))"`), add one entry to the env var, give them their URL. No redeploy of a new service, no code change.
- Identity is never a model-supplied value for anything that affects a filename or a save — it's resolved by server code (`_IdentityMiddleware` → `current_user()`) before the tool function body ever executes.

---

## 10. Relationship to OV2 (raj-wiki-vault)

- **Fully separate repo, separate Render service, separate branch strategy, separate push credential.** This vault's `GITHUB_TOKEN` can only ever push to `claude-notes-vault`; `OV2_GITHUB_TOKEN` is a distinct, narrowly-scoped credential that can only push to `raj-wiki-vault`.
- The **only** sanctioned data crossing into OV2 is a 1-2 sentence pointer line, written under a `## Related Claude Threads` heading on an existing OV2 page, and only after the stage→approve→apply flow in §6.3 — never raw transcript content, never full chat-summary content.
- This vault has **read** access to OV2's wiki content (via `search_ov2_wiki`, using the same `OV2_GITHUB_TOKEN`) to verify a candidate cross-reference is genuine before proposing it — but that's the only read path, and it's local-clone-based, not a live query against OV2's own service.
- OV2 itself is accessed by the agent (in a session where that connector is also enabled) via entirely different tools (`mcp__eoxs-wiki-db__*` — calls, emails, tickets, invoices, wiki pages, client files) that have no code-level relationship to this vault at all.

---

## 11. Current data scale (as of this document's writing)

- `raw/claude-chat-queries/`: 303 saved transcript files, across users `raj`, `ayan`, `jaskeerat`, and others.
- `wiki/chat-summaries/`: 21 synthesized, topic-clustered pages (e.g. *Sabre Alloys — Account History, Payment Discipline & AskCruz Proposal*, *AskCruz — Product Positioning & Vision*, *DPS (Discount Pipe & Steel) — Tickets, Licensing & Churn Signal*).
- `wiki/analyses/`: 9 one-off analysis pages.
- No entries currently staged in `.ov2-xref-staging/` at time of writing (local-only, gitignored, so this can only be checked live via `list_staged_ov2_xrefs()`).

This section is a point-in-time snapshot, not authoritative — use `list_claude_chat_queries()`, `list_chat_summaries()`, and `list_analyses()` for current counts.

---

## 12. Key design decisions and why (quick reference)

| Decision | Why |
|---|---|
| Git as the only datastore, no DB | Every write is small, infrequent, and benefits from GitHub as durable, versioned, human-inspectable storage; avoids running/paying for a separate DB for a scratchpad vault |
| One process serves all users via URL-secret identity | Avoids N separate Render services for N users; adding a user is a one-line env var edit |
| Two-leg SSE identity resolution via session_id snooping | FastMCP exposes only one fixed `sse_path`; there's no other hook to inject per-request identity into leg-2 POSTs, which carry no secret |
| Fetch+rebase+recover before every push | Multi-user, no locking — the branch WILL diverge under concurrent writers or manual pushes; discovered via a real incident, not designed speculatively |
| Two separate GitHub tokens (this repo vs. OV2) | Structural blast-radius containment — a bug here can never touch OV2's repo, enforced by credential scoping rather than application logic |
| Auto-save reminder injected into every tool response + server `instructions` | Best-effort compensation for the fact that nothing server-side can force a model to call a tool before ending its turn |
| `current_user()` never accepts a model-supplied override | Removes an entire class of misattribution risk — whose thread a save belongs to is a server fact, not something Claude reports |
| OV2 writes require explicit per-item human approval, staged first | The one place this vault can affect another system's data — deliberately slow and reviewable, never batch/silent |
