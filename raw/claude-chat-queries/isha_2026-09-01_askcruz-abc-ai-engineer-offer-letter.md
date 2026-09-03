---
thread_name: "askcruz-abc-ai-engineer-offer-letter"
user: "isha"
type: claude-chat
created: 2026-09-01
updated: 2026-09-03
---

## Exchange: New standalone AskCruz Confidentiality/IP/Restrictive Covenants document

User pasted a 10-clause legal block (Confidentiality & NDA, IP, Non-Compete/Non-Solicitation, Data Protection, Conflict of Interest, Professional Conduct/Defamation, Background Verification, Additional Clauses x2 duplicated, Governing Law/Jurisdiction) originally written for EOXS and asked to rebrand it for AskCruz only.

Asked 3 clarifying questions before proceeding:
1. Duplicate "Additional Clauses" (8 and 10, identical content) — user chose "Keep both as-is"
2. Clause 9 jurisdiction (India/Chandigarh/Delhi/Toronto) vs AskCruz's New Rochelle NY letterhead mismatch — user chose "Keep as written (Recommended for now)"
3. Destination — user chose "Just give me the text" (not inserted into any file)

Delivered the rebranded text in chat (EOXS -> AskCruz throughout, both duplicate Additional Clauses sections kept, jurisdiction clause left unchanged with a flagged note about the New Rochelle mismatch).

Follow-up: user said "give me word format". Built a new standalone docx titled "CONFIDENTIALITY, INTELLECTUAL PROPERTY & RESTRICTIVE COVENANTS — AskCruz" using python-docx, reusing the same AskCruz header_v2.png/footer_v2.png branding assets and matching heading/bullet style (Times New Roman, bold underlined section headings with bottom border rule, bullet lists) used in the Jaee Moharir offer letter documents. All 10 clauses included with both duplicate "Additional Clauses" sections intact and jurisdiction clause unchanged. Rendered to PDF via LibreOffice + pdftoppm and visually verified pages 1 and 4 (4 pages total) — clean formatting, consistent branding, no page-break/spacing issues.

Delivered: AskCruz_Confidentiality_IP_RestrictiveCovenants.docx via SendUserFile.
