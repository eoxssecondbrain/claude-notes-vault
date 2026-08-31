---
thread_name: "rillet-erp-post-askcruz-relevance"
user: "ron"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

**User:**
I want to explain what they do and any conversation that we have moving forward in a simpler format. Let's try a bachelor's format, which might be based on my understanding, and think of myself as someone who is a bachelor.

**Assistant:**
Got it — plainer, less jargon, more explaining terms as I use them. Here's the same finding again in that format:

Rillet replaced the actual accounting software at the core — the master record of every financial transaction, called the general ledger — instead of just adding an AI assistant on top of the old software companies already had. Because they own the whole system, they could build the approval steps and record-keeping directly into how the software works, rather than adding it on afterward. That's why they get big jumps in results instead of small speed-ups: the AI runs inside a system built for it, not on top of an old one it doesn't control.

AskCruz is in a harder spot than Rillet. Rillet owns the core system for its customers. AskCruz doesn't — it has to work with whatever system a client already has (Odoo, or something else). So AskCruz has to build that same "approval and record-keeping" structure without owning the base system underneath.

There's already a company doing something close to this in steel: turian adds AI on top of whatever ERP a company already uses, instead of replacing it, and it's a real, funded business. So this path can work — it's just a harder version of what Rillet did.

The big question going forward: does AskCruz build its own consistent way of tracking approvals and records that works no matter which system is underneath — or does it just rely on each client's existing system to handle that part? The first is closer to what actually made Rillet succeed. The second is closer to the basic AI-assistant approach the post says only gets small gains.

I'll keep explanations at this level from here on.

**User:**
[Uploaded image: 1788203544343_image.png — a screenshot of a project/task note. "Note by Nidhi Rana - 6 hours ago", tagging @Ayan Dutta @Priyanshu Sinha: "Please note down the billing details for the following services running for AskCruz:
1. Linear - 12$ plan per month
2. Hetzner Ubuntu VPS - 37.19$ usage
3. Anthropic API keys - 2: a. Uses Haiku: cheap spam filtration + call relevance filtration. b. Uses Haiku for Access-tier classification, kept for raw new data & wiki pages when pushed live; citation_llm_resolver uses sonnet for citation repair and redaction logic uses sonnet for restricting information. Redaction logic runs on every single tool call for every non-full identity.
4. DigitalOcean's services: a. eoxs-staging-server: 1. staging app droplet: $11.61, 2. staging agent droplet: $11.61, 3. staging cruz database: $7.33. b. eoxs-live-server: 1. live droplet: $6.47, 2. eoxs-db-live-cluster: $1.91. c. askcruz 3gm staging server: 1. staging droplet: $0.18, 2. cruz-3gm-outlook-db database: $0.68
5. Render: claude-notes-vault service for repo claude threads saving functionality. $25 per month"]

I asked the team to give me a text tag of everything that we have, and this is what they gave me. This is the text tag that is there. Can you go through this and see what you understand? I will have a dedicated, detailed call with them tomorrow to understand exactly what they have built and how we can actually improve the product further so that it brings more automation in the system and in the workflows of the companies. I want to understand what is built right now.

**Assistant:**
[Read /areas/askcruz-email-infra.md and /areas/infrastructure-security.md from memory for corroborating context on Mailcow/hosting before answering.]

Going through it line by line, in plain terms:

1. Linear – $12/month
A task-tracking tool for the engineering team, like a to-do board (similar to Jira or Trello). Cheap, standard, nothing to flag here.

2. Hetzner Ubuntu VPS – $37.19
A VPS is a rented server in the cloud, running Ubuntu (a type of Linux operating system). Hetzner is a hosting company, usually cheaper than AWS or DigitalOcean. The note doesn't say what runs on this one — but AskCruz already has a self-hosted email server called Mailcow (mailcow.askcruz.com), and self-hosted mail servers are commonly run on exactly this kind of box. My guess is this is where Mailcow lives. Worth confirming tomorrow, not assuming.

3. Two Anthropic API keys
An API key is basically a password that lets AskCruz's own software talk to Claude (me, the AI) automatically, without a person typing into a chat window. They're using two different versions of Claude for different jobs:
- Haiku (the cheaper, faster version) handles spam filtering and deciding which incoming calls/messages are actually relevant.
- Haiku again for "access-tier classification" — when new data comes in, or a wiki page goes live, Haiku sorts it into confidentiality levels (who's allowed to see it).
- Sonnet (a stronger, more expensive version) handles "citation repair" (making sure quoted sources are actually accurate) and "redaction" — actively hiding information a given user isn't cleared to see. This redaction check runs on every single tool call for anyone without full access.

That last point is worth understanding clearly: the "different people see different data" system isn't just a written policy — it's a live AI filter (Sonnet) checking every request, every time. Good for security, but it also means every restricted-user action pays for an extra AI call. Worth asking how much that costs and whether it slows anything down.

One real gap: unlike everything else in this note, there's no dollar figure for these two API keys. For an AI product, this is very often the single biggest cost of all — so it's the one missing number you'll most want tomorrow.

4. DigitalOcean services
DigitalOcean is the main hosting provider. A "droplet" is just their name for a rented server (same idea as the Hetzner one above). Three separate setups:
- eoxs-staging-server — a "staging" environment is a practice copy used for testing before anything goes live. This has a server for the main app, a separate server just for "the agent" (the AI logic, kept apart from the main app), and a test database.
- eoxs-live-server — this is production, what real users actually use: one app server, plus a database "cluster" (spread across more than one machine, usually for reliability).
- askcruz 3gm staging server — a separate test setup just for 3GM Steel (your first paying AskCruz client), with its own server and its own database for 3GM's Outlook/email data.

Worth asking tomorrow: is giving each client their own dedicated server and database (like 3GM has) the actual long-term plan, or was that just how the first client got set up before a shared system existed? That answer matters a lot for how cost and complexity grow as more clients come on.

5. Render: claude-notes-vault, $25/month
This is the actual tool I've been using this whole conversation to save our chat history into your notes system. Confirmed, working as described.

Rough total from what's listed: about $114/month — not counting whatever the two Anthropic API keys actually cost in usage, which is probably the real number to chase tomorrow.

Questions worth bringing to the call:
- What exactly runs on the Hetzner VPS?
- What do the two Anthropic API keys actually cost per month?
- Is per-client dedicated infrastructure (like 3GM's setup) the plan going forward, or a one-off?
- What's the cost/speed impact of running Sonnet redaction on every tool call for restricted users?
