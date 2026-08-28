---
thread_name: "dps-austin-mcp-writeaccess-request"
user: "hashir"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User (Hashir Saleem, EOXS):
Hey this is Hashir we got this from Austin (from Discount Pipe) can you make me understand what he is referring to and talking about :-
I have discussed this with Zana in depth. It is my understanding that the system (EOXS) is matching the incorrect sales order lines with the correct tag numbers? If so, We may have a solution of our own. We have an external load check tool that currently matches tags with SO order lines correctly. If we could add write options to our DPS MCP connector, our tool would be able to create the packing slip without error. In case of any error while loading due to missing tag number or inventory issues it could then automatically flag a user to get involved and resolve issue manually. 
Yes this would required write access to EOXS through the DPS MCP connector; however, it should require no code change on your end. 
Please let me know what your thoughts are on this solution.

Assistant:
Austin is describing a real, already-documented issue and proposing a fix. Here is the breakdown.

What he's referring to:

The underlying complaint: when a Discount Pipe sales order has multiple lines, scanned inventory tags sometimes get matched to the wrong SO line on the packing slip. This is the exact behavior tracked as Odoo task #364 ("Scanned Tags Create Incorrect SO Line on Packing Slip") — worked May through August, and marked fixed and confirmed live on 2026-08-20. Six days later (Aug 26), Zana hit new blockers on packing lists/transfers, which she suspected was the recent CodePushLive update reintroducing bugs already fixed. That triggered the escalation call on Aug 26-27, which produced two separate asks in the same thread:

1. Austin's ask (this message): DPS has its own external "load check" tool that already matches tags to SO lines correctly on their end. His proposal — give that tool write access into EOXS via the DPS MCP connector, so it creates the packing slip directly, bypassing EOXS's own matching logic entirely, and only pings a human when a tag is missing or there's an inventory mismatch. He claims this needs no code change on your side.

2. Zana's ask (separate, in the same thread) — a different angle: salespeople manually calculate weights and add tags to the manual-reserve area on SO lines, and make mistakes doing it. She's asking either to loosen reservation strictness for manually-reserved tags, or to auto-tie a manually-reserved tag to its SO line at packing time.

The wiki analysis built from this thread explicitly flags that it's not established whether Austin's "wrong SO line matching" complaint and Zana's "manual reservation strictness" complaint are the same bug or two different things. Worth resolving before you scope anything.

Also relevant: Ron's reply to the thread (the last message) already assigned you a task — estimate how long the code-fix route would take — before any decision on Austin's write-access proposal gets made. That has not been answered yet as of this thread.

My read on the proposal itself, since you'll likely need to respond to it: Austin's "should require no code change on your end" claim doesn't hold up on its face. Write access through the DPS MCP connector into EOXS means an external tool creating packing slips directly against your database — that bypasses whatever validation/business logic currently governs tag-to-SO-line matching, inventory reservation, and packing slip creation (the same logic that's the source of this and other reservation bugs you've been chasing all year). Standing up scoped write access safely — auth, field-level permissions, conflict handling with your own reservation system, error handling on partial failures — is not a no-op even if no application code changes. It's also a standing external-write surface into production data, which is a different risk profile than the read-only support/analytics connectors already in place.

If I were pushing back in the room: the actual leverage move is figuring out whether the Aug 26 regression and the Aug 20 "fixed" task #364 are related (looks likely, given the one-week gap and matching symptoms), fixing that properly, and only then evaluating whether DPS's external tool is even still needed as a workaround. Handing them write access now, before root-causing the regression, risks building a permanent bypass around a bug that might get fixed anyway.

User:
My question was to understand about MCP request which he is suggesting and how that will not involve code changes ?

Assistant:
The MCP piece specifically:

DPS already has a connector into their own Odoo instance (discount_pipe2) — currently read-only, used for querying data (the tool I have access to for it is literally called "DPS LIVE" and only exposes a read-only SQL query). Austin's ask is to add write capability to that same connector, so his external load-check tool can call it to create packing slip records (stock.picking / stock.move / tag-lot assignment) directly, instead of a human or EOXS's own logic doing that matching step.

His "no code change on your end" claim rests on one assumption: that creating a packing slip is just calling an operation Odoo already knows how to do. If that's true, "adding write" is a permissions/infra change — flip the connector from read-only to allowing specific write calls — not new application code. In that narrow sense he could be right.

Where the claim breaks down:

Odoo's own core write path (creating a stock.picking) is generic. But the tag-to-SO-line matching logic — the thing that's actually been buggy all year (task #364, the Aug 26 regression) — is EOXS's custom logic layered on top of stock Odoo, not stock Odoo itself. If DPS's tool writes packing slips directly through the connector, one of two things happens:

1. It goes through EOXS's existing custom validation/reservation logic — in which case it's exposed to the same bug that's already causing wrong-line matching, so the fix accomplishes nothing.
2. It bypasses that logic and writes stock moves directly — in which case it skips your reservation system entirely (the same reservation system multiple other DPS tickets this month depend on), and now you have two paths creating packing slips with no guarantee they agree on tag state. That's a new failure mode, not a fix, and preventing it requires new validation code — which contradicts "no code change."

There's also connector-layer work Austin isn't counting as "code" but is real effort: defining exactly which models/fields the write scope covers, auth/permissioning so the external tool can't write outside that scope, and error handling for partial writes (his own proposal assumes a clean "flag a human on error" path, which itself has to be built).

So: the claim is true only if you read "code change" narrowly as "new EOXS product features," and false the moment you count the validation and access-control work needed to make an external write path safe against the same matching bug this whole thread is about. That's exactly why Ron asked you for an effort estimate before anyone decides — this isn't a config toggle.
