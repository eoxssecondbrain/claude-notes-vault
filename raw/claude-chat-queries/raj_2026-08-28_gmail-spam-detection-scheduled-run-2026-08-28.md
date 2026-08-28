---
thread_name: "gmail-spam-detection-scheduled-run-2026-08-28"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

## Scheduled Email Spam Detection (v3) — Run 2026-08-28

**Trigger:** Automated scheduled task, no live user present.

**Step 0 (repair pass):** Searched `label:AI-SPAM -in:spam` (includeTrash) — 0 orphaned threads found. No repair needed.

**Step 1 (run size):** AI-Reviewed label already had 1509 threads from prior runs, AI-SPAM had 0 threads/messages ever — treated as a normal run: `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginated.

**Work done:** Reviewed 350 inbox threads across 7 pages (sender/recipient/subject/snippet; get_thread PLAIN_TEXT used for 2 ambiguous cases). Applied AI-Reviewed to 348 threads (NOT_SPAM). Applied AI-SPAM + sub-label and mark_thread_spam (atomic per thread) to 2 threads:
- Thread `1994e8a894de246e` (emcgeachy@hayesgibson.com, "Executed ACH Disbursement Addendum Advice – Review Requested") — classic ACH/BEC fraud lure: mismatched sender role (maintenance tech signing as "Accounts Payable"), suspicious redirect link (hsm.za.com, unrelated to hayesgibson.com), self-addressed/bcc pattern. Labeled AI-SPAM/Fraud, moved to Spam.
- Thread `19957cc03a54ac44` (hannah.leadspro@gmail.com, "RE: Get Access to Odoo ERP, SAP, NetSuite and More Users") — unsolicited data-broker list-selling spam, bcc'd (not To/Cc) so it didn't hit the eoxs-address skip rule. Labeled AI-SPAM/Advertising, moved to Spam.

**Key finding — ruleset gap:** This is rajat@eoxs.com's own inbox, so virtually every inbound email has an eoxs.com address in To/Cc by definition. The v3 instruction's skip rule 3 ("sender domain eoxs.com/eoxsteam.com, or any eoxs address in To/Cc → NOT_SPAM, overriding every indicator") therefore exempts almost the entire inbox from real analysis. Confirmed 0 AI-SPAM threads existed before this run despite 1509 AI-Reviewed threads from prior runs — the filter has effectively never caught anything addressed directly to Rajat.

Examples of likely-malicious mail that got auto-exempted as NOT_SPAM under this rule during today's review (not moved, per the literal instructions):
- `19964332e49079f2` — "View Added Benefits from Sun Life" from sun10@royalrnail.com — spoofed/typosquat domain (royalrnail.com, unrelated to Sun Life or Royal Mail), classic phishing pattern.
- `19971d5a05836bbb` — "single-family office funding round $2M to $15M for EOXS" from j.moreno@nassaufowealthframework.info — unsolicited investment-scam pitch.
- `198ccd9aac9b1587` — "Investment in Prata Inc" from r.morgan@fundriskexpense.help — same pattern, suspicious `.help` domain.
- `198a556228398f9f` — "Ai Calls | Prata Inc" from ryan_c@loancatergetbuild.info — nonsensical/spam-generator-style domain.
- Multiple "Attendees list of SMU Steel Summit 2025" data-broker emails (clara.danielleleadinfo@gmail.com, emma.tylerinfodata@gmail.com) that would have been flagged as Advertising spam if not for being addressed directly To rajat@eoxs.com — contrast with the one that WAS flagged (hannah.leadspro@gmail.com) purely because it was bcc'd instead of To'd.

**Remaining backlog:** Gmail's resultCountEstimate stayed ~201 through the run (likely a stale/approximate figure), so an estimated 150-200+ inbox threads are still unprocessed. Did not continue further in this run to keep resource use reasonable; recommend a follow-up run soon to keep working through the backlog.

**Report to user (counts):**
- Orphans found/fixed (Step 0): 0
- Threads checked (Step 1): 350
- SPAM: 1 (Fraud)
- SUSPICIOUS: 1 (Advertising) — treated as spam per instructions (SPAM or SUSPICIOUS both get moved)
- NOT_SPAM: 348
- Moved to Spam: 2
- Remaining unprocessed inbox backlog: ~150-200 (estimate)

**Action taken:** Sent a push notification to Raj summarizing the run and flagging the skip-rule gap as a real risk, since it means genuine phishing/fraud mail addressed directly to him will keep sliding through as NOT_SPAM until the rule wording is tightened (e.g., only exempt via CC when the primary thread participant is external/EOXS staff, not simply because rajat@eoxs.com is a direct recipient).
