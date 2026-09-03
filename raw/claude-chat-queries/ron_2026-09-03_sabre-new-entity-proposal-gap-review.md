---
thread_name: "sabre-new-entity-proposal-gap-review"
user: "ron"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

**User:**
[Uploaded file: /mnt/user-data/uploads/Sabre_-_Proposal_-_Copy_of_Quote-3.csv]
Go through this proposal with a fine-tooth comb and find me gaps in what all is mentioned here.

**Assistant:**
This proposal doesn't cleanly map to an existing skill: sabre-account-strategist is built for relationship/strategy moves ("what should I do about Sabre"), not document completeness review, and there's no contract/quote-review skill loaded for EOXS's own outgoing proposals. I'll proceed as a straight gap analysis grounded in the Sabre account context already on file (this is the new-entity/multi-company proposal for Sabre's new laser-cutting business, per the account notes).

Before I dig in — this is an analysis task, so pick a rigor level:
[Asked via interactive options: 5ft deep (Quick), 10ft deep (Verified), 50ft deep (Deep)]

**User:**
[Selected] 50ft – Deep: verified + adjacent risks (multi-company/access, billing separation, renewal terms)

**Assistant:**
Verified against the Sep 2, 2026 call where this exact proposal was walked through line-by-line with Raj, Tye, Michael, and Dave, and against Sabre Alloys' live EOXS invoicing data. Bottom line: pricing math checks out, but the proposal is missing the two features the buyers actually cared about most, and it carries at least one clause that looks copy-pasted from an old template rather than rewritten for this entity — which is the exact failure mode Raj called out in that same call.

**Pricing and math — verified, no gaps**
- 10 users × $425 = $4,250; 47% discount = $1,998 off; net $2,252 vs. the sheet's $2,253 (rounding, immaterial).
- $425/user/month standard rate matches Sabre Alloys' actual current billing (confirmed on live invoices: 27–28 users billed at $425 each, no discount on Sabre's own account). So the 47% is a new concession being extended to the new entity specifically — it isn't something Sabre already has and is now just being copied forward. Worth knowing since it means this discount is a fresh commitment, not an inherited one.
- $25,000 one-time / 5-week timeline matches what was verbally quoted on the call.
- Monthly total ($2,253 + $400 server = $2,653) is $0.50 off the sheet's printed $2,652.50 — trivial, not worth fixing but technically a typo.

**The two features the buyers pushed hardest on aren't in the document at all**
This is the real gap. On the call, Michael repeatedly pressed for two things before agreeing to anything, and Raj confirmed both were possible but explicitly deferred building them ("we're putting the cart ahead of the horse"):
- Automated PO generation — a button on a Sabre sales order that auto-creates the corresponding PO to the new laser company, no manual entry.
- AI/formula-driven pricing on that auto-generated PO, based on Tye's production pricing matrix (dimensions, plate, per-square-inch formula).

Neither appears anywhere in the proposal — not priced, not scheduled, not even named as an exclusion. The only catch-all is "Custom development, quoted separately as needed" buried in the Included list, which is too generic to cover something this specific and this important to the buyer. If this ships to Michael and Tye as-is, the natural reading is "the $25k covers what we asked for," and the automation becomes a change order dispute later. This needs its own explicit line, even if it just says "automation and pricing-matrix integration: scoped and quoted separately, target timeline TBD."

**A clause that looks like leftover language from a different proposal**
The Users note reads: "Any user beyond that count — and any new hire who isn't an existing Sabre Alloys employee — is billed at the full Standard Rate." That eligibility test only makes sense for headcount growth inside Sabre Alloys itself. This new entity is going to hire its own laser operators who were never Sabre Alloys employees — under this clause, every single new hire the new company makes would be excluded from the discount by definition, which can't be the intent. This reads like it was carried over from Sabre Alloys' own contract language rather than rewritten for a standalone entity. Notably, at the start of this same call Raj directly criticized whoever drafted this ("this proposal you give, just number change" — i.e., an old proposal reused with only the dollar figures updated). This clause looks like exactly that failure mode.

**Contract vehicle / entity gaps**
- Entity name, and therefore the actual signing party, is still TBD — the signature block has no legal name, no EIN, nothing to actually execute against.
- No reference to whether this is a standalone agreement or an addendum under an existing Sabre Alloys MSA. That matters here specifically because Sabre Alloys itself has an unresolved contract-entity mismatch dating back to its 2023 acquisition (formerly Optimal Alloys) — the same ambiguity (wrong or unclear legal counterparty) has already caused friction once on this account. Worth closing before signature, not after.
- Renewal clause says pricing reverts to Standard Rate "unless a new term is negotiated" — but doesn't say whether that's negotiated with the new entity or piggybacks on whatever Sabre Alloys' status is at that time. If Sabre Alloys' relationship changes, does this entity's terms move independently? Not addressed.

**Smaller items**
- "System configuration" during setup implies new product masters and new branded invoice/document templates (both were explicitly discussed on the call), but neither is itemized — fine if intentional, but worth confirming it's covered rather than assumed.
- $400/month server fee for the new entity vs. Sabre Alloys' own recurring $1,200/month "Server Upgrade" line — different scope, possibly fine, but if the new company is running a laser machine with its own data/processing load, worth a gut-check that $400 isn't underpriced relative to what a comparable second instance actually costs to run.
- Payment terms (30/70 split, Net 15) weren't discussed on the call at all — presumably boilerplate from the template, not specific to this deal, but flagging since nothing in the call confirms the buyers agreed to those terms specifically.

If you want, I can turn the two missing-feature and copy-paste-clause items into redline comments directly on a copy of the sheet.
