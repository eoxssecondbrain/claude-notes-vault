---
thread_name: "fastercapital-spam-misclassification-review"
user: "raj"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# FasterCapital email misclassification — review

**User (Nidhi, on behalf of Rajat):** Flagged that the FasterCapital follow-up email ("Re: FasterCapital:USA:EOXS:Insights & Next Steps" from celine.rai@fastercapital.com) was labeled AI-Reviewed instead of spam by the scheduled spam-detection task, and asked why — calling it a classic cold-outreach example and questioning whether the system is working.

**Claude's analysis:**
- Root cause: in the earlier scheduled run, classification jumped to bucket 4 (Investor-Outreach) because of the "Fundraising Associate" framing, found the prior-contact exception (rajat@eoxs.com had cold-emailed contact@fastercapital.com in 2023 and gotten a reply), treated that as clearing the email entirely, and defaulted to NOT_SPAM via the "if torn, default NOT_SPAM" fallback — without ever checking it against bucket 3 (Advertising), which the ruleset's own stated order (1→5) puts *before* bucket 4.
- Bucket 3 evidence present in the email: unsubscribe link repeated in every quoted layer of the thread, generic "Fundraising Associate" drip copy, follow-ups spaced Apr/May/Aug/Sep 2026 — classic automated marketing drip.
- Conclusion: this was an execution error (rule order not followed), not a defect in the scheduled task's prompt/ruleset itself. No change to the trigger's stored prompt was made or recommended.

**Action taken:**
- Thread `1a06d630cd9a1ec1`: removed AI-Reviewed (Label_37), applied AI-SPAM (Label_33) + AI-SPAM/Advertising (Label_34), called mark_thread_spam.
- Verification: get_thread on this ID now returns a permission error (consistent with Gmail blocking reads on spam-folder threads, and a change from before the move when the same call succeeded); `label:Label_34 in:inbox` returns no results for it. Direct read-back confirmation wasn't available, but the two indirect signals are consistent with a successful move.

**Outcome:** Thread reclassified correctly. No systemic rule change made — flagged as a one-off application error, corrected in place.
