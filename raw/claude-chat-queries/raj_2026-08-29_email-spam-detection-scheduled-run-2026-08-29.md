---
thread_name: "email-spam-detection-scheduled-run-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

## Scheduled run: Email Spam Detection (v3) — 2026-08-29

**User turn (scheduled task prompt, verbatim):**

# Scheduled Email Spam Detection (v3)

At each scheduled run, call `list_labels` first to get label IDs; create any missing label with `create_label` (AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-Reviewed).

**Step 0 — Repair pass (run this FIRST, every single firing, before anything else):**
Search `label:AI-SPAM -in:spam` (pass `includeTrash: true`) to find any thread that was already labeled as spam/suspicious by a past run but never actually got moved into the Spam folder. This is a known failure mode: `label_thread` can succeed while a later `mark_thread_spam` call for the same thread doesn't complete (the run gets interrupted, hits a turn/budget limit, or errors) — and because the normal-run search below permanently excludes anything already carrying the AI-SPAM label, an orphaned thread like this is never revisited by any future run unless this repair pass catches it. Call `mark_thread_spam` on every thread this search returns, paginating with pageToken until it returns none. This step requires no re-classification (the thread is already labeled) — just complete the move. Record how many orphans were found and fixed; report this count at the end of the run.

**Determining run size (Step 1):**
- If the AI-Reviewed and AI-SPAM labels do not yet exist, or neither has ever been applied to any thread (i.e. this is the first run ever), treat this as the FIRST RUN: call `search_threads` with query `in:inbox` sorted newest-first, pageSize 100, and process at most the 100 most recent inbox emails (paginate with pageToken only up to that 100 cap).
- Otherwise (a normal run): call `search_threads` with query `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, and process what comes back, paginating with pageToken if more than 50 unprocessed emails exist (this covers a gap after downtime or a backlog).

Call `get_thread` with `messageFormat PLAIN_TEXT` when the body needs to be read.

For every email in the run:

1. Read sender, subject, and body.
2. Check for common spam/phishing indicators: suspicious or misleading links; requests for passwords, OTPs, banking details, or other sensitive information; a one-time code, verification code, PIN, launch code, or magic sign-in link that is more than 24 hours old (a spent credential — codes under 24 hours old are still usable and must not be flagged); fake prizes, offers, marketing emails, or urgent requests; impersonation of companies or individuals; unusual sender information; suspicious attachments or instructions.
3. Before classifying, skip these entirely — mark NOT_SPAM without further analysis, overriding every indicator in step 2:
   - sender domain eoxs.com or eoxsteam.com, or any eoxs address in To/Cc
   - security notices: "security alert", "new sign-in", "new login", "password was changed", "account was recovered", "passkey", "You shared some Google Account data with"
   - payment, invoice, receipt, or subscription-charge mail
   - calendar mail: subject starting "Accepted:", "Declined:", "Invitation:", "Updated invitation:", "Canceled event:"
   - auto-replies and out-of-office
   - offer letters, contracts, onboarding forms, repository or system access invitations
   - any code or sign-in link less than 24 hours old
   - outbound sales/prospecting correspondence sent BY someone representing EOXS to a third-party prospect (e.g. bcc'd or cc'd to an eoxs.com address, or the body itself pitches EOXS/ERP to the recipient) — this is EOXS's own sales activity, not incoming spam, even if the sender's domain is unfamiliar
   When torn between this list and a spam indicator, choose this list.
4. Classify as SPAM, SUSPICIOUS, or NOT_SPAM.
5. **If SPAM or SUSPICIOUS — treat labeling and the spam-move as ONE atomic step per thread, never deferred to a later pass:**
   a. Call `label_thread` to apply the AI-SPAM label plus the matching sub-label (AI-SPAM/Advertising, AI-SPAM/Expired-OTP, or AI-SPAM/Fraud), recording the reason.
   b. Immediately, before evaluating the next email, call `mark_thread_spam` on that same thread to move it out of the Inbox into the Spam folder. Do not label a batch of threads first and come back to move them in a second phase — if the run ends between the two calls for a thread, that thread becomes permanently unreachable to future runs (the exclusion filter hides anything already carrying AI-SPAM), so the label and the move must never be separated by other work.
6. **If NOT_SPAM:** apply the AI-Reviewed label and nothing else. Do not move or archive it.
7. Do not modify or delete email content itself — only labeling and the one permitted `mark_thread_spam` move for confirmed SPAM/SUSPICIOUS threads. Never call `trash_thread` or archive anything.
8. Do not process the same email twice — the label state (AI-SPAM / AI-Reviewed) is the record; a thread carrying either label is skipped by the Step 1 search on all future runs (which is exactly why Step 0's repair pass exists — it's the only thing that can still reach an orphaned thread).
9. At the end of the task, report: how many orphans Step 0 found and fixed (should be 0 on a healthy run), number checked in Step 1, and counts of SPAM, SUSPICIOUS, NOT_SPAM, plus how many were moved to Spam.

Note: because Gmail's Spam folder auto-purges after ~30 days and moving mail there is a stronger action than labeling, this is a real, semi-destructive write — confirm this is the intended behavior before relying on it unattended.

**Assistant response (verbatim):**

Ran the scheduled spam-detection routine. Findings:

Step 0 (repair pass): searched `label:AI-SPAM -in:spam` (including trash) — 0 orphaned threads found. Nothing to fix.

Step 1 (normal run, since AI-Reviewed/AI-SPAM already exist and have history): queried `in:inbox -label:AI-SPAM -label:AI-Reviewed`. This is not a first run.

Processed 250 threads across 5 pages of 50. Every single one classified NOT_SPAM and got the AI-Reviewed label — 0 SPAM, 0 SUSPICIOUS, 0 moved to Spam.

Two things worth flagging rather than quietly continuing:

1. Rule design issue. The skip clause "sender domain eoxs.com or eoxsteam.com, or any eoxs address in To/Cc" fires on almost every message in this inbox, because the mailbox's own address (rajat@eoxs.com, alka@eoxs.com, mike@eoxs.com, etc.) is itself an eoxs.com address and sits in the To/Cc of virtually all inbox mail by definition. Since this skip list overrides every spam indicator ("When torn between this list and a spam indicator, choose this list"), the classifier never actually reaches step 4 for the vast majority of mail. In this batch alone I saw several threads with classic phishing/social-engineering shape — fake INTERAC e-Transfer notices with a mismatched recipient name ("Hi Janu Bhaiya" / "RanjanJain sent you money"), fake RingCentral "account about to be suspended" billing-failure emails, a "Stars Account" gambling deposit/password-reset pair, SVB card "past due" and "wire approver settings" scare emails — all auto-cleared as NOT_SPAM purely because they were addressed to an eoxs.com account, not because they were reviewed and found benign. As written, this rule makes the SPAM/SUSPICIOUS branch close to a no-op for this mailbox. If the intent was to protect internal EOXS-to-EOXS correspondence, the clause probably needs to key off a *third-party* eoxs.com address (e.g., cc'd on mail between two external parties, indicating outbound sales) rather than the mailbox owner's own address appearing in To.

2. Backlog size. `in:inbox -label:AI-SPAM -label:AI-Reviewed` reported resultCountEstimate 201 on every page (Gmail's estimate appears stale), but pagination kept returning fresh threads through 5 full pages with no sign of stopping. Cross-checking label totals: INBOX has 20,475 threads total; AI-Reviewed had 11,399 before this run. That gap suggests roughly 8,800+ inbox threads (dating back to at least March 2022) have never been labeled by this routine — a backlog far larger than the "up to 50, paginate if needed" the routine's spec assumed. Grinding through all of it in one run would mean roughly 175+ more pages and thousands more label calls.

Given both points, I stopped after this batch rather than continuing to burn through an ~9,000-thread backlog under a skip rule that isn't actually screening anything. Recommend: (a) decide whether the eoxs-address skip clause should be scoped to third-party cc's only, and (b) decide whether the historical backlog should be processed at all, or whether the routine should only run forward from today's mail.

Final tally for this run: Step 0 orphans found/fixed: 0. Step 1 checked: 250. SPAM: 0. SUSPICIOUS: 0. NOT_SPAM: 250. Moved to Spam: 0.
