---
thread_name: "scheduled-spam-sweep-2026-09-01"
user: "raj"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

## Scheduled Email Spam Detection (v9) — Run 2026-09-01

**Trigger:** Automated scheduled task, no live user present.

**Fix-up pass:** Searched `label:AI-SPAM in:inbox` — 0 threads found. Nothing needed fixing (the one pre-existing AI-SPAM thread, 17a94e9d6c91e4fb, was already correctly out of Inbox).

**Run type:** Normal run (AI-Reviewed already applied to 45,811+ messages historically; AI-SPAM already applied to 1 thread previously). Not a first run.

**Query used:** `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed`, pageSize 50 → resultCountEstimate 804 total unprocessed threads (old backlog, mostly from 2021).

**Page 1 processed (50 threads):**
- 44 classified NOT_SPAM → labeled AI-Reviewed (Label_37). Mix of: eoxs.com sender exemption, calendar invites/RSVPs (Accepted/Invitation/New Event from Calendly), security "New Device Login" alerts, DocuSign offer-letter completion/view notices, Odoo test sales-order/quotation emails, one VC calendar invite (Mucker Capital — protected by calendar-mail skip-list override).
- 6 classified SPAM:
  - 17a3962fb82d970c — "Your DocuSign verification code is: 751623" (expired OTP, 2021) → AI-SPAM/Expired-OTP
  - 17a35431c70f80b4 — "Verify a New Device" code 875518 (expired OTP, 2021) → AI-SPAM/Expired-OTP
  - 17a38f62e12759d4 — Crunchbase newsletter → AI-SPAM/Advertising
  - 17a3836ff54c1c5e — Best Buy newsletter → AI-SPAM/Advertising
  - 17a33cf8c7adf046 — Crunchbase newsletter → AI-SPAM/Advertising
  - 17a3372f3a3d53fd — Google Workspace upsell email → AI-SPAM/Advertising

**CRITICAL ISSUE FOUND:** After calling `label_thread` (succeeded) then `mark_thread_spam` (returned success) on all 6 SPAM threads, verification via `get_thread` failed with "The caller does not have permission" (distinct from the "not found" error a bad/nonexistent thread ID produces). Follow-up `search_threads` with `in:anywhere` (which per tool docs includes Spam and Trash) returned zero results for all 6 threads — they are not in Inbox, Spam, or Trash. This means `mark_thread_spam` hard-deleted these 6 threads instead of moving them to the recoverable Spam folder, contradicting the task's explicit assumption that this is a reversible action.

**Action taken:** Halted immediately. Did NOT process further pages of the 804-thread backlog. Did NOT call mark_thread_spam again. The 44 AI-Reviewed labels already applied are safe (label-only, non-destructive) and were left in place.

**Notified user via PushNotification** with full details and a recommendation to check Gmail/Workspace admin settings for an auto-purge-on-spam or retention policy, and to verify whether the 6 disappeared threads are recoverable.

**Remaining work:** ~750+ threads in the backlog still need classification once the mark_thread_spam issue is understood/resolved. Do not resume automated spam-moving until this is fixed.
