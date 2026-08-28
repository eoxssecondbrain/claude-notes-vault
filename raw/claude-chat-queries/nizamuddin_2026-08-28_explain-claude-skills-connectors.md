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
