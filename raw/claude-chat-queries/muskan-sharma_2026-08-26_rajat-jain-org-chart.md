---
thread_name: "rajat-jain-org-chart"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-26
updated: 2026-08-26
---

## User

[Attached: Image 1 — reference organizational chart screenshot (Google Sheets), showing Rajat Jain/CEO at top, departments Product/Innovation Cell/Sales/PR with TLs Ron J, Ayan, Yashvir, and existing team members]
[Attached: Image 2 — WhatsApp screenshot list of names (Yash Sharma, Himanshu Kumar, Pragya Kumari, Aakrist Sharma, Jatin Rao, Lakshit Singh, Somil Srivastava, Tanvi Kumari, Abhinav Samuel, Mohan Dwivedi, ...) captioned "TL: Ayan"]
[Attached: Image 3 — WhatsApp screenshot of a spreadsheet table "Name | TL" with employees and their TLs, captioned "ask cruz team name of employee and TL"]

I want you to create an organizational hierarchy / org chart in Excel or Google Sheets format, using the first image as the exact visual/reference style.
I have provided 3 images:
1. Image 1: Reference organizational chart. Follow its structure, hierarchy, spacing, alignment, department grouping, and professional appearance.
2. Image 2: List of candidates/employees whose names need to be included.
3. Image 3: Employee/Intern names along with their TL (Team Lead / Reporting Manager). Use this to determine the reporting hierarchy.
Main requirement
Create a clean, professional organizational chart where:
Rajat Jain → CEO / Top Level
Then organize employees according to their respective TL / reporting manager from Image 3.
Data from Image 2 – Candidates
Include these names where applicable:
* Harsh Yadav
* Dhruv Maheshwari
* Hitesh Parmar
* Dhanshree Ratneria
* Yash Sharma
* Himanshu Kumar
* Pragya Kumari
* Aakrist Sharma
* Jatin Rao
* Lakshit Singh
* Somil Srivastava
* Tanvi Kumari
* Abhinav Samuel
* Mohan Dwivedi
* Utkarsh Sharma
* Abhishek Maurya
* Vaibhav Tez Shakya
* Vickey Kumar
* Shubham Srivastava
Reporting information from Image 3
Name	TL / Reporting To
DIVYANSH SHARMA	Ron
Kashish Chauhan	Reporting to Ron
Ankita Sharma	Isha
Muskan Sharma	Isha
Shubham Pathania	Ayan
Jaee Moharir	Raj sir
Ankush Justa	Ron
Shubham Sharma	Ron
Prachi Mahajan	Ayan
Nisha Attri	Isha
SNATA DAS	Ayan
PRIYANSHI SINGH	Ayan
Bhoomi	Ron
Parshant Sharma	Ron
Tanya Shrivastava	Ron
Kushali Chauhan	Reporting to Raj
Parshant Sharma	Ron
Important instructions
* Do not invent reporting relationships.
* If a person's TL is not available, place them in a clearly marked "TL Not Specified" section rather than guessing.
* Treat "Raj sir" / "Reporting to Raj" as Rajat Jain, unless the reference chart clearly indicates otherwise.
* Keep Ron, Ayan and Isha as reporting managers/TLs under Rajat Jain if that is consistent with the reference hierarchy.
* Put each employee underneath their respective TL.
* Preserve the hierarchy visually using connected lines/arrows or grouped cells.
* Use merged cells where appropriate.
* Make the chart look similar to Image 1: professional, clean, horizontal department/role sections, with names underneath their managers.
* Keep names properly spelled and capitalize them professionally.
* Avoid duplicate names. If the same name appears more than once, keep only one entry unless the data clearly indicates two different people.
* Make the spreadsheet easy to edit later.
Recommended hierarchy structure
Rajat Jain
CEO
↓
Team Leads / Managers
* Ron
* Ayan
* Isha
* Other confirmed managers from Image 1
↓
Employees / Interns
Place every person under their corresponding TL.
Excel formatting
Create the final output as an editable Excel (.xlsx) organizational chart.
Use:
* Professional corporate formatting
* Dark grey/blue header sections similar to Image 1
* Light grey boxes for roles
* White background
* Center-aligned names
* Wrapped text
* Borders around hierarchy boxes
* Consistent font and sizing
* Merged cells for department/role headings where necessary
* Enough spacing so names do not overlap
* Connected hierarchy lines wherever possible
Also create a second sheet called "Employee Reporting Data" containing:
Employee Name | TL / Reporting Manager | Role/Department | Status
Do not fabricate Role/Department information. Leave it blank where it is not provided.
Before finalizing, cross-check all names from Images 2 and 3 and make sure no provided person is accidentally omitted.

## Assistant

This task doesn't cleanly match the eoxs-data-general connectors (no EOXS data involved) — it's a standalone Excel build task, so I'm treating it as a straight xlsx-skill deliverable rather than pulling from EOXS/CRM data.

Before I build this, I need to flag one judgment call and confirm the polish level.

Judgment call I'm making unless you object: the 19 names in Image 2 (Harsh Yadav, Dhruv Maheshwari, Hitesh Parmar, Dhanshree Ratneria, Yash Sharma, Himanshu Kumar, Pragya Kumari, Aakrist Sharma, Jatin Rao, Lakshit Singh, Somil Srivastava, Tanvi Kumari, Abhinav Samuel, Mohan Dwivedi, Utkarsh Sharma, Abhishek Maurya, Vaibhav Tez Shakya, Vickey Kumar, Shubham Srivastava) all report to Ayan, since that screenshot is captioned "TL: Ayan." Everyone in Image 3 has an explicit TL already, so nobody lands in "TL Not Specified." Also treating "Isha" and "Yashvir" (Sales, from Image 1) as existing TLs I'm not fabricating reports for — no new data ties anyone to Yashvir, so Sales stays as-is from the reference chart.

[AskUserQuestion: "What craft/polish level for the Excel org chart deliverable?" → User selected: "Draft" — styled, functional, presentable, dark header bands, grey role boxes, merged cells, borders, matches Image 1's look without pixel-level tuning.]

[Built Org_Chart.xlsx with openpyxl: Sheet 1 "Org Chart" — title band, Rajat Jain/CEO header box, four columns (Ron, Isha, Ayan, Rajat Jain (Direct Reports)) with dark grey header row, light-grey bordered name boxes per TL, Ayan column split into "Existing Team" (Shubham Pathania, Prachi Mahajan, Snata Das, Priyanshi Singh) and "Candidates (Pending)" sub-groups (19 candidate names, green-tinted fill), connector arrows (▼) between levels, footnote documenting the Ayan/candidate assumption, the Raj sir→Rajat Jain mapping, and that Sales/PR/other reference-chart departments were left untouched since no new data was provided for them. Sheet 2 "Employee Reporting Data" — columns Employee Name | TL / Reporting Manager | Role/Department | Status, one row per person (36 rows: Rajat Jain + 35 others), Role/Department left blank throughout since not provided, Status = "Candidate" for the 19 Image-2 names and blank otherwise, "Reporting to Ron"/"Ron" normalized to "Ron", "Raj sir"/"Reporting to Raj" normalized to "Rajat Jain (Raj sir)", the one duplicate "Parshant Sharma" entry in Image 3 collapsed to a single row. Set landscape/portrait page setup with fit-to-width so the org chart columns and the data table print cleanly. Rendered to PDF/PNG and visually verified: all 4 TL columns fit on one page width, no overlapping text, footnote fully visible, and programmatically verified 36 unique names with zero duplicates, matching all 19 Image-2 candidates and all 16 unique Image-3 people (Parshant Sharma deduped) — nothing omitted, nothing invented.]

Delivered Org_Chart.xlsx.

Both sheets look clean and correct — all 35 names plus Rajat Jain, no duplicates, no omissions, no fabricated reporting lines.
