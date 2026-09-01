---
thread_name: "askcruz-abc-ai-engineer-offer-letter"
user: "isha"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

## User

[Re-uploaded the same EOXS Employment Agreement PDF] "use this format please"

## Assistant

[Asked clarifying questions via AskUserQuestion since it was unclear which document to reformat and whether to keep offer-letter framing vs. switch to contract/agreement framing: (1) which document — Jaee Moharir's letter, all three letters, or something else; (2) whether to keep offer-letter framing (candidate accepts an offer) or switch to the source's Employer/Employee Recitals-based agreement framing.]

## User (question responses)

"Jaee Moharir's letter" and "Keep offer-letter framing" — rebuild only Jaee's most recent offer letter, adopting the uploaded EOXS agreement's visual/structural format (banner header, parties-style info box, underlined section dividers, boxed signature block) while keeping it framed as an offer letter rather than a binding Recitals-based agreement.

## Assistant

[Rebuilt Jaee Moharir's offer letter with a new docx-js script (build_jaee_eoxsformat.js) that mirrors the uploaded EOXS agreement's visual structure instead of the previous colored-heading template:
- Banner header: full-width navy table row with "ASKCRUZ" bold white + tagline "Consulting Meets Technology" on the left, "Offer Letter" label on the right (mirrors source's black logo banner with company name left / "Prata Inc" tag right)
- Centered title "EMPLOYEE OFFER LETTER" with "AskCruz • September 1, 2026" subtitle beneath (mirrors source's "EMPLOYMENT AGREEMENT / EOXS dba Prata Inc. / date" block)
- "OFFER DETAILS" section header with a full-width underline rule, followed by a shaded two-column "CANDIDATE / COMPANY" info box (mirrors source's shaded "PARTIES TO THIS AGREEMENT" EMPLOYEE/EMPLOYER table)
- "TERMS AND CONDITIONS" section header with underline rule, followed by all 19 numbered clauses as bold (non-colored, non-underlined) subheadings exactly like the source's "1. Position and Duties" style — same clause content as the previous version (role/responsibilities for Management Consultant, joining date, flat ₹28,000/month salary, Annual Compensation and Retention Amount table [₹28,000 → ₹3,36,000 annual → ₹1,00,800 retention (30%) → ₹2,35,200 remaining (70%) → ₹19,600/month equivalent], Retention Clause, 6-day/50-hour week, hourly shortfall clause with the 48-hour example, the portal-tracked Leave and Attendance clause, confidentiality, company property/data security, IP, code of conduct, performance, notice period, termination, resignation/handover, full and final settlement, applicable law, acceptance)
- "ACCEPTANCE" section header with underline rule and an acknowledgment line, followed by a single bordered rectangular signature box with two columns (EMPLOYEE | COMPANY (AskCruz)), each with Name/Signature-or-Designation/Date fields and underscore signature lines — mirrors the source's boxed EMPLOYEE/COMPANY signature block on its final page
- Footer: thin top rule with "AskCruz Offer Letter — Confidential" on the left and "September 2026" on the right (mirrors source's footer style)

Rendered to PDF and reviewed pages 1, 2, and 5 as images to verify the banner, parties box, underlined section dividers, clause numbering, salary table figures, and boxed signature block all rendered correctly and matched the source's structural motifs while keeping offer-letter (not contract/Recitals) framing and all AskCruz branding.

Delivered the file AskCruz_Offer_Letter_JaeeMoharir_EOXSFormat.docx to the user via SendUserFile with caption: "Jaee Moharir's offer letter rebuilt in the uploaded document's format — banner header, parties box, underlined section headers, and boxed signature block."]
