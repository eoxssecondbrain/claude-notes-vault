---
thread_name: "scheduled-email-spam-detection"
user: "raj"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

# Scheduled Email Spam Detection Run — 2026-08-31

**Trigger**: Automated scheduled task (v3 spam detection spec).

## Step 0 — Repair pass
Searched `label:AI-SPAM -in:spam` (includeTrash=true): 0 results. No orphaned threads found (labeled but never moved to Spam). Nothing to fix.

## Step 1 — Run size determination
AI-Reviewed label already had 18,282 threads applied (from prior runs) and AI-SPAM/sublabels existed but had 0 threads — so this was NOT a first run. Used normal-run query: `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginated.

## Processing
Discovered a very large unprocessed historical backlog (inbox threads dating back to 2018 that predate this automation). Processed 12 pages (600 threads total) across the session, applying skip-list rules (eoxs.com/security notices/invoices/calendar mail/auto-replies/expired-code exclusions) and classifying the rest.

### Results this run
- Orphans found/fixed (Step 0): 0
- Threads checked (Step 1): 600
- NOT_SPAM (labeled AI-Reviewed): 565
- SPAM (labeled AI-SPAM + sublabel, moved to Spam folder): 35
  - AI-SPAM/Advertising: 31 (cold LinkedIn sales pitches, TechCrunch/Collision-adjacent conference marketing unrelated to a real registration, Best Buy/Expedia/Print Den retail promos, Google Ads upsell emails, LinkedIn engagement-bait notifications like "11 connections away" / "be recognizable on LinkedIn")
  - AI-SPAM/Expired-OTP: 4 (LastPass, Alibaba, Amazon, Tinder verification emails/codes, all 7 years old and unusable)
  - AI-SPAM/Fraud: 0
- SUSPICIOUS: 0 (no borderline cases required this tier this run — classification was confident either way)

### Notable non-spam observations (not actioned, flagged for awareness only)
- One 2019 internal email thread contained the user's actual credit card number and CVV shared in plaintext between team members (thread 168b72184711163b). Old and unrelated to spam classification, left untouched per task scope, but worth the account owner's awareness as a historical exposure.
- A large volume of legitimate historical vendor/business correspondence (Appinventiv, Design8 Creatives, upGrowth, Zeifmans, Swoop Airlines receipts, Eventbrite tickets, Google Workspace invoices, Indeed job-candidate notifications) was reviewed and marked AI-Reviewed — none of it was spam.

### Remaining backlog
This backlog goes back to at least December 2018 and was not fully exhausted in this run (resultCountEstimate stayed pinned at Gmail's capped "201" the whole time and did not reflect true remaining volume). Future scheduled runs will automatically continue from where this run left off, since already-labeled threads are excluded from the next run's search.

## Notification sent
Pushed a summary to the user: 600 processed, 35 moved to Spam (31 advertising, 4 expired codes), no active phishing/fraud, backlog continues next run.
