---
thread_name: "scheduled-spam-detection"
user: "raj"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

[SCHEDULED TASK] Scheduled Email Spam Detection (v4) fired automatically. Task: scan mailbox for spam/phishing/suspicious/investor-outreach emails, label and move confirmed spam to Gmail Spam, label everything else AI-Reviewed.

[ASSISTANT] Ran the full v4 procedure: called list_labels, found AI-SPAM/Investor-Outreach sub-label missing and created it; determined this was a normal run (AI-Reviewed already had history). Queried -in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed and processed 15 batches of 50 threads (750 total) from newest back to ~May 2025, classifying each against the v4 rules (skip-list overrides, expired-OTP >24h, unsolicited investor/VC/PE outreach with no prior sent-mail relationship, phishing/fraud DocuSign-style requests, marketing/advertising cold pitches).

Results: 689 threads labeled AI-Reviewed (NOT_SPAM). 61 threads labeled AI-SPAM + sub-label then moved to Gmail Spam via mark_thread_spam (all confirmed removed from normal search afterward): 45 AI-SPAM/Advertising, 6 AI-SPAM/Fraud (fake DocuSign funding-application and lease-agreement phishing emails), 6 AI-SPAM/Investor-Outreach (K1 Investment Management/Katie Rogers, Guidepost Growth Equity x2, Lone View Capital, LLR Partners, SGEP/Tobias Lange — all verified via in:sent search showing zero prior replies from rajat@eoxs.com), 4 AI-SPAM/Expired-OTP (bare Docusign verification codes >24h old with no "new device/login" framing).

Discovered a platform limitation: Gmail strips custom labels (including the AI-SPAM/* audit sub-labels) when a thread is moved into the system Spam folder via mark_thread_spam — verified via search that spammed threads no longer carry Label_33/34/35/36/38, even though the move itself succeeded. This breaks the intended audit trail persistence described in the task spec; flagged to the user.

Backlog is far larger than a typical "gap after downtime" — search estimate grew to 1,400+ remaining unprocessed threads still going back before May 2025, out of ~19,820 total threads in the mailbox. Did not attempt to clear the full backlog in one run given the scale; stopped after 750 threads and notified the user via push (real phishing/fraud and unsolicited investor outreach were found, plus the audit-label limitation and the unexpectedly large remaining backlog).
