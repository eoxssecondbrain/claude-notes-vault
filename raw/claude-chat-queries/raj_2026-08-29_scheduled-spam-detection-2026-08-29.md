---
thread_name: "scheduled-spam-detection-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

# Scheduled Email Spam Detection Run — 2026-08-29

This was an automated scheduled task run (Scheduled Email Spam Detection v3), not an interactive user conversation.

## Summary of actions taken

**Step 0 — Repair pass:** Searched `label:AI-SPAM -in:spam` (including trash) to find orphaned threads labeled but never moved to Spam. Result: 0 orphans found. Healthy state.

**Step 1 — Run size determination:** AI-Reviewed label already had 7021 messages / 3294 threads applied historically, so this was treated as a normal run (not first run). Searched `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginating with pageToken.

**Processing:** Worked through 10 pages (500 threads total) of a large historical backlog (inbox mail from Dec 2024 – Feb 2025 that had never been reviewed by this system). For each thread, classified SPAM / SUSPICIOUS / NOT_SPAM per the skip-list rules (eoxs.com/eoxsteam.com senders, security alerts, payment/invoice mail, calendar mail, auto-replies, offer letters, codes <24h old) and spam indicators (marketing/cold-outreach, expired OTP/sign-in codes >24h old, phishing/fraud/financing-scam patterns).

**Results (500 checked):**
- NOT_SPAM (labeled AI-Reviewed): 446
- SPAM/Advertising (cold sales pitches, generic marketing blasts, newsletters unrelated to core steel-industry business — labeled AI-SPAM + AI-SPAM/Advertising, moved to Spam): 41
- SPAM/Expired-OTP (one-time codes / password-reset links / sign-in codes over 24h old, from Expedia, Healthians, Atlassian/Bitbucket, Contabo): 8
- SPAM/Fraud (unsolicited financing/loan "you've been selected" scams, a suspicious Contabo-impersonating alert sent from an unverified brevosend.com domain rather than contabo.com): 5
- Orphans fixed: 0

**Classification judgment calls of note:**
- Industry-specific content (Steel Market Update, AWMI Chicago, MSCI, CRU Group) was kept NOT_SPAM even though promotional in tone, since it's directly relevant to EOXS's steel/metals business — reserved the "Advertising" spam label for generic/unrelated cold pitches (VA outsourcing, web/app dev agencies, cold email tools, Reddit ads, "founders club" invites, ERC/business-loan solicitations, Odoo competitor pitches).
- Vendor account/transactional mail (Contabo billing/order alerts from the legit contabo.com domain, Healthians bookings/invoices, SHEIN/DHL/MakeMyTrip transactional notices, Google/Microsoft security alerts, SVB banking notices) kept NOT_SPAM.
- Flagged as Fraud: three "connection limit" alerts that used Contabo's exact template wording but arrived from `support@1671916.brevosend.com` instead of `support@contabo.com` — domain mismatch on a security-flavored alert is a phishing/impersonation indicator.
- A large volume of `info.eoxs@gmail.com` internal Odoo/ERP task notifications and employee leave-request emails (from eoxsteam.com / personal gmail addresses cc'ing HR) were all NOT_SPAM as ordinary internal business operations.

**Outstanding:** The backlog is larger than the ~402 initially estimated — after 500 threads processed, `in:inbox -label:AI-SPAM -label:AI-Reviewed` still returns further pages (Gmail's resultCountEstimate stayed around 201 per page fetch, which appears to be an approximate/refreshing count rather than a hard remaining total). This run stopped after 500 threads for practical turn-length reasons. Because AI-Reviewed/AI-SPAM labels are now applied to everything processed so far, the next scheduled firing will automatically continue with the next unprocessed batch — this is expected/by-design per the task's own instructions ("paginate ... this covers a gap after downtime or a backlog").

A push notification was sent summarizing the fraud finds and backlog status.
