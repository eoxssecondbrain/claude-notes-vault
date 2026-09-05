---
thread_name: "eoxs-askcruz-salary-structure"
user: "isha"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# EOXS/AskCruz Session Transcript

## Context
User: Isha Bisht, HR Executive at EOXS. Session covers salary structure queries, HR automation scheduling, and iterative creation of AskCruz-branded HR documents (resignation letters, termination letters, experience/relieving certificate) using real brand assets extracted from an uploaded genuine AskCruz offer letter.

## Key milestones this session
1. Salary structure query for EOXS/AskCruz — no fabricated percentages, reported factually.
2. "Analyze Isha's performance" request — raised twice, never matched a loaded skill, never fulfilled/withdrawn explicitly.
3. HR automation: scheduled weekly Friday 10PM IST check-in for pending resignations/probation, test email requested to isha@eoxsteam.com, then hreoxs@gmail.com, then eoxshr@gmail.com. Delivery status last known: PENDING (never confirmed received).
4. Document work (AskCruz rebrand of EOXS HR letters):
   - Anvitha_Resignation_letter.docx → AskCruz_Resignation_Letter_Template.docx (blank reusable template, header rebranded, www.askcruz.com / isha@askcruz.com, same phone).
   - Ankush Jasta termination letter (EOXS branding, 31 Aug 2026 termination date), then AskCruz version with new header/footer screenshots.
   - Bhoomi-style termination letter reused for employee "Abc" (same date, first name only).
   - Real brand assets extracted from AskCruz_Offer_Letter_JaeeMoharir_v4.docx: header (image1.png, 1485x297) → /tmp/real_askcruz_header.png, footer (image2.png, 1600x300) → /tmp/real_askcruz_footer.png, Rajat Jain's real signature (image3.png, 150x36) → /tmp/real_rajat_signature.png. Abc termination letter rebuilt with these real assets.
   - Prashant Kashyap resignation letter, AskCruz version, built with docx-js (/tmp/termgen/build_resignation_prashant.js), preserving verbatim wording/typos/date mismatch from user's screenshot ("effectiv", 31st Aug vs 13th Aug), delivered plain then with real header/footer added.
   - User asked for suggested resignation letter content in plain text (provided).
   - Kashish Chauhan experience/relieving certificate (HR Intern, 10-31 Aug 2026): built via /tmp/termgen/build_experience_letter.js using real header/footer/signature assets, per user instruction "use header and end page from pdf". Body text used verbatim as provided by user (5 paragraphs). Added closing signatory block (For AskCruz / Rajat Jain / CEO + real signature) on own initiative since user's text had none — flagged to user after delivery. Rendered, verified single-page layout, delivered via SendUserFile (file_uuid 83eeaa6c-c3f7-4669-9ab2-46a335a5af25).

## Technical patterns established
- docx-js (npm `docx`) used to build new letters from scratch; unzip/edit word/document.xml used for editing existing docs.
- Real brand assets (extracted from genuine AskCruz offer letter) now the canonical source for all AskCruz letters, superseding earlier hand-recreated/screenshot-cropped versions.
- Standard page setup: 12240x15840 twips, header image ~590x118, footer image ~590x111, signature image ~100x24, font size 22 (11pt), rendered/verified via LibreOffice headless + pdftoppm before every delivery to confirm single-page fit.
- User preference: preserve exact user-provided wording/dates even if inconsistent; flag judgment calls (e.g., added signature blocks, email address choices) explicitly after delivery rather than asking first when pattern is well-established.

## Pending/open items
- HR automation test email delivery to eoxshr@gmail.com never confirmed received.
- "Analyze Isha's performance" request never fulfilled.
- No further action requested by user as of last turn; awaiting feedback on Kashish Chauhan letter (particularly the added signature block).
