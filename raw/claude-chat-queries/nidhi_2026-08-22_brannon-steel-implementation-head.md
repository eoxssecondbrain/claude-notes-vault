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
