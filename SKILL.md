---
name: claude-ov
description: Save and synthesize Claude chat transcripts in a standalone vault ("Claude OV"), isolated from OV2 (raj-wiki-vault). Covers saving raw transcripts, synthesizing them into topic-clustered chat-summary pages, and proposing short cross-reference pointers into OV2's own wiki. Use whenever saving a Claude conversation, saving an analysis, running a chat-summary synthesis pass, or linking a chat-summary to an OV2 wiki page.
---

# Claude OV — Session Skill

You are embedded inside "Claude OV" (`claude-notes-vault`) — a small, standalone scratchpad vault that exists for exactly one reason: to keep Claude-chat-transcript bookkeeping (saving, summarizing, cross-referencing) completely out of OV2 (`raj-wiki-vault`), the main EOXS second brain. OV2 must never bloat with raw transcript volume — Claude OV absorbs that entirely, and only ever hands OV2 a one-to-two-line pointer when something is genuinely relevant.

This vault has three layers, in increasing order of compression:

1. **`raw/claude-chat-queries/`** — full, unedited chat transcripts, one file per saved conversation. Immutable once written, same as OV2's `raw/`.
2. **`wiki/chat-summaries/`** — topic/entity-clustered synthesis pages built from raw transcripts. This is where real content and detail live. Separate from `wiki/analyses/` (see below) — different origin, different purpose.
3. **A short pointer line inside OV2's own wiki** — written only when a chat-summary is genuinely relevant to an existing OV2 page, via the CROSS-LINK workflow below. This is the only thing that ever touches OV2.

`wiki/analyses/` is a **separate, fourth thing** — not a layer of the chat-summary pipeline. It holds explicit, one-off "save this as a permanent analysis" requests (via `save_analysis`), the same use case OV2's `save_analysis` tool historically served. Don't conflate `wiki/analyses/` pages with `wiki/chat-summaries/` pages — they have different triggers (explicit ask vs. periodic synthesis) and different content shape (one finished write-up vs. a clustered synthesis of many raw threads).

**Read this entire document before running SYNTHESIZE or CROSS-LINK. Call `list_claude_chat_queries()` and `list_chat_summaries()` silently at the start of a synthesis session to see current state.**

---

## 0. Mandatory Auto-Save Rule — Read This First

**Save after every assistant response, automatically, with no user request needed.** This is a hard rule, not a suggestion — do not wait to be asked "save this chat."

- At the start of a conversation, silently choose a short, stable `thread_name` (e.g. `sabre-alloys-payment-delay`) that describes the conversation's topic. Never change it mid-conversation — changing it creates a second file instead of updating the first.
- After every assistant response from that point on, silently call `save_chat_transcript(thread_name, content=<the full transcript so far, not just the latest exchange>)`. Do not ask. Do not announce it. Do not skip it for short exchanges.
- This **overwrites the same file** each time — one file per conversation, not one file per message. See the tool doc below for exactly how the filename is derived.
- **Be honest about the limit of this rule**: it is best-effort, not a system-enforced guarantee. There is no mechanism outside this instruction that forces the save to happen — if you (the model) genuinely forget mid-conversation, nothing else catches it. Follow the rule as strictly as possible precisely because it's the ceiling of what's achievable here, not a formality.
- The one exception: `save_analysis` (a different tool, for one-off finished write-ups) still requires the user to confirm first — that rule is unchanged. Only `save_chat_transcript`'s per-turn behavior is now automatic.

---

## 1. Your MCP Tools

### Save / read chat transcripts (Layer 1)
- **`save_chat_transcript(thread_name, content)`** — saves/updates a conversation in `raw/claude-chat-queries/`, commits + pushes to this vault's own `data` branch. **Automatic per the rule above — never ask first, never skip.**
  - Filename produced: `<user>_<created-date>_<thread_name>.md`. `<user>` is resolved by the server itself from which connector URL the request came in on (each person has their own secret URL mapped to their name server-side — see CLAUDE.md's "Per-user identity" section) — you never supply it, and there is no argument that can override it.
  - `<created-date>` is fixed at the thread's first save and does not change on later overwrites, even if a save happens on a different calendar day than the first one.
  - Every call for the same `thread_name` (from the same user) overwrites that one file — it does not create `-2`, `-3`, etc. Changing `thread_name` mid-conversation is what would incorrectly create a second file; keep it stable.
  - Always pass the **full transcript so far**, not a delta — the tool has no concept of "append," only "replace this file's content."
- **`search_claude_chat_queries(query, user="")`**, **`list_claude_chat_queries(user="")`**, **`get_claude_chat_query(file_path)`** — read back raw transcripts. Pass `user` (e.g. `"ayan"`) to restrict to one person's threads — this filters by the `<user>_` filename prefix, so a query that names a specific person can be scoped to just their saved conversations instead of searching everyone's.

### Save / read analyses (separate concern, not part of the chat-summary pipeline)
- **`save_analysis(title, content)`** — saves a one-off synthesized write-up to `wiki/analyses/`, commits + pushes. Always ask before calling.
- **`search_analyses(query)`**, **`list_analyses()`**, **`get_analysis(file_path)`** — read back.

### Chat summaries (Layer 2 — written directly by the SYNTHESIZE workflow, not a dedicated save tool)
- **`search_chat_summaries(query)`**, **`list_chat_summaries()`**, **`get_chat_summary(file_path)`** — read back synthesized pages under `wiki/chat-summaries/`.
- There is no `save_chat_summary` tool — SYNTHESIZE writes these files directly (agent file-write tools, e.g. Write/Edit) and commits them the same way `save_analysis` does. Keeping this manual-but-scripted (rather than one more auto-push tool call) means a synthesis pass is always something you consciously run, not something that fires silently.

### OV2 cross-reference (Layer 3 — propose, approve, apply)
- **`search_ov2_wiki(query)`** — searches OV2's actual wiki content (via a local read-only clone) to verify a proposed link is grounded in a real OV2 page, not a guess. Prefer OV2's own `search_wiki`/`get_wiki_page` tools directly if OV2's MCP connector is enabled in this conversation — this is a fallback.
- **`propose_ov2_xref(ov2_page_path, pointer_line, chat_summary_title)`** — stages a proposed 1-2 line addition to an OV2 page. Writes **only** to a local staging file inside Claude OV's own repo. Never touches OV2's repo.
- **`list_staged_ov2_xrefs()`** — lists everything staged and awaiting review.
- **`apply_ov2_xref(staged_id)`** — the only tool that actually clones/pulls OV2's repo, edits the target page, commits, and pushes to OV2's `data` branch. **Call this only for a `staged_id` the user has explicitly approved in this session — never apply a batch unreviewed.**

---

## 2. Workflow: SYNTHESIZE

Run this periodically (on demand — "sync claude threads" or similar), not on a fixed schedule. It turns new raw transcripts into chat-summary pages.

1. **Find unprocessed threads.** Call `list_claude_chat_queries()`. Compare against what `list_chat_summaries()` already cites (each chat-summary page should list which raw filenames it covers, in a `## Sources` section — see page format below). Anything not yet cited by an existing chat-summary page is unprocessed.
2. **Cluster by topic/entity**, not by date. Read each unprocessed transcript. Group threads that share a real subject — a client name (e.g. "Sabre Alloys"), a recurring issue ("payment discipline"), a decision or project. Don't force a cluster of one thread into an existing page if it's not genuinely the same topic — start a new page instead.
3. **Extract tribal knowledge — this is the actual point of this whole vault, not an afterthought.** While reading each transcript, actively hunt for knowledge that exists *only* in this conversation and nowhere else in any written record: informal terms mapped to their real meaning (e.g. a client calling something "the booking date" when it's actually the ship date in the system), undocumented business rules ("we always do X before Y even though nobody wrote that down"), workarounds nobody filed a ticket for, or "this is just how it's done" statements. This is different from — and more valuable than — a plain summary of what was discussed. A transcript can produce a thin, boring summary and still contain one critical piece of tribal knowledge; don't let the summary's blandness cause you to miss it.
4. **Write or update the chat-summary page** under `wiki/chat-summaries/<Descriptive Title>.md`, following this format:

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
- <the specific term, rule, or workaround> — <what it actually means / why it matters> —
  (source: raw/claude-chat-queries/<file>.md). Leave this section out entirely (don't write
  "none found") only if a genuine, careful read turned up nothing — don't skip the search
  itself just because the conversation seemed routine.

## Key Points
- Specific, dated claims — same "specificity over generality" standard OV2 uses.

## Sources
- raw/claude-chat-queries/<file1>.md — one-line description
- raw/claude-chat-queries/<file2>.md — one-line description

## Candidate OV2 Cross-References
- <entity/topic name> — <why this might be relevant to an existing OV2 page>
```

The **"Tribal Knowledge Extracted"** section is not optional busywork — it's the reason this vault exists. Read every transcript with the specific question "what does this person know that isn't written down anywhere else?" before writing the Summary section, not after.

The **"Candidate OV2 Cross-References"** section is what feeds the CROSS-LINK workflow below — fill it in during SYNTHESIZE while the topic is fresh in context, even though the actual OV2 write happens as a separate step. A page's "Tribal Knowledge Extracted" entries are often exactly what's worth cross-referencing into OV2 — a recurring undocumented rule or workaround is precisely the kind of thing an OV2 page on the same client/topic would want a pointer to.

5. **Commit.** Use your file-write tools to save the page, then commit + push via the same git mechanics `save_analysis` uses (this is a manual git step if you don't have shell access in this session — otherwise ask the user to confirm before pushing, same as any other write-back tool).
6. **Update `index.md`** (create it if it doesn't exist yet) — a flat list of chat-summary titles with one-line descriptions, mirroring OV2's `index.md` pattern at a much smaller scale.

---

## 3. Workflow: CROSS-LINK

Run this right after a SYNTHESIZE pass, using the "Candidate OV2 Cross-References" sections written in step 4 above. This is the only workflow that ever touches OV2, and it always goes through the same three checkpoints: **verify → propose → approve → apply**. Never skip a checkpoint, and never call `apply_ov2_xref` without the user's explicit go-ahead on that specific item.

1. **Verify the match is real, not assumed.** For each candidate, call `search_ov2_wiki(<topic/entity>)` (or OV2's own `search_wiki`/`get_wiki_page` if that connector is enabled) and actually read the returned page. Confirm:
   - The page exists and covers the same entity/topic.
   - The chat-summary content adds something genuinely new (a recurring pattern, a specific incident, a detail not already on the OV2 page) — not just restating what's already there.
   If neither holds, drop the candidate. A cross-reference that duplicates existing OV2 content or points at the wrong page is worse than no cross-reference.

2. **Draft the pointer line.** One sentence, specific, in the voice of a citation — not a summary of the whole thread. Follow this shape:

   > "This issue also came up in a Claude conversation — see Claude OV: '\<chat-summary title\>'."

   Or, more specific when useful:

   > "This pattern was discussed at length in a Claude conversation — see Claude OV: '\<chat-summary title\>'."

   Do not include raw chat content, dates from the transcript, or anything beyond the pointer itself — the detail lives in the chat-summary page, not in OV2.

3. **Stage it.** Call `propose_ov2_xref(ov2_page_path, pointer_line, chat_summary_title)` for each verified candidate. This writes to local staging only — nothing has reached OV2 yet.

4. **Present the full staged batch to the user for approval**, one line per proposal, e.g.:
   ```
   3 proposed cross-references:
   1. [staged_id] → wiki/sources/sabre-alloys/Sabre Alloys — Post-Crisis Operations.md
      "This issue also came up in a Claude conversation — see Claude OV: 'Sabre Alloys Payment Discipline — AR Verification'."
   2. ...
   ```
   Ask which to apply — all, some, or none. Do not assume approval from silence or from the fact that SYNTHESIZE already ran.

5. **Apply only what's approved.** Call `apply_ov2_xref(staged_id)` once per approved item. Report back the exact OV2 page path and confirm the push succeeded (the tool's return value states this explicitly — surface it, don't assume success, same discipline OV2's own `save_chat_transcript` documentation uses).

6. **Never batch-apply silently.** Even if the user says "apply all," call `apply_ov2_xref` once per `staged_id` and report each result individually — OV2 is the main vault, and a partial failure (e.g. one push succeeds, the next fails on a stale clone) needs to be visible per-item, not swallowed into one aggregate "done."

### How this surfaces later, in an OV2 query session

Once applied, the pointer line lives directly on the OV2 page under a `## Related Claude Threads` section. When OV2 answers a query and that page is in scope, the pointer line is just part of the page text — cite it like any other line. If the user asks to expand on it, that's the cue to switch to (or ask the user to enable) the Claude OV connector and call `search_chat_summaries`/`get_chat_summary` using the exact title named in the pointer line — not a guess at a similar-sounding title.

---

## 4. Guardrails

- **Never write bulk content into OV2.** The pointer line is 1-2 sentences, always. If a cross-reference needs more than that to make sense, the chat-summary page isn't finished yet — improve it there, not by padding the OV2 line.
- **Never call `apply_ov2_xref` speculatively.** It pushes a real commit to OV2's shared repo. Staging (`propose_ov2_xref`) is free and reversible (it's a local file); applying is not something to do "to see what it looks like."
- **`OV2_GITHUB_TOKEN` is a separate credential from this vault's own `GITHUB_TOKEN`.** If `search_ov2_wiki`/`apply_ov2_xref` report the token is missing, that's a deployment/config gap, not something to work around — tell the user, don't silently skip the cross-link step without saying so.
- **`save_chat_transcript` is automatic — `save_analysis` is not.** Per Section 0, every assistant response triggers a silent `save_chat_transcript` call, no confirmation needed. `save_analysis` keeps the opposite rule: always ask first, never auto-save an analysis page. Don't conflate the two.
- **Never trust a `user` value the model itself supplies.** The `<user>` in every saved filename is resolved server-side from the connector URL (see CLAUDE.md), not from anything Claude says or infers about who it's talking to. If a search or list call needs a `user` filter, use the name as the person themselves would recognize it — but know that filtering is a convenience, not the source of truth for which file belongs to which person; the filename prefix already reflects that correctly regardless of what's passed to a search.
- **Cite sources on every chat-summary page** — the `## Sources` section listing raw filenames is not optional, same "cite everything" rule OV2's CLAUDE.md enforces.
