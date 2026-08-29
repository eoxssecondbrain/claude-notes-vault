---
thread_name: "scheduled-gmail-spam-detection-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

# Scheduled Email Spam Detection (v3) — Run 2026-08-29

**Trigger:** Automated scheduled task, no live user present.

**Step 0 (repair pass):** Searched `label:AI-SPAM -in:spam` (includeTrash). Result: empty — 0 orphaned threads found/fixed.

**Step 1 (run size):** AI-SPAM and AI-Reviewed labels already existed with prior history (AI-Reviewed had ~11,895 threads applied) → normal run, not first run.

**Processing:** Searched `in:inbox -label:AI-SPAM -label:AI-Reviewed`, paginated pageSize 50. Processed 5 pages = 250 threads (backlog is old, dating to Dec 2021–Feb 2022). A large backlog remains (~8,000+ threads still unprocessed going further back in time) — normal for a long-running catch-up; left for future scheduled runs rather than exhausting one session on it.

**Classification approach:** Applied the skip list (eoxs.com/eoxsteam.com senders, security notices, payment/invoice/receipt mail, calendar mail, auto-replies, offer letters, outbound EOXS sales) as NOT_SPAM overrides. For the large volume of ambiguous B2B cold-outreach/investor/vendor pitches typical of a CEO inbox, treated them conservatively as NOT_SPAM (business development, not spam) to avoid false positives on a semi-destructive action (Spam folder auto-purges in ~30 days). Only flagged: classic scam-pattern cold pitches from personal Gmail addresses with poor grammar (SEO scams, recruiter spam), a sender impersonating a Google Workspace account manager (dellsworth@google.com, appeared twice), an OTP code sent in 2022 (long expired), and two pure consumer promotional blasts (TravelBrands, Crave).

**Results across 250 threads processed:**
- SPAM/SUSPICIOUS (labeled + moved to Spam): 10 total
  - AI-SPAM/Advertising: 7 (2 SEO-scam cold pitches from personal Gmail; 1 recruiter-outsourcing cold pitch from personal Gmail; 2 TravelBrands consumer sale blasts; 1 Crave subscription marketing blast)
  - AI-SPAM/Fraud: 2 (both from "dellsworth@google.com" impersonating a Google Workspace account manager — same sender, two separate threads, classic pretexting pattern)
  - AI-SPAM/Expired-OTP: 1 (Aeroplan verification code from Jan 2022, long past 24h)
- NOT_SPAM (AI-Reviewed): 240

**Notable finding:** This is the first run (of many, given ~25k+ prior AI-Reviewed messages) to ever apply the AI-SPAM label — previous runs apparently never encountered content matching a clear scam pattern in the batches they processed. The dellsworth@google.com impersonation sender is worth Raj's awareness since it specifically targets Google Workspace admins.

**Action taken:** Sent a push notification to Raj summarizing this run's findings (spam moved, phishing impersonation pattern found, backlog status).

**No changes made to email content itself** — only labeling and the mark-spam move on the 10 flagged threads, per task rules (no trash, no archive).
