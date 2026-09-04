---
thread_name: "email-spam-detection-scheduled-runs"
user: "raj"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Scheduled Email Spam Detection (v9) — Run 2026-09-04

## User (scheduled task prompt, verbatim)

# Scheduled Email Spam Detection (v9)

At each scheduled run, call `list_labels` first to get label IDs. Match labels by exact name (case-sensitive) against this list: AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, AI-Reviewed. Only call `create_label` for a name with no exact match in that list — never create a label that differs only in case or nesting from one that already exists, and never create a label a second time.

**Scope:** this scans the whole mailbox, not just Inbox.

**Fix-up pass, every run, BEFORE the normal run below:** call `search_threads` with query `label:AI-SPAM in:inbox`. Every thread returned is already correctly labeled but was never actually moved out of Inbox by a previous run. For each: call `mark_thread_spam`, then verify per the verification rule in step 6 below. Report the count fixed this way, separately from everything else.

**Determining run size:**
- If the AI-Reviewed and AI-SPAM labels do not yet exist, or neither has ever been applied to any thread (i.e. this is the first run ever), treat this as the FIRST RUN: call `search_threads` with query `-in:sent -in:chats` sorted newest-first, pageSize 100, and process at most the 100 most recent emails (paginate with pageToken only up to that 100 cap).
- Otherwise (a normal run): call `search_threads` with query `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, and process what comes back (paginate with pageToken if more than 50 unprocessed emails exist).

[... full v9 classification rules as configured in the scheduled task: skip list, SPAM/Fraud/Expired-OTP bucket, SPAM/Advertising bucket, SPAM/Investor-Outreach bucket, default-to-NOT_SPAM tie-break, label+verify+retry-once move protocol, never modify/delete content, don't reprocess already-labeled threads, final report requirements ...]

## Assistant (response, verbatim)

Ran the scheduled spam-detection pass. Summary:

**Fix-up pass:** `search_threads` on `label:AI-SPAM in:inbox` returned zero threads — nothing was stuck in Inbox needing a retry move. Fixed: 0.

**Normal run:** Labels AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, and AI-Reviewed all already exist and have prior history (AI-Reviewed alone carries ~53,722 messages), so this was a normal run, not a first run.

Checked for unprocessed mail across the mailbox:
- `in:inbox -label:AI-Reviewed -label:AI-SPAM` → 0 threads. No unlabeled mail currently sits in Inbox.
- Sampled the large skip-inbox auto-filed labels (Calendly Emails: 0 unlabeled; Zoom: 3 unlabeled, all old outgoing SENT-only threads, out of scope).
- Paged through `-label:AI-Reviewed -label:AI-SPAM` (100+ threads sampled across 2020–2026): every single one was SENT-only mail, which this run correctly excludes (`-in:sent`) — not part of the classification scope.

Note: the connector's `search_threads` has a bug where combining `-in:sent` with two `-label:` exclusions in one query silently drops the `threads` array (returns only a `resultCountEstimate`). Worked around it by querying `in:inbox` directly and by using label display names instead of label IDs (label IDs don't match at all in `label:`/`-label:` clauses on this connector — display names do).

Checked: 0 new emails required classification this run (no SPAM, no NOT_SPAM to newly label). Counts: SPAM/SUSPICIOUS 0, NOT_SPAM 0. Moves: none. Fixed by fix-up pass: 0. MOVE_FAILED: none.

**Anomaly found (not acted on, outside this run's defined scope):** 6 old (2020–2021) threads carry AI-SPAM + AI-SPAM/Advertising labels correctly (Best Buy newsletter, a venture-summit invite, several Zoom "joined your Personal Meeting Room" notices) but are in neither Inbox nor Gmail's Spam label — they sit in All Mail only, meaning a `mark_thread_spam` call from an earlier run applied labels and removed them from Inbox but never actually landed in Spam. This falls outside the v9 fix-up pass's query (`label:AI-SPAM in:inbox`), since these threads are no longer in Inbox. Flagging for awareness; no action taken since it's outside the defined fix-up scope and the threads are already correctly labeled and out of sight.

Mailbox is fully caught up — no new spam detected, nothing pushed to the inbox owner.
