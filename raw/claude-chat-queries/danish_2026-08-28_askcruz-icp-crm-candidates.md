---
thread_name: "askcruz-icp-crm-candidates"
user: "danish"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: do you have client preference for AskCruz, like who would be ideal candidate for Askcruz who can potentially benefits from it, i want you to list 5 compnay names from our CRM who can benefits directly from what AskCruz is providing

Assistant: [Asked 3 clarifying questions via ask_user_input_v0: what AskCruz solves, what defines "ideal candidate", rigor level]

User: Q: What does AskCruz actually solve? Give me the core value prop so I filter CRM companies correctly.
A: i want you too look up what AskCruz does and then gives me the list

Q: What should define 'ideal candidate' for this list?
A: Both — just show best 5 regardless of stage

Q: Rigor level for this pull?
A: 10ft - verified against underlying CRM records

Assistant: I'll check the skill files first per your standing instructions, then research AskCruz, then pull CRM data.

[Read /mnt/skills/user/threads-ov/SKILL.md]
[Read /mnt/skills/user/eoxs-data-general/SKILL.md]
[Searched tool_search for eoxs-db tools referenced in skill — not found in actual tool list]
[Queried EOXS Data General:search_repo_docs and list_repo_docs for AskCruz — both empty]
[Queried AskCruz MCP:list_tables — returned Odoo schema with note: "This instance is HR + Project + Training focused"]
[Queried Team EOXS MCP:get_business_schema — confirmed EOXS Team is a steel distribution and operations company]

I hit a wall and want to flag it rather than guess, per your instructions.

**What I found so far:**

1. Your skill preferences reference a "raj-eoxs-vault" skill — I don't have that skill available, only `eoxs-data-general`, which itself references tools (`get_client_profile`, `search_wiki`, `search_assets`, `get_index`, etc.) that also aren't actually in my tool list. What I actually have connected is: **AskCruz MCP** (raw SQL to an Odoo DB), **Team EOXS MCP** (raw SQL to EOXS Team Live), **EOXS Data General** (repo docs — came back empty), **Gmail**, **Thread OV**, **claude-in-chrome**.

2. When I queried the AskCruz MCP connector to understand what AskCruz *is*, it returned the schema of an actual live Odoo instance — with `crm_lead`, `hr_employee`, `emp_training_*`, `sale_order`, etc. — the internal note says sale/purchase apps aren't even installed. This reads like **AskCruz's own internal operations database** (HR, projects, training, CRM for AskCruz's own sales), not a product-spec doc explaining what AskCruz sells to customers.

Two possible readings, and I don't want to guess:

- **A)** AskCruz is a product/tool EOXS built or is building, and I should find its ICP/value-prop from a different source (a wiki page, an asset doc, an email thread, or you telling me directly).
- **B)** "AskCruz" in this system is itself a client company (an Odoo customer), and you're asking me to identify EOXS *steel-distributor* clients who'd benefit from something else — and I've misread the request.

Can you clarify what AskCruz actually is/does in one or two sentences, or point me to where that's documented (a wiki page title, an asset name, an email thread)? I'd rather get this right than produce a list built on a wrong premise.

User: Can you clarify what AskCruz actually is - i want you to lookup in our database and see what Askcruz is, what does and then give me recommendations on what i have asked

Assistant: [Queried AskCruz MCP crm_stage — found stages: Leads, Intent, Discovery Call, Follow-up Action, Proposal, Won]
[Queried AskCruz MCP project_project — found projects including "Customer 1 - EOXS", "AskCruz", "Customer 2 - 3GM", "GTM Ideas", "Hiring Funnels"]
[Queried AskCruz MCP project_task for project_id=6 (AskCruz) — found tasks: "Register the company as a Delaware C-Corp", "Open an SVB bank account", "Ask Cruz iOS App V.01", "R&D: AskCruz Voice Call-In — Exec Capture + Customer Support Order-Status (Open-Source Feasibility)", "Integrate All Ask Cruz Email Data into Vault", "SMS Chat - Lead Gen", "Alternative to ZoomInfo", "Have another company configure AskCruz", "3GM proposal"]
[Queried AskCruz MCP crm_lead — found pipeline entirely composed of steel/metals distributors: Sabre Alloys, 3GM Steel (Won), Eastern State Steel, Greer Steel, FerroSource, Curtis Steel, Maverick Steel, Ratner Steel, Esserman Steel, Hascall Steel, Alliance Metal Products, North American Steel Alliance, Cowtown Express, Bossard - Smart Quote AI, Modern Metals Magazine]
[Queried Team EOXS MCP:get_business_schema — confirmed EOXS Team Live is a steel distribution and operations company running Odoo 13]
[Queried Team EOXS MCP res_partner for customer_rank > 0 AND is_company = true — returned large prospect/contact list of steel companies, not filtered to actual transacting customers]
[Queried Team EOXS MCP joining res_partner to sale_order, grouped and ordered by last_order_date — returned 14 actual transacting customers with order counts and last order dates]

This is a huge marketing/prospect contact list (steel companies), not necessarily EOXS's actual current ERP customers. I need to filter to actual customers with real sales activity. Let me check who's actually transacting — join to sale_order.

Now I have full clarity. Confirming with you what I found and giving the recommendation.

## What AskCruz actually is

AskCruz is a separate company/venture EOXS spun up (own Delaware C-Corp, own bank account, own iOS app), targeting **steel and metals distributors specifically** — not steel ERP like EOXS's core product. Its build tasks (voice call-in for exec capture + customer support order-status automation, email-data vault integration, SMS chat lead-gen, "alternative to ZoomInfo") point to it being an **AI-driven prospecting/sales-outreach and customer-communication automation tool**, built and sold to the same steel-distributor market EOXS already serves.

Its CRM pipeline (`crm_lead`) is 100% steel/metal distributors and adjacent logistics/publications — Sabre Alloys, 3GM Steel (Won), Eastern State Steel, Greer Steel, FerroSource, Curtis Steel, Maverick Steel, Ratner Steel, Esserman Steel, Hascall Steel, Alliance Metal Products, North American Steel Alliance, Cowtown Express.

## The overlap that matters

**3GM Steel and Greer Steel are already EOXS ERP customers** — they show up both in AskCruz's pipeline (3GM as Won) and in EOXS Team Live's active order history. That's a warm cross-sell path already validated once (3GM), not a cold theory.

## 5 candidates from EOXS's actual live customer base

Filtered to companies with real, recent transaction history in EOXS's ERP (not the raw prospect list, which is thousands of unvetted contacts) — these are proven steel distributors, already trust EOXS operationally, and are the same buyer profile AskCruz is chasing:

| Company | EOXS order activity | Why AskCruz fits |
|---|---|---|
| Sabre Alloys | 37 orders, active through Aug 2026 | Already an AskCruz lead in "Leads" stage — highest order volume of any EOXS customer, biggest single expansion target |
| Discount Pipe & Steel | 20 orders, active through Aug 2026 | Highest-activity customer not yet in AskCruz pipeline at all — clean net-new |
| Greer Steel Company | 18 orders, active through Jul 2026 | Already in AskCruz pipeline, already an EOXS customer — same cross-sell logic as 3GM |
| Hansen Metallurgical Services (HMS) | 16 orders, active through Jun 2026 | Steady EOXS customer, not yet touched by AskCruz — net-new |
| Eastern Steel Sales | 15 orders, active through Jul 2026 | Note: distinct from "Eastern State Steel" in AskCruz's pipeline — worth checking if that's the same company under a slightly different name before treating as fully net-new |

3GM Steel itself is the 6th and arguably strongest reference case (already Won in AskCruz, already an EOXS customer) — worth using as the proof point when approaching the other four.

One flag on rigor: this is 10ft — verified against underlying sale_order records, not summary fields. I did not cross-check order dollar values (redacted in this session) or reach out to AskCruz's own team to confirm the product description; the "what AskCruz does" read is inferred from task names and CRM data, not a written product spec, since no such doc surfaced in the connectors available to me.
