---
thread_name: "sabre-alloys-landed-cost-email"
user: "raj"
type: claude-chat
created: 2026-08-18
updated: 2026-08-18
---

User: Tye / Michael, 
My understanding is that landing cost is working fine when you have one line item. Its breaking when you have 2 line items. Could be a glitch. Guys, we are swapped with this AI solution. A simple work around to this is to create 2 landed costs. Out of the 1900 landed costs we have less than 1% scenario when that happens. Its not the best use of the team to have to fix this. Can you please take care of it from your end. 

R. 

Christy sent me an email, and she tagged support where she is facing this challenge: she is not able to make the functionality work correctly if she adds two line items on one landed cost form. We tested it, and it is working perfectly fine with one landed cost. It does break when you enter two landed cost. This rarely happens when they enter two landed cost in one landed cost form. I was thinking of sending Tye and Michael this email. 

Tye / Michael, 
My understanding is that landing cost is working fine when you have one line item. Its breaking when you have 2 line items. Could be a glitch. Guys, we are swapped with this AI solution. A simple work around to this is to create 2 landed costs. Out of the 1900 landed costs we have less than 1% scenario when that happens. Its not the best use of the team to have to fix this. Can you please take care of it from your end. 

R.

Assistant: Feedback on the draft before you send it, per sales-strategist stance:

**Problems with the current version**

1. "We are swamped with this AI solution" — this tells the client you're capacity-constrained. Irrelevant to their problem, and it signals internal strain to someone who's paying you. Cut it entirely.
2. "It's not the best use of the team to have to fix this" — reads as dismissing a bug report from a paying client, even a rare one. Sabre already had a Feb 2026 outage and a settlement over it. Telling an executive sponsor you're choosing not to prioritize a confirmed bug is the kind of line that gets forwarded and escalated later, especially if Christy hits it again.
3. "Could be a glitch" — hedges when you've already confirmed the repro (works with 1 line item, breaks with 2). State it as a known edge case, not a guess.
4. No commitment to actually fix it. Right now this reads as a permanent punt. If it recurs or Christy pushes back, you have nothing to point to.

**Revised version**

Tye / Michael,

Quick update on the landed cost issue Christy flagged: it works correctly with one line item but breaks when a second is added. Confirmed on our end — a low-frequency edge case, under 1% of the ~1,900 landed costs processed.

Workaround for now: split into two separate landed cost entries when this comes up. We'll log the underlying fix and get it into a future cycle.

R.

Same outcome — workaround now, no fire drill — without the resourcing complaint or the "not worth fixing" framing, and it leaves you covered if this surfaces again.
