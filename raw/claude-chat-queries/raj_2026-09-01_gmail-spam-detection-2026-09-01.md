---
thread_name: "gmail-spam-detection-2026-09-01"
user: "raj"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

## Scheduled task: Gmail Spam Detection (v9) — run 2026-09-01

**Trigger:** automated scheduled task firing (no live user present). Normal run (AI-SPAM/AI-Reviewed labels already existed with prior history — not a first run).

**Fix-up pass:** searched `label:AI-SPAM in:inbox` — 0 threads found stuck in Inbox. Nothing to fix.

**Main run:** searched `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed` (pageSize 50), processed 4 pages = 200 threads (backlog of old, unprocessed mail dating to 2021; resultCountEstimate started at 804 and fluctuated down as pages were labeled — large remaining backlog still exists for future runs to continue).

**Results this run:**
- Checked: 200 threads
- NOT_SPAM (labeled AI-Reviewed): 160
- SPAM/SUSPICIOUS (labeled AI-SPAM + sub-label, then moved to Spam): 40
  - AI-SPAM/Advertising: 36 (Crunchbase/BestBuy/DocuSign newsletters & promos, "viewed/opened your document" DocuSign tracking pings, Favro activity notification, two trademark-scam solicitation emails self-labeled "- Advertisement")
  - AI-SPAM/Expired-OTP: 4 (DocuSign "verify a new device" codes, all 2021-dated, long expired)
  - AI-SPAM/Fraud: 0
  - AI-SPAM/Investor-Outreach: 0
- Moves confirmed by verification (re-check of `label:AI-SPAM in:inbox`): 40/40 confirmed moved out of Inbox, 0 stuck
- MOVE_FAILED: none
- Fixed by fix-up pass: 0

Skip-list heavy categories kept as NOT_SPAM: Calendly booking notifications, calendar Accepted/Declined/Updated/Canceled/Invitation mail, DocuSign "Completed"/contract/offer-letter emails, Google Drive/Docs/Sheets "invitation to edit/comment" (system access), invoices/quotations/sales orders from the team's own Odoo/EOXS demo/test accounts (odoxsofthubtest@gmail.com), any thread with an eoxs.com/eoxsteam.com sender or eoxs address in To/Cc, and genuine business correspondence.

No MOVE_FAILED threads, no Fraud or Investor-Outreach hits, nothing time-sensitive — routine backlog cleanup of 5-year-old mail. No push notification sent (per notification policy: no anomaly, no failure, nothing requiring Raj's attention right now). Remaining backlog (several hundred more old threads) will continue to be processed on subsequent scheduled runs since the same exclusion query picks up where this run left off.
