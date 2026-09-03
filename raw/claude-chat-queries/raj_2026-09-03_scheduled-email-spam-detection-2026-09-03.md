---
thread_name: "scheduled-email-spam-detection-2026-09-03"
user: "raj"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

## Scheduled Task: Email Spam Detection (v9) — run 2026-09-03

**Trigger:** automated scheduled task, no live user present.

### Fix-up pass
Query `label:AI-SPAM in:inbox` → 0 threads found. Nothing needed fixing.

### Run-size determination
AI-Reviewed (Label_37, 53,723 msgs / 29,464 threads) and AI-SPAM (Label_33, 7 msgs / 6 threads) both already exist and have been applied → this is a normal run, not a first run.

### Tool issue discovered
The specified query pattern `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed` (and label-ID equivalents like `-label:Label_37`) does NOT actually exclude already-labeled threads from `search_threads` results — every thread returned still carried the excluded label. Positive `label:X` queries and `-in:X` (folder) exclusions work correctly; only negated `-label:` filtering is broken in this Gmail connector. One call with the fully negated query returned a `resultCountEstimate` but no `threads` array at all.

### Workaround / verification performed
Since the documented exclusion query is unreliable, sampled ~150 threads via three alternate angles instead:
- 50 most recent threads mailbox-wide (`-in:sent -in:chats`, page 1)
- next 50 (page 2, back to 2026-08-28)
- 50 most recent unread threads (`is:unread -in:sent -in:chats`, back to 2026-07-01)

Every single thread across all three samples already carried Label_37 (AI-Reviewed) or was part of an already-reviewed thread. No thread was found needing classification.

### Outcome
- Checked (sampled): ~150 threads across recency/unread angles, plus fix-up pass query
- New SPAM/SUSPICIOUS found: 0
- New NOT_SPAM (AI-Reviewed applied): 0
- Fixed by fix-up pass: 0
- MOVE_FAILED: none
- No labels applied, no threads marked spam this run (nothing qualified)

### Conclusion
No backlog of unprocessed mail currently exists — recent activity (down to threads from early July, both by recency and by unread status) is already fully labeled. No user notification sent (nothing changed, no action needed). Flagging for a human/dev pass separately: the connector's `-label:` negation appears broken and should be fixed or worked around in the next iteration of this scheduled task's instructions (e.g., switch to client-side filtering on returned `labelIds` rather than relying on server-side negated label queries).
