---
thread_name: "askcruz-company-brain-knowledge-list"
user: "raj"
type: claude-chat
created: 2026-08-03
updated: 2026-08-03
---

User: So technically, we have just build a company Brain with ask Cruz. No efficiently work we need to make a list of all the things that this Brain needs to know and it should probably be categorized in must have or would like to have.

Assistant: This is a strategic/product-design task for AskCruz, not really a vault-data question or a sales-deal question — it doesn't cleanly match raj-eoxs-vault or sales-strategist. I'll proceed using what's already documented about AskCruz's architecture (Company Brain → Company Hands → Digital Workforce layers) rather than pulling client-specific vault data, since this is about defining the input schema, not answering a client question.

Before I build the list, pick a rigor level:

5ft deep — Quick: I draft the list from AskCruz's known architecture and general "AI operating system" best practice. Fast, directionally right, not checked against what Sabre/Monarch's actual pilots have already shown you needs ingesting.

10ft deep — Verified: same list, but I cross-check it against what's actually been scoped for AskCruz so far (IRIS live-ERP layer, OV knowledge layer, email/call ingestion, static KB) so the must-have list matches what's already been designed, not just generic best practice.

50ft deep — Deep: full pass — plus I look at adjacent angles: what SA2/Sabre's pilot and IRIS's existing query layer have already proven clients actually ask for, what's missing that killed value in early demos, data-source rights/privacy issues per client, and what "must have" really means for a $30K ACV mid-market CEO buyer (i.e. minimum viable Brain vs. nice-to-have Brain).

Which one?

User: 50

Assistant: Grounded this against what's actually documented for AskCruz/IRIS/Second Brain — not just the general architecture. Key inputs: IRIS's real deployment history (data-quality prerequisite, token limits, chart-gen capability, 85% success bar), the Second Brain pilots at Sabre and Monarch (what CEOs actually query for), a real retrieval-failure incident, and EOXS's own "EOXS Bible" internal KB, which shows what happens when you skip the boring stuff.

Must have — the Brain fails without these

Structured, clean core data
- Live ERP feed: sales orders, inventory, AR/AP, invoices, customer/vendor master data. This is IRIS's proven core and the thing every real client query has hit so far (revenue/GP by period, dormant accounts, invoice distribution).
- A data-cleanup pass before ingestion. IRIS's own GTM treats this as mandatory phase 1 — "IRIS cannot deliver value on messy/unstructured data." Raj has already turned down 25 of 30 prospects on exactly this basis ("their data is shit").

Complete, unfiltered communications ingestion
- Email and call transcripts, fetched unfiltered rather than filtered by a contact list. The Discount Pipe & Steel gap — a whole thread silently never ingested because the sender wasn't on a hardcoded name list — is a documented failure mode you've already hit once internally. Must-have means verified complete ingestion, not sampled.

Entity and process grounding
- Org chart / role map — who owns what, needed both for role-based access and for the "sales director / CFO / bookkeeper" agent personas already pitched to clients.
- SOPs and process docs. The EOXS Bible critique is the cautionary tale here: no SOPs, no employee directory, no jargon glossary — meaning your own internal AI grounding attempt already hit this exact gap. Don't repeat it in AskCruz.
- A jargon/glossary layer per client. Internally your own vault still has an unresolved "what is Velox" naming mystery. A client Brain that can't disambiguate internal shorthand will misfire on exactly the kind of relationship/history queries CEOs actually ask ("tell me my relationship with X").

Trust infrastructure
- Source-record drill-through — every answer traceable to the record it came from. Already a working IRIS differentiator; without it, a CEO has no reason to trust a number over their own report.
- Access control / role-based permissioning. Flagged internally as "close to a solution, not solved" — Raj currently can't safely share his own Claude account. This has to be must-have before multi-seat client rollout, not an afterthought.
- Cost/spend caps. The $300K-bill-in-a-4-person-company anecdote is a live cautionary example, not hypothetical.

Qualification gate (not a data category, but a precondition)
- Digitization maturity as a go/no-go filter on which prospects even get a Brain attempt. This has already functioned as your real bottleneck (25 of 30 rejected) — it belongs in the AskCruz sales/fit-call process, not just the build process.

Would like to have — real value-adds, not yet load-bearing

- Tribal knowledge injection beyond structured data — Monarch's stated intent (org chart, processing capabilities, "company intelligence") is qualitatively richer than transactional data but harder to structure and lower urgency than the must-haves above.
- Query-depth tiering ($5 / $50 / $500 problem framing) — a real UX idea Raj has articulated but not built. Nice differentiator, not required for MVP.
- Multi-modal input (screenshot/image analysis) — proven working on IRIS already, but not something every client query needs.
- Action-triggering, not just analysis — Raj's own maturity model puts this explicitly as stage 3 (reporting → analysis → action). Building it before reporting is solid is premature.
- Cross-account/portfolio benchmarking — comparing one client against similar companies. Nobody's asked for this yet; it's speculative.
- Proactive alerting — genuinely valuable, but your own SupportAI escalation-bot pattern is a live cautionary example of automated nudges firing for months with zero human follow-up. Build the human-response loop before automating alerts, not after.
- Live-call assist (Zola-style) — a separate, adjacent R&D track, not core Brain scope.

Blind spots worth flagging explicitly

- Retrieval reliability is unverified at scale. You have one confirmed ingestion gap (DPS) and one open, unconfirmed worry (Ron J's "AI sometimes drops info when summarizing" concern) — neither has a resolution on record. Before pitching AskCruz as a source of truth, you need a spot-check/audit process, not just an assumption that ingestion = complete.
- Token/context limits are a real scaling constraint, not theoretical — Tye Webb hit this at Sabre. The index → wiki → raw retrieval architecture (which this very vault uses) is the actual mitigation, not "throw more context window at it."
- Data ownership/rights per client are undiscussed in everything I can see. You're about to ingest client email/ERP data into a product you're charging $30K ACV for — there's no documented contractual language anywhere about data ownership, retention, or what happens to a client's ingested data if they churn. That's a gap, not a preference.
- Your own build-timeline estimate (1-2 months to a working client bot) has never been validated against an actual completed delivery — it's aspirational, quoted verbally, not proven against Sabre's own SA2 timeline.
