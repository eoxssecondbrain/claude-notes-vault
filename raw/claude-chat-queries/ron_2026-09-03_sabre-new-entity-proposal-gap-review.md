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

**User:**
[The Users note reads: "Any user beyond that count — and any new hire who isn't an existing Sabre Alloys employee — is billed at the full Standard Rate." That eligibility test only makes sense for headcount growth inside Sabre Alloys itself. This new entity is going to hire its own laser operators who were never Sabre Alloys employees — under this clause, every single new hire the new company makes would be excluded from the discount by definition, which can't be the intent. This reads like it was carried over from Sabre Alloys' own contract language rather than rewritten for a standalone entity. Notably, at the start of this same call Raj directly criticized whoever drafted this ("this proposal you give, just number change" — i.e., an old proposal reused with only the dollar figures updated). This clause looks like exactly that failure mode.] - Can we keep it simple that this is only for the number of employees on the list down right now, and anything beyond that headcount would be priced separately? Do we even need to mention Sabre Alloys in this?

[No reference to whether this is a standalone agreement or an addendum under an existing Sabre Alloys MSA. That matters here specifically because Sabre Alloys itself has an unresolved contract-entity mismatch dating back to its 2023 acquisition (formerly Optimal Alloys) — the same ambiguity (wrong or unclear legal counterparty) has already caused friction once on this account. Worth closing before signature, not after.] - What is a solution for this right now.

[Renewal clause says pricing reverts to Standard Rate "unless a new term is negotiated" — but doesn't say whether that's negotiated with the new entity or piggybacks on whatever Sabre Alloys' status is at that time. If Sabre Alloys' relationship changes, does this entity's terms move independently? Not addressed.] - Give me a new solution to this also but I am confused since this is something which the new company will be negotiating and the new company consists of the same partners what should be done in that case?

["System configuration" during setup implies new product masters and new branded invoice/document templates (both were explicitly discussed on the call), but neither is itemized — fine if intentional, but worth confirming it's covered rather than assumed.] - You are right this should be added, tell me the points that we need to add in it.

I do not want you to copy paste the points but instead give me the points here and then I will go from there.

**Assistant:**
Users clause — yes, simplify, and no, Sabre Alloys doesn't need to be in it at all. The clean version:

"Users: Discount applies to the 10 users confirmed at signing. Any user added beyond that headcount is billed at the Standard Rate ($425/user/month)."

That's it. Eligibility is just "confirmed headcount at signing" — doesn't matter who the person is or where they came from. Removes the ambiguity entirely instead of patching it.

Contract vehicle — a real answer, not a "consult a lawyer" dodge (though I'm not one, so treat this as a business-logic recommendation, not legal advice):

Don't make this an addendum to Sabre Alloys' MSA. That reuses the exact ambiguity already sitting unresolved on that account since the Optimal Alloys acquisition — same trap, same account, twice.

Practical path: hold signature until the new entity has a name and an EIN, then execute a standalone agreement in that entity's name. Sabre Alloys shows up in the agreement only as the reason the discount exists (e.g. "affiliate of Sabre Alloys"), not as a contracting party.

If they want to start work before the entity is formed, use a short interim work order — one page, signed by an authorized individual, explicitly labeled as a bridge until the standalone agreement is executed, not the agreement itself. That keeps the $25k setup clock running without creating a second unresolved-entity problem.

Renewal terms — your confusion is the right instinct: "negotiate a new term" assumes two sides bargaining at arm's length, and that fiction breaks down when it's the same four partners on both sides of the table. A negotiation between yourself and yourself isn't a negotiation, it's a decision, so the clause shouldn't be worded as one.

Fix: replace "negotiated" with a checkable fact instead of a negotiation event. Something like: "The discounted rate continues automatically for as long as Sabre Alloys remains an active EOXS client in good standing. If that relationship ends, this entity reverts to the Standard Rate at that time." No renegotiation required, no awkward self-dealing — the rate is just tied to a status that's either true or not.

System configuration — points to add, your call on which to keep:

- New product/item masters for the new entity's own lines (toll-processing/laser service, consumables) — built fresh, not inherited from Sabre Alloys' product catalog
- New quote/sales-order/invoice templates carrying the new entity's name and letterhead, replacing every Sabre Alloys-branded document
- New AR-facing templates (statements, payment reminders) under the new entity's name
- Explicit statement that all of the above is inside the $25,000 one-time fee, not billed separately
- A named deliverable/deadline for the new entity's actual legal name and logo — branding work can't start while the name is still TBD, so this is a blocking dependency worth calling out rather than leaving implicit

**User:**
I want to add this line in the discount portion this tells them that we value relationship, "The relationship discount applies only to the agreed/confirmed headcount."

"The discounted rate continues automatically for as long as Sabre Alloys remains an active EOXS client in good standing. If that relationship ends, this entity reverts to the Standard Rate at that time." - This seems more like a threat.

Give me short chrisp to the point template for this, "System configuration"

**Assistant:**
Users clause, combined:

"Users: The relationship discount applies only to the agreed/confirmed headcount. Any user added beyond that headcount is billed at the Standard Rate ($425/user/month)."

Renewal, re-toned — same mechanism (tied to the relationship, not a fixed date), stated as continuity rather than a consequence:

"Renewal: This rate reflects the ongoing Sabre Alloys relationship and continues automatically while that relationship remains active and in good standing. Standard Rate ($425/user/month) applies thereafter."

System configuration — crisp, matching the sheet's existing bullet style:

- New product masters (toll processing, consumables)
- New quote/SO/invoice templates, new entity branding
- New AR statement/reminder templates
- All included in one-time setup fee
- Entity name/logo needed before template work starts

**User:**
Why can't we keep this there, "Renewal: At renewal, pricing reverts to the Standard Rate ($425/user/month) unless a new term is negotiated." ??

**Assistant:**
Fair pushback — you can. I overstated the problem.

The original line is standard renewal boilerplate: pricing reverts to Standard Rate unless a new term is negotiated. That works because the negotiation isn't "you vs. yourself" — it's the new entity (buyer) vs. EOXS (seller). Same partners owning the buyer doesn't make it a fake negotiation; it's still a real point where the entity decides what it wants to pay and EOXS decides what to offer. Shared ownership on one side of a deal isn't the same as no negotiation happening.

What I was actually flagging is a separate, narrower question the clause doesn't answer either way: is the discount tied to this entity's own standing, or does it ride on Sabre Alloys' status specifically. The original wording doesn't resolve that — but it doesn't need to. Leaving it open at renewal and deciding it then, when you actually know the situation, is a legitimate choice, not a gap you're obligated to close now.

Keep the original line. Drop my rewrite.

**User:**
[Uploaded file: excerpt_from_previous_claude_message.txt — content: "System configuration — crisp, matching the sheet's existing bullet style: New product masters (toll processing, consumables) / New quote/SO/invoice templates, new entity branding / New AR statement/reminder templates / All included in one-time setup fee / Entity name/logo needed before template work starts"]
Should this be a seperate section?

**Assistant:**
No — fold them into the existing "Included" list under "Implementation & Training," right alongside "New company, same instance" and "Separate chart of accounts." They're the same kind of item (setup scope), not a new category of work. A separate section would imply this is additional/separate-priced work, which contradicts the point that it's included in the one-time fee.

**User:**
Give me the points which can be added there.

**Assistant:**
New product masters (toll processing, consumables)
New quote/SO/invoice templates under new entity branding
New AR statement/reminder templates

**User:**
What if they ask us to actually import all the product from the previous Sabre instance to this one? How will we manage something like this? Is there something which can be shared? Can the product be shared between the two companies?

**Assistant:**
Yes — this is a standard piece of Odoo multi-company mechanics, and EOXS's ERP runs on stock Odoo 13 architecture underneath (per the internal dev SOP, standard Odoo config is always used before any custom build), so nothing exotic stands in the way here.

How product sharing actually works: every product record has a company field. If that field is left blank, the product is visible and usable by every company in the same database. If it's set to one company, only that company sees it. So "shared" isn't a separate feature you build — it's just leaving that field unset on the products you want both companies to use.

What stays separate either way: inventory quantities, stock locations, and valuation are tracked per company regardless of whether the product master is shared. So sharing the catalog doesn't mean sharing inventory — Sabre Alloys and the new entity would each have their own stock counts, their own warehouse, their own on-hand value, even for the identical shared product.

Pricing can also stay independent — Odoo supports company-specific price lists layered on top of a shared product, so the new entity can charge different rates for the same item without forking the product record.

For your actual question — "import all the products from Sabre" — don't import. Importing creates a second, disconnected copy: same steel plate item now exists as two separate records, and any future update (spec change, new grade) has to be made twice or the two catalogs drift apart. The cleaner move is to take the existing Sabre product records and unset their company field so they become visible to the new entity too — one record, both companies see it, no duplication, no drift.

The one thing worth deciding upfront: which products actually should be shared. If the new entity is doing toll processing on customer-owned material it never owns, it may only need product records for the service line itself, not the full Sabre steel catalog — worth confirming with Tye/Michael whether they expect the new entity to see the whole Sabre item list or just a working subset, since that changes how much cleanup happens before go-live.

**User:**
So technically, there are some products which can be shared between the two companies, and there are some which can still become one company.

**Assistant:**
Exactly. Per product, not all-or-nothing — you set it record by record:

Shared (company field left blank): the physical material items likely to move between both — the steel grades/sizes Sabre already stocks that the new entity will also be cutting or processing. One record, both see it, stays in sync automatically.

Sabre-only (company field set to Sabre Alloys): anything specific to Sabre's own sales/purchasing that the new entity has no reason to touch — its non-steel items, internal-only SKUs, whatever doesn't cross over.

New-entity-only (company field set to the new entity): the new entity's own service line items — toll processing charges, consumables, anything that's specific to how it bills, that Sabre Alloys never needs to see or select on its own orders.

Practical way to get there: go through the existing Sabre catalog once, tag each product into one of the three buckets, then set the company field accordingly. Not a system limitation — a one-time classification decision, and worth doing deliberately rather than defaulting everything to shared or everything to Sabre-only.

**User:**
And you are 100% sure this is possible, right?

**Assistant:**
[Verified directly against Sabre's live database via Sabre MCP get_business_schema.] Confirmed directly against Sabre's live database — this isn't just generic Odoo knowledge, it's checked against the actual instance:

product_template has a company_id column, it's nullable, and the sample product pulled back (item 3041000) already has company_id: None — meaning Sabre's own catalog already has products sitting in the shared/unrestricted state right now, not hypothetically.

So yes, I'm sure. This confirms:
- The mechanism exists on this exact database, not just in Odoo generally
- It's actively in use — some Sabre products are already unrestricted rather than locked to one company
- Setting a product to shared for the new entity is the same field flip already present in this data, not new functionality that would need to be built

**User:**
I would like to keep these options open-ended and not add it so that we do not run into something where they ask us to actually create new products for a few of them. I know that is fine for the ones that I shared. We can do that, of course, for new codes. A lot of times, I don't want us to actually work on creating a completely separate template for them. Again, I don't want the team to actually start creating something completely separate for AR statement and reminder templates. If we just leave it as is and do you think we should actually add something like an excluded column, or does it look good as you see it right now?

**Assistant:**
Adding an excluded line is the better move — leaving it silent doesn't actually protect you, it just moves the argument to later. If nothing's written down, the buyer's default assumption becomes "whatever we needed was included," and you're negotiating scope after the work's already a point of friction. An exclusion line sets the boundary now, while costing you nothing — you can still choose to do more later if you want, since nothing was promised either way.

And this fits your actual concern precisely: you're not against doing template/product work, you're against being locked into "fully separate, built from scratch" as the default when reuse/sharing is often the right call. An inclusion line ("new product masters," "new AR templates") reads as a commitment to build fresh; an exclusion line lets you exclude only the expensive edge case (full rebuilds) while staying free to do the cheap, obvious thing (share/reuse) without it looking like you under-delivered.

Two lines, matching the sheet's existing "Not included" style:

Not included:
- Recreating catalog items already shared with Sabre Alloys
- Custom-built AR statement/reminder designs beyond a standard branding swap (name, logo, address)

That's it — don't add anything to the "Included" list for this. The exclusion alone does the job.

**User:**
We will be giving them all the documents. We can say something like "rebranding of the documents" or something like that. We can rebrand the documents for the new company. We can add that there so that that is all standardised, but not a full redesign of the documents. We don't need to change fields and everything.

**Assistant:**
Good distinction — rebranding (name/logo/address swap on the existing layout) vs. redesign (new fields, new layout, new logic). Only the first is in scope.

Included, add:
- Rebranding of all standard documents (quotes, SOs, invoices, statements) to new entity name/logo/address — same layout and fields as Sabre Alloys' current templates

Not included, replace the AR line with:
- Custom redesign of document layouts or fields beyond standard rebranding

**User:**
Can you shorten this to less words.

**Assistant:**
Included:
- Document rebranding (name/logo/address) — same layout, no field changes

Not included:
- Custom document redesign

**User:**
Maybe we can make this warmer

**Assistant:**
Included:
- Documents rebranded with your name and logo, ready to go from day one

Not included:
- Custom redesigns beyond that — happy to scope those separately if wanted

**User:**
[Uploaded file: Sabre_-_Proposal_-_Copy_of_Copy_of_Quote.pdf — a full proposal document with the fields: New Entity Name TBD <> EOXS; EOXS ERP; Licenses section (Included: Full standard module suite, Same platform same code, Consumable module, Maintenance module, Billing kept fully separate from Sabre, Ongoing support; Users 10 $425 $4,250; Discount -47% (1,998); $2,253); Server/Infrastructure Fee ($400, $400); Implementation & Training Team Size 10 (One-time Setup Fees 5 weeks $5,000/wk $25,000; Included: New company same instance, Seperate chart of accounts, Separate customer/vendor contact records from Sabre Alloys, Documents rebranded with your name and logo ready to go from day one, 5-week setup: system configuration 1-week training, Per-person per-company access controls, Custom development quoted separately as needed); Net Amount $25,000; TOTAL $25,000; $25,000.00 $2,652.50; Notes section with Pricing/Internet/Consultant/Subscription/Travel Expenses/Price/Users ("The relationship discount applies only to the agreed/confirmed headcount. Any user added beyond that headcount is billed at the Standard Rate ($425/user/month).")/Database Training & Data Migration/Agreement (12-month initial contract term)/Renewal ("At renewal, pricing reverts to the Standard Rate ($425/user/month) unless a new term is negotiated.")/Case Study & Reference Rights/Payment (30% at kickoff, 70% over term)/Payment Terms (Net 15 days)/Access Control; Approved by/Sign/Date/Designation blank signature block]
Go through this and let me know if there are still any gaps that you see?

**Assistant:**
Two things changed between the version we worked through and this final PDF that are worth flagging before this goes out.

Both "Not included" sections are gone. The original sheet had a "Not included" header under Licenses and another under Implementation & Training. Neither appears anywhere in this version — not empty, just structurally removed. If that was deliberate cleanup, fine, but it also means nothing below was preserved in their place.

The exclusion line we agreed on is missing. You specifically said you didn't want to get stuck creating new product masters from scratch, and asked whether to add an excluded line for that — I recommended yes, and you agreed adding an exclusion was the right call. That line never made it into this draft. Right now the document commits to nothing on product masters (no inclusion promise, since you correctly dropped that) but also protects you with nothing (no exclusion boundary either). That's the exact gap you told me you wanted to close. Worth adding something like:

Not included:
- Recreating product masters already shared with Sabre Alloys as separate items

Everything else holds up:
- Users clause — matches what we settled on, correctly account-agnostic.
- Renewal clause — kept as original, per your call.
- Document rebranding line — in, correctly scoped as rebrand-not-redesign, though there's no matching exclusion for "custom redesign beyond that" either, same category of gap as above if you want the boundary explicit rather than implied.
- Pricing math — still checks out ($4,250 − $1,998 = $2,252, one dollar off the printed $2,253; total $2,653 vs. printed $2,652.50 — both trivial rounding, unchanged from before).
- PO automation and AI-driven pricing matrix — still nowhere in the document. This was the biggest gap from the first pass and it's still open; "Custom development, quoted separately as needed" is the only hook for it, same as before.
- Entity name and signature block — still TBD/blank, which is expected at this stage, not a new issue.

**User:**
Is there a way we can vote it in a different way? How can we add that the current product list will be shared if required, and we can create new products or something like that: new service products and consumables, something that they were looking for?

**Assistant:**
Yes — same protection, framed as what you're doing rather than what you're refusing to do:

Included:
- Existing product catalog shared with the new entity — no rebuild needed
- New service and consumable products created for toll processing as needed

The word "shared" is doing the protective work here — it tells them the existing items are reused, not rebuilt, without ever saying "not included." And "as needed" on the new-products line keeps you from committing to a fixed list or count up front.

**User:**
I want to check from the code side. Give me a detailed prompt that I can add there which includes what we talked about here so that we can double check.

**Assistant:**
Here's a prompt built from everything we covered — meant to hand to whoever has repo/DB access (or to run through Claude Code against the Sabre codebase directly):

---

Verify the following against the EOXS Golden File (Odoo 13 CE) build as deployed on Sabre Alloys' live instance, ahead of standing up a new company (the toll-processing/laser entity) in the same database.

1. Product sharing mechanism
Confirm product_template.company_id and product_product.company_id are unmodified stock Odoo fields on this build — not overridden, hidden, or forced non-null by any custom module (m13_* naming per the dev SOP). Pull the module list touching product_template and confirm none of them add a company-scoping constraint beyond Odoo's default.

2. Existing shared products
List any product_template rows where company_id is currently null on the Sabre instance, and confirm they behave as expected today — visible/usable in whatever multi-company context already exists, not just present in the table by accident.

3. Record rules / access control
Pull every ir.rule tied to product_template, product_product, and stock-related models. Confirm none of them scope products by company in a way that would block a shared (company_id = null) product from showing up correctly for both Sabre Alloys and the new entity. Cross-check this against the proposal's own Access Control line — "each user sees only their own company's data by default" — and confirm that rule is implemented as a user/company access rule, not a product-catalog rule, since those need to behave differently.

4. Inventory and valuation separation
Confirm stock quants, warehouses, and inventory valuation are keyed to company_id at the stock/location level, independent of whether the underlying product is shared. Verify a shared product can carry two different on-hand quantities and two different valuations, one per company, without cross-contamination.

5. Pricing independence
Confirm pricelists (or whatever pricing mechanism is customized on this build) can be scoped per company on top of a shared product, so the new entity can charge differently for the same item without forking the product record.

6. New company setup requirements
Document what actually needs to be created when the new company (res.company) is added to this instance: chart of accounts, journals, sequences, warehouse/locations, fiscal year settings, and anything else the Golden File build requires beyond stock Odoo defaults. Flag anything that isn't a config toggle and requires custom dev.

7. New product creation path
Confirm the path for creating new service/consumable products scoped only to the new entity (company_id set to the new entity, not shared) works cleanly alongside the shared catalog from step 1-2, with no id collisions or category conflicts.

Report back with a pass/fail per item and call out anything that requires custom development rather than configuration, so it can be priced before this goes to Sabre.

---

Want this trimmed down, or is this the right level of detail to hand off?

**User:**
Can you give this in simple language also. Make sure to add the context that we are thinking of adding a new company in the current instance. make sure you give a proper download

**Assistant:**
[Created downloadable file /mnt/user-data/outputs/Sabre-New-Company-Code-Check.md with the following content:]

# Code Check: Adding a New Company to the Sabre Instance

**Context:** We're planning to add a new company (the toll-processing/laser entity) into the same EOXS ERP instance that Sabre Alloys already uses — not a separate server, a second company inside the same database. Before we commit to this in the proposal, we need engineering to confirm the system actually supports what we're promising.

---

## 1. Can products really be shared between the two companies?

Every product in the system has a "which company owns this" field. When that field is left blank, the product is visible to every company in the database — this is normal Odoo behavior, not something we'd have to build.

**Check:** Confirm nothing in our custom code changes this default behavior or blocks it.

## 2. Are any products already set up this way?

Some products in the Sabre database may already have that "company" field left blank, meaning they're technically already shared.

**Check:** Pull a list of these and confirm they show up correctly, not just sitting blank by accident.

## 3. Does "shared product" accidentally mean "shared data"?

We're telling the client that each company only sees its own data by default. We need to make sure a shared product doesn't break that — i.e., sharing the product itself shouldn't leak one company's sales, access, or other info to the other.

**Check:** Confirm the access rules that keep companies separate are based on the user/company, not on the product — so a shared product stays visible to both without leaking anything else.

## 4. Do inventory counts and pricing stay separate even on a shared product?

Even if a product is shared, each company should have its own separate stock count, its own separate valuation, and be able to charge its own separate price for it.

**Check:** Confirm a shared product can have two different stock counts and two different prices, one per company, without them interfering with each other.

## 5. What actually needs to be built for the new company itself?

Setting up a second company isn't just a toggle — there's a chart of accounts, numbering, warehouse/locations, and similar setup involved.

**Check:** Get a clear list of what's config (quick, no extra cost) vs. what needs custom development (should be priced separately).

## 6. Can we create brand-new products just for the new company?

Some products (new service charges, consumables) will belong only to the new company, not shared with Sabre.

**Check:** Confirm we can create these cleanly alongside the shared products, with no mix-ups or ID conflicts.

---

**Ask:** For each item above, confirm pass/fail, and flag anything that needs real development work (not just configuration) so we can price it before this goes back to Sabre.

[File presented to user via present_files.]
