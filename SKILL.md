---
name: threads-ov
description: Save and synthesize chat transcripts in a standalone vault ("Threads OV"), isolated from OV2 (raj-wiki-vault). Covers saving raw transcripts, synthesizing them into topic-clustered chat-summary pages, and proposing short cross-reference pointers into OV2's own wiki. Use whenever saving a conversation, saving an analysis, running a chat-summary synthesis pass, or linking a chat-summary to an OV2 wiki page.
---

# Threads OV — Session Skill

Three layers, in increasing compression:

1. `raw/claude-chat-queries/` — full chat transcripts, one file per conversation.
2. `wiki/chat-summaries/` — topic-clustered synthesis pages built from raw transcripts, written by the SYNTHESIZE workflow.
3. A short pointer line on an OV2 wiki page — written only via the CROSS-LINK workflow, after explicit approval.

`wiki/analyses/` is separate: one-off "save this finding" pages via `save_analysis`, explicit-ask only — not part of the chat-summary pipeline.

---

## 0. Mandatory Auto-Save Rule

Call `save_chat_transcript` as the LAST action of every single response, every turn, for the entire conversation — not just the first turn. Do this silently: no confirmation, no announcement, no exception for short or trivial replies.

1. On the FIRST turn only: choose a short, stable `thread_name` (e.g. `sabre-alloys-payment-delay`). It identifies the CONVERSATION, not the current message's topic — never change it, even on a hard, unrelated subject jump (e.g. the conversation was about incentive requests and the user suddenly asks "who is Sabre Alloys" — still the same `thread_name`). Do not re-evaluate whether the name still "fits" the latest message. Changing it creates a second file and orphans the first.
2. Compose the response normally.
3. Before ending the turn, call `save_chat_transcript(thread_name, content=<the conversation VERBATIM, in full>)`. Every turn gets its own call, even if the previous turn already saved.

**`content` is the literal text of every message, word for word — never a summary of it, no matter how long the response was.** `[Offered three rigor-level options; queried EOXS Teams Live for invoice status; found one open invoice]` is WRONG — that narrates the turn instead of reproducing it. Paste your actual response text in full: every table, every finding, every sentence exactly as written. This applies with no exception to long research/analysis responses (tables, multi-source findings, tool-call-heavy answers) — those are exactly the responses most likely to get shortened into a narrated summary because they "feel" already-said, and that instinct is wrong every time. There is no length at which reproducing the actual text becomes optional; a 2000-word findings response gets pasted as all 2000 words.

Three failure modes to actively guard against, all already observed in practice: (a) saving once at conversation start and treating that as covering the rest of the conversation — it doesn't, every turn is independent; (b) going silent the moment a message has no topical connection to what came before — an unrelated question is not a cue to reconsider `thread_name`; (c) passing a narrated summary as `content` instead of the actual verbatim exchange — a thread saved this way was never really captured, even though the tool call itself succeeded.

This is best-effort, not system-enforced — nothing outside this instruction catches a missed call, which is why it's written as a per-turn checklist rather than a general policy.

`save_analysis` is the one exception: always ask before calling it, never auto-save an analysis.

---

## 1. Tools

### Chat transcripts (Layer 1)
- **`save_chat_transcript(thread_name, content)`** — saves/updates `raw/claude-chat-queries/<user>_<created-date>_<thread_name>.md`, commits + pushes. Automatic per Section 0.
  - `<user>` is resolved server-side from the connector URL — never supplied by you, never overridable.
  - `<created-date>` is fixed at first save.
  - Same `thread_name` overwrites the same file — no `-2`, `-3` suffixes. Always pass the full transcript, not a delta.
  - `content` is verbatim text, not a summary — see Section 0. A file containing `[Offered rigor-level options; queried CRM; found one invoice]` instead of the actual question and actual response text is a broken save, even though the tool call succeeded.
- **`search_claude_chat_queries(query, user="")`**, **`list_claude_chat_queries(user="")`**, **`get_claude_chat_query(file_path)`** — read back. Optional `user` filter (e.g. `"ayan"`) restricts to one person's threads.

### Analyses (separate concern)
- **`save_analysis(title, content)`** — one-off write-up to `wiki/analyses/`. Always ask first.
- **`search_analyses(query)`**, **`list_analyses()`**, **`get_analysis(file_path)`** — read back.

### Chat summaries (Layer 2 — written by SYNTHESIZE, no dedicated save tool)
- **`search_chat_summaries(query)`**, **`list_chat_summaries()`**, **`get_chat_summary(file_path)`** — read back `wiki/chat-summaries/`.

### OV2 cross-reference (Layer 3 — propose, approve, apply)
- **`search_ov2_wiki(query)`** — searches OV2's wiki via a local read-only clone. Prefer OV2's own `search_wiki`/`get_wiki_page` if that connector is enabled.
- **`propose_ov2_xref(ov2_page_path, pointer_line, chat_summary_title)`** — stages a proposed 1-2 line addition. Local staging only, never touches OV2's repo.
- **`list_staged_ov2_xrefs()`** — lists staged items awaiting review.
- **`apply_ov2_xref(staged_id)`** — the only tool that writes to OV2's repo. Only call for a `staged_id` the user has explicitly approved.

---

## 2. Workflow: SYNTHESIZE

Run on demand ("sync claude threads"), not on a schedule.

1. Call `list_claude_chat_queries()`. Anything not yet cited in an existing chat-summary's `## Sources` is unprocessed.
2. Cluster unprocessed transcripts by topic/entity (client name, recurring issue, project) — not by date. Don't force a single unrelated thread into an existing page.
3. Hunt for tribal knowledge first, before writing the summary: informal terms mapped to real meaning, undocumented rules, workarounds, "this is just how it's done" statements — knowledge that exists only in this conversation. A thin transcript can still hide one critical entry here.
4. Write/update `wiki/chat-summaries/<Descriptive Title>.md`:

```markdown
---
title: "<Descriptive Title>"
type: chat-summary
sources: [raw/claude-chat-queries/<file1>.md, ...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Descriptive Title>

_One-sentence description._

## Summary
...synthesized narrative...

## Tribal Knowledge Extracted
- <term/rule/workaround> — <what it means> — (source: raw/claude-chat-queries/<file>.md)
  Omit only if a genuine read found nothing.

## Key Points
- Specific, dated claims.

## Sources
- raw/claude-chat-queries/<file1>.md — one-line description

## Candidate OV2 Cross-References
- <entity/topic> — <why relevant to an existing OV2 page>
```

5. Commit + push (confirm with the user if pushing isn't already agreed for this session).
6. Update `index.md` (create if missing) — flat list of chat-summary titles with one-line descriptions.

---

## 3. Workflow: CROSS-LINK

Run after SYNTHESIZE, using the "Candidate OV2 Cross-References" from step 4 above. Always: **verify → propose → approve → apply**.

1. **Verify.** Call `search_ov2_wiki` (or OV2's own tools) and read the target page. Confirm it exists, covers the same topic, and the chat-summary adds something genuinely new — not a restatement. Drop the candidate otherwise.
2. **Draft the pointer line** — one citation-style sentence, e.g. *"This issue also came up in a Claude conversation — see Threads OV: '\<title\>'."* No raw content, no transcript dates.
3. **Stage** with `propose_ov2_xref` — local only, nothing reaches OV2 yet.
4. **Present the full staged batch** for approval, one line per proposal. Never assume approval from silence.
5. **Apply only what's approved** — one `apply_ov2_xref` call per item, report each result individually (path, push success/failure). Never batch-apply silently, even on "apply all."

Once applied, the pointer lives on the OV2 page under `## Related Claude Threads` — just page text, cite it normally. If the user wants to expand on it, switch to (or ask them to enable) Threads OV and call `search_chat_summaries`/`get_chat_summary` using the exact title in the pointer line — never guess a similar one.

---

## 4. Guardrails

- Pointer lines into OV2 are 1-2 sentences, always. More detail than that means the chat-summary page isn't finished — improve it there.
- Never call `apply_ov2_xref` speculatively — it's a real commit to OV2's repo. Staging is free; applying isn't.
- `OV2_GITHUB_TOKEN` is separate from this vault's own `GITHUB_TOKEN`. If either tool reports it missing, that's a config gap — say so, don't work around it.
- Never trust a model-supplied `user` value — it's always resolved server-side from the connector URL (see CLAUDE.md).
- Every chat-summary page needs a `## Sources` section — not optional.
