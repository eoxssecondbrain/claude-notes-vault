---
thread_name: "claude-tooling-concepts-overview"
user: "sebastian"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

USER: make a list of different concepts such as automations, Claude skills, Claude Cowork, Company Brain, and others im not considering in this list. This is for us to learn about each and its own diferences for us to implement and use in the correct way

ASSISTANT: This spans multiple things, not a clean match to eoxs-data-general (no EOXS data lookup here) or sales-strategist (not GTM/deal/objection work). It's a product-knowledge research task, so I'll pull from docs rather than guessing.

Two things before I start:
[ask_user_input_v0 widget: 
Q1: "Rigor level for this?" options: ["5ft - quick summary from docs","10ft - verified against primary sources","50ft - deep, includes adjacent concepts + tradeoffs","100ft - staged, delivered section by section"]
Q2: "What do you mean by 'Company Brain' in your list?" options: ["Our own eoxs-db / internal wiki setup specifically","The generic concept (any org's internal AI knowledge base) as one list item","Not sure - you decide how to frame it"]
]

USER (widget response):
Q: Rigor level for this?
A: 50ft - deep, includes adjacent concepts + tradeoffs

Q: What do you mean by 'Company Brain' in your list?
A: Our own eoxs-db / internal wiki setup specifically

ASSISTANT: Quick framing before the list: several of these aren't peers — some are layers that sit inside others. I'll flag that as I go, because treating them as parallel options is the most common way this gets misapplied.

1. Automations (general term — Zapier / Make / n8n style)
Deterministic, trigger-based workflows: "when X happens, do Y," no model reasoning involved, no judgment calls. Fast, cheap, predictable, auditable. Right tool when the steps never change — e.g. "new lead in Odoo → assign to SDR queue → Slack the rep." Wrong tool the moment the task needs interpretation (reading a call transcript and deciding what matters). This is infrastructure you'd run alongside Claude, not a Claude product.

2. Model Context Protocol (MCP) / Connectors
The plumbing, not a feature you "use" directly — an open standard (Anthropic, Nov 2024) that lets Claude call out to external systems (databases, Slack, your own tools) through a common interface instead of a custom integration per source. Claude for Work customers can test MCP servers locally, connecting Claude to internal systems and datasets. This is the layer everything else in this list either sits on top of or gets exposed through — your "AskCruz," "Eoxs-Teams," "Eoxs-data-general," and "Thread OV" connectors are all MCP servers. Company Brain (below) is delivered to me through this exact mechanism.

3. Claude Skills (Agent Skills)
Not a data source, not an app — a packaged instruction set (a folder with a SKILL.md file, optionally scripts/reference docs) that teaches Claude how to do a specific task consistently. Skills package your expertise and procedures so Claude delivers expert-level output every time, and organizations use them to apply brand guidelines or follow preferred formats in docs, meeting notes, and more. Loads only when relevant, no context cost until read. This is what your sales-strategist and eoxs-data-general skill files already are — the mechanism, formalized. Right fit for: standardizing how every SDR handles an objection, or how every proposal gets formatted.

4. Claude Projects
A Claude.ai workspace with persistent context (uploaded docs, custom instructions) scoped to one recurring subject — lighter-weight than a Skill (no procedural logic, just standing context) and lighter than Company Brain (static uploads, not live-synced data). Good for "everyone drafting AskCruz outreach should see the same ICP doc and messaging examples" without wiring up a connector.

5. Claude Cowork
An agentic mode inside Claude Desktop, using the same agentic architecture that powers Claude Code, accessible without opening the terminal. Give it a multi-step outcome, it plans, executes across sub-agents in parallel, and returns finished deliverables — Excel spreadsheets with functional formulas, PowerPoint presentations, and formatted documents. It's the orchestrator that calls Skills and MCP connectors as needed, on its own judgment, rather than a fixed workflow. Cowork is best-fit for one-off or semi-recurring heavy lifts (a market scan, a client research pack) — not for something that needs to run identically every single time, which is where deterministic automation is more reliable and cheaper per run.

6. Claude Code / Claude Agent SDK / Managed Agents
The developer end. Claude Code is the terminal/IDE agent for building software. The Agent SDK is that same agent loop exposed as a library so your own engineers can embed a Claude-powered agent inside a product or an unattended pipeline — Claude Agent SDK: build agents that run in a process you operate, versus Claude Managed Agents: run agents in Anthropic's managed infrastructure if you don't want to host it yourself. This is the option if AskCruz itself wants to ship agentic behavior to customers, not just use Claude internally.

7. Company Brain (your eoxs-db setup)
Your own build, not an Anthropic product — a curated "second brain" combining live-ingested emails/calls, a synthesized wiki layer, and tiered access control (tier1/tier2/tier2_confidential, with monetary figures and monitoring data stripped at the response layer). Architecturally it's MCP (item 2) plus a retrieval/synthesis layer you built on top — closer to RAG than to a Skill, since it's injecting live company knowledge rather than teaching a procedure. Its distinguishing risk, correctly handled here, is that anything exposed to a model this way is a confidential-data exposure surface — the tiering and redaction you've already built is the mitigation, and it's the bar any new connector should be held to before it gets added.

8. Memory (Claude's built-in persistent memory)
Different from Company Brain: this is Claude retaining facts about one user across their own conversations (preferences, project context), not a shared organizational knowledge base. Useful for individual continuity, not for "everyone on the team should know this."

9. Claude Tag
Slack-native, tag-and-delegate — @Claude in a channel to hand off a task without leaving Slack. Lower ceremony than Cowork, narrower scope, good for quick asks from non-technical staff who live in Slack.

Where this actually bites you if left unclarified: these aren't a menu of alternatives to pick one from — they stack. A realistic AskCruz build looks like: Company Brain and AskCruz data exposed via MCP → an SDR-training Skill standardizing how calls get scripted/critiqued → Cowork or the Agent SDK orchestrating the actual multi-step task → plain automation handling the deterministic parts (lead routing, notifications) that don't need a model's judgment at all. Treating "should we use Skills or Cowork" as an either/or is the most common misapplication. Second flag: roughly half of what's above shipped or changed materially in the last two quarters (Cowork went GA mid-2026, the Agent SDK was renamed from Claude Code SDK), so re-verify specifics against docs before committing engineering time to any one of these.

Sources: claude.com/docs/cowork/overview, anthropic.com/news/model-context-protocol, platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, claude.com/blog/building-agents-with-the-claude-agent-sdk, platform.claude.com/docs/en/cli-sdks-libraries/overview.
