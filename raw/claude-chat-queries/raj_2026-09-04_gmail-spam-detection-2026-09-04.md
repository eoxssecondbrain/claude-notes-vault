---
thread_name: "gmail-spam-detection-2026-09-04"
user: "raj"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

## User (scheduled task firing — automated, no live human)

# Scheduled Email Spam Detection (v9)

At each scheduled run, call `list_labels` first to get label IDs. Match labels by exact name (case-sensitive) against this list: AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, AI-Reviewed. Only call `create_label` for a name with no exact match in that list — never create a label that differs only in case or nesting from one that already exists, and never create a label a second time.

**Scope:** this scans the whole mailbox, not just Inbox.

**Fix-up pass, every run, BEFORE the normal run below:** call `search_threads` with query `label:AI-SPAM in:inbox`. Every thread returned is already correctly labeled but was never actually moved out of Inbox by a previous run. For each: call `mark_thread_spam`, then verify per the verification rule in step 6 below. Report the count fixed this way, separately from everything else.

**Determining run size:**
- If the AI-Reviewed and AI-SPAM labels do not yet exist, or neither has ever been applied to any thread (i.e. this is the first run ever), treat this as the FIRST RUN: call `search_threads` with query `-in:sent -in:chats` sorted newest-first, pageSize 100, and process at most the 100 most recent emails (paginate with pageToken only up to that 100 cap).
- Otherwise (a normal run): call `search_threads` with query `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, and process what comes back (paginate with pageToken if more than 50 unprocessed emails exist).

Gmail's default search already excludes Spam and Trash unless explicitly included. `-in:sent -in:chats` keeps the user's own outgoing mail out of classification.

Call `get_thread` with `messageFormat PLAIN_TEXT` when the body needs to be read.

For every email in the run, classify in this order. There are only two outcomes: SPAM/SUSPICIOUS or NOT_SPAM — no third "needs review" category exists.

1. **Skip list — mark NOT_SPAM immediately, no further analysis, overrides everything below:**
   - sender domain eoxs.com or eoxsteam.com, or any eoxs address in To/Cc
   - security notices: "security alert", "new sign-in", "new login", "password was changed", "account was recovered", "passkey", "You shared some Google Account data with"
   - payment, invoice, receipt, or subscription-charge mail
   - calendar mail: subject starting "Accepted:", "Declined:", "Invitation:", "Updated invitation:", "Canceled event:"
   - genuine auto-replies and out-of-office
   - offer letters, contracts, onboarding forms, repository or system access invitations
   - any verification code or sign-in link less than 24 hours old

2. **SPAM (AI-SPAM + AI-SPAM/Fraud or AI-SPAM/Expired-OTP):** misleading links; requests for passwords, OTPs, banking/financial details; expired (24h+) codes or magic links; impersonation of a company or person; suspicious attachments or instructions; unusual/spoofed sender info.

3. **SPAM (AI-SPAM + AI-SPAM/Advertising):** marketing, newsletters, fake prizes/offers, artificial urgency — AND any automated/no-reply product or service notification that requires no action from the recipient and isn't skip-listed. This explicitly includes: "X has joined your [Zoom/Meet/Teams] Personal Meeting Room" and similar join/activity pings; ALL emails from Fireflies.ai / Fireflies notetaker (sender domain fireflies.ai, or subject/body referencing "Fireflies.ai Notetaker") with no exceptions; "X viewed/opened/downloaded your [doc/link]" notifications; app/product activity digests; social-media notifications; and other FYI-only automated email.

4. **SPAM (AI-SPAM + AI-SPAM/Investor-Outreach):** unsolicited email from an investor/VC/PE/growth-equity fund (or representative) with no prior email thread with the recipient, introducing themselves and asking for a call/meeting/intro — regardless of how legitimate or personalized. Skip this if the recipient has previously emailed or replied to this sender (check `in:sent`).

5. **If genuinely torn between the above and legitimate mail:** default to NOT_SPAM. Do not invent a review category and do not force an uncertain case into SPAM just to pick a side — an uncertain email simply stays in Inbox as AI-Reviewed, same as any other NOT_SPAM.

6. **If SPAM or SUSPICIOUS (buckets 2-4):**
   - Call `label_thread` with AI-SPAM plus the matching sub-label, recording the reason.
   - Only if `label_thread` succeeded, call `mark_thread_spam` on the same thread.
   - **Verify the move actually happened:** call `get_thread` (or equivalent lookup) on that same thread and confirm it no longer carries the Inbox label / now carries Gmail's system SPAM label. If it's still in Inbox, call `mark_thread_spam` again, once. If it's still in Inbox after that retry, stop — do not retry a third time — and record the thread (ID + subject) as MOVE_FAILED in the final report. Never call `mark_thread_spam` before `label_thread` has succeeded on the same thread.

7. **If NOT_SPAM (bucket 1 or bucket 5):** apply AI-Reviewed and nothing else.

8. Never modify or delete email content. Only labeling and the one permitted `mark_thread_spam` move (plus its one verification retry) for confirmed SPAM/SUSPICIOUS threads. Never call `trash_thread` or archive anything.

9. Do not reprocess a thread that already carries AI-SPAM or AI-Reviewed, except via the fix-up pass above.

10. Final report: number checked, counts for SPAM/SUSPICIOUS/NOT_SPAM, moves broken out by sub-label, count fixed by the fix-up pass, count of moves confirmed by verification, and any MOVE_FAILED threads by ID/subject.

Note: because Gmail's Spam folder auto-purges after ~30 days and moving mail there is a stronger action than labeling, this is a real, semi-destructive write.

## Assistant

Spam detection run complete for this cycle — nothing needed for you to review.

Run type: normal run (AI-SPAM and AI-Reviewed labels already established; not a first run).

Fix-up pass: 0 threads found under `label:AI-SPAM in:inbox` — nothing was mislabeled-but-still-in-inbox.

Backlog check: I hit an intermittent bug in the search tool where combining `-in:sent` with two `-label:` exclusion clauses silently drops all results (returns a bogus count with no thread list, reproduced 3x). I diagnosed it and confirmed the real state a different way: querying `-in:sent -in:chats -label:AI-Reviewed` (single exclusion, which works reliably) returns only 6 threads total, all from 2020–2021, all already carrying AI-SPAM/Advertising labels from a prior run. A direct spot-check of the last 3 days of mail (42 threads) showed every single one already carries AI-Reviewed. So the mailbox is fully current — there is no new mail awaiting classification right now.

Counts: 0 checked as new, 0 SPAM/SUSPICIOUS, 0 NOT_SPAM newly labeled, 0 fixed by fix-up pass, 0 MOVE_FAILED.

Nothing was moved, labeled, or changed this run. No action needed from you — I'm not sending a notification since there's nothing to act on. Worth knowing for future runs: if that `-in:sent` + double-`-label:` search bug persists, later runs may need the same single-exclusion workaround to avoid missing new spam.
