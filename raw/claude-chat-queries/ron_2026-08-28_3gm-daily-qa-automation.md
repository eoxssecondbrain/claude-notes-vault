---
thread_name: "3gm-daily-qa-automation"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

Human: The 3GM implementation that we have started for AskCruz is something which is very important. I talked to Raj before, and he mentioned that we should understand the North American culture on how they actually deal with support and how they deal with their communication. The communication style is different, and in the scene industry it is more reference-based.
We need to keep all the existing customers in EOXS and also the customers that are going to come in AskCruz happy. The only way to do that is, of course, by doing a flawless and good implementation but also providing good support. If you go in Teams.EOXS, you will see that there is a board for customer 2 - 3GM, which has a bunch of tasks in it, and then you will soon have access to Ron's email for ron@askcruz.com, rajat@askcruz.com, and also for ayan@askcruz, and any other email that is in that company.
If you were to set an automation where every single day you were doing a QA on the client's health and seeing what are all the places that we can improve on and how you can actually make it better, how would you go about building that automation? If required, there is a human approval setup in it, but the AI is ensuring that the client is happy throughout the implementation and after as well with good support.

Assistant: Before diving in — two flags, then a rigor check.

First: your preferences call out a "sales-strategist" skill to stack on raj-eoxs-vault for account-strategy queries, but that skill isn't in my current catalog — I only see raj-eoxs-vault, threads-ov, dps-account-strategist, sabre-account-strategist, and client-email-tone-scale. This 3GM question is support/implementation-health design, not sales/GTM/objection handling, so I don't think sales-strategist would've applied here anyway — but flagging since it's referenced in your preferences and missing.

Second: you mentioned I'll soon have access to ron@askcruz.com, rajat@askcruz.com, and ayan@askcruz.com — I don't have that connector yet. Anything below that would touch actual email content (e.g. checking whether a client already voiced a concern) will need that once it's live. I do have Teams.eoxs (the Customer 2 - 3GM board) available now.

This is a strategic design task, not a lookup, so per your standing instruction — pick a rigor level:

5ft deep — quick sketch of the automation architecture and daily QA checklist based on general implementation-health signals and what I already know, no digging.

10ft deep — same, but I actually pull the 3GM board from Teams.eoxs first (task stages, blockers, open comments) so the checks are designed against what's really there, not assumptions.

50ft deep — verified, plus I look at adjacent angles: how DPS/Sabre/Greer implementations historically went sideways, what "healthy" actually looked like for them, the North American support/communication norms Raj flagged, and specifically where human approval gates should sit vs. where the AI can act on its own — with risks and blind spots named.

100ft depth — same as 50ft but delivered section by section (e.g. data sources → daily check logic → escalation/approval design → communication cadence → rollout plan), one section at a time, you say "next" to continue.

Since this is meant to become the template for AskCruz client health generally, not just 3GM, I'd lean 50ft or 100ft — but your call.

Human: 100ft

Assistant: Good — that's enough grounding to build the outline properly. Here's the structure:

1. Data sources & signals — what actually feeds the daily QA (project board reality check included)
2. Daily check logic — what gets evaluated each day and how a "health score" gets derived
3. What "unhealthy" has actually looked like at EOXS clients — grounding the checks in real failure history (3GM's own past, plus DPS/Sabre/Greer patterns)
4. North American / steel-industry communication norms — how that reshapes tone, cadence, and what the AI is allowed to say directly to a client
5. Escalation & human-approval design — where the AI acts alone vs. where it stops and asks
6. Risks, blind spots, and rollout plan — sequencing from 3GM to an AskCruz-wide template

Section 1: Data Sources & Signals

What's live right now, checked directly rather than assumed:

The 3GM implementation board (askcruz Odoo, "Customer 2 - 3GM," project_id 14) has 21 tasks. Of those, 14 have sat untouched in "Intake" since they were created on 2026-08-21 — a full week with zero movement. Only a handful have actually progressed: platform review (Assigned), Outlook email integration (in QA), onboarding email and the Gmail-approval doc (Complete), SOP ingestion (on Hold since 8/24). That's a real, checkable signal today — not a hypothetical one — and it's exactly the kind of thing a daily QA pass should be catching and asking about, rather than something Ron notices three weeks in when Travis asks why nothing's moved.

Sources available to the automation now:
- teams-askcruz (Odoo, read + scoped write) — the implementation task board itself: stage, owner, last-updated timestamp, deadline, description.
- Fireflies/Fathom — call transcripts and summaries, if 3GM calls are being recorded through either.
- OV2 (eoxs-db) — the synthesized history of 3GM as an existing EOXS client: past support tickets, past churn-risk episodes, contact turnover. This is old-system history, not the AskCruz relationship itself, but it's the closest thing to "how has this specific client behaved when unhappy" that exists.

Not yet available: ron@askcruz.com / rajat@askcruz.com / ayan@askcruz.com. This matters more than it might seem — a huge share of "is the client happy" signal in a relationship-based, reference-driven industry lives in email tone and response latency, not in task-board state. Until that connector is live, the daily QA is structurally blind to the actual client-facing conversation and can only watch internal execution. I'd flag that gap explicitly in whatever you show Raj, rather than let the automation look more complete than it is.

One adjacent risk worth naming now: the board itself mixes internal build/infra tasks (MCP whitelisting, server setup, skill files) with client-facing implementation milestones (onboarding email, training materials). A daily QA that just reports "14 of 21 tasks stale" without separating internal plumbing from client-visible commitments will either cry wolf or hide the one that actually matters. Section 2 covers how to split those.

Next: what the automation actually checks every day, and how "stale," "at risk," and "healthy" get defined in a way that's specific enough to act on.
