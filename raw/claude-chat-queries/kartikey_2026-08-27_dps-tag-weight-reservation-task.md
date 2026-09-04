---
thread_name: "dps-tag-weight-reservation-task"
user: "Kartikey"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

USER:
explain me this task "Reference:  S04384 (and SO4329)
Customer was packed out.  Put on tag, move it to received/delivered.  As soon as she moved it, it added a second Done quantity for the same tag # but with a different weight.  Turns out:  Weight on the control tag used was higher than the shipping weight on the SO, so we can see the system likely wants to do something with the excess weight.  (see email from Ron to Zana on 3/29 Re: BPT/OUT/03339)

* Weight is not a factor (today) for any shipping process except the effort to completely fill a tractor trailer load if at all possible when tractor trailer shipping is used for freight.
* When tractor trailer loads need to be filled, it is an internal need - nothing that goes on an invoice.  (Validate what may be needed for internal accounting / scrap calcs)
* For some sales, actual weight needs to be known when the sales order is being worked, so sellers will have to select specific tags. This is for when buyers are buying on weight and not length / pieces.
* Review the Reservation Function issue to ensure the processes align.  Ideally sellers do not select "

ASSISTANT:
## What this task is describing

This is the DPS (Discount Pipe & Steel) control-tag / weight-reservation bug — internally tracked as **task 9051 ("Actual Weight > Shipping Weight")** in the same cluster as their Reservation Function work. Cross-checked against EOXS wiki and email records:

- Task 9051 was filed, marked "not replicable" by Siddhant Pathak/Aryan Bakshi on 2026-05-06, tabled, then reopened 2026-07-01 after Humaira Zainab supplied logs. It was reassigned to **Dhrup** (your manager) with no confirmed root cause as of the last recorded event — so this ticket lands right in your team's queue, not a random assignment.
- The underlying weight-vs-quantity mismatch is the same design tension Ron/Kunal Chauhan flagged back in Oct 2025 (email "Build reservation functionality based on weight"): tags carry a weight, sale order lines/packing lists don't support decimal weights, so when a tag's actual weight exceeds what's on the SO, the system doesn't know what to do with the leftover and appears to spawn a second "Done" quantity line for the same tag at a different weight.

## The bug, in plain terms

1. SO4384 (and SO4329) — customer's material was packed and moved to received/delivered.
2. The control tag used had a higher actual weight than what the SO specified as the shipping weight.
3. The system responded by creating a second "Done" quantity entry for the same tag number, at the delta weight — instead of just marking it delivered once. So one tag is now generating two done-quantity records.
4. Root cause per Ron's email to Zana (3/29, re: BPT/OUT/03339): the system is trying to "do something" with the excess weight (tag weight minus SO shipping weight) rather than discarding or ignoring it, and that "something" is the duplicate line.

## The four requirements listed (what needs deciding/built)

1. Confirm weight is not used anywhere in the shipping/invoicing pipeline today — it only matters for maximizing trailer loads on freight shipments. This needs validating against internal accounting/scrap-calculation needs (i.e., don't just assume — check if Accounting relies on captured excess weight for scrap reconciliation).
2. Trailer-load-fill logic is purely internal — it must never leak onto a customer invoice. So whatever fix is built has to guarantee the duplicate/adjusted quantity stays internal-only.
3. Carve-out: for weight-sold (not length/piece-sold) customers, sellers do need to pick a specific tag by weight when building the SO — so any fix can't break that manual-tag-selection flow.
4. Tie this to the Reservation Function review — the goal is sellers shouldn't have to hand-pick tags at all (auto-reservation should handle it), so this bug and the reservation redesign are meant to be solved together, not patched separately. (The sentence is cut off in what you pasted — "Ideally sellers do not select" — worth getting the rest of that line from whoever wrote it.)

## Net read

This isn't a new discovery — it's a recurrence of a known, previously "not replicable" bug (9051) sitting inside a larger unresolved cluster (reservation reallocation, control-tag accuracy) that's been open since March 2026 and already burned ~7 weeks on a related delivered-quantity bug (9049). The open question isn't really "what's happening" (that's understood: weight overflow has nowhere to go), it's "what should happen to the excess weight" — and that's a product decision, not just a dev fix.

Want me to pull the full task 9051 chatter/history or the Reservation Function analysis page in full next?
