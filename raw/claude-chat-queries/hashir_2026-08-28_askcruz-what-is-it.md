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
