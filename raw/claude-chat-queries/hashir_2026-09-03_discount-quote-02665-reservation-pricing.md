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
