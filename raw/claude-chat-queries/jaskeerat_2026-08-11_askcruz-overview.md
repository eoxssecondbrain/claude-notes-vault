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

User: One thing I can't fully resolve from the data: there's naming overlap/inconsistency across threads between AskCruz, "Company Brain," and IRIS (a separately-documented natural-language BI product, also sold both as an EOXS add-on and standalone against other ERPs like Invera)

where is this mentioned?

Assistant: That comes from three separate pages I pulled:

3GM Steel — AskCruz (Company Brain) Proposal Call (Aug 2026) — this page itself notes the pivot: Ron J's Aug 17 corrected proposal included "a notable strategic decision to run Company Brain on Claude rather than AskCruz as the client-facing front end." That's Rajat/Ron treating AskCruz and the Claude-direct approach as two different implementation paths for the same "Company Brain" pitch.

AskCruz API Cost Pause (Aug 13, 2026) — contains this flag verbatim in the tool data: "Tanya Shrivastava says AskCruz couldn't answer questions 'about EOXS,' which is odd if AskCruz is... 'the same system this wiki runs on'... the transcript is ambiguous between 'eos' (EOXS) and 'Ask[C]ruz' as what couldn't be answered." That's the unresolved confusion I referenced.

IRIS (wiki page, filed under "3GM Steel — IRIS AI Historical Data Preload") and EOXS ERP page — these describe IRIS separately as "Natural-language BI — type a question, get a live cross-module report," sold both as an EOXS add-on and as a standalone product for non-EOXS ERPs (Invera, Steel Tracks, QuickBooks). Nothing in the wiki explicitly states IRIS and AskCruz are the same or different product — they're just documented on separate pages with separate naming, which is the inconsistency.

None of these pages state directly "AskCruz and IRIS are the same/different" — that's my own inference from seeing both used to describe similar AI-reasoning-over-ERP-data functionality without a page that cross-references or distinguishes them. Flagging it as unresolved was my call, not a sourced claim from any single page.

User: How is IRIS different than AskCruz?

Assistant: That asset doc — "EOXS ERP — Product Features Overview" (the official internal product-features reference) — settles this more than the wiki threads did.

IRIS is an official, catalogued EOXS product. It's listed in the AI Tools table alongside 14 other named tools (SmartQuote AI, Contract Review AI, PromptPO AI, etc.), officially defined as: "Natural-language business intelligence across all modules; type a question and IRIS generates the report — covering sales, ops, finance, and supply chain."

AskCruz does not appear anywhere in that official product-features document. Not in the AI Tools table, not elsewhere.

So the practical difference:

IRIS — a formalized, documented product module, sold as part of the EOXS catalog and pitched standalone to non-EOXS-ERP prospects (Invera, Steel Tracks, QuickBooks users). It's the natural-language BI layer specifically — ask a question, get a cross-module report.

AskCruz — not in the official product catalog at all. It's functioning as an internal, still-forming initiative: an AI agent/reasoning layer built on Claude, referred to informally as "Cruz" or "Company Brain," being pitched ad hoc to specific prospects (3GM, Ohio Strip Steel, Collier Metals, a legal-services company) without a settled feature definition, pricing model, or even consistent internal naming — hence the confusion in the Aug 13 call about whether it can answer "about EOXS" questions.

That's a meaningful distinction for your ARR target: IRIS is a shippable, definable product with an existing sales motion inside the EOXS catalog. AskCruz right now reads as pre-product — pitched deal-by-deal, without the same institutional definition, which is likely part of why the 3GM proposal had pricing inconsistencies and a mid-deal pivot to a different technical approach.

User: What are similarities in IRIS and AskCruz?

Assistant: Both surface from the same underlying idea, even though only one is formally catalogued:

Both are AI layers on top of data, not the system of record. Neither replaces EOXS ERP — they answer questions about the data the ERP (and other sources) holds, rather than storing/processing transactions themselves.

Both use natural-language query as the interface. IRIS: "type a question and IRIS generates the report." AskCruz: same interaction pattern, reasoning over ERP, email, and call data via an MCP query layer.

Both are sold two ways — as an EOXS add-on to existing clients, and standalone to organizations with no EOXS ERP relationship at all. IRIS standalone targets are other ERPs (Invera, Steel Tracks, QuickBooks). AskCruz standalone target so far is the legal-services prospect (virtualilegal.com) — different vertical entirely, same "sell the intelligence layer without the ERP" motion.

Both are being pitched into overlapping accounts. 3GM Steel has an active IRIS trial (data preload discussion, Aug 2026) running at the same time as the AskCruz/Company Brain proposal. Sabre Alloys shows up in both AskCruz-adjacent threads (Claude AI Agent Request) and prior IRIS deployment notes from memory — so the sales motions aren't cleanly separated by account either.

Both have real deployment friction documented. IRIS at Sabre was flagged as sandbox/QA only, no signed commercial terms. AskCruz at 3GM has the pricing-inconsistency and mid-deal technical pivot problems already covered.

Net: they're two expressions of the same strategic bet — that the reasoning/query layer over business data is a sellable product distinct from the ERP itself. IRIS is the version EOXS has formalized and named in its own product catalog; AskCruz is the version still being improvised deal by deal. Worth asking Raj directly whether these are meant to converge into one product or stay separate — the data doesn't show that decision has been made, and running two undifferentiated AI-layer pitches into the same accounts is the kind of thing that costs you deal velocity, not gains it.

User: Does IRIS have access to email, companies database historic data, ?

Assistant: Per the official product-features doc, no — IRIS is scoped to ERP modules only. It's defined as "natural-language business intelligence across all modules... covering sales, ops, finance, and supply chain." That's ERP transactional data, not correspondence.

Breaking down your three questions:

Email — not in scope. No source describes IRIS ingesting email. Email/call ingestion is documented specifically for the AskCruz/Claude-agent side and the internal second-brain vault, not IRIS. The AI Workers page draws this line explicitly: it separates workflow-automation tools and IRIS (ERP-only BI) from "the concept of a Claude AI agent connected directly to client ERP data" — which Sabre Alloys piloted May–June 2026 and which is the thing that became AskCruz/Cruz. That pilot is the one with the broader multi-source reach.

Companies/contacts database — likely yes, since IRIS spans "all modules" and CRM/Contacts is one of EOXS ERP's core modules, but I don't have an explicit line confirming IRIS queries the Contacts module specifically. Flagging that as inferred, not sourced.

Historical data — yes, this one is solid. ERP modules include inventory forecasting (explicitly historical), sales history, financial statements with drill-down. If IRIS spans "all modules," it spans that historical data too.

So the real dividing line here isn't "does IRIS see less data" in a vague sense — it's that IRIS is bounded to the ERP system itself, while AskCruz/the Claude agent concept is the one built to reach outside the ERP into email and calls. That's consistent with everything else we've found: IRIS is the catalogued, ERP-native BI tool; AskCruz is the broader, still-informal cross-source agent.

User: So it just have an access to an inbuilt ERP CRM that breakdowns the complex answers to simple words?

Assistant: Close, but two corrections worth making:

Not just CRM — it spans all ERP modules, not one. Sales, inventory, finance, purchasing, processing, supply chain — same natural-language interface across all of them, and it can pull cross-module (e.g., a question that needs both sales and inventory data in one answer).

It's not simplifying existing complex answers — it's generating the report from raw data on the fly. You ask a question in plain language, it queries the underlying data and produces the report itself, rather than taking some existing complex output and rephrasing it simpler.

So more accurate framing: IRIS is a natural-language query layer over the ERP's own data across every module, that builds the answer/report live rather than translating a pre-existing one. What it doesn't do is reach outside the ERP — no email, no calls, no external correspondence. That's the boundary that separates it from AskCruz.

User: Ohhh that makes sense now.

Assistant: Good. Anything else on AskCruz/IRIS, or a different topic?

User: noo, lets come back to the main thing, so you know that askcruz is a different product right?

Assistant: Yes, confirmed. AskCruz is a separate product from EOXS ERP — it's not a module inside the ERP platform. It's an AI reasoning/agent layer (Claude-based) that sits on top of ERP, email, and call data, sold both as an add-on to existing EOXS clients and standalone to prospects with no EOXS ERP relationship at all.

It's also distinct from IRIS, the other AI layer product — IRIS is officially catalogued in EOXS's product-features doc and scoped to ERP modules only; AskCruz is not in that catalog and reaches beyond the ERP into email/calls.

So: EOXS ERP (core platform), IRIS (catalogued, ERP-only BI layer), and AskCruz (uncatalogued, broader cross-source AI agent) are three distinct things, not one product with different names.

User: Do you also know that AskCruz has its own website?

Assistant: This adds a real fact I didn't have before, and it corrects a naming assumption from earlier in this thread.

Direct answer: yes — askcruz.com is the website. This is confirmed in a raw email (Aug 5, 2026, Rajat to Ryan Capinski at Eastern States Steel): "While 'askcruz' is the website. The AI is called just Cruz."

Two things this email surfaces that we hadn't established yet:

AskCruz was renamed from Krinox on Aug 5, 2026. Same email: "We renamed Krinox to AskCruz." Krinox is documented elsewhere in the wiki as a query-layer product for freight/logistics-heavy operations, pitched to Eastern States Steel — not yet confirmed/signed there. So Krinox = AskCruz's earlier name, at least for this product line.

It's explicitly positioned as not steel-specific. Rajat's own words: "this is not limited to Steel. This product fits any business with 20+ employees." That's a materially different scope than what the 3GM/Sabre steel-account threads implied — those are just where the current sales activity happens to be.

One thing to flag honestly: this creates real naming instability I should have caught sooner. In one thread it's "AskCruz," pitched broadly beyond steel; in another it's "Company Brain," pitched specifically to steel clients as an EOXS upsell; and Krinox was the freight-specific predecessor name. Whether these are all the same evolving product under different names at different times, or genuinely separate initiatives that happen to share underlying tech, isn't settled in the data — worth asking Raj directly rather than me continuing to infer.

User: So until now whatever responses you gave, you didn't know everything about askCruz?

Assistant: Correct — and worth being precise about why.

My earlier answers were built from the synthesized wiki pages (the "second brain" layer), which is a curated summary sitting on top of the raw emails, not the raw emails themselves. Those wiki pages never mentioned askcruz.com, the Krinox rename, or the "any business with 20+ employees, not steel-specific" positioning. I only found those by running a direct full-text email search just now — something I hadn't done for this thread until you specifically asked about a website.

So the gap wasn't that the data doesn't exist in the vault — it does, in a raw email from Aug 5. It's that the synthesized layer I was defaulting to hadn't captured it yet, and I didn't cross-check raw correspondence until prompted.

Practical implication for you: everything I told you earlier about AskCruz's product identity, naming, and scope should be treated as "what the synthesized wiki currently reflects," not "the full picture." The wiki itself has a known lag (per the connector's freshness rules — new pages draft every 6 hours, and there's no guarantee everything gets promoted or written up). Given that AskCruz's whole pitch to clients is being a more complete, always-current second brain than what a human would piece together manually, this specific gap is a little ironic — and a reason to verify anything AskCruz-related against raw emails/calls before treating the wiki synthesis as final, especially for anything client-facing or pricing-related.

User: Out of everything do you atlease know we're selling askcruz as a seperate product?

Assistant: Yes — that part is solid, corroborated across four independent accounts, not just one thread:

3GM Steel — a standalone written proposal (separate pricing lines) for "Company Brain," pitched as an add-on/upsell to an existing EOXS client.

Eastern States Steel — Krinox/AskCruz pitched with its own proposed pricing structure, evaluated by Ryan Capinski as a separate purchase decision against just "getting more value out of core EOXS first." That framing alone confirms it's being sold and evaluated as distinct from the ERP.

Ohio Strip Steel — a dedicated "Ask Cruz: Intro Call," separate from ERP onboarding, run by Rajat specifically to demo Cruz.

Legal-services prospect (virtualilegal.com) — pitched with zero EOXS ERP relationship at all, which only works if it's sold as its own product.

So across four separate deal threads, four different prospects, and two different account owners, AskCruz consistently shows up with its own sales motion, its own proposal documents, and its own pricing — never bundled silently into an ERP implementation. That's the one fact in this whole conversation I'd call fully confirmed, not inferred.
