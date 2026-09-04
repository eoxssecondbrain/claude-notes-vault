---
thread_name: "sabre-proposal-quote-review"
user: "ron"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

Human: [Uploaded file: Sabre_2_-_Proposal_-_Quote.pdf — Sabre Alloys <> EOXS ERP proposal/quote: 10 users at $425/user with 47% discount ($2,253/mo subscription), $400/mo server fee, one-time implementation/training setup fee of $25,000 (5 weeks x $5,000, team size 8), 12-month initial contract term, Net 15 payment terms, 30% of setup fee due at kickoff with remaining 70% invoiced over contract term, renewal reverts to standard $425/user/month rate, per-person/per-company access control model.]

/small-business:contract-review

Assistant: I've read the Sabre Alloys quote/proposal. Quick context before diving in: this is EOXS's outgoing proposal to Sabre, not a third-party contract you're being asked to sign — it's an order form for ERP licensing plus implementation, not a full MSA. So most of the standard contract-review categories (liability caps, indemnification, IP assignment, non-compete, confidentiality) aren't addressed here at all, because this document type doesn't cover them. What it does cover: pricing/discount structure, payment terms, agreement term, renewal, and access control.

I'll review it from EOXS's side (protecting your company's interests as the party issuing this quote), flagging anything ambiguous, missing, or that could bite EOXS later, plus anything Sabre would likely push back on.

Before I dig in, pick a rigor level:

5ft quick — read the document as-is, flag what stands out, no cross-checking.

10ft verified — same, plus cross-check the numbers and terms against Sabre's account history in EOXS records (prior invoices, prior correspondence on this deal, whether these terms match what's typically offered).

50ft deep — verified, plus flag adjacent risks (how this compares to your other client agreements, anything that deviates from standard EOXS terms, blind spots in what's silent).

100ft staged — same as 50ft, delivered in sections.

It's a one-page quote, so even 50ft should move fast. Let me know which.

Human: 50ft

Assistant: Full review, sourced against EOXS's own records where it mattered.

Contract summary
EOXS proposes onboarding what the document calls "the new entity" — a second company distinct from Sabre Alloys, per the Access Control note ("Sabre staff and the new entity's staff each see only their own company's data by default"). 10 users at $425/user list, 47% discount, $2,253/month subscription, $400/month server fee, $25,000 one-time implementation (5 weeks, 8-person team), 12-month initial term, Net 15, 30% of setup due at kickoff with the remaining 70% invoiced over the term, renewal reverting to standard $425/user rate.

Red flags — fix before this goes out

1. The contracting entity is never actually named. The document's own access-control language confirms this is for a second company, not the existing Sabre Alloys account, but nowhere does it name that company, and there's a single undifferentiated signature block. I checked EOXS's own billing system (Teams.eoxs): no second/child contact exists yet under the Sabre Alloys commercial record, and no sales order has been created for this deal. This isn't a hypothetical concern — Sabre Alloys already has one unresolved contract-entity mismatch on file from the Optimal Alloys acquisition (Dec 2023), documented in your own wiki. Sending a second contract with the same ambiguity risks the same problem twice.

2. The 70% balance ($17,500) is "invoiced over the contract term" with no monthly figure or schedule. The original 2023 Sabre proposal had this same kind of vagueness, and it produced a real discrepancy on record: the proposal said $4,500/month, the actual invoices billed $5,000/month, and it took a wiki flag to even notice the mismatch. This account has a documented history of proposal-language-vs-actual-invoice drift — worth pinning down an exact number now.

Yellow flags — worth tightening

3. 47% is a much steeper discount than this same client got at original signing (20%, per the 2023 proposal on file), and your own Ideal Customer Profile notes specialty-alloy distributors like Sabre typically take premium per-seat pricing, not steep discounts. Not unprecedented for this account specifically — Raj gave Sabre a 75% discount on one line item last year — but worth confirming this is a deliberate call and not just a copied number, since it sets a new floor this relationship can point back to.

4. Implementation team size doubled (4 people in 2023 → 8 now) at the same $5,000/week rate. That halves the effective per-person-week rate ($1,250 → $625). If that's not explained by genuine reuse of Sabre Alloys' existing configuration (same steel-processing setup, less discovery work needed), it's quietly compressing implementation margin.

5. Server fee is $400/month here vs. $1,200/month currently paid by Sabre Alloys for its own infrastructure. That's consistent with the new entity riding on shared infrastructure rather than a standalone server, but worth confirming that's actually the intended architecture (see next point for why that matters).

Adjacent risk, not a clause problem but material

6. Sabre Alloys' EOXS-hosted environment is the subject of an active legal matter, as of September 1-2, 2026, over unauthorized access — an evidence package on a "hack incident" naming a defendant went to counsel this week. The Access Control clause in this quote is effectively promising the new entity that exact kind of thing won't happen to them. Before this goes to signature, worth a quick internal check that whatever allowed that access has actually been closed, especially if the new entity ends up sharing infrastructure with Sabre Alloys (point 5 above suggests it might).

7. Beyond that one incident, the existing Sabre Alloys account has a real reliability history: a separate Feb 2026 outage (settled at $25k credit + $1,000/month for 25 months), a stalled dual-server backup project, and ongoing inventory-valuation/AR-AP reconciliation issues. If the new entity shares that environment, it inherits that track record.

Key terms, for awareness
12-month initial term, standard Net 15, renewal reverts to full $425/user rate, 30/70 kickoff split, per-company data segregation as the stated access model.

What's simply not in this document (expected, given it's a quote/order form, not an MSA): liability caps, indemnification, IP terms, termination-for-cause, dispute resolution, insurance requirements. Nothing wrong with that for this document type — just don't assume they're covered anywhere else unless a separate MSA exists.

Want me to export a redlined version marking up 1, 2, and the entity-name gap specifically?

Human: THere are things that raj wanted to include in the proposal which was what is included and what is not included can you give me that list by getting that from OV?

Assistant: I searched eoxs-db thoroughly — wiki, emails, and calls — for an "included / not included" scope list tied to this specific quote, and came up empty. Here's exactly what I checked:

Wiki: searched for "Sabre included not included proposal scope," "What's Included / Not Included," and related terms across the Sabre Alloys pages. Nothing matched an inclusion/exclusion list for this deal.

Emails: searched for "Sabre new entity proposal Raj," "Sabre Steel Farmington laser proposal quote," and "Sabre multi-company setup Raj scope modules" (including scoped to raj_gmail). No hits.

Calls: searched for "new company included not included scope laser." The one Sabre-relevant hit (the Aug 11 Juan/Raj call) turned out to be entirely about inventory-aging reports, unrelated.

One thing worth flagging: the quote itself references "the proposal's Included list" as if it's a defined section, but that phrase may just be pointing back to the LICENSES/products table already at the top of the same document (Sales, Purchase, CRM, Inventory Management, etc.), not a separate included/excluded scope document. If that's all it means, there's nothing more to retrieve.

But if Raj actually laid out a separate included/not-included list somewhere, two likely places I haven't checked:

The Sabre Alloys account brief in Google Drive — your own notes mention contract terms and account notes live there, not in the wiki/email index. I can search Drive if you want.

The IRIS (AI/AskCruz) proposal for Sabre — that one does have documented scope back-and-forth in my notes (what's in vs. out of the flat monthly fee, support hours, etc.). If that's actually the proposal you mean rather than this ERP/new-entity quote, say so and I'll pull that instead.

Which of those is it — or something else?
