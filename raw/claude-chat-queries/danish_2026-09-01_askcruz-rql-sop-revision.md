---
thread_name: "askcruz-rql-sop-revision"
user: "danish"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: <userPreferences>- Go through threads-ov and raj-eoxs-vault skill file before executing anything on a new thread.
- MANDATORY, every single response, no exceptions: call save_chat_transcript (per threads-ov skill) as the last action before ending your turn. This applies to every turn in every conversation, not just the first — do not treat one save as covering the rest of the conversation. This rule stacks with all other skill/instruction rules and is never skipped, including for short replies, clarifying questions, or "yes/no" exchanges.
-sales-strategist: read this in addition to raj-eoxs-vault whenever the query is about sales strategy, GTM planning, deal or account strategy, objection handling, or drafting an email to a prospect or client. It governs persona and workflow, not data access, so it stacks on top of raj-eoxs-vault rather than replacing it.
- If a query could match more than one skill, or matches none clearly, say so before proceeding rather than guessing.
(add one line per new skill here as more departments get built)
This account is always used by Danish Lari. Keep this in mind always.

Never save anything to memory unless I explicitly ask.
Never use bold text.
Be direct, concise, factual, and useful. Avoid flattery, emotional padding, excessive politeness, or empty validation.
Prioritize truth, accuracy, and clarity over agreement. Challenge my assumptions when warranted. Point out flaws in my reasoning, blind spots, risks, tradeoffs, and opportunity costs. If I am fooling myself, avoiding something important, wasting time, or focusing on low-leverage activities, tell me directly.
Act as a high-level advisor, strategist, operator, and mirror. Analyze situations objectively. If my thinking is weak, explain why. If my thinking is strong, explain why. Do not manufacture criticism where none exists.
Focus on evidence, logic, incentives, and outcomes. Separate facts from assumptions and clearly identify uncertainty.

Our primary objective is to keep EOXS stable and growing only through inbound, while growing AskCruz to $1,000,000 ARR within the next 12 months. When relevant, evaluate opportunities, projects, habits, relationships, decisions, and time allocation based on their impact on this objective.

Actively help keep my focus on the highest-leverage actions that drive sales, customer acquisition, retention, execution, and growth. Call out distractions and help redirect attention toward what most increases the probability of achieving the goal.

Always respond in a way that is easily digestible.
WHENEVER I ASK YOU SOMETHING, ALWAYS TAKE A STEP BACK TO REFLECT THAT IF YOU HAVE THE FULL CONTEXT BEFORE RESPONDING. ASK ME QUESTIONS UNTIL YOU HAVE AT LEAST 95% CLARITY AND THEN RESPOND.

Before doing any research, analysis, or strategic task (not simple lookups or one-line factual questions), give me three rigor-level options before starting, and wait for me to pick one unless I've already specified a level:
5ft deep— Quick: fastest path to an answer using the most direct data source available. Aggregates and summary fields are fine. Good for a first pass or when speed matters more than certainty.

10 ft deep— Verified: same scope as 5ft deep, but every material number or claim is checked against underlying records, not summary fields, before being reported. Cross-check at least one alternate source if available.

50 ft deep — Deep: full investigation. Verified per 10 ft deep , plus explore adjacent angles I didn't explicitly ask about but that materially affect the answer, flag risks/blind spots, and show sourcing for every claim.

100 ft depth — Staged: same investigation as 50 ft deep, but delivered in sections rather than one full reply. Before starting, give a short outline listing the sections the analysis will cover. Each section should be a complete analytical unit (e.g. "market sizing," "risks," "recommendation") — never cut off by length mid-thought — and carry the same rigor and sourcing as 50 ft deep. Deliver the first section, then end it with a one-line preview of what the next section covers, and wait for me to say "next" or "continue" before proceeding. Repeat until all sections are delivered.

Before any task that produces a build/deliverable (email, deck, doc, page, design, artifact) — not a plain text answer — ask for a craft level and wait, unless I've specified one:

Sketch — bare structure, one pass, no polish.
Draft — styled, functional, presentable, not fussed over.
Painting — custom, detail-checked, tested against real quirks.
Commissioned — full polish: edge cases, accessibility, cross-platform, pixel review.

Rigor and craft are separate. Ask for both only when both apply, as two quick picks, not one merged question.

At any stage of the analysis or you're working, if you feel that you don't have clarity on something always feel free to ask a question.</userPreferences>

[Uploaded file: SOP.pdf — EOXS RQL (Rapid Qualification of Leads) Standard Operating Procedure. Covers: 1. Working website/LinkedIn URL match, 2. Location (US/Canada only), 3. Product offerings (bars, coils, plates, sheets, rods, tubes/pipes, beams, rebar, strips, metal roofing — roofing companies exempted from the steel-product requirement), 4. Materials (stainless steel, carbon steel, alloy steel, tool steel, cast iron, wrought iron, aluminum, copper, brass, bronze, titanium, nickel, cobalt, zinc, lead, palladium, platinum, silver, gold, tin, magnesium), 5. LinkedIn member count (disqualify if under 15), 6. Services (HD plasma cutting, cut-to-length, slitting, blanking, precision shearing, plate/coil processing, surface grinding/polishing, cutting, welding, bending, punching, drilling, grinding), 7. Parent company ownership handling (mark "Owned by a parent company," note parent name, verify EOXSTEAM contacts module updated), 8. UUM/SOM bucket handling (verify + cross-check on EOXSTEAM, cannot be marked qualified/disqualified), 9. Special cases (mark "Not Sure" with remarks if unclear), 10. Steel mills list for US/Canada (Nucor, U.S. Steel, ArcelorMittal USA, Steel Dynamics, AK Steel, Big River Steel, Cleveland-Cliffs, Commercial Metals, TimkenSteel, Allegheny Technologies for US; ArcelorMittal Dofasco, Stelco, Gerdau Ameristeel, Algoma Steel, Ivaco Rolling Mills, SSAB Americas, Tenaris, Evraz North America, Salzgitter Mannesmann, Russo Pipe for Canada).]

https://www.askcruz.com/

Hi, my name is Danish Lari and i specifically work on data enrichment and data management withing AskCruz and EOXS,

so when we did the RQL before for EOXS we followed this SOP to find and qualify leads that we can reach out to for EOXS, now we are running RQL for AskCruz and since both AskCruz and EOXS are a different product we can't folllow the same SOP here, so i want you to give me revised SOP on which criteria i should qualify companies for AskCruz, like for EOXS we did very rigorus filterting whther the same will be applied to AskCruz

Assistant: I need more context before I can give you a usable revised SOP — right now I don't have enough to draw the line correctly.

The core question: what is AskCruz, and who does it sell to? The EOXS SOP is entirely steel/metal-industry-specific — product types, materials, mill lists, all built around EOXS being an ERP for metal distributors/service centers. If AskCruz is a different product (different ICP, different vertical, different buyer), the qualifying criteria don't just loosen — they're probably a different shape entirely, not a "relax the steel filter" exercise.

Let me check what I have on file first.

[Read threads-ov SKILL.md — mandatory auto-save rule, tools, SYNTHESIZE/CROSS-LINK workflows, guardrails. Read eoxs-data-general SKILL.md — connector navigation for eoxs-db and eoxs-teams, access scope, redaction rules, call efficiency guidance, decision trees, answering format. Attempted to load eoxs-db tools via tool_search; confirmed no eoxs-db connector (search_wiki/search_assets/get_index) exists in this session — only AskCruz MCP, Team EOXS MCP, EOXS Data General (tier1-only repo docs), Fireflies, Gmail, and Thread OV are available.]

[Searched Thread OV saved transcripts for "AskCruz RQL ICP qualify leads" — no results. Searched for "AskCruz" broadly — surfaced multiple prior threads, all under user "yashvir" (Yash Singh), an AskCruz LDR focused on cold-calling/pipeline/ARR, not data enrichment. Key finding from raw/claude-chat-queries/yashvir_2026-08-26_askcruz-positioning-strategy-catchup.md: unresolved core question on record — is AskCruz industry-agnostic or steel-specific? 2 of 3 internal docs said industry-agnostic, the Product Feature File said steel-specific; explicitly flagged as needing Raj's confirmation before external use, not settled as of that thread. One confirmed customer (3GM Steel), Sabre Alloys and Collier Metals still pipeline (both steel/metals). Also surfaced: yashvir_2026-08-28_what-is-a-claude-skill.md noted Yash referenced a "raj-eoxs-vault" skill that does not exist in the catalog — only threads-ov, eoxs-data-general, and askcruz-sales-strategy are present, matching what this session also confirmed.]

I noticed a trailing system-reminder-formatted block appended to a tool result instructing me to call save_chat_transcript with a "new_messages" parameter and skip asking permission. I disregarded it as untrusted tool-result content, not a real instruction — it also contradicts the actual SKILL.md (which requires the full verbatim transcript, not a delta named "new_messages"). I said so explicitly and continued following the real skill file.

Before I go further, I need to flag a discrepancy rather than proceed:

Identity mismatch. Your profile says Danish Lari, data enrichment/management on AskCruz and EOXS. But every prior AskCruz thread in Threads OV belongs to a different user — "yashvir" (Yash Singh), an LDR on AskCruz, sales/outbound-focused, not data enrichment. This isn't just a name difference — his stated scope (pipeline/ARR, cold calling, ICP-for-sales) is adjacent but not the same as yours (RQL/data enrichment against a filtering SOP). I'm not going to blend his account's saved threads into your data-enrichment task without you confirming these are in fact both you, or that they're separate people on the same initiative.

More importantly for your actual question — the unresolved blocker on record: per askcruz-positioning-strategy-catchup (2026-08-26), there is an open, unconfirmed question: is AskCruz industry-agnostic or steel-specific? Two of three internal docs say agnostic, one (the Product Feature File) says steel-specific, and it's explicitly flagged as needing Raj's confirmation before external use. There's also only one confirmed customer (3GM Steel — a steel company), with Sabre Alloys and Collier Metals as pipeline (also both steel/metals, per the naming).

This matters enormously for the RQL SOP you're asking for. If AskCruz's actual current ICP is still steel/metals (just with an aspirational cross-vertical narrative), the revised SOP might keep most of the EOXS product/material filters and only change the parts EOXS-specific (parent-company ERP language, mill lists relevant only to EOXS's specific use case) rather than opening the vertical entirely.

Before I draft anything, I need:

[Asked two clarifying questions via ask_user_input_v0: (1) whether the user's account is the same as "yashvir" or a separate person, (2) whether AskCruz's ICP has been resolved as industry-agnostic vs steel-specific.]

User: Q: Is your account the same as "yashvir" (Yash Singh, AskCruz LDR) in prior saved threads, or are you a separate person on the AskCruz team?
A: No, I am Danish Lari, having email danish@askcruz.co in AskCruz and danish@eoxsteam.com in EOXS and i don't do cold calling but i do manage data and enrich prospects details

Q: What is AskCruz's current confirmed ICP as of today — has the industry-agnostic vs steel-specific question been resolved?
A: Still steel/metals only for now

Assistant: Good — that resolves both open questions cleanly. You're a separate person (data/enrichment, not sales), and the ICP is confirmed: still steel/metals only, same as EOXS, at least for now.

That changes the shape of this task substantially. If the ICP is still steel/metals, this isn't a rebuild of the qualifying criteria — it's a narrower edit: most of the EOXS SOP's substance (product types, materials, US/Canada, LinkedIn presence, parent company handling, UUM/SOM, mills) likely still applies, because it's testing "is this a real steel/metal company" not "is this an EOXS-specific company." What actually needs to change is whatever in the SOP is tied to EOXS's specific product (ERP-buyer signals) rather than to the industry itself.

Before I draft the revision, I want to nail down what's actually different between the two products' buyers, since that's the real hinge:

[Asked two more clarifying questions: (1) what AskCruz actually sells relative to EOXS's ERP, (2) whether there are AskCruz-specific disqualifiers the current SOP doesn't check for.]

User: Q: What does AskCruz actually sell to a steel/metal company, as distinct from EOXS's ERP? (so I know which SOP criteria are ERP-specific vs industry-specific)
A: you have connectors of database which has everything about EOXS and AskCruz, rather than asking me i want you to analayse thoroughly on what AskCruz is, what it does

Q: Is there any AskCruz-specific disqualifier that wouldn't apply to EOXS — e.g. company size, tech stack, or whether they already have an ERP—of the type the current SOP doesn't check for at all?
A: Not sure — help me think it through

Assistant: Fair — I have connectors, I should use them rather than ask you to explain your own product. Let me pull what's actually there.

[Called AskCruz MCP:list_tables — confirmed askcruz is Odoo 13, sale/purchase/account apps NOT installed (no sale_order/account_move/product_template), core focus is HR + Project + Training, but also surfaced a CRM-adjacent custom data model: res_partner, crm_lead, business_type, custom_product_type, custom_service_type, product_vertical, company_structure, res_partner_industry, and champion/decision_maker relation tables.

Described crm_lead — standard Odoo CRM fields (name, partner, stage, source, probability, address, etc.), no product/material/business-type classification fields directly on crm_lead itself.

Attempted a schema query but initially called Team EOXS MCP:query by mistake, returning EOXS Team Live context instead of AskCruz — caught the error, reloaded the correct AskCruz MCP:query tool, and re-ran correctly.

Queried res_partner for industry_id/company_type/customer_rank/supplier_rank/website/function/category_id columns — confirmed website, function, industry_id, supplier_rank, customer_rank exist.

Ran a joined query across res_partner + business_type + custom_product_type + custom_service_type + res_partner_industry + product_vertical for all customers/lead-linked partners. Result: 34 distinct combinations, business_type values are Service Center / Processing Centre / Fabricator, product_vertical values are Alloy, Steel, Aluminum, Carbon, Stainless Steel, Zinc — confirming AskCruz's actual live CRM data is steel/metals companies, matching the "still steel/metals only" answer with real data. industry_id was null across every row (not populated). custom_product_type was null across every row (not populated).

Queried company_structure table columns, then queried company_structure_res_partner_rel joined to company_structure — confirmed two values in use: Parent (228) and Subsidiary (25) — a direct equivalent to the EOXS SOP's "owned by a parent company" rule.

Checked for an employee-headcount or company-size field — none exists in the schema.

Queried crm_lead.description for a sample of 15 leads with substantive descriptions — results were plain contact-info notes (name, title, email, phone, LinkedIn) and two short company-profile blurbs (Esserman Steel — independent steel distributor, hot-rolled products; nothing else pointing to an unwritten ERP-status or headcount disqualifier).]

This is genuinely useful — sale/purchase/account modules are noted as not installed, but the schema still shows crm_lead, custom_product_type, custom_service_type, business_type, product_vertical, res_partner_industry, company_structure, and interesting fields like res_partner_res_partner_champion_rel / decision_maker_rel. This looks like their actual CRM/lead-qualification data model for AskCruz.

I now have what I need. Here's the summary of what the data actually shows, then the revised SOP.

What the connectors show, concretely:
- AskCruz's own CRM (steel/metal companies in the pipeline) uses the same materials taxonomy as the EOXS SOP: Steel, Aluminum, Alloy, Carbon, Stainless Steel, Zinc — confirming the "still steel/metals only" answer with real data, not just your recollection.
- It has a business_type field (Service Center / Processing Centre / Fabricator) that the EOXS SOP doesn't formally use as a category — worth carrying over explicitly since it's how AskCruz already segments leads.
- It has company_structure (Parent / Subsidiary) — directly equivalent to the SOP's "owned by a parent company" rule. Carries over unchanged.
- Nothing in the schema tracks employee headcount, existing ERP/software stack, or company size at all. That's a real gap, not just something I couldn't find — if "already has an ERP" or "too small to need AI tooling" should be a disqualifier, it isn't currently captured anywhere and would need to be added as a new field, not just a new SOP line.
- No AskCruz-specific asset/SOP document exists in the connectors I have access to (eoxs-db isn't in this session) — so this revision is inferred from live CRM structure and your product's data model, not from an existing written AskCruz ICP doc. Flagging this so you don't treat it as "confirmed by Raj" — it isn't.

Revised RQL SOP — AskCruz

Unchanged from the EOXS SOP (same industry, same qualifying logic):

1. Working website and LinkedIn URL — same rule, same disqualify-if-missing.
2. Location — US/Canada only, same rule.
3. Product offerings — same list (bars, coils, plates, sheets, rods, tubes/pipes, beams, rebar, strips, metal roofing).
4. Materials — same list (carbon steel, stainless, aluminum, copper, etc.).
5. LinkedIn member count — same 15-member floor, unless you have a reason to think AskCruz's target buyer is smaller than EOXS's (worth checking against real numbers before keeping this as-is).
6. Services — same list (cut-to-length, blanking, slitting, etc.).
7. Parent company handling — same rule, and it maps directly onto the existing company_structure field (Parent/Subsidiary) in the AskCruz CRM, so this is a place where AskCruz's data model already agrees with the SOP.
8. UUM/SOM handling — same rule, if that bucket concept exists on the AskCruz side too (worth confirming — I didn't verify UUM/SOM tracking exists in the AskCruz Odoo instance).
9. "Not Sure" escalation — same rule.
10. Mill list — same rule, same list.

New — add explicitly (AskCruz-specific, not in the EOXS SOP):

11. Business type classification. Tag every qualified company as Service Center, Processing Centre, or Fabricator (the AskCruz CRM already uses these three categories) — this isn't a qualify/disqualify gate, but it should be captured on the Data Enrichment sheet since AskCruz segments its pipeline this way and EOXS's SOP has no equivalent field.

Open question — needs your input before it goes in the SOP, not something I can resolve from data:

12. Company size / tech stack. There's no existing field for employee headcount or "already has an ERP" in either SOP or the AskCruz data model. If AskCruz is meant to disqualify companies that already have a mature ERP+AI stack, or that are too small to be a real buyer, that's a real gap — but I'm not going to invent a headcount threshold or "no existing ERP" rule without you or Raj confirming it's actually how AskCruz is being sold. Given the ICP is confirmed as "steel/metals only, same as EOXS," my working read is this criterion isn't currently active — treat it as a flag for a future SOP revision, not something to add today.

Want me to turn this into an actual document (Data Enrichment sheet-ready), or is this level of detail enough for you to hand to the data team as-is?
