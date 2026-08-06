---
thread_name: "who-is-priyanshu-sinha"
user: "jaskeerat"
type: claude-chat
created: 2026-08-06
updated: 2026-08-06
---

# Who is Priyanshu Sinha? (+ follow-up: weekly activity/productivity data)

## Turn 1
User: do you know about priyanshu sinha?

Assistant: Found via EOXS Team Live (Odoo) HR records — Priyanshu Sinha is a Startup Generalist Intern:
- Title: Startup Generalist Intern; Department: Startup Generalist (dept id 60, job id 50)
- Contract (hr_contract id 354): state=open, monthly, date_start=2026-07-21, wage=0.0 (stub)
- Employee record (hr_employee id 432): male, single, minimal fields
- Email/login: priyanshu1820sinha@gmail.com
- res_users id 460, res_partner id 506019 — created 2026-07-21, last write 2026-08-03, active
- Context: part of ~50-person MBA internship cohort per prior vault syntheses (raj_2026-07-29_eoxs-prospect-list.md, jaskeerat_2026-08-06_who-is-ankit-pachauri.md)
- Not found: HR Weekly Team Report emails, Fireflies/Fathom calls, support tickets, dedicated wiki page. Not named in Dhrup's 2026-07-31 Production Team Growth email (different track — Startup Generalist, not engineering).
- Unrelated: "Priyanshu Yadav" (Jan 2024 calendar invite) is a different person.

## Turn 2
User: Can you check if Priyanshu Sinha has any weekly activity or productivity data I might have missed?

Assistant: Ran an extensive second-pass search across emails, wiki, and the live Odoo DB directly. Confirmed NO weekly activity/productivity data exists for him anywhere in the vault:

**Emails searched (no hits for him specifically):** "priyanshu1820sinha@gmail.com", "Priyanshu Sinha", "Weekly Team Report", "HR Weekly Team Report", "Monthly Performance Summary", "productivity Sinha", "Hi Priyanshu Sinha", "Startup Generalist", "Cattr Priyanshu", "Time Champ", "Concern Regarding Low Productivity". Found many productivity-concern emails for OTHER staff (Jaskeerat Singh, Hashir Saleem, Ayan Dutta, Azra Saleem, Chandvi, Humaira Zainab, Kriti Jain) from isha@eoxsteam.com, but none naming Priyanshu Sinha.

**Wiki searched:** "Priyanshu Sinha", "Priyanshu Sinha — Weekly Reports", "Startup Generalist Intern", "weekly report overview", "MBA intern cohort", "Sinha", "Bidisha" — no dedicated page exists. Attempted direct file fetches of wiki/entities/eoxs-team/Priyanshu Sinha.md and wiki/analyses/hr-weekly-reports/Priyanshu Sinha.md — both "not found."

**EOXS Team Live (Odoo) DB queried directly (ground truth check):**
- hr_attendance WHERE employee_id=432 → 0 rows
- hr_timesheet_sheet_sheet WHERE employee_id=432 → 0 rows
- hr_leave WHERE employee_id=432 → 0 rows
- hr_contract confirms wage=0.0 (placeholder, not real financial data)

**Calls/tickets/tasks:** No Fireflies/Fathom mentions, no implementation task mentions.

**Interpretation (labeled as inference):** His contract start date is 2026-07-21 — only ~2 weeks of tenure as of the latest vault data (early Aug 2026). Isha Bisht's weekly productivity-concern emails (the mechanism that generates this kind of data for other interns like Ankit Pachauri, who has 8+ weeks of logged hours) have not yet included him. Also relevant: Rajat Jain's own 2026-08-04 "Product issue" email (id 272) explicitly flags that EOXS's internal HR/employee data has known hygiene problems ahead of 100 new interns starting — e.g. Nidhi Rana's job title is confirmed stale/wrong in that same email — so the absence of data could reflect either genuine non-tracking (too new) or a known data-quality/pipeline gap, not a search miss.

**Bottom line:** Unlike Ankit Pachauri (who has a full weekly hours/productivity % trail across May-Aug 2026), there is no equivalent activity trail for Priyanshu Sinha anywhere in the vault — email, wiki, or live Odoo attendance/timesheet tables.

## Sources
- EOXS Team Live DB: res_partner(506019), res_users(460), hr_employee(432), hr_contract(354), hr_department(60), hr_job(50), hr_attendance, hr_timesheet_sheet_sheet, hr_leave (all empty for id 432)
- Emails: id 272 (Product issue, 2026-08-04, Rajat Jain), id 30/24 (Team growth thread), ids 7457/7507/7514/7530 (Concern Regarding Low Productivity — other staff), id 60877 (AskCruz - EOXS clean up, re: HR weekly report page collisions)
- raw/claude-chat-queries/raj_2026-07-29_eoxs-prospect-list.md
- raw/claude-chat-queries/jaskeerat_2026-08-06_who-is-ankit-pachauri.md
