---
thread_name: "brannon-steel-implementation-head"
user: "nidhi"
type: claude-chat
created: 2026-08-22
updated: 2026-08-22
---

USER: Give me detailed information about Brannon. Who was the implementation head. give me the last conversation with them and issue which we fixed.

ASSISTANT: Brannon Steel (brannonsteel.com, Brampton, Ontario) — EOXS client, MTR AI deployment. First Canadian client, first MTR-AI-only engagement. Win date January 20, 2026.

Key people:
- David Brannon — client contact, introduced the deal at SMU Steel Summit Sept 2025
- Kevin Brannon (K.R.) — client contact
- Manish Trivedi — Head of Operations at Brannon Steel, client-side technical lead
- Ranim Fallaha (aka Raneem Fallaha) — APQP Manager / Materials Engineer, ex-Gerdau, does daily UAT testing and flags issues
- Ayan Dutta ("Ayaan" internally) — EOXS implementation lead for this account, runs the weekly huddles with Ranim, triages bugs to EOXS dev
- Jaskeerat Singh — EOXS dev, handles most of the technical fixes in the task thread

Implementation head: Ayan Dutta, on the EOXS side. Manish Trivedi is his client-side counterpart (Head of Operations, primary account contact).

Last conversation: an ongoing Odoo task thread ("MTR Samples," running since Jan 27, 2026, most recent activity Aug 21, 2026). Latest message, Aug 21, from Ranim to Ayan:

MTRs showing a matched status but not displaying in results — two examples given (heat 3533T6, heat 727921). This is still open, not fixed — no EOXS reply on record yet after that message.

Before that, Aug 14, Ranim flagged three separate false-negative/mismatch issues in one week (results not showing despite matching inventory, spec mismatches). Jaskeerat's reply that day only acknowledged them and said EOXS would look into it and update by Monday — also not confirmed fixed in this thread.

The most recent issue actually confirmed fixed: SSAB MTR handling logic, closed out July 28, 2026. Sequence:
- July 22: Jaskeerat asked how to handle a batch (A69) that shared a heat/test stream with tested pieces (A70/A72/A73) but wasn't itself tested
- July 27: Ranim gave the resolution rule (associate A69 with one of the tested pieces, per ASTM minimum-slab-check logic)
- July 28: Jaskeerat confirmed the logic was updated and SSAB MTR uploads could resume

Before that, a rotated-MTR extraction bug (bad OCR on rotated scans corrupting batch/heat numbers) was fixed July 16 — records manually corrected, process note added to rotate MTRs before upload.

Source: eoxs-db (client profile, wiki, email thread id 60897 "Re: MTR Samples").

USER: what is the role of Jaskeerat in brannon

ASSISTANT: Jaskeerat Singh's role at Brannon Steel: AI Developer (EOXS full-time staff, converted to FT 2026-06-22). On the account since July 10, 2026, he took over day-to-day inventory/MTR data-validation communication with Ranim Fallaha from Ayan Dutta.

His actual work in the task thread:
- Requests and validates client inventory data against uploaded MTR records
- Communicates data-quality findings back to Ranim (e.g. diagnosed the scan-orientation extraction bug in mid-July)
- Implemented the SSAB batch-matching logic fix (the A69/A70/A72/A73 issue, closed July 28)
- Is the one who logged/acknowledged the Aug 14 batch of false-negative issues, promising a Monday update

So he's not the implementation head — Ayan Dutta still holds that role for Brannon Steel — Jaskeerat is the dev doing the hands-on data-quality fixes under him.

Source: eoxs-db wiki (Jaskeerat Singh entity page).

USER: Give me a detailed information about sabre alloys , there background. How we got this deal. What was the recent conversation with them . And how much we are charging them for the monthly subscription?

ASSISTANT: Sabre Alloys — background:

Steel service center (slitting, cut-to-length, blanking operations). Full EOXS ERP + CRM client since 2024, not a recent signup — one of the largest, longest-running accounts in the portfolio (1,461 emails, 114 calls, 200 implementation tasks on record).

Key contacts: Charles White, Christi, Ernie Valdez, Jesus Rios, Jim Zeigler (Senior Sales Director), Michael Mercadante, Tye Webb, Juan Deshon. Rajat Jain is the EOXS account owner/salesperson.

How the deal was won: proposal dated Dec 27, 2023 — full ERP+CRM deployment, 12 licensed users, 9 modules (Sales, Purchase, CRM, Inventory Management, Contact Management, Manufacturing, Logistics Management, Executive Dashboards x2, Accounting I), 3-year contract term, 18-week implementation across 7 phases (Discovery through Go-Live/Support). Onboarding kicked off Jan 5, 2024 with credential provisioning, followed by a run of Sales CRM training sessions (Jan 9/11/12) for their whole sales floor, then deep-dive product demos driven by Rajat and Ron. I don't have the earlier discovery/demo-call history before the Dec 2023 proposal in what I can access this session — the archive picks up at proposal stage.

Most recent conversation: Aug 13, 2026 call, "Sabre Alloys - AI Transformation Proposal" — Rajat, Michael Mercadante, Tye Webb. This is a new, separate pitch layered on top of the existing ERP relationship: a Claude/AI "company brain" setup for ~15 of their users (Claude accounts, an AI agent to summarize their email data into a shared knowledge base, plus an optional prompt-logging layer so management can see what staff are asking AI). Mechanically it'd pull data via a direct MCP database connection rather than an API. Good chunk of the call was Tye and Michael pressure-testing whether their existing ERP (Invera) would allow that kind of third-party DB access at all — inconclusive, action item for Rajat to check with a contact (Lawrence, a CIO with Invera background). Outcome: Rajat to send a formal proposal doc with pricing/scope; Tye to review internally with Jesus and Dave and get back.

Monthly subscription charge: I can't surface that — dollar figures are stripped from everything I have access to in this system, including this one. What I can say: the core ERP deal is a 3-year term with pricing locked for that duration; the new AI/Claude add-on pricing discussed on the Aug 13 call is separately proposed and also came back redacted.

Source: eoxs-db (client profile, wiki, call id 2393).
