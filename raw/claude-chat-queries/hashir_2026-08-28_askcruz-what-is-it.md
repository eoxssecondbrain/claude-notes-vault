---
thread_name: "askcruz-what-is-it"
user: "hashir"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: What is askCruz?

Assistant: AskCruz (product family name "Cruz") is EOXS's internal AI-powered company knowledge base and conversational assistant — a "second brain" that turns scattered business information into searchable, synthesized, cited knowledge.

Architecture: a ten-stage pipeline — Source Systems → Ingestion → Filtering → Sensitivity Classification → Central Knowledge Store → Knowledge Generation → Citation Check → Human Approval → Retrieval → Response.

Data sources: Gmail (3 accounts), Zoho (shared support inbox), Fireflies (call transcripts), Fathom (call recordings), and Odoo implementation/onboarding boards for 6 clients (Greer Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, 3GM Steel, Sabre Alloys). Two clients — RW Conklin Steel and Brannon Steel — have no Odoo instance, so they only show up via email/calls. Support tickets and invoices/sales orders sit outside this ingestion (that's the eoxs-teams/CRM boundary, not AskCruz's).

Beyond internal use, AskCruz is also being positioned and sold externally as a client-facing product ("Company Brain") — described in wiki pages as "a company-specific AI product for steel businesses," currently in active sales motion (e.g. 3GM Steel closed a deal at reduced 2-user scope, Sabre Alloys in a joint proposal push).

Internally: frontend owned by Jaskeerat; server/DB and Linear credentials held by Ayan (and Nidhi for Linear) — flagged in the source as unverified/possibly stale, so don't treat as current without checking.

There's also a cost-governance thread from Aug 13, 2026: the team paused paid AskCruz API usage internally and moved to a single shared Claude account.

User: Does askCruz have any competitor in Current AI market.

Assistant: This is a market/competitive question, not a one-line lookup, so pick a depth:

5ft (quick) — one or two searches, list the obvious named categories/players (e.g. Glean, Guru, Notion AI, enterprise RAG tools) based on surface-level fit.

10ft (verified) — same, but confirm each named competitor's actual feature set and target market against AskCruz's specific claims (industry-agnostic knowledge layer, citation-checked, human-approval gate) rather than assuming from their marketing.

50ft (deep) — full landscape: named competitors, adjacent categories (internal search tools, AI second-brain startups, ERP-vendor-bundled AI), where AskCruz's differentiators (citation verification, human approval step, multi-source ingestion incl. Odoo/CRM) actually hold up vs. don't, and risks (e.g. is "industry-agnostic" even a defensible position against players like Glean who already do this at scale).

Which level?

User: 50

Assistant: Yes — real competitors exist, and the internal AskCruz docs don't name any of them or seriously engage with this problem. Two separate competitive fronts:

Direct category competitors (horizontal "company brain" / enterprise knowledge assistant market)

Glean is the dominant player at this exact positioning — connects 100+ apps, permission-aware retrieval, agentic actions, median enterprise contract ~$97,500/yr, 8-14 week deployments.
Guru has moved from "verified wiki" to what it calls an AI Agent Center — human-verified Cards plus a March 2026 Slack MCP integration that queries live conversations in real time, explicitly marketed against Glean's "stale retrospective indexing."
Sana/Lore, Sentra, Onyx (open-source), Coveo, Sinequa, Squirro, Dashworks, Shelf, Bloomfire, Hebbia, GoSearch, Coworker AI, Notion AI, Microsoft 365 Copilot, Atlassian Rovo, Moveworks — all compete in the same "connect scattered company data, answer in one conversational interface" category as of 2026.

This category is not thin. Multiple outlets in 2026 describe it as a maturing, well-funded space that has already moved into an "agentic phase" — the exact horizontal positioning the AskCruz PMF doc claims for itself.

Adjacent competitors closer to AskCruz's actual ingestion layer

AskCruz ingests Odoo implementation/onboarding boards. There are already AI copilots built natively inside Odoo: Synconics' Odoo Co-Pilot, Bista Solutions' Odoo Copilot, Copilot AI Core, and a generic "Odoo AI Copilot Assistant" module — all doing conversational query + action directly inside the same ERP a steel client already runs, no separate tool required.

Vertical steel/metals competitors

Steel- and metals-specific ERP/inventory tools already ship an "AI assistant" layer tuned to grade, heat number, and weight-based pricing — e.g. Matrex Global's steel inventory software (AI assistant + WhatsApp bot) and ERP Agent's steel-distribution quote/order automation. Larger industrial ERPs serving steel (Infor CloudSuite Industrial, SAP S/4HANA) are also adding AI/IoT features for grade tracking and yield optimization. EOXS's own ERP product even shows up as one of the "Top 20+ ERP Systems for Metal Fabrication & Steel" in third-party comparisons — a separate product from AskCruz, but worth noting since it's in the same buyer's stack.

Differentiator check against AskCruz's own claims

Citation verification + human approval before publishing: this is not novel. Guru already ships a comparable verified-answer model (SME re-check on schedule) and has pushed further with real-time MCP integration. AskCruz's version is a reasonable implementation, not a market-first.
Industry-agnostic horizontal positioning: this is the exact turf Glean, Guru, Sana/Lore, and Notion AI already occupy at far greater scale, connector depth, and proven enterprise contract value. AskCruz has one external customer (3GM), no established pricing, no proven retention/ROI. Claiming "industry agnostic" here isn't a differentiator — it's competing head-on against better-resourced incumbents with nothing yet to show for it.
Multi-source ingestion including Odoo: undercut on two sides at once — generic Odoo copilots already answer conversational queries inside the same ERP without requiring a second tool, and steel-vertical software already bakes AI into the data model (grade, heat, pricing) that actually matters day-to-day to a steel distributor's staff.

Risk worth flagging directly: your own internal docs already contradict each other on this — the PMF/positioning doc says "industry-agnostic," the Product Feature File frames AskCruz as steel-specific, and the wiki flags this contradiction explicitly. That's not a documentation nitpick — it determines which competitive set you're actually fighting. Against Glean/Guru you're a tiny horizontal player with one customer. Against Odoo copilots and steel-vertical AI you're a bolt-on tool competing with things already embedded in the ERP the customer runs. Positioning against both simultaneously, with no named answer to either, is the actual competitive exposure — not the absence of competitors.
