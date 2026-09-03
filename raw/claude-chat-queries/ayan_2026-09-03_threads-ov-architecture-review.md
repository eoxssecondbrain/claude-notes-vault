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

1. Raw transcripts (`raw/claude-chat-queries/`) — one file per conversation, full verbatim text. This is what `save_chat_transcript` writes to.
2. Chat summaries (`wiki/chat-summaries/`) — topic-clustered synthesis pages built from those raw transcripts, produced on demand via a SYNTHESIZE workflow (not automatic).
3. OV2 cross-references — short pointer lines added to your other wiki's pages, but only through a verify → propose → approve → apply chain, and only with your explicit sign-off per item.

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
- Fragility inverted, not eliminated. Every one of the extensions found documents this: claude.ai's frontend and internal API can change without notice, and when it does, the extension silently breaks until someone patches it.
- CORS / cross-origin call. The vault's `/api/save` endpoint has no documented CORS policy in ARCHITECTURE.md — solvable, but a real implementation detail, not a given.
- Secret handling. An extension approach means the connector secret (or a scoped variant) has to live in the extension's storage — a larger exposed-credential surface than today.
- Web only. Doesn't touch the mobile app at all.
- thread_name continuity. Needs a mapping between claude.ai's conversation UUID and SKILL.md's agent-chosen slug convention.
- Terms-of-service exposure. Relies on an undocumented internal API — worth checking claude.ai's terms before building on it.

Option B — stop trying to hook claude.ai; build your own thin front end on the Claude API instead

Mechanism: replace claude.ai's consumer chat UI with a small app built on the Claude API/Agent SDK. Because you own the request loop, you can have your own backend call `/api/save` after every turn unconditionally in your own code (not a tool call at all), or use the API's `tool_choice` parameter to force the model to call `save_chat_transcript` specifically — something claude.ai's consumer interface doesn't expose.

This is the structurally correct fix — determinism enforced by code you own.

Risks: largest lift by far (rebuilding UX/mobile parity/artifacts/memory), different billing model, trades away claude.ai's UX for reliability.

Option C — network-level interception (mitmproxy watching claude.ai's internal API traffic), covers web and mobile in principle.

Risk: mobile apps often use certificate pinning specifically to defeat this — likely dead on mobile without rooting devices. Heavier infrastructure than A for narrower gain. Ranked below A and B.

An honest ranking: for "keep claude.ai, make saves deterministic, client-side" — Option A. For "eliminate every category of non-determinism including mobile, permanently" — Option B is the only one that gets there.

User: we need this working both on browser, mobile and app. How can we instruct claude to make the tool call everytime? Should we have plugin function setup on claude, that ties skills to relevant MCPs to help with this? Would that be helpful?

Assistant: Two different questions here, and honestly, one has a hard ceiling you should know about before we go further.

Can wording make Claude call the tool every time, on browser, mobile, and app

No. Not with certainty, and this isn't a gap in how the instruction is worded — it's structural. On every consumer surface (claude.ai web, the mobile apps, the desktop app), a tool call happens because the model decides to make it, based on context, instructions, and the reminder text injected into every response. That's a probabilistic choice, not a protocol-enforced one. There's no equivalent of Claude Code's Stop hooks on any of these three surfaces — confirmed again by Anthropic's own comparison of these primitives: hooks fire at a fixed lifecycle event, deterministically, every time, while skills fire only when Claude decides the task matches. Skills and plugins sit on the "Claude decides" side of that line, same as the current save_chat_transcript setup. No system prompt, no reminder banner, no skill instruction changes which side of that line a tool call is on.

What you can do is raise the compliance rate, not guarantee it:
- Put the reminder as close as possible to the point of action rather than only at the top of the conversation — this system already does this, which is the right instinct, just not sufficient on its own.
- Keep the instruction short, singular, and unconditional rather than one instruction among many competing priorities in the skill file.
- Shorten how long a thread runs before drift sets in — long conversations degrade instruction-following generally.
- Add a second-order tripwire in the skill: check for a missed save at the start of the next turn and backfill it. That doesn't prevent a miss, but it bounds how long a gap lasts.

None of that changes the fundamental fact: any of these techniques takes you from "sometimes" to "usually," never to "always." If the requirement is genuinely 100%, prompting is the wrong layer to solve it at.

Would a plugin tying skills to the MCP connector help

Partially, but not with the problem you actually have. A plugin is a shareable package that bundles skills, connectors, slash commands, and subagents together, so a team member gets the MCP connector and the SKILL.md instructions in one install instead of configuring each separately. That solves a real but different problem — configuration drift across your team. It's a legitimate thing to do regardless of the determinism question.

What it doesn't do: change how a tool call gets triggered. Bundled skill instructions are still model-decided. A plugin can add a slash command (e.g. an explicit /save), which is deterministic in the sense that typing it reliably fires the action — but that shifts the reliance from "the model remembers" to "the human remembers to type it every turn."

Where this leaves you, given all three surfaces are now in scope

Of the options from the last pass: Option A, the browser extension, only ever covers the browser — nothing for mobile app or desktop app. Option C, network interception, is likely dead on mobile specifically because of certificate pinning, and is heavier infrastructure than it's worth even where it works. Neither prompting improvements nor a plugin gets you past "usually" on any surface, let alone all three.

The only option that achieves the same guarantee on browser, mobile, and desktop simultaneously is Option B — stop depending on claude.ai's client software at all, and build a thin front end on the Claude API where your own code fires the save after every turn, on every platform, because you wrote that platform.

If rebuilding the front end is off the table, the honest fallback is: accept a two-tier reliability model — near-deterministic on browser only, via the extension, and best-effort-with-monitoring everywhere else — rather than one plan that claims 100% and quietly doesn't deliver it on mobile.

User: shorten this message for the CEO on why this wont be possible to make 100% deterministic.

Assistant: Subject: Why 100% reliable auto-save isn't achievable as-is

Right now, Claude decides whether to call the save tool each turn based on instructions — there's no way to force that call, the same way there's no way to force a person to always remember a step. This works most of the time but not every time, and no amount of stronger wording changes that; it's how the underlying system is built, not a wording problem.

The tools that would force this deterministically (like Claude Code's "hooks") only exist in the developer version of Claude, not in the browser, mobile, or desktop apps we actually use — so nothing available today can guarantee 100% across all three.

We can raise the success rate meaningfully with better reminders and a catch-up check next turn. But if we need a hard guarantee, the only real fix is moving off the consumer Claude app to a version we build ourselves, where our own code (not Claude) triggers every save. That's a bigger project, not a settings change — happy to scope it if we want to go that route.
