---
thread_name: "how-skills-work-explainer"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

# Thread: how-skills-work-explainer

## User
Can you tell me how does skills work.

## Assistant
Skills are markdown instruction files that get loaded on demand rather than kept in context all the time. Each one has a name and a description, and the description is the only thing checked against a new request to decide whether that skill fires — so the description has to be specific enough to trigger correctly and not overlap with others.

Two separate systems are running for you:

Anthropic's built-in skills (docx, pdf, pptx, xlsx, frontend-design, etc.) — these tell me how to produce a specific file format correctly (library quirks, layout rules, output paths). I read the relevant one before touching code or creating a file of that type.

Your own vault skills (threads-ov, raj-eoxs-vault, dps-account-strategist, sabre-account-strategist, client-email-tone-scale, and now sales-strategist per your latest note) — these aren't about file formats, they're persona and workflow instructions plus tool routing for your EOXS/AskCruz work. Each SKILL.md tells me:

- which situations trigger it (a new DPS email, a request to draft a client email, a query touching EOXS emails/calls/CRM)
- what tools to reach for and in what order (e.g. raj-eoxs-vault routes you to eoxs-db vs eoxs-teams vs teams-askcruz depending on the question)
- what output shape to produce (strategist skills give numbered options with reasoning; client-email-tone-scale gives calibrated draft text)

How triggering actually works in a turn: I look at your message, scan the available skill descriptions, and open (view) the ones whose description matches. Several can stack — e.g. a Sabre-related email draft would pull in raj-eoxs-vault (data access), sabre-account-strategist (analysis persona), and client-email-tone-scale (drafting), all at once. If nothing matches clearly, or more than one plausibly does and they'd conflict, your instruction says I should flag that instead of guessing — which is what triggered reading threads-ov and raj-eoxs-vault just now, since your standing rule says to check those two on any new thread regardless of topic.

The auto-save rule lives inside threads-ov specifically: every turn, I save the verbatim transcript so far under one stable thread_name for this conversation.
