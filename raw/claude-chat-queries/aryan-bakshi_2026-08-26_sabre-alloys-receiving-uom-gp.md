---
thread_name: "sabre-alloys-receiving-uom-gp"
user: "aryan-bakshi"
type: claude-chat
created: 2026-08-26
updated: 2026-08-26
---

USER: Looping back to this. I tagged support this morning regarding the receiving. I received by the foot rather than by the pc so it inflated the price and tanked the GP. need to reply on this yes christi we are looking into this we found a way to fix this and now we are working on it

ASSISTANT: Couldn't pull up today's specific ticket — nothing matching "receiving by foot" in the synced email threads yet (ingestion runs on a lag), and direct query access to Sabre Alloys' live Odoo instance isn't approving right now (Sabre Live connector returned "no approval" on every call, including schema/list_tables). Christi Deaton at Sabre Alloys is the right contact based on prior threads — she's flagged GP/receiving-accuracy issues before (e.g. the SO-20173 thread where she pushed back on manually validating GP).

Draft reply:

"Hi Christi,

Confirming — we're on this. The receiving posted by the foot instead of by PC, which inflated the unit cost and hit GP on that order. We've identified the fix and are implementing it now. Will confirm once it's corrected and let you know if any past receipts need to be adjusted."

I added the last line as a flag, not a promise — worth deciding whether other receipts have the same UOM error before you send this, otherwise Christi will reasonably ask next. Cut it if you already know this was a one-off.

I have no send capability on any of these connectors (all read-only), so you'll need to post/send this yourself — email or Odoo chatter note, whichever the ticket lives in. If you give me the SO or receipt number I can try to pull the actual record once Sabre Live approves or the email syncs.
