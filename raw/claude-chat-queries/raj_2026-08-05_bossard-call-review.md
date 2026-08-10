---
thread_name: "bossard-call-review"
user: "raj"
type: claude-chat
created: 2026-08-05
updated: 2026-08-10
---

User: we had a call with Bossard yesterday. pull it up. pull the fireflies transcript.

Assistant: Pulled it. Bossard (fastener distributor, Dynamics 365 shop, Cedar Falls IA) — this is a new lead, not in the vault's prior EOXS client/prospect history or your named pipeline accounts. First contact on record.

Call: "Amy Mihm and EOXS," Fireflies, Aug 4, 2026, 1h 35m. You hosted.

Participants (Bossard side):
- Amy Mihm — supply chain analytics
- Lucas Meyer — buyer, quoting for OEM customers
- Tyler Aries — buyer, same role as Lucas
- Emily Laizure — customer-facing sales
- Kathryn (Katie) Wittgreve — business analyst, sales

What they're solving for:
Bossard doesn't manufacture — they're the middleman between fastener vendors and customers. Quoting is their bottleneck: RFQs of 100-500+ line items are managed manually across spreadsheets when they exceed what Dynamics can handle cleanly. New-part quotes take up to 45 days. They're losing business to faster competitors.

Numbers they gave you:
- ~500,000 released SKUs in Dynamics, ~100,000 active
- Product master data is 75-80% clean by their own estimate (Amy and Lucas landed there independently)
- 60,000-65,000 parts shipped monthly
- Estimated 3,000-4,000 new-business quotes/month outside blanket orders
- Self-estimated new-part revenue opportunity: ~$22M/year if they win more of what they currently lose to slower competitors
- ~5,000 hours/year of manual quoting effort at 10% AI adoption, by their own model
- Sales team ~150 people across Americas (workforce ~7,500 total)

Your proposed structure, as you laid it out on the call:
1. Company brain — ingest Dynamics ERP data + email into a structured knowledge base (three layers: live ERP, static SOPs, pricing/knowledge base)
2. Smart Quote AI agent — reads inbound RFQ emails, matches to SKU or drops a placeholder generic SKU, drafts the quote in Dynamics, routes to the salesperson for approval before it ever reaches the customer
3. Pricing hook: $4/quote for the agent, plus a separate implementation/maintenance cost for the company brain scaled to seat count — you didn't give a number, said you'd follow up
4. You surfaced a real blocker: Dynamics currently allows attachments at the quote header level but not the line-item level — you flagged this as a cheap Dynamics customization ("a couple thousand dollars," their words) they should push their Dynamics partner on, since it directly unblocks getting 100% of quoting into the system instead of staying in spreadsheets

What you're on the hook for:
- Meeting summary + solution proposal doc (you offered a 1-page, then 3-page, then 20-page version)
- Pricing: implementation cost, company-brain maintenance cost, $4/quote agent fee
- Security/technical documentation — IAM, SSO, data residency (Azure vs. your environment), audit/logging visibility. Emily raised this explicitly; their IT runs everything through a global CIO approval process
- All three deliverables need to land before their internal executive review

Timing flag: Emily said this group was commissioned by Bossard's CEO and VP of Sales, and that they present to the executives "next Wednesday." Said on a Tuesday (Aug 4), that's ambiguous — could mean tomorrow (Aug 5, today) or Aug 12. Worth confirming directly with Emily rather than assuming, since your three documents are load-bearing for whatever they walk into that room with.

What's outstanding from Bossard: sample product master data and a video/demo of their sales-order quoting flow in Dynamics — both promised by Emily, neither delivered yet on this call.

Source: raw/calls/2026-08/call-2026-08-04-amy-mihm-and-eoxs.md

Want the full raw transcript pasted out, or is this enough to work from for the follow-up docs?

User: On the surface, I have two ideas. At this point, I don't think it would make sense for us to build a second brain for them. It is going to be a lot of work and would require a lot of accesses directly on their dynamics and the second is to offer them Smart Quote AI where the AI can send the salesperson a copy of the quote when they recieve an inquiry. We can inject pricing structures if they have a set pricing matrix, and we can even look at available inventory for the items in that email. Basically, this acts more like a quoting AI assist.

do a 50ft deep analysis. take your time.. take it step by step. 

My pricing thoughts. /
Implementation fee: 40-60k. Divided into 4 phases or something. 
Flat monthly fee: 3k maybe
Price per quote: $4 ( max 5 lines ); anything over 5 lines is 0.75/line

We should say, what all it includes.. Support. Etc. Review the transcript and see what all needs to be included also. 

dont write the email or the proposal yet. think like a seasoned SaaS enterprise salesperson and a solutions architect.

Assistant: Good call to cut the second brain for now — but let me walk through why, and where the real risk moved to as a result. I checked this against what's actually on file for Bossard (no CRM record exists yet — this is still pre-pipeline) and against how EOXS's comparable deals have actually played out, not just how I remembered them.

One thing to flag before the analysis: the pricing anchor I'm holding for Bossard is $48K implementation + $3,500/month, tied to a "one-click salesperson-credentialed save" feature. I can't find that documented anywhere — no CRM lead, no saved analysis, no chat summary, nothing in the vault beyond the raw Aug 4 call, which is pure discovery with no pricing discussed. Worth noting: I just checked the IMS Metals deal, which I also had tagged as "$48K, full cycle completed" — the actual current record shows it evolved to an $8K feasibility gate and is still open, unresolved. So background notes on pricing anchors have proven stale at least once already today. Tell me if $40-60K/$3K/$4-tiered is a deliberate reset or if I should be reconciling against something else.

Dropping the second brain — is it right

Yes, and for a sharper reason than "less work." Three things converge:

Bossard is running an active global Copilot consolidation mandate. Emily said it directly — IT is actively pushing everyone off ChatGPT/Claude and onto Copilot "so that it's governed," and Copilot doesn't have ERP access yet but it's "on the roadmap." A second brain with its own front end (Cruz) is a second, competing AI surface inside an org that is actively trying to reduce the number of AI surfaces. You'd be selling into headwind, not just complexity.

The CIO approval chain is real and already flagged. Emily asked for IAM/SSO, data residency, and audit visibility unprompted, before you even sent anything. A full second brain — email ingestion, ERP-wide access, a separate hosted front end — is a much bigger governance review than a scoped, read-mostly quoting agent. Bigger review = slower deal, and this deal already has a ticking clock (their exec meeting).

It matches what was actually asked for. The group was commissioned by the CEO/VP Sales specifically to solve quoting speed. A second-brain pitch answers a question nobody in that room asked yet.

Where this actually leaves you exposed: the second brain was your moat. A narrow quoting agent — reads an email, matches a SKU, drafts a quote in Dynamics — is close to the textbook use case for Microsoft's own Copilot Studio, which is explicitly a low-code agent builder that plugs into Dynamics. You are proposing the exact shape of tool their own governed stack is built to let them build in-house eventually. This is the same objection that just forced IMS Metals down from $48K to an $8K gate — Ram Shenoy asked, in writing, why he wouldn't just run Claude against his own data himself. Bossard's IT will get to the same question, faster, because Copilot Studio makes "build it ourselves" a real internal option, not a hypothetical.

Don't drop this thread. Your differentiation has to shift from "we have the AI layer" (true but not exclusive to you anymore) to speed of delivery, matching accuracy on their specific dirty data, and a support/tuning relationship a two-week internal Copilot Studio pilot won't have on day one. Say that explicitly somewhere in the doc — not as a slogan, as a comparison table if useful later.

Scope precision — two different problems are getting merged

You described one tool: "reads inquiry, injects pricing, checks inventory, drafts quote." But the call actually describes two distinct workflows, and they need different mechanics:

Known SKU, existing pricing/stock — the quoting agent can pull the pricing matrix and check on-hand inventory and draft a real, priced quote fast. This is a clean win and matches what you scoped.

Brand-new part, no SKU yet — this is the 45-day bottleneck they led with, and the one behind the $22M number they're excited about. There is no inventory to check here — nothing has been sourced. What the agent can actually do for this bucket is extract specs from the email/print, create the placeholder SKU, and route the RFQ to the right vendors faster based on historical fulfillment data. That's RFQ triage, not quoting — Bossard still has to wait on a vendor's price before anything is quoted to the customer.

If the proposal doesn't separate these two explicitly, you set up a credibility problem: the exec team heard "$22M in new-part revenue" on this call, and $22M is entirely a new-part-bucket number. If v1 only ships the known-SKU path (which is the easier, faster build), you haven't touched the number they'll remember from this meeting. Decide now which bucket v1 actually covers, and if it's known-SKU only, say so plainly rather than letting the $22M framing imply otherwise.

Data quality doesn't go away with the scope cut

75-80% clean was their own number (Amy and Lucas landed there independently, unprompted), and both flagged the same failure mode — same attribute (zinc/Zn/color) represented multiple ways, inconsistent spacing in dimensions. That directly breaks SKU-matching accuracy regardless of whether you're running a full second brain or a narrow quoting agent. This needs to be Phase 1 work either way — either a data-profiling pass before matching logic ships, or a defined low-confidence fallback (agent flags "not sure, pick from these 5" rather than guessing), which you already described conceptually on the call. Make this an explicit deliverable, not an assumption.

Access, specifically: Emily's line — "I'm not sure that we want [write-back]" — is IT signaling resistance to the AI creating anything in Dynamics without a human clicking submit. Your human-in-the-loop design already satisfies this, but say so explicitly and early in the security doc, because it's likely the first question their CIO's team asks.

Pricing — the math, and where it breaks

Implementation: $40-60K is priced like the full second-brain-adjacent engagements (Sabre, prior IMS anchor), not like a scoped single-agent build. For comparison, IMS Metals — after the DIY objection surfaced — settled into an $8K feasibility gate as the actual entry point, with the bigger number gone. Given Bossard's approval chain alone will slow this down, I'd think hard about a smaller Phase 1 feasibility fee (data-matching proof against their real dirty data + security sign-off) rather than asking them to commit $40-60K before you've proven matching accuracy against their actual product master. Lower commitment, faster yes, and it directly defuses the "why not build it ourselves" question by giving them a cheap, fast way to see it work before they're financially or politically committed.

Monthly flat fee: $3K is in line with your other SaaS-fee anchors (Sabre, prior IMS number), fine as a baseline platform/maintenance fee. Just be clear internally that it's not the deal — it isn't.

Per-quote/per-line: this is where I'd slow down. You told them "$4 per quote" on the call, flat, no caveats, in response to a direct ask for a ballpark. Introducing a 5-line cap and $0.75/line overage now is a real number relative to what they heard, and it lands hardest on exactly the segment Lucas described as their growth trend — 100-500 line packages replacing smaller ones. Run the math: at ~150 lines, one package quote is $4 + 145 × $0.75 = ~$113. If a meaningful share of their "new business" volume looks like Tyler's 400-500 line packages, per-quote cost balloons well past what a flat-fee mental model suggests, and it taxes their biggest, most strategic wins the hardest — which cuts against the "we help you win the big packages faster" pitch.

Also worth noting: nobody on that call could actually produce a real quotes/month number. Emily punted to Power BI twice and never got one. Pricing the entire model off "quotes/month" — a metric they can't currently report — is fragile. I'd model this in package-size tiers instead (e.g., flat rate for ≤10 lines, a mid-tier flat rate for 11-50, a large-package flat rate for 51-500) rather than uncapped linear per-line, so their finance team can model total spend without a spreadsheet, and so you're not the vendor whose bill spikes exactly when they win a big deal.

Suggested phasing

Given the CIO gate is the real bottleneck, not the build itself:

Phase 1 — feasibility + access: small fixed fee (think IMS's $8K, not a slice of $40-60K), data-matching proof against a real product master sample, security/IAM/SSO documentation delivered, CIO sign-off obtained. This is the gate everything else depends on and shouldn't be bundled into a big upfront number.

Phase 2 — core agent: email parsing, SKU matching with confidence thresholds, quote draft creation in Dynamics, salesperson approval workflow. Known-SKU path only.

Phase 3 — pricing matrix + inventory integration, plus a decision on whether the new-part/RFQ-triage path is in v1 or a phase 2 upsell.

Phase 4 — rollout: training across the buying team and however much of the 150-person sales org gets access, support handoff, first-cycle tuning of the SKU-matching model.

What should be explicitly included

- Named support contact and a defined SLA — this sits in a daily sales workflow, "email us and wait" isn't going to fly with an org this size
- Monthly/quarterly usage reporting — quote volume, matching accuracy, time saved — this hands their team the exact ROI data they'll need to defend the spend internally, and reuses the $22M/5,000-hour framing they already built themselves
- Security and compliance package as a real deliverable: IAM/SSO approach, data residency (worth citing your Anthropic ZDR certification here — real asset, not marketing), audit logging on every AI-drafted quote
- Explicit exclusions in the SOW: blanket/replenishment orders (Amy was clear these carry no quote), vendor-side RFQ automation (unless it's formally in scope), no customer-facing send without human approval
- A defined cadence for curating the "screw X = Tom" learning loop — that's real ongoing work, not a free background feature, and should sit inside the monthly fee explicitly rather than being assumed
- The Dynamics line-item-attachment fix called out as a named dependency with a target date — it's their Dynamics partner's work, not yours, but the whole thing stalls without it

What's still open before this is proposal-ready

- Reconcile the pricing anchor discrepancy above
- Get Emily's actual quote-volume and line-count distribution (the Power BI pull she never completed) before locking per-quote/per-line numbers — right now that pricing is built on a live guess Raj made on the call, not their data
- Confirm whether "next Wednesday" was Aug 5 or Aug 12 — this sets how fast the docs need to land
- Decide v1 scope on the new-part path now, since it's a deal-shaping decision, not a detail
- Get the product master sample and Dynamics quoting demo Emily promised, so matching-feasibility is validated before you commit to a fixed price on Phase 1

User: you are talking too much.

Assistant: Noted — I'll cut the padding. What do you want next: numbers finalized, or something else?

User: show me a framwork for the proposal. what are we proposing.

Assistant: What we're proposing: Smart Quote AI Assist — a Dynamics-embedded agent that reads inbound RFQ emails, matches to SKU, pulls pricing + inventory, drafts the quote inside Dynamics, and routes it to the salesperson for one-click approval before anything goes to the customer. No second brain, no separate front end. Known-SKU path is the v1 core — new-part RFQ triage is still an open call.

Proposal doc framework:

1. Problem — their own numbers: 45-day new-part cycle, manual spreadsheet quoting past ~5-line RFQs, $22M leakage, ~5,000 hrs/year
2. What we're proposing — Smart Quote AI Assist definition + workflow: email in → SKU match/flag → pricing + inventory pull → quote drafted in Dynamics → salesperson approves → sent
3. Scope boundaries — explicitly excluded: blanket/replenishment orders, no auto-send without approval, vendor RFQ automation (unless you decide to include it)
4. Delivery plan — 4 phases: feasibility/access → core agent → pricing+inventory integration → rollout/training
5. Security & access — IAM/SSO, audit log per quote, ZDR cert, read-only + human-approved writes only
6. Pricing — phased implementation fee, flat monthly, per-quote (package-tiered, not raw per-line)
7. What's included — support SLA, usage reporting, onboarding, ongoing model-tuning/curation
8. Dependencies — Dynamics line-item attachment fix, owned by their Dynamics partner, named with a target date
9. Next steps — timeline to their exec meeting

Two decisions still open before this locks: new-part RFQ triage in v1 or not, and per-quote priced as package tiers or straight per-line.
