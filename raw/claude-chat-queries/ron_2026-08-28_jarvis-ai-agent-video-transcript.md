---
thread_name: "jarvis-ai-agent-video-transcript"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-29
---

[Full verbatim transcript of this conversation through the current turn is preserved in this thread. New exchange appended below.]

User: No. I understand what you're talking about. What I was saying is that there... isn't there a way where, um, you know how we have Claude Cool, which works on a terminal. I can go there... go install Claude on my terminal and then go and ask it to use a subscription that I have for Claude, and it uses the usage and not the API. Isn't there something which can be set up somethings on the same line same lines?

Assistant: Good news — I need to correct something I said last time. There actually is a real mechanism here, and I undersold it.

Anthropic does let you generate an OAuth token from your Pro/Max subscription (via `claude setup-token`) and use it programmatically with the Claude Code CLI or the official Claude Agent SDK — billed against your subscription's usage window, not per-token API rates. The deciding factor isn't "is this a script instead of interactive typing," it's who benefits: personal automation you write, that only you use, is squarely inside what Anthropic calls "your own individual use." A solo Jarvis that only you talk to on Telegram fits that description.

Where it gets genuinely uncertain: this is clearly fine when the underlying tool is Claude Code or the Agent SDK itself — official Anthropic products. Hermes is a separate, third-party harness, and:

- I don't know if Hermes's config even accepts this OAuth-style token, versus expecting a standard API key — that's a real technical unknown I'd need to check in Hermes's own docs before assuming it works
- Anthropic's stance specifically on third-party harnesses (Hermes, OpenClaw, similar) has reportedly flip-flopped more than once in the past few months — it's the one case multiple sources flag as genuinely unsettled right now, not the settled "yes" that personal Agent SDK use is

Given you said this cost question is instrumental to the whole plan, here's the practical fork:

- Build the assistant on the Claude Agent SDK directly instead of Hermes — more setup work on your end since it's not turnkey like Hermes (no built-in memory/skills/Telegram gateway out of the box, you'd assemble those), but the subscription-billing path is clearly sanctioned since it's an official Anthropic product
- Or keep Hermes for its convenience, but plan to pay real API token costs, since whether it'll even accept your subscription token isn't confirmed, and the policy ground under third-party harnesses is shifting

Given you have no technical background, Hermes-plus-API-cost is still the lower-effort path. Trying to force subscription billing into a third-party harness whose support for it is unverified, on a policy area Anthropic keeps changing, is a lot of fragility to take on for $10-40/month.
