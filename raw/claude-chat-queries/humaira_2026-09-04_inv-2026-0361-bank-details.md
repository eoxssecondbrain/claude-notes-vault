---
thread_name: "inv-2026-0361-bank-details"
user: "humaira"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: [Uploaded file: /mnt/user-data/uploads/INV_2026_0361.pdf — Invoice #INV/2026/0361, Invoice Date 09/04/2026, Due Date 09/04/2026. Billed to: Eastern Steel Sales, 346 East Washington Street, Norristown, Pennsylvania, 19401, United States. Billed from: EOXS, 125 Maywood Road, New Rochelle, New York, 10804, United States. Line item: Monthly Licensing - Aug'26, Price 390.00, Quantity 6.00, Total $2,340.00. Subtotal $2,340.00. Total Price $2,340.00. Terms and Conditions: We accept wire transfer. Please do not send checks. Banking Details: Account Name - Prata Inc., Bank Name - Silicon Valley Bank SJ, ABA Routing & Transit # - 121140399, Swift Code - SVBKUS6S, Account Number - 3303151300, Branch Address - 3003 Tasman Drive, Santa Clara CA 95054.]

Check this invoice, in the bottom there are terms and condition, If I want to change bank details from here, how can I do that ?

Assistant: [Called ask_user_input_v0 tool with question: "What do you actually need — edit just this one PDF, or update the source so future invoices show new bank details?" Options: "Edit only this PDF file", "Update the invoicing system template/settings", "Not sure — explain both"]

User: [Selected] Not sure — explain both

Assistant: Editing just this PDF: I can directly edit the text in the uploaded file — change the account name, bank name, routing number, SWIFT code, account number, or branch address in the "Banking Details" block, and hand you back a corrected PDF. This only fixes this one document; it has no effect on future invoices.

Updating the source so all future invoices change: this PDF looks system-generated (EOXS branding, structured invoice numbering INV/2026/0361), which means the bank details block is very likely pulled from a stored bank account record or a fixed template field in your invoicing backend — not typed manually per invoice. To change it permanently, someone with access to that system needs to update the bank account / company settings there (or the invoice template text if it's hardcoded), and then it'll reflect on all invoices going forward. I only have read-only access to EOXS's connected data systems, so I can't make that change myself — I can only tell you it needs to happen upstream.

Want me to edit this specific PDF now with the corrected details?
