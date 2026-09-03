---
thread_name: "threads-ov-architecture-review"
user: "ayan"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

User: Hi My name is Ayan. I want to talk about how we are saving threads of claude into our threads ov repo through the MCP. Before starting on this I want to undetstand how much do you know about this?

Assistant: I've read both. Here's what I understand about the Threads OV setup, in plain terms.

Threads OV is a separate vault (isolated from your other repo, OV2/raj-wiki-vault) with three layers:

1. **Raw transcripts** (`raw/claude-chat-queries/`) — one file per conversation, full verbatim text. This is what `save_chat_transcript` writes to.
2. **Chat summaries** (`wiki/chat-summaries/`) — topic-clustered synthesis pages built from those raw transcripts, produced on demand via a SYNTHESIZE workflow (not automatic).
3. **OV2 cross-references** — short pointer lines added to your other wiki's pages, but only through a verify → propose → approve → apply chain, and only with your explicit sign-off per item.

Key mechanics on the save side, since that's what you're asking about:

- I'm supposed to call `save_chat_transcript(thread_name, content)` as the last action of every turn in this conversation, silently, with `content` being the actual verbatim text of the exchange — not a summary of it.
- `thread_name` gets picked once, on the first turn, and stays fixed for the life of the conversation even if the topic shifts.
- Same `thread_name` overwrites the same file each time — no versioned copies — so every call needs to carry the full transcript so far, not just a delta.
- `<user>` in the filename is resolved server-side from the connector URL, not something I supply.
- There's a separate, explicit-ask-only tool (`save_analysis`) for one-off findings — that's not part of the auto-save loop.

What I don't have visibility into: the underlying storage/repo structure beyond what's in the skill doc, how the auto-save is actually enforced (the doc says explicitly it's best-effort, nothing catches a missed call), or anything about how synthesis/cross-linking has gone historically for you.

What did you want to dig into — the save behavior itself, a problem you've hit with it, or something else?

User: I will give you files on this so you have a comprehensive understanding about the system.

Assistant: Go ahead — send them over and I'll go through them.

User: [uploaded ARCHITECTURE.md]

Assistant: This gives a clear architecture picture. Key points on top of the SKILL.md workflow:

**System**: single-process Python MCP server, no database — git repo is the entire datastore. Every tool call that "writes" is a commit+push to GitHub. Hosted on Render, `data` branch carries both code and content.

**Identity**: your `save_chat_transcript` calls are attributed via a secret embedded in your personal connector URL, resolved server-side (`_IdentityMiddleware`) — never something the model supplies or can override. That's how `raw/claude-chat-queries/ayan_<date>_<thread_name>.md` gets your name in it correctly.

**Why overwrite-per-call**: no versioning inside a thread — each `save_chat_transcript` call replaces the same file for that `thread_name`, so I have to resend the full transcript every turn, not a delta. That matches what SKILL.md told me.

**Resilience layer**: this is the part I didn't know before — the git push path does fetch+rebase before every push (multi-user, no locking, so the branch can diverge), with a documented recovery procedure if rebase fails (abort → diff stranded commits → hard-reset → reapply as patch → recommit). This was born from a real incident, not speculative design. Worth knowing because it means a save can occasionally take a retry cycle server-side, but it's built to not silently lose data.

**Blast-radius containment for OV2**: two separate GitHub tokens, two separate repos — this vault's token can never touch `raj-wiki-vault`. Cross-referencing into OV2 only happens through the stage→approve→apply flow, one pointer line, human-approved per item.

**Current scale**: 303 raw transcripts, 21 chat-summary pages, 9 analyses, across you, Raj, Jaskeerat and others — though the doc flags that as a point-in-time snapshot, not authoritative.

One thing worth flagging: line 372 says the auto-save reminder is injected into every tool response and the server's `instructions` specifically *because* nothing server-side can force me to call the tool before ending my turn — it's acknowledged as best-effort on their end too, matching what SKILL.md said.

Anything else in the file structure you want me to dig into, or is this the context you wanted before we get into the actual topic?

User: this tool is a hit and miss right now, sometimes claude is doing the tool call as we have instructed in the skill file and instruction and sometimes it just drops them. The behavious is not deterministic. I want to have a function where we are able to make it work 100% of the time and we are not reliant on claude LLM to make the call if it wants to go through that tool or not. How can we do this. Lets do a brainstorming session. This function has to run from claude front end itself.

Assistant: This changes the shape of the problem — before brainstorming, one thing is worth surfacing and one thing I need from you.

**What already exists**: the vault's own architecture already has a deterministic, non-LLM-dependent save path built in. There's a plain HTTP endpoint, `POST /<secret>/api/save`, that calls `save_chat_transcript` directly — bypassing the MCP tool-call round trip entirely. It was built specifically for a **Claude Code Stop hook**: a shell command that Claude Code fires automatically when a turn ends, with no dependence on whether the model decides to call a tool. That's exactly the "not reliant on the LLM" mechanism you're describing — it's just not wired up yet as a hook config.

Stop hooks are a real, documented Claude Code feature (confirmed current): a shell command in `.claude/settings.json` under the `Stop` event, given `session_id`, `transcript_path`, `cwd`, etc. on stdin, run deterministically every time a response ends — not something the model can skip.

**The catch**: Stop hooks only exist in Claude Code. If these Threads OV conversations are actually happening in Claude Code (terminal/IDE), the fix is largely "wire up the hook that was already designed for it." If they're happening in claude.ai web/mobile chat or Claude Desktop chat — which is where I am right now — there is no equivalent client-side hook surface exposed to users today. That's a materially different (harder) problem: no shell command fires deterministically outside the model's own tool-call decision in that surface.
