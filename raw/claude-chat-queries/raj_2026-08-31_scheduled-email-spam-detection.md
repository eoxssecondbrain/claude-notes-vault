---
thread_name: "scheduled-email-spam-detection"
user: "raj"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

# Scheduled Email Spam Detection (v3) — Run 2026-08-31

## User (scheduled task prompt)

# Scheduled Email Spam Detection (v3)

At each scheduled run, call `list_labels` first to get label IDs; create any missing label with `create_label` (AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-Reviewed).

**Step 0 — Repair pass (run this FIRST, every single firing, before anything else):**
Search `label:AI-SPAM -in:spam` (pass `includeTrash: true`) to find any thread that was already labeled as spam/suspicious by a past run but never actually got moved into the Spam folder. This is a known failure mode: `label_thread` can succeed while a later `mark_thread_spam` call for the same thread doesn't complete (the run gets interrupted, hits a turn/budget limit, or errors) — and because the normal-run search below permanently excludes anything already carrying the AI-SPAM label, an orphaned thread like this is never revisited by any future run unless this repair pass catches it. Call `mark_thread_spam` on every thread this search returns, paginating with pageToken until it returns none. This step requires no re-classification (the thread is already labeled) — just complete the move. Record how many orphans were found and fixed; report this count at the end of the run.

**Determining run size (Step 1):**
- If the AI-Reviewed and AI-SPAM labels do not yet exist, or neither has ever been applied to any thread (i.e. this is the first run ever), treat this as the FIRST RUN: call `search_threads` with query `in:inbox` sorted newest-first, pageSize 100, and process at most the 100 most recent inbox emails (paginate with pageToken only up to that 100 cap).
- Otherwise (a normal run): call `search_threads` with query `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, and process what comes back, paginating with pageToken if more than 50 unprocessed emails exist (this covers a gap after downtime or a backlog).

[... full classification rules as configured in the scheduled task, including spam/phishing indicators, the NOT_SPAM override list (eoxs.com/eoxsteam.com senders, security notices, payment/invoice mail, calendar mail, auto-replies, offer letters, codes <24h old, outbound EOXS sales correspondence), the SPAM/SUSPICIOUS labeling + mark_thread_spam atomic step, the NOT_SPAM AI-Reviewed labeling, and the end-of-run reporting requirement ...]

## Assistant (this run)

Checked labels: AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, and AI-Reviewed all already exist (Label_33, Label_34, Label_35, Label_36, Label_37). AI-Reviewed has been applied to 39,190 messages historically, so this is a normal run, not a first run.

Step 0 (repair pass): searched `label:AI-SPAM -in:spam` with includeTrash true — 0 results. No orphaned threads found.

Step 1 (normal run): searched `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50 — 0 results. No unprocessed inbox threads to classify.

## Run Summary
- Orphans found and fixed (Step 0): 0
- Threads checked (Step 1): 0
- SPAM: 0
- SUSPICIOUS: 0
- NOT_SPAM: 0
- Moved to Spam: 0

Nothing to do this run — inbox is fully caught up (every inbox thread already carries either AI-SPAM or AI-Reviewed). No notification sent to the user since the run was a clean no-op.
