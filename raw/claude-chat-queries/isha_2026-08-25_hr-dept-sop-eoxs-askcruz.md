---
thread_name: "hr-dept-sop-eoxs-askcruz"
user: "isha"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

**User (turn 4):**

create Ask Cruz employee conduct policies it should be in a ppt format and pdf with ptoffesional use chart and table if required  # ASKCRUZ
## New Joiner & Intern Induction Program SOP
**Department:** Human Resources
**Applicable To:** Interns & New Joiners
**System:** Odoo / Cattr / Approved Company Tools
**Prepared By:** HR Department
**Company:** AskCruz
---
# 1. Leadership & Key Contacts
[full content: leadership table (CEO Rajat Jain, Implementation Head EOXS Ron Jain, Implementation Head AskCruz Ayan Dutta, Manager Sheenam Rawat, HR Isha Bisht), Management Communication guidance; Section 2 Purpose of Induction Program (13 topics); Section 3 New Joiner/Intern Induction Checklist (16 HR onboarding items); Section 4 Communication, Work Hours & Availability (5-min response times, EST basis, communication standards); Section 5 Zoom & Video Call Etiquette (camera/background, meeting environment, meeting prep, dress code); Section 6 Cattr Time Tracking & Productivity (requirements, monitoring, compliance consequences incl. 2-week zero-hours = possible immediate termination); Section 7 Leaves & Time-Off (planned leave via Team EOXS portal 48hrs advance, sick leave >1 day needs medical cert within 48hrs of return, 5 sick + 5 casual leave entitlement/year, emergency leave, leave process flow); Section 8 Payroll & Reimbursements (reimbursement by 27th, salary by 7th, key dates table); Section 9 Work Output & Reporting (complete tasks, report progress, update trackers, ask questions, daily workflow); Section 10 ChatGPT & AI Tool Usage (approved usage, account setup, data protection, prohibited uses); Section 11 Tech Setup & Internet Reliability (equipment requirements, connectivity standards); Section 12 Workplace Conduct & Respect (zero tolerance, mutual respect, inclusive environment, professional conduct); Section 13 Professional Conduct With Management (general + CEO-specific numbered steps); Section 14 Data Protection & Intellectual Property (confidentiality, IP rights, data security); Section 15 Exit & Experience Letter Policy (complete full term, finish handover, return assets, manager confirmation, final settlement & experience letter, exit process flow); Section 16 HR Induction Completion (15-item sign-off checklist + signatures for HR Isha Bisht, Manager Sheenam Rawat, Implementation Head AskCruz Ayan Dutta, Implementation Head EOXS Ron Jain, CEO EOXS Rajat Jain).]

**Assistant (turn 4):**

Built a 19-slide professional PowerPoint deck (plus PDF export of the same deck) titled "AskCruz — New Joiner & Intern Induction Program / Employee Conduct Policies & Standard Operating Procedure," using only the content the user provided.

Design approach: loaded the pptx skill first, then built with pptxgenjs on a 13.3"×7.5" wide layout using a "Midnight Executive" palette (navy 1E2761 primary, ice blue CADCFC secondary, amber E8A33D accent, white). Visual motif: numbered circular badges (section number badge top-left of every content slide, small numbered/lettered badges within cards) repeated consistently across all slides — avoided any accent-stripe/color-bar decoration per design guidance. Dark navy background used for title and closing slides (sandwich structure), light background (F4F6FB) for all 17 content slides.

Slide-by-slide structure:
1. Title slide (dark navy, radial circle motif) — AskCruz, program title, department/system/prepared-by metadata.
2. Agenda — all 16 sections in two numbered columns.
3. Section 01 Leadership & Key Contacts — a styled table (Role/Name: CEO Rajat Jain, Implementation Head EOXS Ron Jain, Implementation Head AskCruz Ayan Dutta, Manager Sheenam Rawat, HR Isha Bisht) plus a card of Management Communication bullet guidance.
4. Section 02 Purpose of the Induction Program — 4×4 icon-badge grid of the 13 topics.
5. Section 03 New Joiner/Intern Induction Checklist — 16-item two-column checkbox list.
6. Section 04 Communication, Work Hours & Availability — three navy stat-callout cards (5 min / 5 min / EST) plus a Communication Standards card.
7. Section 05 Zoom & Video Call Etiquette — 2×2 numbered-badge card grid (Camera & Background, Meeting Environment, Meeting Preparation, Dress Code).
8. Section 06 Cattr — Time Tracking & Productivity — two side-by-side cards (Time Tracking Requirements, Productivity Monitoring) plus an amber "Compliance Consequences" warning card (disciplinary action / immediate termination risk).
9. Section 07 Leaves & Time-Off — a native pptxgenjs bar chart (Sick Leave 5, Casual Leave 5), a Planned/Sick Leave card, and a 5-step process-flow diagram (Plan → Submit → Approval → Take Leave → Submit Medical Doc).
10. Section 08 Payroll & Reimbursements — two big stat cards (27th / 7th), Reimbursement and Salary detail cards, and a "Key Dates at a Glance" table.
11. Section 09 Work Output & Reporting — 4-step arrow-connected card flow (Complete Tasks → Report Progress → Update Trackers → Ask Questions) plus a navy Daily Workflow summary bar.
12. Section 10 ChatGPT & AI Tool Usage — green "Approved Usage" card vs. red "Never Use AI Tools For" card, plus a bold misuse-consequence line.
13. Section 11 Tech Setup & Internet Reliability — 4 navy equipment cards (laptop, webcam, microphone, 10 Mbps internet) plus a Connectivity Standards card.
14. Section 12 Workplace Conduct & Respect — a navy zero-tolerance statement banner plus 3 numbered pillar cards (Mutual Respect, Inclusive Environment, Professional Conduct).
15. Section 13 Professional Conduct With Management — a white "When Speaking With Management" bullet card plus a navy "When Speaking With the CEO" 6-step numbered card.
16. Section 14 Data Protection & Intellectual Property — 3 numbered-badge cards (Confidentiality, Intellectual Property Rights, Data Security) plus a red consequence line.
17. Section 15 Exit & Experience Letter Policy — 4 numbered process cards plus an amber Final Settlement & Experience Letter card plus a 5-step process-flow diagram.
18. Section 16 HR Induction Completion — 15-item two-column checkbox list plus a navy Sign-Off bar with HR/Manager/Implementation Heads names.
19. Closing slide (dark navy) — "Welcome to AskCruz" with the full contact list recap.

QA performed: ran the pptx skill's validate.py (all validations passed), ran markitdown + grep for leftover placeholder text (none found), then rendered the deck to PDF and visually inspected all 19 slides. Found and fixed three real defects on the first pass: (1) title slide — the italic subtitle line was crowding/overlapping the wrapped two-line main title, fixed by reducing title font size and repositioning the subtitle, divider line, and metadata block; (2) Section 02 Purpose slide — the footer italic note was sitting too close to the page footer, fixed by nudging it up; (3) Section 08 Payroll slide — the Key Dates table was taller than its card and collided with the page footer (table row height didn't match the card height budget), fixed by resizing the stat/detail cards and enlarging the table's card. Rebuilt, re-validated (passed), and re-rendered all 19 slides to confirm every fix and that no other slide regressed.

Delivered both files to the user via SendUserFile: `AskCruz_Induction_Conduct_Policies.pptx` and `AskCruz_Induction_Conduct_Policies.pdf` (PDF exported from the same finalized deck via LibreOffice).
