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
