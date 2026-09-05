---
thread_name: "scheduled-spam-detection-2026-09-05"
user: "raj"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Scheduled Email Spam Detection (v9) — Run 2026-09-05

**Trigger:** Scheduled task (automated, no live user present).

## Task
Run the v9 scheduled email spam detection playbook: fix-up pass for AI-SPAM threads still in Inbox, then a normal run classifying new mail into AI-SPAM (+ sub-label) or AI-Reviewed.

## Actions taken

1. `list_labels` — confirmed AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, AI-Reviewed all already exist (Label_33/34/35/36/38/37). AI-Reviewed already applied to 54,086 messages / 29,785 threads → this is NOT a first run.
2. **Fix-up pass**: `search_threads` for `label:AI-SPAM in:inbox` (and by label ID `Label_33 in:inbox`) → 0 results. Nothing to fix.
3. **Normal run**: `search_threads` with `-in:sent -in:chats -label:Label_33 -label:Label_37`, pageSize 50, paginated through 5 pages (250 threads, newest-first, from 2026-09-05 back to mid-August).
   - Discovery: the `-label:<id>` / `-label:<name>` exclusion is **not functioning** in this search tool — queries with and without the label exclusions returned identical result sets and identical `resultCountEstimate` (201, though more pages existed beyond that estimate). Verified via diagnostic queries (`-label:Label_37` alone, `label:Label_37`, `label:AI-Reviewed` all returned the same broad, unfiltered-looking set).
   - Manually inspected every message's `labelIds` in all 250 returned threads (via jq on saved tool output for the larger pages): **100% already carry Label_37 (AI-Reviewed)**. Zero threads found lacking both AI-SPAM and AI-Reviewed labels.
   - Spot-checked 3 threads with `get_thread` (including suspicious-looking "job application" emails from askcruzai.com / askcruzpredictive.com / askcruzagentic.com — domains that mimic the user's own AskCruz brand) — confirmed already labeled AI-Reviewed from a prior run; per step 9 of the playbook, not reprocessed.
4. No labels applied, no threads moved to spam this run — nothing met the criteria for action (nothing unprocessed found).

## Final report
- Checked: 250 threads examined this run (well beyond the normal 50/page minimum, done to confirm nothing was missed given the broken label filter)
- SPAM/SUSPICIOUS: 0 | NOT_SPAM (newly labeled): 0 | Already AI-Reviewed (skipped, not reprocessed): 250
- Moves by sub-label: Advertising 0, Fraud 0, Expired-OTP 0, Investor-Outreach 0
- Fixed by fix-up pass: 0
- Moves confirmed by verification: N/A (no moves made)
- MOVE_FAILED: none

## Notable finding (flagged to user via notification)
The Gmail search tool's negative label filter (`-label:Label_33`, `-label:Label_37`, and `-label:AI-Reviewed`) does not actually exclude labeled threads — confirmed via direct comparison. This means the "normal run" query in the v9 playbook cannot rely on the exclusion to scope to unprocessed mail; it returns recent mail regardless of review status. Newest-first ordering means genuinely new mail still surfaces at the top, so this run's manual verification found nothing missed, but future runs should either keep doing this manual labelIds check or fix the query approach, since paging cost will grow as reviewed mail accumulates.

## Outcome
Mailbox fully caught up — no unprocessed mail found, no spam to move. Flagged the search-filter bug to Raj via push notification since it affects the automation's reliability going forward.
