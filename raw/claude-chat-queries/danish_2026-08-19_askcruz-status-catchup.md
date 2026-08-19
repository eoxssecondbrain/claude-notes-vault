---
thread_name: "askcruz-status-catchup"
user: "danish"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: what's AskCruz, i have been away lately and wants to know about it so what you can tell me about it?

Assistant: [Read threads-ov and eoxs-data-general skill files as required. Called get_index, search_wiki, get_wiki_page on relevant AskCruz pages.]

This is a lookup question about AskCruz — matches eoxs-data-general (client/entity info). Let me pull the tools and check.

Here's the state of AskCruz as of what's on record (through Aug 18):

**What it is**

AskCruz — internally called "Company Brain" — is an AI layer built on top of EOXS's own operational data/experience, pitched to prospects as reasoning over the same knowledge base EOXS itself runs on. It's being sold both as a standalone product to non-EOXS companies (e.g. a legal-services prospect) and as an add-on/upsell to existing EOXS steel clients.

**Sales pipeline (active, this month)**

- **3GM Steel** — furthest along. Travis Lane (CCO) pitched Aug 12. Two proposals went out Aug 14 with inconsistent unit pricing that rolled up to the same total; Travis caught the inconsistencies himself, looped in their CFO, and wouldn't take it to their CEO until reconciled. Ron sent a corrected proposal Aug 17 — also a notable pivot here: running Company Brain on Claude as the client-facing front end rather than AskCruz itself. Whether 3GM has actually signed is unconfirmed in the record.
- **Sabre Alloys** — parallel pitch, Aug 13 call happened with client attendance, but there's a real gap in the record: the proposal email sent to the client (Mercadante/Webb) appears to have gone out with no attachment. Unconfirmed whether they ever received actual pricing/terms.
- **Ohio Strip Steel**, **Three D Metals**, **Collier Metals**, and a legal-services prospect (virtualilegal.com) — earlier-stage intro/exploratory conversations, per the wiki index.

**Internal state**

Aug 13: Raj paused the team's paid AskCruz API access for internal use on cost grounds — not a product judgment (he called the product itself "good," "brings good value"), just run-rate at this stage. Team consolidated onto a single shared Claude account instead. Separately, there's an Aug intern cohort being onboarded with AskCruz mailbox access.

**What's unresolved**

Both live deals (3GM, Sabre) have open reconciliation/delivery gaps — nothing here confirms a signed contract yet. There's no formal product spec or pricing sheet in the asset library; everything above is reconstructed from emails and calls.

Given your stated objective (AskCruz to $1M ARR in 12 months), the pricing-inconsistency pattern showing up on both live deals independently is worth flagging as a systemic issue, not two one-off mistakes — same root cause hitting two prospects the same week suggests the proposal-generation process itself needs a fix, not just a resend.

Want me to pull the Ohio Strip Steel and other earlier-stage prospect threads too, or is this enough to get you current?

User: i am asking you about AskCruz, i don't want prospect information, i wants to know about Askcruz, why it's built and what's the motive behind this?

Assistant: The prospect data is already pulled — let me check for a founding rationale doc before answering, since that's a different question than what I answered.

Here's why AskCruz exists, based on what's on record — not prospect status, the actual origin and rationale:

**Origin: it started as an internal tool, not a product**

AskCruz grew out of the "Second Brain Initiative," an internal EOXS project starting around June-July 2026. The original problem it solved: EOXS's own knowledge — emails, Zoom calls, client history — was scattered and unsearchable. The initiative consolidated that into one system, with email and Zoom feeding directly into it as the record of truth. It was built for EOXS's own internal use first — Raj, Ron, Nidhi, Ayan were the core people involved in standing it up.

**The architecture is the actual "why"**

The most precise description on record — ironically from an outside investor's cold email, which Raj apparently never corrected — is that AskCruz is an AI layer built on the experience behind EOXS that reasons over a company's ERP, email, and call data, building both the system of record and the intelligence layer on top of it. Internally it's confirmed as the same system this wiki itself runs on: raw ingestion → synthesis → query layer. So the motive isn't "build an AI chatbot" — it's "turn a company's own operational exhaust (emails, calls, ERP data) into something that reasons over itself."

**Why turn it into a sold product**

Once it worked for EOXS internally, the pitch to clients became: EOXS already reasons over its own ERP/email/call data this way — sell that same capability to other companies as "Company Brain," either standalone or bolted onto the existing EOXS platform relationship. Raj's own framing on the internal cost-pause call was that the underlying product "is good" and "brings good value" even while he was cutting internal spend on it — meaning the belief in the product's worth and the cost discipline are two separate calls, not a signal he's doubting it.

**One thing worth flagging directly**

There's a separate, unrelated initiative — an "AI Spinout" — where the AI sales-automation line (different tools: SmartQuote AI, AI Workers, Sales Coach) is planned to be moved into a separately-capitalized entity, explicitly timed to avoid triggering a revenue-share commitment to an investor named Scott Begin. That's a different product family from AskCruz/Second Brain, but if you're not tracking that structural decision, it's the kind of thing that materially affects how "AskCruz" as a business asset is positioned going forward — worth knowing exists even though it's not what you asked about.
