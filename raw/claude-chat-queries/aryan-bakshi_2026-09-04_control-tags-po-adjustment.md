---
thread_name: "control-tags-po-adjustment"
user: "aryan-bakshi"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: So I had an original purchase order for sixty control tags, but something happened and twelve of those control tags became zero after receiving. So what I want to do is make another receiving for only those twelve control tags. But for that to have the correct information, I need to have the unit price adjusted for the twelve twelve control tags. So the original sixty control tags had a unit price of one seven two zero metric tons. Victor twenty three point seven five inches, thickness of zero point zero one eight five and no m, with weight hundred metric ten. grade eighty So I have the weight of the twelfth control tags. I have the footage of twelfth control tags. How can I make a purchase order adjusted for this? adjust the metric ton adjusting unit price for this.

Assistant: This doesn't clearly fit either available skill (threads-ov is just for saving this conversation; eoxs-data-general covers correspondence/tickets/CRM, not PO/receiving calculations) — flagging that per your instruction, then proceeding since the underlying task is a straightforward calc question, not a lookup.

On the actual question: a few things are unclear before I can give you a real adjustment method, not a guess:

1. **Which instance is this PO in** — Discount, Greer, or Sabre? (I can pull the actual PO/receiving record read-only if you want me to check the real numbers instead of working from the dictation.)
2. **The 12 tags' actual weight and footage** — you said you have both, but the numbers weren't in your message. I need the actual figures to compute anything.
3. A few terms didn't transcribe cleanly and I don't want to guess wrong:
   - "Victor twenty three point seven five inches" — is this **width = 23.75"**?
   - "no m" — no idea what this field is (coating? finish? mill?). What was it?
   - "weight hundred metric ten" — is total order weight **100 MT** for all 60 tags, or something else?
4. Is $1,720 the unit price **per metric ton** in USD?
5. Core question on method: are you trying to (a) figure out a **$/MT price to key into the new receiving** so the extended value comes out correct given the actual weight/footage of the 12 differs from nominal, or (b) something else — e.g. the system won't let you receive at the original price because the theoretical vs actual weight variance is too large and it wants a recalculated per-ton or per-foot rate?

If it's (a): with unit pricing in $/MT, the total extended value is just `actual weight (MT) × unit price`. That's self-correcting for weight variance — you would NOT need to change the $1,720/MT rate at all unless your system is actually costing this by piece or by linear footage rather than by weight, in which case the "adjusted unit price" is really a footage-based or piece-based re-derivation of that $1,720/MT rate against the actual specs. That's a different formula depending on which basis your receiving screen uses.

Tell me the missing numbers and confirm the basis (weight-based vs footage-based receiving), and I'll give you the exact adjusted figure to enter.
