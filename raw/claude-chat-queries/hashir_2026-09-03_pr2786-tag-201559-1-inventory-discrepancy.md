---
thread_name: "pr2786-tag-201559-1-inventory-discrepancy"
user: "hashir"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

User: [Uploaded screenshot of Odoo Processing Orders / PR2786, showing chatter notes:
"Note by Humaira - 18 hours ago: Hi @Ernie - We are looking into it, we'll provide you with an update within the next hour. @Tye W."
"Note by Ernie - 19 hours ago: @EOXS Support @Tye W. RE: tag 201559-1 coming into this process, tag was assigned at 120 x 193.5; then the restock was a leg 29 x 64 L 14 x 56. Then the other process on this order uses up the leg. How can 201559-1 still show available in stock as 120 x 193.5? Looks like this whole plate has been used up, need to remove, but want to know how it happened."]

Could you please provide me like the response that I should give on this particular ticket? And I am trying to understand why this app happening, but since this has been very long before data, like, one year ago data, so we need to fetch all the information and that will take... for for now now, we have corrected this and that control tag is now marked as zero in the inventory. Even the weight of overall is also also zero. This is a control completely utilized in this processing order. So we need to tell them, I am also attaching you the screenshot. Please go through that and then provide me a proper response, which I can provide them so that they can have the assured that we are looking into this, and we will be providing them the proper explanation why this has happened.

Assistant: Two things here are separate tasks and pull different skills: drafting the ticket reply is customer-support:draft-response; digging into why tag 201559-1 showed 120 x 193.5 in stock after being consumed is an eoxs-data-general / eoxs-teams investigation. I'll do the first now since you've already given me the facts; the second needs an actual data investigation.

**Ticket reply (note on PR2786)**

Hi @Ernie, @Tye W. — thanks for flagging this.

You're right: tag 201559-1 was showing 120 x 193.5 as available even though it had already been fully consumed — the restock split it into a leg (29 x 64, L14 x 56), and that leg was then used up by the other process on this order, but the original tag's inventory wasn't zeroed out at that point.

We've corrected this now: tag 201559-1 is set to zero quantity and zero weight in inventory, since it was completely utilized in this processing order.

This traces back to data from roughly a year ago, so we're still tracing the exact step where the zeroing was missed. We'll follow up with the specific root cause once we've gone through the history.

Let me know if you want this shorter, or want the internal explanation split out separately from the customer-facing part.

Now for the actual root-cause investigation — how deep do you want it:

5ft — quick: pull the order/tag movement history from eoxs-teams as-is, summarize what the records show.
10ft — verified: same, but cross-check tag movements against the restock/leg records and processing order history before reporting.
50ft — deep: full trace of tag 201559-1's lifecycle across processes, flag whether this is a one-off or a pattern (other tags with the same stale-quantity issue), sourced.
100ft — staged: same as 50ft but delivered in sections (e.g. tag history, restock/leg trace, root cause, exposure check) one at a time.

Which level?
