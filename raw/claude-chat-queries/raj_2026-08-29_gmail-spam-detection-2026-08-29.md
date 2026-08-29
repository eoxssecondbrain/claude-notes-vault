---
thread_name: "gmail-spam-detection-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

# Scheduled Email Spam Detection Run — 2026-08-29

## User (scheduled task prompt)

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
2. Check for common spam/phishing indicators.
3. Before classifying, skip these entirely — mark NOT_SPAM without further analysis (eoxs.com/eoxsteam.com senders, security notices, payment/invoice mail, calendar mail, auto-replies, offer letters/contracts, expired OTP under 24h, outbound EOXS sales mail).
4. Classify as SPAM, SUSPICIOUS, or NOT_SPAM.
5. If SPAM or SUSPICIOUS — label_thread then immediately mark_thread_spam, atomically per thread.
6. If NOT_SPAM — apply AI-Reviewed label only.
7. Do not modify/delete/trash/archive anything beyond labeling and the spam move.
8. Do not process the same email twice — label state is the record.
9. At the end, report: orphans found/fixed, number checked in Step 1, counts of SPAM/SUSPICIOUS/NOT_SPAM, and how many were moved to Spam.

## Assistant (final report)

Step 0 (repair pass): searched `label:AI-SPAM -in:spam` (includeTrash: true) — 0 orphaned threads found. Nothing to fix.

Step 1 (normal run, since AI-Reviewed/AI-SPAM already exist and AI-Reviewed had prior history — 7,483 threads / 15,456 messages before this run): ran `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, and paginated through 6 pages (~334 threads returned as "candidates"). On inspection, every single one already carried the AI-Reviewed label on every message in the thread — none were genuinely new/unprocessed. Cross-checked with a direct `in:inbox newer_than:3d` search (34 threads, the actual most recent inbox mail) and confirmed the same: 100% already labeled AI-Reviewed, nothing missing.

Effective results this run: 0 new threads processed. SPAM: 0. SUSPICIOUS: 0. NOT_SPAM (newly labeled): 0. Moved to Spam: 0. The inbox is fully caught up — there was nothing left to classify.

Technical note: the `search_threads` tool's `-label:X` exclusion is not reliably narrowing results on this account — every "candidate" it surfaced in Step 1 was in fact already fully labeled (a known caveat the tool itself documents: label exclusions can return stale matches). This cost extra verification calls but did not cause any misclassification or wrong action, since each candidate was checked against its actual label state via `get_thread`/full metadata before anything was touched. Worth knowing for future runs: don't trust the Step 1 exclusion filter at face value — verify before acting.
