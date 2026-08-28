---
thread_name: "askcruz-what-is-it-explainer"
user: "danish"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: last time i asked you about what Askcruz is, what's is agenda was and how it works but you gave me vague answers so i want o repeat this again and i wants concise answers about everything you know about AskCruz

Assistant: I need to check the relevant skills first per your standing instructions, then pull what's actually in the data before answering — otherwise I'll give you the same vague answer again.

[Loaded Thread OV tools, read threads-ov SKILL.md in full]

The user preference asks me to note explicitly: I found and loaded Thread OV tools (threads-ov skill), but there is no "raj-eoxs-vault" skill in your available skills list — the closest is eoxs-data-general. Let me check both skill files properly before doing anything else, per your instruction to flag ambiguity rather than guess.

[Read eoxs-data-general SKILL.md in full]

There's no "raj-eoxs-vault" skill in the available skills — closest match is eoxs-data-general. Flagging that per your instruction rather than guessing. Let me check that one too since it governs data access for EOXS/AskCruz questions.

[Loaded AskCruz MCP tools]

This is a live Odoo/project management DB for AskCruz — not a "what is the product/strategy" document store. Given your last complaint was vague answers, I should check EOXS wiki/assets on eoxs-db first, since a company-overview or product-spec asset is exactly where "what AskCruz is / its agenda / how it works" would be documented properly.

[Loaded EOXS Data General, Team EOXS MCP, Thread OV additional tools]

The eoxs-db connector's dedicated tools (get_index, search_wiki, search_assets) aren't loading via search — I'm getting Team EOXS MCP (raw Odoo SQL, per your connector list "EOXS Data General" maps to codebase repo docs, and "Team EOXS MCP" to the live business DB) and EOXS Data General (repo docs — code architecture, not business/product docs). Let me check repo docs first since AskCruz is a product Rajat/EOXS built — its spec may live there.

[Called EOXS Data General:search_repo_docs("AskCruz") -> empty. Called EOXS Data General:list_repo_docs() -> empty.]

Empty. This repo doc store isn't the AskCruz product itself — it's returning nothing. Let me check the AskCruz Odoo DB directly for a company/project description, and also check EOXS Team Live for any CRM notes on AskCruz as an internal initiative.

[Called AskCruz MCP:get_business_schema() -> returned full schema: askcruz Odoo 13 DB, HR + Project + Training focused, no sale/purchase/account apps installed. Sample rows showed res_partner (contacts including sebastian@askcruz.com, 3gm steel, Esserman Steel/Jacob Esserman), project_project (Team Sales, AI interns, Customer 2 - 3GM, etc), project_task samples including "Tracking techstack and billing", "LinkedIn revamp — update his profile to reflect AskCruz", "Learn LinkedIn Sales Navigator", project_task_type stages (Completed, In Progress, Task List), hr_employee samples (Sebastian, Lakshit Singh, Priyanshi Singh, all @askcruz.com emails), hr_department (Product, Product Intern, Sales), hr_job, and empty emp_training_* tables.]

Now I have real signal. This is an internal Odoo instance (HR + Project + Training) — it confirms AskCruz has employees, sales pipeline, and product/dev work, but it's an operations DB, not a "what is AskCruz" document. To answer your actual question properly, I need the product-description content — projects/tasks describing what's being built and sold. Let me pull the project list and a sample of task content.

[Called AskCruz MCP:query("SELECT id, name FROM project_project ORDER BY id DESC LIMIT 30") -> 15 projects: Team Sales(17), AI interns(16), Customer 2 - 3GM(14), Internal Project(13), HR(12), GTM Ideas(11), Test(10), Hiring Funnels(9), Idea Board(7), AskCruz(6), Daily Snippets(5), Customer 1 - EOXS(4), 50 MBA Inters Cohert(3), Test1(2), Start here to discover Odoo(1)]

Project 6 is literally "AskCruz." Project 4 is "Customer 1 - EOXS" and project 14 is "Customer 2 - 3GM" — this tells me AskCruz treats EOXS itself as a customer. Let me pull the AskCruz project's tasks and the GTM/Idea Board projects for agenda/positioning content.

[Called AskCruz MCP:query on project_task where project_id=6 -> 52 rows returned, including: company registration/banking setup tasks, "AI QA Layer", task id 94 "R&D: AskCruz Voice Call-In — Exec Capture + Customer Support Order-Status (Open-Source Feasibility)" with a long description describing AskCruz as feeding "the existing Company Brain," architecturally adjacent to "Agent Vinod" and "Zola"; iOS app v0.1; "0 to 1 Lead (Cold Calling)" task targeting 2 qualified leads/meetings for September; "SDR SOP"; "3GM proposal"; "Have another company configure AskCruz"; MCP write attribution bug task naming mcpwrite@cruzai.com and Rajat Jain; and more.]

This is rich and confirms a lot. One task (id 94) explicitly frames AskCruz as sitting alongside "the existing Company Brain," "Agent Vinod," and "Zola" — internal R&D products. Let me check the Idea Board and GTM Ideas projects for positioning/agenda content, and confirm what "AskCruz" the product actually does day to day (task 94 implies it's an ERP/OV-connected AI system, similar to what's described in your own EOXS skill for "Company Brain").

[Called AskCruz MCP:query on project_task where project_id IN (7,11) -> 13 rows returned including: "CRM AI / Agent Architecture" (task 55) laying out a commander/scribe/AE-agent/engagement-agent architecture and a single-generalist-agent-vs-specialists decision (recommendation: single agent with full context); "Obsidian Vault / OV2 (Second Brain Data Layer)" (task 56) describing three layers (Claude instructions, Claude skills, OV company brain) and a "Cruz LLM" local-hardware option framed as a data-sovereignty sales differentiator for security-conscious clients like steel distributors; "EOXS Product / ERP Features" (task 58) stating the core thesis that businesses stitch together CRM/ERP/billing/contracts/spreadsheets to answer basic questions and AI agents given that same mess fail the same way without complete data + context; "scalable customer information system" (task 160) covering Collier account strategy and a centralized customer DB with Obsidian as a lightweight interface; QA Agent concept; "100 Domains Email Marketing" for cold outreach infrastructure.]

Now I have a genuinely clear, first-hand picture. Here's what AskCruz actually is, straight from the internal record:

What it is
AskCruz is an AI system built on top of a company's data — ERP, CRM, email, calls, tickets, documents — that lets a "Human + Agent" workforce query and act on that data instead of hunting across a dozen disconnected tools. Internally it's called the "Company Brain" or "second brain," with the data layer referred to as OV/OV2 (Obsidian Vault-based). The pitch: businesses already stitch together CRM, ERP, billing, contracts, spreadsheets just to answer basic questions like "what's my ARR" — and AI agents thrown at that same mess fail the same way humans do, not because the model is bad but because of context gaps.

Agenda / thesis (task 58, "EOXS Product / ERP Features," is close to a manifesto):
- The core belief is that AI agents need complete data + business context to act reliably, or they'll confidently hallucinate.
- The wedge is steel-industry ERP data (EOXS's own customer base — steel distributors), positioning AskCruz as the AI layer that sits on top of a client's existing systems rather than replacing them.
- EOXS itself is customer #1 internally (project "Customer 1 - EOXS"); 3GM Steel is customer #2; Collier Metals, Sabre, and others appear as active prospects/accounts.

How it works, mechanically
1. Client's ERP, email (Gmail/Zoho), calls (Fireflies/Fathom), tickets, and docs get ingested into a structured vault (OV2) via automations already built.
2. On top of that sits an agent layer — task 55 lays out a real architectural decision: single generalist agent with full context vs. multiple specialist agents handing off. Current call is one agent with full context, specialists only if evidence shows the generalist is failing something specific — because handoffs lose signal.
3. Planned agent roles include a "commander" that routes requests to sub-functions (scribe, AE/account-executive-style strategist, engagement/send agent, pipeline agent) — this is roadmap/vision, not all shipped.
4. A "Cruz LLM" local/self-hosted model option is being evaluated — not as a replacement for Claude/GPT-class reasoning, but as a data-sovereignty sales angle for security-conscious clients (e.g., steel distributors who don't want ERP data leaving their premises).
5. There's a QA layer concept: an AI reviewer that checks internal task deliverables before human QA.
6. Delivery channel: iOS app (v0.1 built), Teams.AskCruz project board, and email/CRM integrations for clients.

Current operating state (not vision — actual status)
- Small team running this like a startup inside EOXS: hiring SDRs, running cold-call lead gen (target: 2 qualified leads/meetings for September), building a proposal format, closing 3GM as a second paying-ish account.
- Explicit stated bottleneck right now: a "30-clients-in-90-days AskCruz delivery risk" — this is called out as the top engineering priority, ahead of exploratory R&D (e.g., a voice call-in feature was explicitly told to wait until that capacity risk is under control).
- Legal/ops setup (Delaware C-Corp registration, SVB bank account) still in progress as of the task list — meaning company formation itself isn't fully done yet.

If you want, I can pull the "30-clients-in-90-days" delivery risk in more depth, or the sales pipeline/deal stages from the CRM side — that's the part most directly tied to your $1M ARR target and isn't in what I pulled here.</content>
