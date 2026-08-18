---
thread_name: "askcruz-overview"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-18
---

User: Tell me about askcruz?

Assistant: AskCruz is EOXS's internal Claude-based AI agent product for ERP data, also called "Cruz" or "Company Brain" in various threads. Per TA Associates' external description, cited internally as unusually accurate: it's an AI layer built on the experience behind EOXS that reasons over a company's ERP, email, and call data, building both the system of record and an intelligence layer on top of it. Architecture is raw ingestion, wiki synthesis, then an MCP query layer — the same approach as the internal "second brain" vault I'm querying right now.

Current state, as of mid-August 2026:

Sales pipeline — active proposal discussions with 3GM Steel (Travis Lane, CCO), an intro call with Ohio Strip Steel (Joe Brom), a referral thread into Collier Metals via Tripp Collier, and outreach into Sabre Alloys running alongside the 3GM deal. A legal-services prospect (virtualilegal.com) is also being explored, outside the steel vertical. The 3GM proposal has had real execution problems: two written proposals sent the same day with inconsistent unit pricing, a wrong version initially sent to the client, and a corrected version with a strategic pivot to run "Company Brain" on Claude directly rather than AskCruz as the client-facing front end.

Internal usage — the team was running paid AskCruz API access for internal work, separate from the externally-sold product. Raj paused that on cost grounds Aug 13, judging the run-rate not justified this early, while stating the underlying product itself is good. Everyone moved to a single shared Claude account instead, managed by Tanya Shrivastava. There's an unresolved internal confusion flagged in that same call about whether AskCruz can answer questions about EOXS itself, given it's built substantially from EOXS's own internal data — access-tier restrictions for interns may be the cause, not settled.

Org/process — there's a dedicated AskCruz project board in the teams-askcruz Odoo instance (39 active tasks), plus a scrum-scoring automation Raj ordered shut down Aug 17 after concluding the scores were measuring his own nagging activity rather than team engagement. A mailbox rollout (mailcow.askcruz.com) happened for the August intern cohort.

Given the $1M ARR target, the load-bearing gap right now is that no deal has closed or been confirmed accepted — 3GM is the furthest along but stalled on proposal accuracy, and none of the others have progressed past intro/referral stage. Pricing figures are redacted in what I can see here.

Sources: EOXS wiki — "3GM Steel — AskCruz (Company Brain) Proposal Call," "TA Associates — Inbound Investor Outreach," "AskCruz API Cost Pause," "AskCruz Board Scrum Reporting," "Ohio Strip Steel — Ask Cruz AI-Agent Intro Call."

User: Is AskCruz a different product than the EOXS?

Assistant: Yes — AskCruz is a separate product from EOXS ERP, not a module inside it.

EOXS ERP is the core platform: cloud-based, steel-industry-specific ERP built by Prata Inc. (trading as EOXS) — sales/CRM, inventory, processing, etc.

AskCruz is an AI agent/intelligence layer that sits on top of ERP, email, and call data — reasoning over that data rather than being the system of record itself. It's sold as an add-on/upsell to existing EOXS clients (that's the 3GM Steel proposal), but it's also being pitched independent of EOXS ERP entirely — the legal-services prospect (virtualilegal.com) has no EOXS ERP relationship at all, which means AskCruz can be sold standalone.

One thing I can't fully resolve from the data: there's naming overlap/inconsistency across threads between AskCruz, "Company Brain," and IRIS (a separately-documented natural-language BI product, also sold both as an EOXS add-on and standalone against other ERPs like Invera). The 3GM proposal call page explicitly flags this — Rajat pivoted 3GM's deal to running "Company Brain" on Claude directly rather than through AskCruz as the front end, and a separate internal call has unresolved confusion about whether AskCruz can answer questions "about EOXS." I'm not treating AskCruz and IRIS as confirmed-identical or confirmed-distinct — the vault itself hasn't reconciled that, and I'd rather flag it than guess.

User: Is AskCruz a different product than the EOXS?

Assistant: Yes. Same answer as above: AskCruz is a separate AI reasoning/agent layer, not part of EOXS ERP itself. EOXS ERP is the core steel-industry ERP platform (sales/CRM, inventory, processing). AskCruz sits on top of ERP, email, and call data and is sold separately — as an add-on to existing EOXS clients (3GM Steel) and also standalone to entities with no EOXS ERP relationship at all (the legal-services prospect, virtualilegal.com).

The one open question, still unresolved in the data: whether AskCruz is functionally the same thing as IRIS (a separately-named natural-language BI product) or genuinely distinct — the vault itself hasn't reconciled that naming overlap.
