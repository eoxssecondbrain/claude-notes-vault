---
thread_name: "sabre-new-company-proposal-task"
user: "ron"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

# Sabre New Company Proposal Task

**User (turn 1):**
Create a task in the teams.EOXS board. I want you to call it "Creating the proposal for Sabre's new company." Ty called and mentioned that they're getting a new laser cutting machine, and they want all the users and everything to be the same. We need to create a proposal for them from EOXS's side. There is an EOXS board. Maybe you can create a task for that and, in it, add the description. He mentioned that they would be needing all the users, but it doesn't make sense for them to pay, again, $10,000 a month every single month for that company. Also, since it's a smaller company, Raj was thinking about two options:

* Actually copying and pasting the code on another server
* Creating a new company in Odoo

He is more leaning towards creating a new company in Odoo itself so that they can do that operation. We need to get a proposal and send it to them. A few clauses that we need to add in this are:

* Ensure that we add a clause for advertising. This is very important. Please flag it when you pay the task, and if there is any other clause, I will let you know.

Please create the task and let me know if you have any questions.

**Assistant (turn 1):**
Two things to flag before I do anything else:

**Skill gap:** Your preferences say to read a "sales-strategist" skill alongside raj-eoxs-vault for deal/account-strategy queries (which this is — a proposal to a client). I don't see that skill file anywhere in my available skills — only dps-account-strategist, sabre-account-strategist, and client-email-tone-scale exist for this kind of work. Let me know if it's named differently or just hasn't been built yet.

**Tool gap:** I don't actually have a way to create a task on the real EOXS Teams project board. Teams.eoxs only gives me read-only SQL access (sales orders, invoices, partners, stock — no task-writing capability at all). The only create_task tool I have writes into AskCruz's own project, which is a separate Odoo instance entirely from EOXS's Build/Support board. So I can't literally log this into "the EOXS board" right now.

Options:
- I hand you the title/description below and you paste it in yourself
- If you have the EOXS Teams project open in Chrome and want me to try clicking through to create it via the browser, I can attempt that with the Chrome connector
- Tell me if there's a connector I'm missing

Here's the draft content either way:

Title: Creating the proposal for Sabre's new company

Description:
- Tye called — Sabre's new company (getting a new laser cutting machine) needs all the same EOXS users/setup as Sabre Alloys has now
- Doesn't make sense for them to pay another $10,000/month for a full duplicate license
- Raj is weighing two options: (1) copy/paste the codebase onto a separate server, or (2) stand up a new company within the same Odoo instance (multi-company setup). Raj is leaning toward option 2
- Next step: draft a proposal for Sabre covering this arrangement, then send
- Clauses to include:
  - Advertising clause — flagged as important, wording still TBD, needs your input on what it should actually say
  - More clauses to follow per Ron

Two things I need from you before this is proposal-ready rather than just a task shell:
1. What should the advertising clause actually cover — case-study/reference rights, a marketing cost split, something else?
2. Does the new company have a name yet, or is it still "Sabre's new company" for now?

**User (turn 2):**
The new company does not have a name yet. I am not sure what the clause is, but please get the task for it right now. We will get to the name of the company later.

**Assistant (turn 2):**
I still don't have a tool that writes to the EOXS Teams board, so I can't put this in a system directly — copy-paste is genuinely the fastest path right now. Here's the finalized version:

Title: Creating the proposal for Sabre's new company

Description:
- Tye called — Sabre's new company (name TBD, getting a new laser cutting machine) needs all the same EOXS users/setup as Sabre Alloys has now
- Doesn't make sense for them to pay another $10,000/month for a full duplicate license
- Raj is weighing two options: (1) copy/paste the codebase onto a separate server, or (2) stand up a new company within the same Odoo instance (multi-company setup). Raj is leaning toward option 2
- Next step: draft a proposal for Sabre covering this arrangement, then send
- Clauses to include:
  - Advertising clause — flagged as important, wording not yet defined
  - More clauses to follow per Ron
- Company name to be added once decided

If you'd rather I try creating it through the actual Odoo UI via the Chrome connector, say so and I'll walk through browser selection — otherwise this is ready to drop in as-is.

**User (turn 3):**
[Uploaded image: WhatsApp screenshot of a LinkedIn post, 11:59, from "Strategic Tech Leader | Ventures Builder | B..." Full text of the post:
"A two-year-old startup just became a unicorn by replacing NetSuite and SAP. Most people will take the wrong lesson from it.
The company is Rillet. Last week they raised $100M at a $1B valuation, with 600+ customers and large enterprises moving off Oracle Fusion, SAP, Workday, and NetSuite.
The wrong lesson is "AI is disrupting ERP." That is true but empty. The real lesson is about what they rebuilt.
Every incumbent in that market added AI the reasonable way: a copilot on top of the existing system. It failed to change much, and here is why. Legacy systems were designed around a human doing the work — human data entry, human review, human checkpoints at every step. A copilot makes the human faster inside that workflow. But the workflow itself is still shaped like a human. You get 20-30% improvement, and the structure of the work stays exactly the same.
Rillet did something different: they rebuilt the ledger itself, so agents and humans operate inside the same data, under the same rules — agents doing the work, humans keeping approvals and full audit records. The unit of work changed. Not "help a person do the task faster" — the system does the task, and a person approves the outcome.
You can tell the difference by the numbers. Copilots produce percentages. Rebuilds produce multiples: multibillion-dollar businesses running finance teams a tenth the traditional size, closing their books continuously instead of monthly.
And there is one detail most coverage missed. The unlock was not intelligence — models are available to everyone. The unlock was the harness: approvals, policies, and audit trails built into the core. That is the part you cannot retrofit. You cannot bolt auditability onto a system that never captured its own reasoning. Which is exactly why the incumbents' copilots stay assistants forever.
So the interesting question is: which function gets rebuilt next? My criteria: the work is structured, rule-governed, and must survive an audit. Accounting was the obvious first. Data management is, in my view, the next — the same 4-to-6-week cycle times, the same human-shaped tooling, the same audit requirements, one layer down the stack..." (post appears cut off at bottom of screenshot)]

Then, after you create this task, I want you to create another task in Teams.askcruz in the AskCruz board where you have to spend 2-4 hours today studying what this company is doing. You can get whatever information you can from this post that Raj shared with me, but please create this task in the system there.

**Assistant (turn 3):**
On the Sabre/EOXS task — still no tool for that board, so that one's still on you to paste in from the draft above.

For the AskCruz task, this is ready to go pending your confirmation (nothing's been written yet):

Project: AskCruz (project_id 6)
Title: Study Rillet — AI-native ERP rebuild (2-4 hrs)
Assigned to: Ron
Deadline: today, 2026-08-31
Stage: Tasks
Description: summarizes the post — Rillet raised $100M at a $1B valuation (2 years old, 600+ customers, displacing NetSuite/SAP/Oracle Fusion/Workday); the author's core claim is that copilots bolted onto legacy workflows cap out around 20-30% improvement, while Rillet rebuilt the ledger itself so agents do the work and humans keep approvals/audit trails, getting multiples instead (1/10th headcount, continuous close); the real unlock is the audit/approval "harness," not the model; and the author's next-target framework is structured, rule-governed, audit-bound work — with data management flagged as the likely next function after accounting. Ends with the task itself: spend 2-4 hrs studying what Rillet's actually doing and how it maps to AskCruz.

Confirm and I'll commit it.

**User (turn 4):**
Confirmed. Please write the description in bullet points.

**Assistant (turn 4):**
This is a new preview since the content changed — confirm this bullet version and I'll commit it (title, project, assignee, and deadline are unchanged from before).

**User (turn 5):**
I do not the description here.

**Assistant (turn 5):**
Here's the actual bullet-point description, shown in full this time:

- Raj shared a LinkedIn post about Rillet — a two-year-old startup that just raised $100M at a $1B valuation, with 600+ customers, replacing NetSuite, SAP, Oracle Fusion, and Workday at large enterprises
- Most incumbents bolted an AI copilot onto existing legacy workflows still shaped around a human doing the work, getting roughly 20-30% improvement at best
- Rillet instead rebuilt the ledger itself so agents do the work and humans keep approvals plus full audit trails — a structural change, not just a speed-up
- Result cited: finance teams running at a tenth of traditional headcount, closing books continuously instead of monthly
- The unlock wasn't the AI models themselves (available to everyone) — it was the "harness": approvals, policies, and audit trails built into the core system, which can't be retrofitted onto legacy software after the fact
- Author's framework for what gets rebuilt next: structured, rule-governed work that must survive an audit. Accounting was first; data management is what the author expects next
- Task: spend 2-4 hours today studying what Rillet is actually doing (product, positioning, GTM, pricing where available) and how it maps to AskCruz's own AI-native approach

Title: Study Rillet — AI-native ERP rebuild (2-4 hrs), assigned to Ron, deadline today, project AskCruz. Confirm and I'll commit it.

**User (turn 6):**
Confirmed. Please create the task.

**Assistant (turn 6):**
Task 390 created in the AskCruz project — Study Rillet — AI-native ERP rebuild (2-4 hrs), assigned to you, due today, bullet-point description as shown above.

The Sabre/EOXS proposal task is still the one item pending on your end since I don't have a write path to that board.
