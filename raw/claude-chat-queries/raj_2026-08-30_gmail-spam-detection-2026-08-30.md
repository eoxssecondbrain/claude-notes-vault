---
thread_name: "gmail-spam-detection-2026-08-30"
user: "raj"
type: claude-chat
created: 2026-08-30
updated: 2026-08-30
---

# Scheduled Email Spam Detection Run — 2026-08-30

**Type:** Automated scheduled task (Gmail Spam Detection v3), unattended run.

## Step 0 — Repair pass
Searched `label:AI-SPAM -in:spam` (includeTrash: true) — 0 orphaned threads found. No repair needed.

## Run size determination
AI-Reviewed label already had 30,774 messages applied historically → treated as a NORMAL run (not first run). Query: `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginated.

## Result
Discovered the inbox has a massive unprocessed historical backlog dating back to 2020 (this appears to be Rajat's old personal/pre-EOXS mailbox, rajat@prata.ca, "The Steel Store" era) — far larger than the normal ~50/run expectation. Processed 9 pages (450 threads total) covering emails from 2020-08-07 down to 2020-07-07, and stopped there due to the scale (thousands of threads likely remain in this historical backlog).

- Checked: 450 threads
- SPAM/SUSPICIOUS (labeled + moved to Spam): 19
  - AI-SPAM/Advertising: Volvero newsletter (x2), FSC/thefifth.com, Data360 Labs bootcamp pitch, TikTok webinar (bigmarker), Fluid Identity webinar (bigmarker), F6S "you've been scouted" pitch, Guerlain beauty newsletter, Social Tradia Instagram-account-selling outreach (x4), TransferWise referral marketing, Mango.com sale blast — total ~13
  - AI-SPAM/Fraud: one Interac e-transfer notification with mismatched recipient name ("Hi Janu Bhaiya" vs account owner Rajat) — classic phishing pattern — 1
  - AI-SPAM/Expired-OTP: Plaid bank-link verification codes (x2, >24h old), WordPress activation link (expired), Mucker Capital password-setup link (expired) — 4
- NOT_SPAM (AI-Reviewed only): 431 — mostly calendar invites/RSVPs, Interac e-transfers from a verified recurring business relation (2727616 Ontario Inc.), building/delivery notices, recruiting correspondence, bank/legal/advisory correspondence, LinkedIn/Calendly/Zoom transactional notices, and eoxs.com-adjacent correspondence (Prata Inc → EOXS domain purchase/transfer threads).

## Not completed
This run stopped at 450 of a much larger remaining backlog (still deep in July 2020 mail) to keep runtime/resource use reasonable for one unattended firing. The label state (AI-SPAM / AI-Reviewed) means future scheduled runs will pick up exactly where this one left off — no work is lost or repeated.

## Notification sent
Pushed a notification to Raj summarizing: 450 checked, 19 moved to spam (1 phishing/fraud, 4 expired OTP/reset links, 13 marketing), 431 reviewed clean, and flagging that this mailbox has a much larger historical backlog than normal runs assume.
