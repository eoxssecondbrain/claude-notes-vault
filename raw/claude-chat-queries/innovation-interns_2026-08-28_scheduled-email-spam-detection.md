---
thread_name: "scheduled-email-spam-detection"
user: "innovation_interns"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

## Turn (scheduled run, 2026-08-28)

**System/Scheduled Prompt:**
Scheduled Email Spam Detection

At each scheduled run, check Gmail using search_threads with query: in:inbox -label:AI-SPAM -label:AI-Reviewed  (pageSize 50, paginate with pageToken). Call list_labels first to get the label IDs; create any missing label with create_label. If get_thread is needed to read a body, use messageFormat PLAIN_TEXT..

For every new email:

1. Read the sender, subject, and email body.
2. Check for common spam and phishing indicators, including:
   - suspicious or misleading links
   - requests for passwords, OTPs, banking details, or other sensitive information
   - a one-time code, verification code, PIN, launch code, or magic sign-in link that is more than 24 hours old (the email DELIVERS a spent credential — this is not a request; codes under 24 hours old are still usable and must not be flagged)
   - fake prizes, offers, marketing emails or urgent requests
   - impersonation of companies or individuals
   - unusual sender information
   - suspicious attachments or instructions
2A. Before classifying, skip these entirely — mark NOT_SPAM without further analysis, and treat this as overriding every indicator in step 2:
   - sender domain eoxs.com or eoxsteam.com, or any eoxs address in To/Cc
   - security notices: "security alert", "new sign-in", "new login", "password was changed", "account was recovered", "passkey", "You shared some Google Account data with"
   - payment, invoice, receipt, or subscription-charge mail
   - calendar mail: subject starting "Accepted:", "Declined:", "Invitation:", "Updated invitation:", "Canceled event:"
   - auto-replies and out-of-office
   - offer letters, contracts, onboarding forms, repository or system access invitations
   - any code or sign-in link less than 24 hours old
   When torn between this list and a spam indicator, choose this list.3. Classify the email as SPAM, SUSPICIOUS, or NOT_SPAM.
4. If the email is SPAM or SUSPICIOUS, flag it by calling label_thread with the AI-SPAM label ID plus the matching sub-label (AI-SPAM/Advertising, AI-SPAM/Expired-OTP, or AI-SPAM/Fraud), and record the reason. Labelling is the only permitted write — never call mark_thread_spam, trash_thread, or archive anything.
5. If the email is NOT_SPAM, apply the AI-Reviewed label and nothing else.
6. Do not modify or delete the original email.
7. The Gmail labels are the record. Every thread ends this run carrying either AI-SPAM or AI-Reviewed. Do NOT write spam_detection_results.csv or any other local file — the container running this task is destroyed after every run, so a file cannot carry state to the next one.
8. Do not process the same email more than once.
9. At the end of the task, provide a short summary showing the number of emails checked and how many were classified as SPAM, SUSPICIOUS, and NOT_SPAM.

**Assistant response:**
Loaded the threads-ov skill, then attempted to run the spam-detection task. Called mcp__Gmail__list_labels first, per the task instructions, and it returned: "MCP server 'Gmail' requires re-authorization (token expired)". The session is non-interactive, so the OAuth flow cannot be run here. No emails were read, checked, or labeled this run — zero threads processed, zero labels applied. Sent a push notification to the user reporting the failure and asking them to re-authorize the Gmail connector via claude.ai connector settings so the next scheduled run can proceed.
