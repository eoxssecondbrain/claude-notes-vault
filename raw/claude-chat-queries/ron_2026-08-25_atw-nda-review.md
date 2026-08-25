---
thread_name: "atw-nda-review"
user: "ron"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

User: Now, I need you to create an NDA for this person in the business card. This is the one that we had already, and I just changed the company name, address, date, and other information in it. Can you please check if everything looks correct? It's a standard NDA that EOXS sends.

[User uploaded: business card image for Monty Hill, SVP of BD & Innovation, American Train Works (ATW), 599 County Road 3706A, Splendora, Texas 77372, mhill@atwteam.com, www.atwteam.com, (903) 229-1369]

[User uploaded: NDA_-_ATW.pdf — a Mutual Non-Disclosure and Confidentiality Agreement between Prata Inc. and American Train Works (ATW), Effective Date 08/25/2026, signed on behalf of Prata Inc. by Rajat Jain (Founder & CEO), ATW signature block blank. Contains standard NDA clauses 1-8 (definition of confidential information, obligations, disclosure, use, term, notice of breach, remedies, general), plus Section 9 "LIMITED SOURCE CODE ACCESS FOR AUDIT PURPOSE" which references an audit "to review and analyze inventory valuation, control tag accounting, and related accounting logic for Sabre Alloys."]

Assistant: A few things checked against the business card — most of it lines up, but there's one real problem.

Matches the card correctly:
- Party name: American Train Works (ATW)
- Address: 599 County Road 3706A, Splendora, Texas 77372
- Effective date: 08/25/2026 (today)
- Prata Inc. is EOXS's legal entity name for contracts like this, so that's expected, not an error

Problem — Section 9 (Limited Source Code Access for Audit Purpose):
This entire clause is still written for Sabre Alloys, not ATW. Section 9(a) literally says the audit is "to review and analyze inventory valuation, control tag accounting, and related accounting logic for Sabre Alloys." This is leftover from whatever NDA you copied this from — it wasn't updated when you swapped the company name elsewhere. You need to either:
- Delete Section 9 entirely if there's no source-code-audit arrangement with ATW, or
- Rewrite it to reference ATW's actual situation, if there is one

This is the kind of clause a counterparty's lawyer would flag immediately, and sending it as-is would look sloppy and expose an unrelated client's name to a third party — that's a confidentiality problem in its own right.

Minor asymmetry — signature block:
Prata Inc.'s side has "Name: Rajat Jain / Designation: Founder & CEO" typed in. ATW's side just says "(Signature of Authorized Signatory)" with no Name/Designation lines at all. Worth adding matching lines for ATW — you could prefill "Monty Hill, SVP of BD & Innovation" from the card, or leave them blank for them to fill, but the block should at least have the same structure on both sides.

Not flagged, but worth a gut check: jurisdiction is still "courts in Iowa and California" — if that's your standard boilerplate across all NDAs, leave it; just confirming it wasn't meant to be client-specific.

This document-review task didn't cleanly match any of my listed skills (not a DPS/Sabre strategy call, not an email draft) — I used the EOXS vault only to confirm the Prata Inc./EOXS entity relationship, then reviewed the PDF directly.
