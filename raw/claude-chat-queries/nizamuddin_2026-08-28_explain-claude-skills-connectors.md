---
thread_name: "explain-claude-skills-connectors"
user: "nizamuddin"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

**User:** their is a skills session in Claude explain me

**Assistant:** Skills in Claude are packaged sets of instructions — folders containing best-practice guides, workflows, or reference material for a specific kind of task. They are not built into Claude's default behavior. Instead, each available skill is listed to Claude with a one-line description, and when your request matches one, Claude calls it explicitly to load its full instructions before proceeding.

There are a few categories active in this session:

Anthropic-provided skills for output formats — docx, xlsx, pptx, pdf, artifact-design, dataviz, and similar. These tell Claude how to build a specific kind of deliverable correctly.

Org/custom skills specific to your setup — threads-ov and eoxs-data-general are yours. threads-ov defines how conversations get saved into a notes vault (raw transcripts, then synthesized chat-summaries, then optional cross-links into your OV2 wiki). eoxs-data-general defines which EOXS data connector to use for a question and what access-scope rules apply.

Workflow skills — things like setup-cowork, cowork-plugin, skill-creator, claude-in-chrome, which handle setup, automation, or meta-tasks like building new skills.

Per your standing preference, I load threads-ov and eoxs-data-general at the start of every new thread regardless of topic — which is why those two loaded above before I answered this.

A skill can either inject its instructions directly into my current turn (what happened here) or run as a background subagent that reports back later. You invoke one explicitly by name (/skill-name) or Claude invokes one automatically when a request clearly matches its description.

This particular question — asking what skills are — doesn't correspond to a task any of the loaded skills cover, so no skill executed beyond the mandatory threads-ov/eoxs-data-general read.

**User:** give me connection between connector and skills

**Assistant:** Connectors and skills sit at different layers.

A connector is an MCP server — the actual pipe to an external system. It exposes callable tools. In this session:

EOXS_data_general connector exposes the eoxs-db tools (get_client_profile, search_emails, search_calls, list_implementation_tasks, get_asset, etc — 20 tools, the curated "second brain").

Team_EOXS connector exposes eoxs-teams tools (query, list_tables, describe_table, get_business_schema — raw SQL against live Odoo, the only source for tickets, invoices, and CRM/pipeline data).

Thread_OV connector exposes save_chat_transcript, save_analysis, the chat-summary readers, and the OV2 cross-link tools.

A skill is the instruction layer that tells me how to use one or more connectors correctly — it doesn't add new tools, it adds judgment. It says which connector to reach for given the question, in what order to call things, what's cheap versus wasteful, what access-scope or redaction rules apply, and how to format the answer.

The mapping here:

eoxs-data-general skill governs both EOXS_data_general and Team_EOXS. One skill, two connectors, because most real EOXS questions need both — eoxs-db for correspondence/history, eoxs-teams for live tickets/invoices/CRM — and the skill's job is telling me which one a given question actually belongs to, plus the tier2/tier2_confidential redaction rules that apply to eoxs-db specifically.

threads-ov skill governs the Thread_OV connector only — the save-every-turn rule, the raw-transcript to chat-summary to OV2-cross-link pipeline, and when each tool in that chain gets called.

So: connector = the tool pipe, skill = the operating manual for that pipe. A connector works without a skill (you could call its tools directly with no guidance), but a skill without its connector is just unusable instructions with nothing to execute against. That's also why your standing rule loads both threads-ov and eoxs-data-general at the start of every thread — they're the manuals for the two connector groups (Thread_OV, and EOXS_data_general + Team_EOXS) that every EOXS-context conversation is likely to touch.

**User:** [Shared two screenshots of another Claude conversation, titled "Section 2: How AskCruz uses this — two angles, and one uncomfortable overlap". Visible text:

Angle A — Internal ops (use Skills right now, low effort, real payoff)
You're already doing this with me (threads-ov, raj-eoxs-vault, sales-strategist). Extend the same pattern across the org:
- Turn recurring playbooks into Skills instead of re-explaining them per chat: the Copilot objection-handling script, the "Sabre never appears externally" rule, pricing floors, the Collier-style deal-stage checklist.
- This matters most for the 50 MBA intern cohort. Right now output quality depends on each intern re-describing context every session. A shared skill folder (or a few, by function — sales outreach, research, fulfillment) standardizes their output without you reviewing every draft.
- This is literally the "Company Personalization" layer in your own 8-layer AskCruz vision, except you can start building it today, for EOXS internally, with zero AskCruz product work.

Angle B — Product positioning, and this is the part worth sitting with
Here's the tension. Skills solve exactly the kind of problem AskCruz says it solves: turning tribal knowledge into a standing, reusable procedure Claude applies automatically. That's not a coincidence — it's the same "why not just use Claude directly" objection you're already fielding from prospects, now sharper, because Anthropic ships a native, free way to encode "how we do things here."

If AskCruz's pitch leans on "we capture your institutional knowledge," a technical prospect can reasonably ask: isn't that just a folder with a SKILL.md? For pure procedural knowledge — SOPs, tone, pricing rules, checklists — the honest answer is yes, mostly.

Where Skills still wins, and where the pitch needs to plant its flag harder:
- Skills are static. They're instructions and s[teps] sitting in a folder — they don't ingest live, unstructured, cross-system data. They don't know what happened on yesterday's [cut off]

Then typed: "give me this simple words"]

**Assistant:** In plain terms:

Two ways this "Skills" feature matters for AskCruz.

First, internal use — easy, do it now. You're already doing this in your own Claude setup with three skill folders (threads-ov, raj-eoxs-vault, sales-strategist). The idea is to do the same thing company-wide. Instead of re-explaining the same playbook to Claude every single chat, you save it once as a Skill. Examples: the script for handling Copilot objections, the rule that Sabre never gets mentioned externally, your pricing floors, the deal-stage checklist. This matters most for your 50 MBA interns — right now their output quality depends on each one re-explaining context from scratch every session. A shared skill folder per function (sales outreach, research, fulfillment) makes their output consistent without you having to check every draft. This is basically the "Company Personalization" layer from your own 8-layer AskCruz plan — except you could start building it today, for free, inside EOXS, without writing a line of AskCruz product code.

Second, and this is the uncomfortable part — what it means for selling AskCruz. Skills do the exact thing AskCruz's pitch claims to do: turn a company's unwritten know-how into a standing rule Claude just follows automatically. That's not a coincidence. It's the same "why not just use Claude directly" pushback you already get from prospects — except now it's sharper, because Anthropic gives this away free and built-in.

If your pitch is "we capture your company's institutional knowledge," a technical buyer can fairly ask: isn't that just a folder with a SKILL.md file in it? For plain procedural stuff — SOPs, tone, pricing rules, checklists — the honest answer is yes, mostly.

Where AskCruz still has an edge, and needs to argue it harder: Skills are static. They're just written instructions sitting in a folder — they don't pull in live, messy data from across systems, and they don't know what happened on yesterday's call. (The screenshot cuts off right here, so that's as far as the point goes.)
