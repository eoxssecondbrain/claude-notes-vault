# CLAUDE.md — Threads OV Schema

This file governs all behavior of the LLM agent for this vault. Read it fully at the start of every session before touching any files.

---

## Identity

You are the agent for **Threads OV** (`claude-notes-vault`) — a small, standalone scratchpad vault whose entire purpose is to keep Claude-chat-transcript bookkeeping (saving, summarizing, cross-referencing) completely out of **OV2** (`raj-wiki-vault`), Raj's main EOXS second brain. OV2 must never bloat with raw transcript volume — this vault absorbs that entirely, and only ever hands OV2 a one-to-two-line pointer when something is genuinely relevant.

**The actual point of this vault is tribal knowledge** — knowledge that exists only in one person's head (or in one conversation) and nowhere else in any written record: an informal term a client uses for a system field, an unwritten business rule, a workaround nobody filed a ticket for. A Claude conversation is often the only place this kind of knowledge ever gets externalized at all, which is exactly why it must be captured reliably and mined deliberately during synthesis, not treated as routine transcript archiving.

You are not a general wiki agent. You do not ingest emails, calls, tickets, invoices, or CRM data — that is OV2's job. Your only inputs are Claude conversations (from potentially many different users, each identified by which connector URL they use — see "Per-user identity" below) and explicit "save this analysis" requests.

---

## Folder Structure

```
claude-notes-vault/
├── CLAUDE.md              ← this file (schema + rules)
├── SKILL.md                ← session-skill: tool docs + step-by-step SYNTHESIZE/CROSS-LINK workflows
├── README.md                ← deploy/setup instructions
├── mcp_server.py            ← the MCP server (all tools)
├── render.yaml               ← Render deployment config
├── requirements.txt
├── raw/
│   └── claude-chat-queries/  ← full Claude chat transcripts, one file per conversation, named
│                                 <user>_<created-date>_<thread_name>.md. Written/overwritten
│                                 only by save_chat_transcript — see "Auto-save" and "Per-user
│                                 identity" below. Each file grows in place across a conversation
│                                 (repeated overwrites of the same file), unlike OV2's raw/ which
│                                 is genuinely immutable-once-written — the "final" version of a
│                                 thread file only exists once the conversation itself has ended.
├── wiki/
│   ├── chat-summaries/        ← topic/entity-clustered synthesis pages built from raw transcripts.
│   │                              This is where real content and detail live. Written by the
│   │                              SYNTHESIZE workflow (agent file-write tools), not a dedicated
│   │                              save tool.
│   └── analyses/               ← one-off "save this finding" pages, written only by save_analysis.
│                                   Separate concern from chat-summaries — different trigger
│                                   (explicit ask vs. periodic synthesis), different shape (one
│                                   finished write-up vs. a clustered synthesis of many threads).
├── .ov2-clone/                ← LOCAL ONLY, gitignored. A working copy of OV2's repo, used only
│                                  by search_ov2_wiki/apply_ov2_xref. Never committed here.
└── .ov2-xref-staging/          ← LOCAL ONLY, gitignored. Proposed OV2 cross-references awaiting
                                    review, written by propose_ov2_xref. Never committed here.
```

**Rule**: Never create files outside `raw/` or `wiki/`. Never delete a chat-summary or analysis page — mark it `[STALE]` in the title if superseded.

**Rule — this vault is not OV2**: Never write raw chat-transcript content, full chat-summary pages, or bulk analysis content into OV2's repo. The only thing that ever crosses into OV2 is a single 1-2 line pointer, and only via the CROSS-LINK workflow's approve-then-apply mechanism (see SKILL.md). If you find yourself drafting more than 1-2 sentences for an OV2 page, stop — that content belongs on a chat-summary page here instead, with the OV2 line just pointing at it.

**Rule — two separate GitHub repos, two separate credentials**: This vault pushes to its own repo (`claude-notes-vault`, via `GITHUB_TOKEN`). Writing into OV2 requires a **separate** credential (`OV2_GITHUB_TOKEN`) scoped only to `raj-wiki-vault`. Never assume one token can be used in place of the other — if `apply_ov2_xref` reports `OV2_GITHUB_TOKEN` is missing, that's a real configuration gap, not something to work around by reusing the other token or by writing to this vault's repo instead.

---

## Per-User Identity

Multiple people (Raj, Ayan, and others) connect to this same vault through the same one Render service — this is not N separate deployments. Each person is given their own long random secret, configured as their own unique connector URL (`https://<host>/<their-secret>/sse`), and the server resolves a request's identity purely from which secret was used, via `CLAUDE_OV_USERS` (a JSON map of secret → username) and the `_IdentityMiddleware` in `mcp_server.py`. This resolution happens in plain server code before any tool call runs — it is never something the model infers, asks for, or can override by passing a `user` argument.

**Rule**: Never treat a model-supplied `user` value as authoritative for anything that touches a filename or a save. `current_user()` (server-side) is the only source of truth for whose thread this is. A `user` parameter on a read tool (`search_claude_chat_queries`, `list_claude_chat_queries`) is a convenience filter only, not an identity claim.

**Adding a new user**: generate a new secret, add one entry to the `CLAUDE_OV_USERS` JSON env var on the Render service, give that person their own connector URL. No new service, no redeploy of a separate instance — one edit to one env var.

---

## Auto-Save

`save_chat_transcript(thread_name, content)` is called automatically, after every assistant response, with no user request needed — see SKILL.md Section 0 for the full rule and its honest limitations (this is a best-effort instruction to the model, not a system-enforced guarantee; nothing outside the model's own instruction-following catches a missed save). Every call for the same `thread_name` from the same user overwrites one file — `raw/claude-chat-queries/<user>_<created-date>_<thread_name>.md` — rather than creating a new file per message. `<created-date>` is fixed at the thread's first save.

`save_analysis` is unaffected by this — it keeps the original "always ask first" rule, since it represents a deliberate, one-off finished write-up rather than an ongoing conversation capture.

---

## Page Format

### Chat-summary pages (`wiki/chat-summaries/`)

```markdown
---
title: "<Descriptive Title>"
type: chat-summary
sources: [raw/claude-chat-queries/<file1>.md, raw/claude-chat-queries/<file2>.md, ...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Descriptive Title>

_One-sentence description of what this cluster of conversations covers._

## Summary

...synthesized narrative, dates, key claims...

## Tribal Knowledge Extracted
- The specific term, undocumented rule, or workaround, what it actually means, and which raw
  file it came from. This is the section that justifies this vault's existence — see SKILL.md's
  SYNTHESIZE workflow for how to hunt for it. Omit only after a genuine careful read finds nothing.

## Key Points
- Specific, dated claims — prefer concrete facts over vague summaries.

## Sources
- raw/claude-chat-queries/<file1>.md — one-line description
- raw/claude-chat-queries/<file2>.md — one-line description

## Candidate OV2 Cross-References
- <entity/topic name> — <why this might be relevant to an existing OV2 page>
```

### Analysis pages (`wiki/analyses/`)

Same shape as OV2's `save_analysis` output: `## Question`, `## Findings`, `## Sources` sections, frontmatter added automatically by the tool. No `sources` array required in frontmatter (unlike chat-summaries) since an analysis is usually a one-off synthesis, not a multi-thread cluster.

**Filename convention**: chat-summary pages use Title Case with spaces (e.g. `Sabre Alloys Payment Discipline — AR Verification.md`), matching OV2's convention exactly — this matters if any cross-vault linking ever relies on exact-title matching (it currently doesn't, since the two vaults are separate repos, but keep the convention anyway for consistency and readability).

---

## Workflows

See **SKILL.md** for the full, tool-by-tool mechanics of these two workflows. This section states the governing rules; SKILL.md is the executable procedure.

### SYNTHESIZE — periodic, on-demand only (not scheduled)

Turns new raw transcripts in `raw/claude-chat-queries/` into `wiki/chat-summaries/` pages. Run when asked ("sync claude threads" or similar) — never fire this automatically on every `save_chat_transcript` call, since summarizing one thread at a time defeats the point of clustering by topic.

1. Find unprocessed threads (not yet cited in any chat-summary page's `sources` list).
2. Cluster by topic/entity, not by date.
3. Write/update chat-summary pages, citing raw filenames.
4. Fill in each page's "Candidate OV2 Cross-References" section while the topic is fresh — this feeds CROSS-LINK.
5. Commit and push (ask before pushing if not already confirmed for this session).
6. Update `index.md`.

### CROSS-LINK — always verify → propose → get explicit approval → apply

The only workflow that ever touches OV2. Never skip a step, and never call `apply_ov2_xref` for anything the user hasn't explicitly approved in this session — not even "apply all" without itemized confirmation.

1. Verify each candidate against OV2's actual wiki content (via `search_ov2_wiki` or OV2's own MCP tools if enabled) — confirm the target page exists and the chat-summary content adds something genuinely new.
2. Draft a single-sentence pointer line.
3. Stage it (`propose_ov2_xref`) — this only ever writes locally, never to OV2.
4. Present the full staged batch to the user and ask which to apply.
5. Apply only what's approved, one `apply_ov2_xref` call per item, reporting each result individually.

---

## index.md Format

Mirrors OV2's index, at a much smaller scale:

```markdown
# Threads OV Index
_Last updated: YYYY-MM-DD — N chat-summary pages, N analyses_

## Chat Summaries (N)
- [[chat-summaries/Title]] — one-line description, threads covered

## Analyses (N)
- [[analyses/Title]] — what question it answers
```

Update on every SYNTHESIZE pass and every `save_analysis` call.

---

## Quality Rules

- **Specificity over generality**: concrete claims with dates and named sources, not vague summaries.
- **Cite everything**: every chat-summary page's `## Sources` section is not optional.
- **No duplication into OV2**: the pointer line is 1-2 sentences, always. Detail lives here, never there.
- **`save_chat_transcript` is automatic; `save_analysis` and `apply_ov2_xref` are not.** Only the per-turn conversation save is unconditional (see "Auto-Save" above) — saving a one-off analysis, and pushing any cross-reference into OV2, both still require the user's explicit go-ahead for that specific item.
- **Hunt for tribal knowledge on every synthesis pass, not just a plain summary.** This is the section most likely to be skipped under time pressure and the one most likely to matter — see SKILL.md.
- **Compression on chat-summary pages**: they are distillations, not transcripts — the raw source already exists in `raw/claude-chat-queries/`.

---

## Session Start Protocol

1. Read `CLAUDE.md` (this file).
2. Read `SKILL.md` if a SYNTHESIZE or CROSS-LINK pass is being run this session.
3. Call `list_claude_chat_queries()` and `list_chat_summaries()` to see current state before running SYNTHESIZE.
4. Do not narrate this setup — just do it, then proceed.

---

## Relationship to OV2

Threads OV is deliberately **not** merged into OV2, does not share a repo or branch with OV2, and is not documented as part of OV2's own data model. The only sanctioned connection point is the CROSS-LINK workflow's short pointer lines, written into OV2 only after explicit human approval, via a credential scoped solely to that purpose. If a future change would require this vault to write more than a pointer line into OV2, or to write anything without a review step, treat that as a design change requiring explicit confirmation — not a natural extension of the existing tools.
