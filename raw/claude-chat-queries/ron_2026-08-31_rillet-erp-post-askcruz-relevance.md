---
thread_name: "rillet-erp-post-askcruz-relevance"
user: "ron"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

**User:**
What do you know about AskCruz and what it does?

**Assistant:**
[Read /areas/askcruz-proposal.md, /areas/3gm-askcruz-implementation.md, /areas/gfc-intelligence-inc-formation.md, /areas/second-brain-knowledge-base.md from memory; searched past conversations for "AskCruz Company Brain features how it works" and found a detailed proposal document describing Company Brain's actual features.]

What AskCruz is

It's an AI product built by EOXS, sold to companies (starting with steel industry ones) as a "Company Brain" — basically an AI assistant that already knows everything about your company, so any employee can ask it plain-English questions and get accurate answers instead of digging through email, ERP screens, or asking a coworker who might know.

It's built on top of Claude (me). AskCruz sets everything up and connects it to a company's data, but each individual user gets their own real Claude account underneath.

A bit of history: it used to be called Krinox and was originally focused on freight/logistics questions. It got renamed AskCruz and repositioned as a general business-brain tool in August 2026. Legally, it's owned by a separate company called GFC Intelligence, Inc. — kept deliberately apart from EOXS, so EOXS's outside investors have no stake in it.

What it actually does, technically

- Connects to all of a company's email inboxes. Reads the full history once at setup, then keeps checking for new emails automatically every couple of hours.
- Connects live to the company's ERP (their day-to-day business software — orders, inventory, customers, pricing), so it's always working off current numbers, not a stale copy.
- Logs every question anyone asks it into a searchable history, so management can see what people are actually asking and where the AI is (or isn't) actually helping.
- All of that data feeds one continuously-updated "brain" that answers questions in plain English, instead of someone hunting through email threads or ERP screens manually.

Business model

The company pays AskCruz to set this up and maintain it. Separately, each individual user pays Anthropic directly for their own Claude subscription ($20 or $100/month depending on how heavily they use it) — that cost doesn't run through AskCruz at all.

Where it stands today

- First actual paying customer: 3GM Steel (contacts Travis Lane and Stefan Brown) — 2 users so far, connected to their Outlook email and their customized Odoo ERP. Two features (searchable question history, and pulling in years of old historical data) were deliberately left for later, to keep the first rollout simple.
- Other companies in active proposal or discussion stages: Sabre Alloys, IMS Metals, Collier Metals, and a few more.
- Current focus is steel distributors and processors specifically, with a stated longer-term plan to expand to any mid-size company in any industry.
- Built to connect to whatever ERP a client already runs — not locked to Odoo.

One thing worth noticing

This is basically the same kind of system I've been running for you this whole conversation — reading emails, calls, and client records, with different access levels for different people, to answer your questions about EOXS and AskCruz accounts. EOXS built that for itself first (internally they call it the "Second Brain"). AskCruz is that same idea, now packaged and sold to outside companies.

It also connects straight back to the Rillet conversation: unlike Rillet, AskCruz isn't trying to replace or own the ERP. It's a knowledge/answer layer sitting on top of whatever system a client already has — which is exactly the harder version of the "harness" problem we talked about earlier. Not hypothetical for you — it's literally the product.

**User:**
Let's talk about the Harness version again.

**Assistant:**
[Queried the actual teams-askcruz (AskCruz Odoo) project board directly via SQL — searched project_task names/descriptions for keywords: agent, automat, approv, write, action, redact, audit, harness. Found 43 matching tasks across projects including "AskCruz", "Customer 1 - EOXS", "Customer 2 - 3GM", "Idea Board", "50 MBA Inters Cohert", "Hiring Funnels". Reviewed the relevant ones in full.]

Good — I actually checked this against your real project board instead of guessing further. Here's what's real.

The harness doesn't exist yet for client ERPs — but there's a named project for exactly this

I found a task called "Cruz Trust Layer — technical spec deep-dive" sitting in your project board. It's asking someone to work out precisely the thing we've been discussing:
- A data model for roles, permissions, risk classifications, action logs, and approval records — this is the actual harness, spelled out as database tables.
- A walkthrough of one real example: a price change. What role check has to pass, what gets logged, what triggers a required approval, what the approver actually sees.
- A comparison against how real companies already do this — Salesforce Agentforce, Microsoft Copilot's governance model, Glean.

So this isn't hypothetical — someone at AskCruz already named and scoped the exact concept we've been calling "the harness." It exists as an idea and a spec task.

But here's the honest part: this task is sitting in the "50 MBA Interns Cohort" project, marked "no hard deadline... a 'sharpen the idea' task, not critical path." It's intern-level exploratory work right now, not something actively being built into the product.

What IS actually built right now: writing capability, but only for your own internal tools

I found several completed or in-progress tasks about giving Claude "write" access — the ability to actually create or change things, not just answer questions. But every one of them is scoped to your own internal project-management board (creating tasks, adding notes, tracking who's assigned what) — not to a client's ERP (creating invoices, changing prices, updating inventory). There's also a task explicitly asking for a write-access connection to your own team's ERP for Raj to use internally. None of this is the client-facing "the AI actually does the transaction with approval and audit" capability yet.

What this means put together

Right now, AskCruz for a client (like 3GM) is exactly what we described earlier: read-only. It reads email and ERP data and answers questions. It does not yet take actions inside a client's system with an approval/audit trail — the "Cruz Trust Layer" that would let it do that is a documented idea, not a built feature. And your own internal write-access work has been used to automate your own operations (task boards, email drafting with human review), not client workflows.

One more thing worth knowing directly: a separate task flags that the current top priority internally is "30 clients in 90 days" — meaning delivery/onboarding speed, not deeper product capability like the Trust Layer, is where the team's attention is currently pointed. That's a real tension with what you told me you want out of tomorrow's call — "more automation in the workflows" specifically requires the Trust Layer work, and right now that's explicitly de-prioritized below onboarding volume.

Worth asking directly tomorrow: is "Cruz Trust Layer" going to stay an intern side-project, or does it need to become real engineering priority if "more automation" is actually the goal? Right now those two things — the current roadmap priority and what you said you want — don't fully line up.

One more small note: I also found a task literally titled "Study Rillet — AI-native ERP rebuild," created because Raj shared that same LinkedIn post internally and assigned 2-4 hours to study it and map it to AskCruz. This conversation this morning is, in effect, that exact assigned task.
