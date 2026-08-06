---
thread_name: "bossard-call-review"
user: "raj"
type: claude-chat
created: 2026-08-05
updated: 2026-08-06
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

User: Build a council that will help us execute this task perfectly. And just don't build a bunch of AI's in this council. Think what kind of people would be required for this task, and there is a lot of intelligence and literature available for those people. The goal is to give them a proper email with a proposal that is clear and crisp.
On the surface, I have two ideas. At this point, I don't think it would make sense for us to build a second brain for them. It is going to be a lot of work and would require a lot of accesses directly on their dynamics and send the salesperson a copy of the code. We can inject pricing structures if they have a set pricing matrix, and we can even look at available inventory for the items in that email. Basically, this acts more like a quoting AI assist.

do a 50ft deep analysis. take your time.. take it step by step. 
i simple email explaining the path we will take and why. , with a 1 page proposal in pdf. 


Ask me as many questions you have , to help me build this email and pdf. dont function with any ambiguity . 

Assistant: Moving into Council mode.

Five seats for this task, each grounded in a real discipline you can pressure-test me on — not generic AI labels:

1. Category positioning strategist — Dunford's "Obviously Awesome" school: competitive alternatives, unique value, right buying committee. Job here: stop this from reading as a feature list and make it read as an obvious, different path than what Bossard already has.
2. Dynamics 365 solutions architect — keeps every technical claim honest. Job: define exactly what "read pricing/inventory, no write-back" actually requires from Bossard's environment, so we don't oversell "no access needed" when it isn't literally true.
3. Enterprise IT governance advisor — the same lens Bossard's CIO process will apply. Job: pre-empt the IAM/SSO/audit/data-residency questions before they're asked, using least-privilege design as the selling point, not an afterthought.
4. Pricing/packaging strategist — MEDDIC-style rigor on the numbers. Job: make sure the ROI story matches the actual scope of what's being sold, not the bigger vision's numbers.
5. Executive proposal writer — job: the actual 1-pager and email, written for a CEO/VP Sales reader in under 90 seconds.

I'm the sixth seat — facilitator, and the one pushing back on you, not just synthesizing what you already believe.

What the council found, verified against the transcript and current CRM state:

The strongest argument for your pivot: Emily said on the call, unprompted, that Bossard's global IT would likely push back on AI "creating things and doing things" — write-back — and that logging and audit visibility matter to them. You're not just simplifying the build for yourself. You're removing the exact objection their own buying committee already raised before you offered anything. That's the headline of the "why this path" section, not a footnote.

Two blind spots that change what you promise, not just what you build:

First — the core bottleneck Amy named first, before anyone else spoke, was waiting on vendor quotes: "we send it to our vendors, we have to wait for them to quote it first." A pricing-matrix-plus-inventory assist solves the estimation half of that — a fast, confident number for parts you've quoted before. It doesn't touch the sourcing half for anything without pricing precedent. If the proposal implies this kills the 45-day cycle across the board, a technically literate committee — the same one that already interrogated its own $22M number live on the call — will catch the gap. Scope the claim to known/precedented parts explicitly.

Second — inventory. Bossard told you directly they don't manufacture and operate largely as a vendor pass-through ("we don't make anything... we're the middleman"), with buyouts triggered when they don't hold stock. "Check available inventory" may apply to a minority of what they actually quote. I need to know whether you mean literal stock-on-hand, or negotiated cost/pricing history per SKU — different data source, different sentence in the 1-pager.

Third, a numbers-integrity issue: Lucas already called your $22M figure "pie in the sky" on the call, live, unprompted. That number was pitched against the full vision — an agent creating quotes directly in Dynamics. This is a narrower, read-only, salesperson-still-acts tool. Reusing $22M / 5,000 hours here isn't optimistic, it's numbers for a different product. The proposal needs its own conservative estimate — time saved per quote on research and estimation, not full quote creation — or it walks straight into the skepticism this committee already showed it has.

Fourth — access framing. "Avoid a lot of accesses" is directionally right but not literally true. Reading pricing and inventory data out of Dynamics still requires API/data access and still hits Bossard's CIO approval queue, just a smaller version of it. Say "read-only, no write-back, reduced access surface" in the proposal, not "no integration." Emily's team will ask the IAM/SSO/audit questions regardless of footprint size — better to answer pre-emptively than get caught softening the framing later.

Fifth — deal hygiene, outside the proposal itself: I checked EOXS Teams Live. Bossard has zero footprint — no CRM lead, no contact record — despite a 95-minute call with six people including a CEO/VP-Sales-sponsored working group. Get it logged regardless of what happens with this document; right now nothing tracks this deal if you get pulled onto something else this week.

Two things I'm not blocking on, just flagging as assumptions: pricing — I'll keep the $4/quote reference loosely in play and note in the proposal that final pricing follows their data confirmation, unless you say otherwise. Timing — get someone to confirm "next Wednesday" with Emily directly; I'll draft against the tighter read since a wrong assumption there costs more than a right one.

Three decisions actually change what I write, so I need them before drafting the email and PDF: [asked via interactive question card] (1) Which entity/brand should this proposal represent — EOXS as introduced on the call, AskCruz repositioned as the AI product line, or Claude's recommendation? (2) Should the pitch stay fully read-only/zero write-back into Dynamics, keep the option to create a pending draft quote in Dynamics for approval, offer both as phased options, or defer to Claude's recommendation? (3) Should the 1-pager present this as a standalone lightweight product, explicitly frame it as Phase 1 of the bigger company-brain vision, or defer to Claude's recommendation?
