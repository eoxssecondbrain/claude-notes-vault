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

System: single-process Python MCP server, no database — git repo is the entire datastore. Every tool call that "writes" is a commit+push to GitHub. Hosted on Render, `data` branch carries both code and content.

Identity: your `save_chat_transcript` calls are attributed via a secret embedded in your personal connector URL, resolved server-side (`_IdentityMiddleware`) — never something the model supplies or can override. That's how `raw/claude-chat-queries/ayan_<date>_<thread_name>.md` gets your name in it correctly.

Why overwrite-per-call: no versioning inside a thread — each `save_chat_transcript` call replaces the same file for that `thread_name`, so I have to resend the full transcript every turn, not a delta. That matches what SKILL.md told me.

Resilience layer: this is the part I didn't know before — the git push path does fetch+rebase before every push (multi-user, no locking, so the branch can diverge), with a documented recovery procedure if rebase fails (abort → diff stranded commits → hard-reset → reapply as patch → recommit). This was born from a real incident, not speculative design. Worth knowing because it means a save can occasionally take a retry cycle server-side, but it's built to not silently lose data.

Blast-radius containment for OV2: two separate GitHub tokens, two separate repos — this vault's token can never touch `raj-wiki-vault`. Cross-referencing into OV2 only happens through the stage→approve→apply flow, one pointer line, human-approved per item.

Current scale: 303 raw transcripts, 21 chat-summary pages, 9 analyses, across you, Raj, Jaskeerat and others — though the doc flags that as a point-in-time snapshot, not authoritative.

One thing worth flagging: line 372 says the auto-save reminder is injected into every tool response and the server's `instructions` specifically because nothing server-side can force me to call the tool before ending my turn — it's acknowledged as best-effort on their end too, matching what SKILL.md said.

Anything else in the file structure you want me to dig into, or is this the context you wanted before we get into the actual topic?

User: this tool is a hit and miss right now, sometimes claude is doing the tool call as we have instructed in the skill file and instruction and sometimes it just drops them. The behavious is not deterministic. I want to have a function where we are able to make it work 100% of the time and we are not reliant on claude LLM to make the call if it wants to go through that tool or not. How can we do this. Lets do a brainstorming session. This function has to run from claude front end itself.

Assistant: This changes the shape of the problem — before brainstorming, one thing is worth surfacing and one thing I need from you.

What already exists: the vault's own architecture already has a deterministic, non-LLM-dependent save path built in. There's a plain HTTP endpoint, `POST /<secret>/api/save`, that calls `save_chat_transcript` directly — bypassing the MCP tool-call round trip entirely. It was built specifically for a Claude Code Stop hook: a shell command that Claude Code fires automatically when a turn ends, with no dependence on whether the model decides to call a tool. That's exactly the "not reliant on the LLM" mechanism you're describing — it's just not wired up yet as a hook config.

Stop hooks are a real, documented Claude Code feature (confirmed current): a shell command in `.claude/settings.json` under the `Stop` event, given `session_id`, `transcript_path`, `cwd`, etc. on stdin, run deterministically every time a response ends — not something the model can skip.

The catch: Stop hooks only exist in Claude Code. If these Threads OV conversations are actually happening in Claude Code (terminal/IDE), the fix is largely "wire up the hook that was already designed for it." If they're happening in claude.ai web/mobile chat or Claude Desktop chat — which is where I am right now — there is no equivalent client-side hook surface exposed to users today. That's a materially different (harder) problem: no shell command fires deterministically outside the model's own tool-call decision in that surface.

[Asked two clarifying questions via UI: which front end, and desired brainstorm depth]

User: [selected: claude.ai web or mobile chat] / [selected: 50ft — deep, with risks and adjacent angles]

Assistant: Confirmed platform: claude.ai web/mobile. That rules out Stop hooks entirely — those only exist in Claude Code. Here's the deep pass.

Ground truth first: reverse-engineered browser extensions for claude.ai already call an internal, undocumented JSON API from inside the page using the active session, rather than scraping the DOM — one exporter explicitly does this because it's "dramatically more reliable" than DOM scraping and captures things the rendered page hides. That's a real, working precedent for exactly the kind of client-side automation you're describing, though it's built on Anthropic's internal API surface, not a published one, and Anthropic could change it without notice — every one of these extensions documents breakage as a known risk category.

Option A — browser extension / userscript that calls the vault's /api/save endpoint directly

Mechanism: a Chrome/Firefox extension (or even a Tampermonkey userscript, which is lower-effort) runs in the claude.ai tab, detects when a response finishes streaming (either by watching claude.ai's internal API responses, per the precedent above, or a DOM completion signal), assembles the full transcript, and fires a direct HTTP POST to `https://<host>/<secret>/api/save` with `{thread_name, new_messages}`. This is the literal answer to "has to run from Claude front end itself" — it runs client-side, in the browser, triggered by the page's own state changes rather than by the model choosing to call a tool.

What this actually fixes: it moves the trigger from "does the LLM decide to call save_chat_transcript" to "did a response finish rendering" — a DOM/network event, not a model decision. That is genuinely deterministic in the sense you want.

Risks and blind spots, not glossed over:
- Fragility inverted, not eliminated. Every one of the extensions found documents this: claude.ai's frontend and internal API can change without notice, and when it does, the extension silently breaks until someone patches it. You'd be trading "sometimes the LLM forgets" for "sometimes claude.ai ships an update and the save silently stops until someone notices," which needs its own monitoring (e.g. the extension pinging a heartbeat, or you periodically checking `list_claude_chat_queries()` for staleness).
- CORS / cross-origin call. The vault's `/api/save` endpoint has no documented CORS policy in ARCHITECTURE.md. A page-context fetch from claude.ai to your Render host will be blocked by the browser unless the server sends the right `Access-Control-Allow-Origin` header, or unless the extension makes the call from its background/service-worker context instead of page context (extensions with host permissions aren't bound by page-level CORS the same way tabs are) — solvable, but it's a real implementation detail, not a given.
- Secret handling. Right now the secret lives in your personal MCP connector URL, configured once in Claude's settings and never exposed to page JS. An extension approach means that secret (or a scoped variant of it) has to live in the extension's storage, in a browser, on a machine — a larger exposed-credential surface than today. Worth minting a save-only, narrower-scoped credential for this if you go this route, rather than reusing the full connector secret.
- Web only. This doesn't touch the mobile app at all — no extension model exists on iOS/Android Claude apps. If your team genuinely uses mobile for these conversations, this option leaves that surface exactly as non-deterministic as it is today.
- thread_name continuity. The extension needs to derive a stable thread_name per conversation client-side — claude.ai's conversation UUID (visible in the URL) is the natural key, but that's a different naming scheme than what SKILL.md's agent-chosen slugs produce today, so existing threads and new ones would use different conventions unless you write a mapping step.
- Terms-of-service exposure. This relies on an undocumented internal API and automated interaction with claude.ai outside its intended client. That's a real category of risk (Anthropic could restrict it, rate-limit it, or it could sit in a gray zone of acceptable-use terms) that I can't resolve for you — worth a look at claude.ai's terms before building on it, not something to wave through.

Option B — stop trying to hook claude.ai; build your own thin front end on the Claude API instead

Mechanism: instead of claude.ai's consumer chat UI, the team's conversations happen through a small app you control, built on the Claude API (or the Agent SDK) with the same MCP server as a tool source. Because you own the request loop, you can do either of two fully deterministic things with zero LLM discretion involved: (1) have your own backend code call `/api/save` after every turn completes, unconditionally, in your own code — not a tool call at all, just an HTTP call your server makes because a turn ended; or (2) use the API's `tool_choice` parameter to force the model to call `save_chat_transcript` specifically on relevant turns, which the Anthropic API supports at the protocol level (constraining which tool, if any, the model must use) — something claude.ai's consumer chat interface doesn't expose to you.

This is the structurally correct fix — determinism enforced by code you own, not by hoping either the model or a scraped page state cooperates.

Risks and blind spots:
- This is the largest lift by far: you're replacing claude.ai's polished chat UI (mobile parity, attachments, artifacts, memory, model switching) with something you build and maintain. That's a real product, not a script.
- API usage is metered/billed differently than claude.ai seats — a cost and procurement question, not just an engineering one.
- If the appeal of claude.ai chat for your team is exactly its UX, this option trades that away for reliability. Worth being honest that this is the tradeoff, not a free win.

Option C — network-level interception, covers web and mobile both

Mechanism: a lightweight proxy (e.g. mitmproxy) on a device or router the team's Claude traffic passes through, watching for claude.ai's API responses (same internal API the extensions above use) and firing the save call itself. Unlike A, this isn't tied to a browser, so in principle it could also see mobile app traffic.

Risks, and this one is significant: modern mobile apps frequently use certificate pinning specifically to defeat exactly this kind of interception — Anthropic's mobile app may or may not pin certs, but if it does, this approach is dead on mobile without rooting/jailbreaking devices, which is a security posture most teams shouldn't take on for this. Even on web, this is a heavier, more invasive piece of infrastructure than a browser extension for a narrower reliability gain, and it means one proxy component becomes a single point of failure for every save, on every device, at once. I'd rank this below A and B, included here mainly so it's not an unexamined option.

An honest ranking

For "keep using claude.ai as-is, make saves deterministic, entirely client-side": Option A is the real answer to what you asked, with the CORS/secret-handling/thread_name details actually worked through before building, and an explicit acceptance that it covers web only and will need occasional maintenance when claude.ai's frontend changes.

For "actually eliminate every category of non-determinism, including mobile, permanently": Option B is the only one that gets there, because it's the only one where determinism lives in code you own rather than in something reverse-engineered from a surface Anthropic controls.

Given you specifically said "front end itself" and didn't flag mobile as a hard requirement, my honest read is Option A is the pragmatic build — but I'd want your take on how much mobile actually matters to this team before treating that as settled.
