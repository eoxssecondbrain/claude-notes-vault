---
thread_name: "gmail-daily-label-routine"
user: "danish"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

User (scheduled routine): Categorize today's promotional/OTP emails in inbox by labeling only (no archive/trash/move). Steps: check/create Promotional and OTP labels, search category:promotions newer_than:1d and label matches, search OTP-subject-pattern newer_than:1d and label matches, don't touch anything else, end with one-line count summary.

Assistant: Found existing labels Promotional (Label_13) and OTP (Label_14) - no creation needed. Promotions search (in:inbox category:promotions newer_than:1d) returned 3 threads (YES Bank rewards, Keychron back-to-school sale, Netmeds offer) - all labeled Promotional. OTP search (in:inbox newer_than:1d subject:(OTP OR "one time password" OR "one-time password" OR "verification code" OR "security code" OR "login code" OR "sign-in code" OR passcode)) returned 0 threads - none labeled. No other emails touched, nothing archived/trashed/moved. Summary: 3 threads labeled Promotional, 0 threads labeled OTP.
