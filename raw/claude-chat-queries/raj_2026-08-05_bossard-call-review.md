---
thread_name: "bossard-call-review"
user: "raj"
type: claude-chat
created: 2026-08-05
updated: 2026-08-05
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
