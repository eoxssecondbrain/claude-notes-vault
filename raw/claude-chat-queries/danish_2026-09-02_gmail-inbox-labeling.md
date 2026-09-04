---
thread_name: "gmail-inbox-labeling"
user: "danish"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

**User:** Using the connected Gmail account, categorize today's promotional/marketing emails and one-time-use OTP/verification-code emails in the inbox by applying labels only (no archive/trash/move). Steps: check/create Promotional and OTP labels, search category:promotions newer_than:1d and label them Promotional, search OTP-related subjects newer_than:1d and label them OTP, don't touch anything else, end with one-line summary.

**Assistant:** Checked labels via list_labels — Promotional (Label_13) and OTP (Label_14) already existed, no creation needed. Searched "in:inbox category:promotions newer_than:1d" — found 11 threads (RBL Bank x2, Netflix, YES Bank, ICICI Bank, Amazon, Booking.com, Shine jobs, Samsung, TataCliq, TechConnect Daily) — applied Promotional label to all 11 via label_thread. Searched "in:inbox newer_than:1d subject:(OTP OR one time password OR one-time password OR verification code OR security code OR login code OR sign-in code OR passcode)" — 0 results, no OTP threads found/labeled. No emails archived, trashed, or moved. Summary: 11 threads labeled Promotional, 0 threads labeled OTP.
