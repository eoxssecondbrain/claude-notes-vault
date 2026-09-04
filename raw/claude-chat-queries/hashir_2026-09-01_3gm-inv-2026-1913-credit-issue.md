---
thread_name: "3gm-inv-2026-1913-credit-issue"
user: "hashir"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

USER: Can you pull off all the informations from this invoice :- INV/2026/1913
 Of 3gm Live and we need to understand what actually they are asking and what they are looking for us to do in order to close this ticket.

ASSISTANT: Found it — email thread 68047 (support_zoho, 2026-09-01), subject "Re: INV/2026/1913", client 3GM Steel.

Full message, verbatim, from 3GM Steel (updates@3gmsteel.com) to EOXS Support, internal note:

"@EOXS Support - another issue where the customer is showing 2 credits but doesn't have a credit to apply. Please advise."

What this means:

- 3GM Steel is flagging that on invoice INV/2026/1913, the customer's account is displaying two credit entries, but the customer does not actually have a credit balance that should apply.
- "Another issue" signals this is a repeat of a known bug class for this client — 3GM has prior documented cases of credit memos being incorrectly/duplicated or "artificially applied" to invoices (e.g. RINV/2025/0014 needed manual correction by 3GM's own staff after a bad credit memo application).
- No dollar amounts, invoice total, or line items were in this note — it's purely a flag, not a detailed bug report.

What they want from us to close the ticket:

1. Open INV/2026/1913 (and the associated customer account) in 3GM's Odoo and confirm the 2 credit lines are real ledger entries, not a display bug.
2. Determine why they exist — duplicate credit memo, an over-applied credit from another invoice, or a UI/reporting bug showing phantom credits.
3. Either remove/correct the erroneous credit(s) or explain to 3GM why they're legitimate.
4. Reply on the thread with the resolution so 3GM can close it out with their customer.

One limitation: I don't have a connected live Odoo instance for 3GM Steel (only Discount Pipe & Steel, Greer Steel, Sabre Alloys, and the internal EOXS Team DB are connected here), so I can't pull the actual invoice/credit ledger rows myself — everything above comes from the email note and prior wiki history, not the source invoice record. Someone with 3GM Odoo access needs to actually inspect INV/2026/1913 and its credit notes to fix this.

USER: We have already connected the 3gm live mcp with you can you go through that and look into this and provide me more information about this in detail

ASSISTANT: There is no 3GM Live connector available. The only Odoo live connectors present are DPS LIVE (Discount Pipe & Steel), GREER LIVE (Greer Steel), SABRE LIVE (Sabre Alloys), and TEAMEOXS LIVE (internal EOXS team DB). No 3GM instance is connected on my end, so I can't query it directly.

If it's genuinely been connected, it may not be showing up in my available tools — can you confirm the exact connector name as it appears on your end? Otherwise this needs to be added on your side before I can pull the live invoice/credit records for 3GM.
