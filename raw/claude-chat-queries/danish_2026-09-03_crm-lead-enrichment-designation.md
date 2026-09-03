---
thread_name: "crm-lead-enrichment-designation"
user: "danish"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

User: i will be working on enriching leads in our CRM so what designation it will be?

Assistant: [Read threads-ov SKILL.md and eoxs-data-general SKILL.md per user preferences before executing on new thread]

Your question isn't fully a data-lookup — it's ambiguous whether this is EOXS or AskCruz CRM, and whether you want the actual field name/schema value or just to know what to fill in. Per your preference, I'll flag the skill-match ambiguity rather than guess, and I need one clarification.

**Skill match:** eoxs-data-general covers CRM/pipeline data lookup — but your leads are in AskCruz's CRM (Odoo, via AskCruz MCP), which isn't covered by this skill (that skill is scoped to EOXS connectors only). The sales-strategist skill wouldn't apply here either — this is a data/schema question, not GTM/deal strategy or email drafting. So: no skill fully covers this, and I'm proceeding on the AskCruz MCP connector directly since it's a straightforward schema lookup.

**Clarification needed:** by "what designation will it be," do you mean:

1. You're asking me to check the CRM (askcruz Project/Odoo `project.task` or a leads table) for what the "designation" field/value options are for a lead you're about to enrich, or
2. You're asking what job title field to fill in for a *specific* lead you're working on right now, or
3. Something else entirely (e.g. what your own role/designation is when tagged on this task)?

If it's (1), I'll pull the schema for whatever table holds leads.
