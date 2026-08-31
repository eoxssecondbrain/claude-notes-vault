---
thread_name: "gmail-spam-detection-2026-08-31"
user: "raj"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

# Scheduled Email Spam Detection (v4) — 2026-08-31

## User turn (scheduled task prompt, automated firing)

At each scheduled run, call list_labels first to get label IDs. Match labels by exact name (case-sensitive) against this list: AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, AI-Reviewed. Only call create_label for a name with no exact match in that list — never create a label that differs only in case or nesting from one that already exists, and never create a label a second time.

*Scope:* this scans the whole mailbox, not just Inbox.

*Determining run size:*
- If the AI-Reviewed and AI-SPAM labels do not yet exist, or neither has ever been applied to any thread (i.e. this is the first run ever), treat this as the FIRST RUN: call search_threads with query -in:sent -in:chats sorted newest-first, pageSize 100, and process at most the 100 most recent emails (paginate with pageToken only up to that 100 cap).
- Otherwise (a normal run): call search_threads with query -in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed, pageSize 50, and process what comes back (paginate with pageToken if more than 50 unprocessed emails exist — this covers a gap after downtime).

[... full classification rules: spam/phishing indicators, investor-outreach rule 2a, skip list step 3 (eoxs.com domain, security notices, payment/invoice/subscription mail, calendar mail, auto-replies, offer letters), classify SPAM/SUSPICIOUS/NOT_SPAM, label_thread + mark_thread_spam sequencing, no double-processing, end-of-task report requirements ...]

## Assistant actions taken

1. Loaded raj-eoxs-vault-adjacent skill context per user preferences (threads-ov skill loaded and followed for this save).
2. Called list_labels: confirmed AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, AI-Reviewed all already exist as labels (Label_33 through Label_38, Label_37 for AI-Reviewed). AI-Reviewed already had 21,131 threads / 40,956 messages applied historically. AI-SPAM and all its sub-labels had 0 threads/messages — this was the first time AI-SPAM would ever be applied. Determined this was a NORMAL RUN (not first run) since AI-Reviewed had prior history.
3. Ran the normal-run query `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, and paginated through approximately 16 pages (~800 threads), covering the entire backlog gap from 2023 through today (2026-08-31), since AI-SPAM had apparently never been run before despite AI-Reviewed being active.
4. Classified each thread using the full ruleset: calendar/Zoom/Calendly/DocuSign system notifications, eoxs.com/eoxsteam.com internal mail, security alerts, payment/subscription mail, and auto-replies were skipped to NOT_SPAM per the mandatory skip list. Genuine investor/VC calendar bookings via EOXS's own "Invest in the future of Steel" outbound funnel were treated as EOXS-initiated (not unsolicited) and left NOT_SPAM. Existing vendor relationships (ZoomInfo, QuestionPro, AIPRM, Level Equity, Pragtech) were confirmed via in:sent history checks before exempting from Investor-Outreach/Advertising treatment.
5. Applied AI-Reviewed to ~770 NOT_SPAM threads.
6. Applied AI-SPAM + sub-label to 32 threads, then called mark_thread_spam on each (only after label_thread succeeded), moving them out of the mailbox into Gmail's system Spam folder:
   - AI-SPAM/Advertising (28): cold sales/marketing pitches (Googly VA, Journey platform under two domains, BlueSignal recruiter, Apex Boardroom, Internet Soft, Revenue Engineering webinar, Ascend Analytics, Vistage, Hustle Fund retreat, elemmir.net "Last try"/follow-up, getgrolmedia.com "Raj?"), pay-to-play magazine/award solicitations (industrywired.net), and unsolicited newsletters (distributionstrategy.com ×4, beehiiv.com SaaS newsletters ×2, indiafoodbrief.com TradeBriefs ×3, HICOOL startup-competition mass email, dataroomHQ, BairesDev referral program).
   - AI-SPAM/Investor-Outreach (2): Fells View Capital ("entrepreneur & veteran seeking to acquire"), FasterCapital's "RaiseCapital Program" — both unsolicited PE/accelerator cold intros with no prior relationship.
   - AI-SPAM/Fraud (2): a mass-BCC "national security"/family-offices chain email from joseph.o.chan@gmail.com, and a fake "your document has been completed" notice from sales@designsketchers.com mimicking a DocuSign completion alert.
   - AI-SPAM/Expired-OTP (0): none found this run.
7. Notable judgment calls flagged for Raj: two "erp.docusign.com" payment-failed emails (odd subdomain, could be spoofed) were kept NOT_SPAM per the explicit skip-list rule that payment/subscription mail is exempted regardless of other indicators — worth a manual look though old (Jan 2024).
8. Sent a push notification to Raj summarizing the run (32 moved to spam, breakdown by category, note on the DocuSign anomaly, note that AI-SPAM had never fired before this run, and that the backlog may not be fully exhausted so future scheduled runs will continue incrementally).

## Outcome
First-ever successful AI-SPAM pass on this mailbox. ~800 threads reviewed, ~770 marked AI-Reviewed, 32 moved to Spam (28 Advertising / 2 Investor-Outreach / 2 Fraud / 0 Expired-OTP). No threads were trashed or archived — only labeled and, for confirmed spam, moved to Gmail's Spam folder per the task's permitted action.
