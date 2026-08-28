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
