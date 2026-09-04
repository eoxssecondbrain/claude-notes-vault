---
thread_name: "spam-detection-run-2026-09-01"
user: "raj"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

# Scheduled Email Spam Detection (v9) — Run 2026-09-01

**Trigger:** automated scheduled task, no user present.

## Setup
- Checked labels via `list_labels`: AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, AI-Reviewed all already existed (AI-Reviewed already applied to 24,575 threads historically) — treated as a normal run, not first run.
- Fix-up pass (`label:AI-SPAM in:inbox`): 0 threads found — nothing needed fixing.

## Normal run
Query: `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginated across 4 pages (backlog is old unprocessed mail from April–May 2021; the mailbox has a large unreviewed historical backlog, estimate fluctuated 804→201→1407 across calls, Gmail's resultCountEstimate is not reliable/stable).

Processed 200 threads total across 4 pages:
- Page 1: 50 checked → 31 NOT_SPAM (AI-Reviewed), 19 SPAM (17 Advertising, 2 Expired-OTP)
- Page 2: 50 checked → 32 NOT_SPAM, 18 SPAM (18 Advertising)
- Page 3: 50 checked → 32 NOT_SPAM, 18 SPAM (18 Advertising)
- Page 4: 50 checked → 29 NOT_SPAM, 21 SPAM (21 Advertising)

**Totals this run:** 200 checked · 124 NOT_SPAM/AI-Reviewed · 76 SPAM/SUSPICIOUS
- AI-SPAM/Advertising: 74 (Crunchbase newsletters, ZoomInfo newsletters, BestBuy ads, Zoom "joined your Personal Meeting Room" / recording-ready / meeting-deleted pings, Favro activity digests, DocuSign "viewed your document" and discount-promo emails, Fiverr message-activity notifications, LinkedIn social notification, a customer-feedback survey solicitation)
- AI-SPAM/Expired-OTP: 2 (DocuSign "Verify a New Device" codes from 2021, well past 24h)
- AI-SPAM/Fraud: 0
- AI-SPAM/Investor-Outreach: 0

Classification notes/judgment calls:
- Treated eoxs.com/eoxsteam.com senders, and threads where an EOXS colleague (not just the mailbox owner) appeared in To/Cc, as skip-listed NOT_SPAM.
- Contracts, NDAs, offer letters, DocuSign completions/send-for-signature, invoices/receipts, Rogers bills, and calendar invites/updates/cancellations (Google Calendar and Calendly) were treated as skip-listed NOT_SPAM.
- "Viewed your document" DocuSign notifications, Zoom join/recording/meeting-deleted pings, Favro digests, newsletters, and Fiverr "you've received messages" activity pings were treated as bucket-3 Advertising spam (FYI-only automated notifications).
- Zoom "exceeded cloud recording storage limit" alerts were treated as NOT_SPAM (actionable account/service alert, not FYI-only).
- Internal Odoo/EOXS test-environment quotation emails (odoxsofthubtest@gmail.com, "Grand Metals" test account) were treated as NOT_SPAM business records.

**Verification:** after each page's `mark_thread_spam` calls, re-ran `label:AI-SPAM in:inbox` — returned empty every time (0 threads still in Inbox). All 76 moves confirmed. 0 MOVE_FAILED.

**Errors:** one transient `label_thread` call ("service currently unavailable") on thread 178dacff9e7eada2 — retried once and succeeded.

## Remaining backlog
Backlog is large (over a thousand older threads still unlabeled, mostly 2021-era Zoom/Calendly/Crunchbase/DocuSign mail). Not fully cleared this run — stopped after 200 threads to keep the run bounded. Already-labeled threads are excluded from the query automatically, so the next scheduled run will continue further back into the backlog without reprocessing today's work.

## Notification decision
No push notification sent: no fraud/phishing found, no investor-outreach spam found, no MOVE_FAILED, nothing requiring the user's attention. Routine, successful spam-filter maintenance.
