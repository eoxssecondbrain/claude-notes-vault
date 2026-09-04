---
thread_name: "company-card-subscription-tracker"
user: "Harsimran"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

User: i want to create a proper system for the employees that what they have purchase or had subscription from the company's card, cause when they leave , the company still got charged for the subscriptions

Assistant: [Asked clarifying questions via AskUserQuestion tool]
Q1: What should I build for tracking employee purchases/subscriptions on the company card?
Options: Spreadsheet tracker + policy (recommended) / Interactive dashboard / Just the process/checklist
Q2: How do employees currently pay for subscriptions — a real card management tool, or a shared/individual card tracked manually?
Options: Ramp/Brex/Divvy/Airbase etc. / Regular company credit/debit card(s) / Not sure / mixed

User answers: "Spreadsheet tracker + policy", "Regular company credit/debit card(s)"

Assistant: [Built and delivered two files via SendUserFile]

Final response to user:
"Built two files:

- **Company_Card_Subscription_Tracker.xlsx** — 4 tabs: Instructions, Subscription Tracker (log every purchase, with employment status, renewal date, auto-renew), Offboarding Checklist, and a Dashboard that auto-flags (red) any subscription still active for an employee marked "Departed," and (orange) renewals due in 30 days.
- **Company_Card_Subscription_Policy.docx** — short policy making the offboarding review mandatory before final clearance, so a leaving employee's subscriptions get cancelled/transferred instead of forgotten.

Note: this didn't clearly match any of your saved skills (not an EOXS data lookup or thread-synthesis task), so I built it from general process design instead of a skill.

To use it: log purchases as they happen, and run the Offboarding Checklist every time someone leaves — that closes the gap you described."

Details of xlsx workbook built:
- Sheet "Instructions": how-to-use guide, column legend for Employment Status, Status, Auto-Renew, Offboarding Action.
- Sheet "Subscription Tracker": columns ID, Employee Name, Department, Card Used (Last 4), Vendor/Subscription, Category, Business Justification, Billing Frequency, Cost per Billing Cycle, Start Date, Next Renewal Date, Auto-Renew (Y/N), Approved By, Employment Status, Departure Date, Subscription Status, Last Reviewed Date, Offboarding Action, Notes. Includes one example row (Jane Doe, Canva Pro), 150 blank fillable rows with yellow-highlighted input cells, dropdown data validations for Category/Billing Frequency/Auto-Renew/Employment Status/Subscription Status, and conditional formatting: red row highlight when Employment Status="Departed" and Subscription Status is Active/Under Review; orange highlight when renewal due within 30 days.
- Sheet "Offboarding Checklist": employee name/departure date/reviewed by fields, 8-step checklist table with Done(Y/N), Date, Notes columns.
- Sheet "Dashboard": live formulas — Total active subscriptions, Total monthly-equivalent cost, Renewals due in next 30 days, Subscriptions tied to departed employees not yet cancelled/transferred, Auto-renewing subscriptions active, Subscriptions not reviewed in 90+ days. Recalculated via LibreOffice (recalc.py), 0 errors, 156 formulas.

Details of docx policy built: "Company Card — Purchase & Subscription Policy" with sections: 1. Purpose, 2. Scope, 3. Purchase & Approval Rules (table of purchase types/approval needed/logging requirement), 4. Logging Requirement, 5. Ongoing (Quarterly) Review, 6. Offboarding Process — the core fix (8-step mandatory numbered process tied to final clearance), 7. Roles & Responsibilities (table: Employee, Manager, Finance/Ops, HR), 8. Red Flags to Act On Immediately, 9. Review of This Policy. Rendered to PDF and visually verified (2 pages, correctly formatted tables and numbering).

Both files delivered to user via SendUserFile. Saved a fact to memory at /areas/company-card-tracking.md documenting the initiative, deliverable choice, and card setup (regular company card, no dedicated platform).
