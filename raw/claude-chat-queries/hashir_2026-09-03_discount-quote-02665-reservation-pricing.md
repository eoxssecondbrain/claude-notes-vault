---
thread_name: "discount-quote-02665-reservation-pricing"
user: "hashir"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

User: Can you pull more information regarding the issue raised by discount team members and i need the next steps which i should perform in order to get this ticket closed.

User: Can you pull more information regarding the issue raised by discount team members and i need the next steps which i should perform in order to get this ticket closed. The name of the ticket is this :- Quote -02665 - Jeff Martin - Upton, Kentucky

Assistant: Ticket: Quote -02665 - Jeff Martin - Upton, Kentucky (Discount Pipe & Steel, sale_order id 2681, draft, $270.64, single line item, created 2026-09-02).

What was raised

Lacee Hulsey (Discount Pipe & Steel) posted an internal note on this SO on 2026-09-02, tagging EOXS Support, Ron, and Zana Williams: since the recent reservation-system update, they can no longer "fudge the numbers" to get the correct price on auction-sourced material. Their workflow: an auction seller quotes one price for a whole bundle, not per unit, and DPS was manually overriding line prices to reflect that. The new reservation logic blocks that override. She's asking how to proceed with auction sales going forward.

Diagnosis

This is not a bug ticket, it's a workflow gap. The reservation change is working as designed — it just didn't account for DPS's auction-bundle pricing pattern. There's an unconfirmed link to Azra Saleem's reservation QA work for Discount Pipe & Steel running through late August into early September — timing lines up but the connection isn't verified in any thread.

Status: as of 2026-09-02, no reply has been sent to Lacee from EOXS Support or Ron. No implementation task has been opened for this yet (I checked — nothing in the Discount Kanban board references it).

Next steps to close this

1. Confirm which reservation update she's referring to. Check with Azra Saleem or whoever owns the reservation function change to verify this is the same update she's been QA-testing, and confirm it's intentional (not a regression).
2. Define the supported workaround for auction-bundle pricing under the new logic — e.g. a bundle/kit product, an allowed manual price-override path, or a discount-field approach that doesn't trip the reservation block. This needs a decision from whoever owns pricing/reservation logic, not just a support reply.
3. Reply to Lacee on the SO chatter with that answer. This is the open item — nobody has responded yet.
4. If the answer requires an actual product change (not just a documented workaround), open an implementation task on the Discount board so it's tracked — right now this issue exists only as an email thread.

Given no response is logged yet, step 3 is the blocker for closing this ticket.

User: So usually what they do is sell there items in auctions also , and in that they sell the item in terms of bundle or something i am not sure, might be possible she is referring that situation, still i need more context to the same and then provide her a proper solution on this.

Assistant: Good context now. Here's the fuller picture.

This isn't a new problem — it's an old, tolerated workaround that just got closed off.

Background

DPS regularly buys steel at auction. Auction sellers price the entire lot as one lump sum for a bundle, not per piece. Odoo, by default, needs a price per line item. DPS's only way to reconcile that has been to manually re-type/override the price on each sale order line after creation so the totals add up to what they actually paid — that's what Lacee means by "fudge the numbers."

This has been a known gap for over a year, never actually fixed:

Oct 2025 (ticket T05124, Quote-00585, Brinkley Auctions): DPS explicitly asked for the ability to manually override per-line total cost for auction sales that don't price by foot or pound. Never built into a real feature — they kept doing it manually.

March 2026 (implementation task 30516, "Updated Auction SO Process," owner Amy Rayzor): DPS formally requested a proper workflow — select control tags in Inventory, click an action to auto-create the SO, then adjust prices. Status: still sitting in "Requirement" stage, never scoped or priced. Zero dev activity in 8+ months.

By contrast, its sibling request (task 30517, "Auction Transfer Action Menu Item," same batch, same day) did get built, priced, and shipped in April 2026 — that's the tag-select-to-Transfer flow. Only the SO/pricing half of the auction workflow was left undone.

So DPS has never had a supported way to allocate a lump-sum auction price across line items. They've been doing it by hand for over a year, and the September reservation update (the one Azra Saleem has been QA-testing through Aug–Sep) now blocks that manual override — almost certainly a side effect of the reservation logic locking line fields once tags are reserved against them, not something aimed at auction pricing specifically.

What this means for a real answer to Lacee

Telling her "here's a workaround" isn't really available anymore — the thing she's asking for a substitute for was itself a workaround, and it's now blocked. The actual fix is the feature that's been sitting unbuilt since March: task 30516.

Recommended next steps

1. Reply on the SO thread acknowledging this is a known, longstanding gap (reference T05124 and task 30516 so she sees it's not being treated as new), and explain the block is a side effect of the reservation update protecting reservation integrity, not a bug that will be reverted.
2. Get task 30516 actually scoped. It's been untouched since March. This ticket is the forcing function to get Ron/dev to price it out the way 30517 was — that's the only path to a real supported auction-pricing workflow.
3. Check for a safe interim option before 30516 ships — ask whoever owns the reservation change (Azra Saleem / the dev who built it) whether there's a controlled way to adjust price post-reservation (e.g., a discount field, or an admin-only override) without reopening the reservation bug this update was meant to fix. Don't just tell DPS to keep manually editing prices if that's the exact thing the update was designed to stop.
4. Loop Ron in — he owns pricing/scoping conversations with DPS and ran the 30517 process, so he's the right person to quote and move 30516 forward.

I don't have visibility into exactly which field/mechanism the reservation update locks (price_unit vs. something reservation-specific) — that needs someone with sandbox access to reproduce it against Quote-02665 directly.
