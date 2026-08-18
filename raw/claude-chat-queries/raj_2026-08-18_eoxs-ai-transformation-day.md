---
thread_name: "eoxs-ai-transformation-day"
user: "raj"
type: claude-chat
created: 2026-08-18
updated: 2026-08-18
---

User: I think this product is good to roll out at our first customer, EOXs. Tomorrow will be our AI transformation day at EOXs. I understand AskRuse and EOXs have a lot of employee overlap, but we will learn from this process.
At 9:00, there will be a meeting with all the people who need to have their own Claude accounts with OV2 connected to them. They will create their own Claude accounts, and we will connect OV2 with them. They will all buy $20 subscriptions by using the company credit card. This is our learning curve to understand how AI implementation will happen in a structured way. Then, after an hour, this entire team will meet again, and we will teach them about MD files and how to create schedules using the scheduler and co-work. Managers like Ron will work on what personalized settings need to go in every individual's Claude account. Homera works in sending client emails for support. We can train that Claude to act and write in a certain way through those Claude settings. Like how we use the rigor level or asking questions for clarity in this specific account. 

Before we start working on it, talk to me in simple language in the least amount of words. Let's make a list of all the things we should be focused on tomorrow so that our company is completely AI-powered by Wednesday morning. 

We have a lot of products that have been integrated into this OV2. We need to make sure that all the users have full access to start with. We need to make sure that all the tools are connected with every user, and then we start setting up access rights. I am not concerned about privacy. I trust my team, so now let's make a list of things we should be focused on doing tomorrow using personalized settings or skills or co-work. How should a day tomorrow go in the company? 

This will even help us create a streamlined workflow for implementing AI at Sabre Alloys or 3GM Steel in the future. This could be a great learning curve for the entire team.

Assistant: Got it. Before I build this out — pick a level:

**5ft** — Quick agenda list, straight from what you described.
**10ft** — Same, but I check what's actually connected to OV2 today (tools, users, permissions) before listing steps.
**50ft** — Full plan: verified current state + I flag rollout risks (security, access, cost, adoption) you didn't ask about.

Given this sets the template for Sabre/3GM later, I'd lean 50ft. Your call.

User: 50

Assistant: Confirmed against current Claude.ai docs and your OV2 headcount (115 active). Two things before the list:

"Homera" — no match in employee records. Closest is Humaira Zainab (support@eoxsteam.com, does support). Confirm the name before tomorrow.

One real risk, stated once: your OV2 MCP URL has the auth token embedded in the URL itself (…/nGJz7LTB39vUUQjRsXEgdiWAUXmCKvvY2tkY3UIbK9I/sse). Anyone who pastes that exact URL into their own Claude account gets whatever clearance that URL carries — not their own scoped access. Same issue on eoxs-teams and teams-askcruz: those are raw SQL consoles, meaning full read access to live production data, invoices, CRM, salaries. Handing that one URL to 115 people means 115 people can query all of it, including tier1/tier2_confidential rows. You said you're not worried about privacy — noting it once because "full access to start" and "raw SQL to production" are different sizes of risk, not just a policy preference.

Here's the day:

[Step card: EOXS AI transformation day plan for tomorrow]
1. Tonight: decide plan type — 115 individual $20 Pro accounts on a company card has no admin panel, no spend cap, no connector allowlist, and no way to revoke one person without cancelling their card charge. A Team plan (paid per seat, similar cost) gives Ron an admin console: add/remove users, push skills to everyone at once, set which connectors each person can see, and cap spend. If this is the template for Sabre and 3GM later, decide this once, tonight, not on the fly tomorrow.
2. 9:00 - account creation — Each person creates their own Claude account with the company card. Have Ron or IT pre-collect names and emails tonight so this isn't done live. If you stay on individual Pro accounts, decide now whether everyone gets the same OV2 URL or whether some roles (interns, MBA cohort) get a lower-access connector instead.
3. 9:00 - connect OV2 — Each person pastes the OV2 URL into Customize > Connectors and authenticates. This is manual per person on Pro (no bulk push exists on Pro). Ron should sit with the room and confirm each connection works before moving on, rather than trusting everyone did it right.
4. 10:00 - MD files, scheduler, Cowork — Teach: what an MD file is and how OV2 uses them, how to set up a scheduled task (Cowork > Scheduled, available on Pro), and basic Cowork use. Keep this hands-on - have each person set up one real scheduled task before the session ends, not just watch a demo.
5. Managers set personalized settings — Ron builds per-person Claude settings the way this account uses rigor levels and clarifying questions. For Homera or whoever handles support email, this means a skill or saved instructions that lock tone and format for client-facing replies. Do this after the two group sessions, one-on-one or in small groups, not in the big room.
6. Wednesday morning check — Confirm: every intended person has an active account, OV2 connected, one scheduled task running, and one personalized setting saved. Anyone missing any of these isn't AI-powered yet, they've just installed an app.

One question for you: Team plan or 115 separate Pro accounts — which way do you want to go tonight?
