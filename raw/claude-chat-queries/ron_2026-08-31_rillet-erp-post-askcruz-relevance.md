---
thread_name: "rillet-erp-post-askcruz-relevance"
user: "ron"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

**User:**
[Uploaded image: WhatsApp_Image_2026-08-31_at_09_30_40.jpeg — a screenshot of a LinkedIn post by a "Strategic Tech Leader | Ventures Builder | B..." account, discussing Rillet, a 2-year-old startup that raised $100M at a $1B valuation with 600+ customers, replacing NetSuite/SAP/Oracle Fusion/Workday. The post argues the real lesson isn't "AI is disrupting ERP" but that Rillet rebuilt the ledger itself so AI agents do the work under the same rules/data as humans, with humans keeping approvals and audit records — unlike incumbents who bolted copilots onto legacy human-shaped workflows (yielding 20-30% gains vs. rebuilds yielding multiples). The post states the unlock was the harness (approvals, policies, audit trails built into the core, not retrofittable) rather than intelligence/models. It closes by asking which function gets rebuilt next, using the criteria: work must be structured, rule-governed, and survive an audit — naming accounting as the first, and data management as the author's pick for next.]

Go through this post here.

**Assistant:**
No skill in the current set (sales-strategist, dps/sabre-strategist, client-email-tone-scale) matches this cleanly — this is a general market/strategy read, not account-specific. Proceeding without one.

Quick read on the post: the author's core claim is that Rillet's edge wasn't "AI on ERP" generically — it was rebuilding the ledger itself so agents (not humans) execute transactions, with approval/audit as the native structure rather than a bolted-on layer. Copilots on legacy systems only speed up the human-shaped workflow (20-30% gains); a from-scratch rebuild changes the unit of work entirely (multiples, not percentages). His prediction: data management is the next function ripe for this kind of rebuild, using the same test — structured, rule-governed, must survive an audit.

This maps directly onto what AskCruz is trying to do inside Odoo for steel distributors, and it's obviously not just a coincidental resemblance.

What do you actually want from this — a quick take on the ideas, or an analysis of what it implies for AskCruz's positioning/roadmap against a Rillet-style approach? If the latter, pick a rigor level (5/10/50/100 ft).

[User selected: "Analyze implications for AskCruz vs a Rillet-style rebuild" via elicitation card]

**User:**
We are not just trying to do this for Odoo. We are trying to do this for all the platforms in the steel and the other industries. I want to understand how they did this and what is something that they are doing differently. I would like to find this post on LinkedIn. Can you please see who posted this?

**Assistant:**
Couldn't pin down the author. General web search doesn't reliably index individual LinkedIn posts, especially a few-days-old post from a smaller consultant-type account — I ran several searches on distinctive lines from the post ("which function gets rebuilt next," "copilots produce percentages," the harness language) and only got general Rillet coverage (Yahoo Finance, Forbes-style pieces on the raise, Wikipedia, Tracxn), not the post itself.

No Chrome browser is currently connected to this session either, so I can't search LinkedIn directly through your logged-in account — that would actually work better since LinkedIn blocks most search-engine indexing of individual posts. If you connect the extension, I can look it up properly.

One relevant find along the way: ICONIQ Growth (a Rillet investor) published a piece titled "Doubling Down on Rillet: Building a Harness for Agentic Finance" that uses nearly identical framing to your screenshot — the "harness," agents and humans sharing the same financial truth, every action auditable. Whoever wrote the LinkedIn post may well have been riffing on that piece. Worth a read regardless: https://www.iconiq.com/growth/insights/iconiq-leading-rillets-100m-series-c

On scope — noted, this isn't an Odoo-specific play for you, it's cross-platform across steel and other industries. That actually changes the Rillet comparison in an important way: Rillet owns its ledger end-to-end on one platform it built from scratch. AskCruz's harness has to sit on top of whatever ERP each client already runs. Same philosophy, harder engineering problem.

"How they did this and what they're doing differently" is a research question, not a quick lookup — pick a rigor level.

[User selected: "50ft - Deep" via elicitation card]

**Assistant:**
[Ran ~10 web searches: Rillet Aura AI agent features, Rillet architecture built-from-scratch vs bolt-on AI, AI-native ERP competitor landscape (Puzzle/Campfire/Digits/Numeric/Truewind/DualEntry/Light/Doss), steel industry ERP AI agents/distributors, turian.ai steel distribution AI agent funding/integration. Delivered the following full analysis:]

How Rillet actually built it

Rillet's core move was replacing the general ledger itself rather than adding AI on top of an existing one. A Sequoia partner who backs Rillet described pulling out a company's general ledger as something close to open-heart surgery — which is exactly why, in his view, no VC had been willing to fund a new GL challenger before Rillet. Rillet did it anyway, describing itself as built "agent-first," with AI systems capable of running hundreds of operations in parallel, executing much of the manual accounting work that traditionally consumed finance teams' time.

The mechanics that make that possible:

- Real-time architecture, not batch. The meaningful difference is architecture: AI embedded in a real-time GL acts on current data, while AI layered onto a batch system analyzes snapshots. That's what actually lets the propose-approve-post loop run continuously instead of at month-end.
- Approval and audit are structural, not bolted on. Rillet ties approvals to dollar materiality thresholds and logs every action immutably — Rillet's Aura agents operate inside a controls framework designed for SOX, ICFR, and external audit, with 100% of AI actions logged and zero auto-posts without approval, independently audited under SOC 1 Type II.
- Domain-scoped agents, not a general chatbot. Each Aura agent handles one accounting workflow (bank rec, accruals, flux analysis) and proposes for a human to approve, with a full audit trail attached to every posting.
- Deep native integrations (Stripe, Salesforce, HubSpot, and now Zapier's 8,000+ apps) feed the ledger enough context that agents can act without a human re-keying data.

What's genuinely different from a copilot

The difference isn't the model — it's that Rillet's audit trail and approval logic live in its own data model from day one, so there's nothing to retrofit. A copilot sitting on NetSuite or SAP inherits that system's batch cycles, its human-shaped approval chain, and its historical schema — it can only speed up the existing steps. Rillet skipped that constraint by owning the ledger outright.

It's not the only one doing this — worth knowing the landscape isn't as clean as "rebuild or fail"

Rillet has real company in the AI-native ERP category — Campfire, DualEntry, and Light are also rebuilding the GL from scratch to take on NetSuite. But there's a legitimate counter-case too: Numeric automates close management on top of your existing ERP rather than replacing it, and it still raised a $51M Series B; Truewind layers AI close automation onto Sage Intacct the same way. So "you must own the ledger to win" isn't a universal law — what seems to actually matter is whether the approval/audit harness is genuinely load-bearing, not whether you literally replaced the base system.

The comparable that actually matters for AskCruz

Steel and metal distribution already has a company doing close to what you described — cross-platform, not owning any single ledger. turian runs agents for order entry, RFQ/quoting, and quality-certificate processing, and is explicitly built to integrate with existing ERP systems like SAP or MS Dynamics rather than replace them, connecting to almost any ERP system. It's seed-stage and narrower in scope than Rillet (workflow automation, not general-ledger ownership), but it's the closest real precedent for "agent layer across multiple steel-industry ERPs." There are also steel-specific AI/ERP vendors like FLOW and erp-agent.com working the same angle. And separately — EOXS itself already turns up in public "best ERP for steel" roundups with a line about modern technology and AI-powered optimization that older systems can't match, which means part of the market already associates EOXS with "AI-powered steel ERP" before AskCruz has a distinct story. Worth being deliberate about how AskCruz's pitch differs from "EOXS, now with an AI feature."

The actual risk this surfaces for AskCruz

Rillet, Campfire, and DualEntry can bake approvals and audit trails directly into their own schema because they own it outright. AskCruz, by your own description, sits on top of whatever ERP each client already runs — Odoo today, potentially others tomorrow, across steel and other industries. That means the harness — the part the post calls the actual unlock — has to be re-earned against every underlying platform's data model instead of being structural once. That's precisely the setup the post says caps incumbents' copilots at 20-30% gains: an AI layer riding on top of a system it doesn't control.

The turian and Numeric precedents say this isn't a dead end — funded businesses do exist on the "layer across multiple systems" side of this line. But it puts the real product question in a specific place: is AskCruz building its own persistent, cross-platform ledger/audit layer that references transactions across whichever ERP sits underneath (closer to what Rillet did, just federated instead of owned) — or is it a workflow-automation layer that writes into each ERP's native approval tables (closer to turian, and closer to the copilot pattern the post is critical of)? Those are two different products with very different defensibility, and the post's whole argument about "multiples vs percentages" only really applies to the first one.

**User:**
If you had to rate a level at which you are giving me these replies, like okay, this is at a grade school level, high school, bachelors, masters, PhD, which level are you giving me these answers at?

**Assistant:**
Somewhere around strong MBA / consulting-analyst level — not higher.

What that response actually did: read company blogs and marketing pages, pulled together a competitor landscape, correctly identified the real axis of comparison (Rillet owns its ledger end-to-end; AskCruz's harness has to sit on top of whatever ERP is already there), and flagged the actual risk that follows from that. That's legitimate synthesis, and the framing is right.

What it isn't: PhD-level, or even solid senior-engineer level, on the technical question that actually matters here. I didn't verify how AskCruz's harness is actually built today — I speculated about two possible architectures (a persistent cross-platform audit layer vs. writing into each ERP's native approval tables) without checking which one is true. That's the difference between a good outside read and real diligence. A PhD-level or "someone who's actually built this" answer would need to look at the actual teams-askcruz implementation and the schema/approval logic that's already in place, not infer from Rillet's public docs and pattern-match.

So: strategy framing, solid B+/A- consultant-grade. Technical verification of your own system, not done — that's a different task, using teams-askcruz directly, if you want the real answer instead of my best external guess.
