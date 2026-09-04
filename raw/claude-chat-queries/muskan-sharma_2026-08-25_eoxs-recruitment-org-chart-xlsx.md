---
thread_name: "eoxs-recruitment-org-chart-xlsx"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

# EOXS Recruitment Org Chart — Excel build

## User

I need you to create a professional organizational chart in an Excel (.xlsx) file based on the information in the attached screenshots/file.
Top-Level Hierarchy
Put Rajat Jain at the very top as the Overall Lead.
Under Rajat Jain, create the TL/team structure based on the following reporting information:
TL Structure
Raj
	●	Jaee Moharir
	●	Kushali Chauhan
Ron
	●	DIVYANSH SHARMA
	●	Kashish Chauhan
	●	Ankush Justa
	●	Shubham Sharma
	●	Bhoomi
	●	Parshant Sharma
	●	Tanya Shrivastava
Isha
	●	Ankita Sharma
	●	Muskan Sharma
	●	Nisha Attri
Ayan
	●	Shubham Pathania
	●	Prachi Mahajan
	●	SNATA DAS
	●	PRIYANSHI SINGH
Additional Candidate List
Also include these candidates in a separate Candidate List worksheet because their TL/reporting information is not provided in the screenshot:
	●	Harsh Yadav
	●	Dhruv Maheshwari
	●	Hitesh Parmar
	●	Dhanshree Ratneria
	●	Yash Sharma
	●	Himanshu Kumar
	●	Pragya Kumari
	●	Aakrist Sharma
	●	Jatin Rao
	●	Lakshit Singh
	●	Somil Srivastava
	●	Tanvi Kumari
	●	Abhinav Samuel
	●	Mohan Dwivedi
	●	Utkarsh Sharma
	●	Abhishek Maurya
	●	Vaibhav Tez Shakya
	●	Vickey Kumar
	●	Shubham Srivastava
Excel Requirements
Create a polished Excel workbook with these sheets:
	1.	Org Chart
	●	Rajat Jain at the top.
	●	Raj, Ron, Isha and Ayan beneath Rajat Jain.
	●	Their respective team members below each TL.
	●	Use actual Excel cells/shapes/SmartArt-style layout where possible.
	●	Use connecting lines/arrows to clearly show reporting relationships.
	●	Make it visually clean and easy to understand.
	2.	Candidate List
	●	Include all 19 additional candidates.
	●	Add columns such as:
	●	Candidate Name
	●	TL
	●	Status
	●	Remarks
	●	Since their TL is currently unknown, leave the TL column blank rather than guessing.
	3.	Reporting Data
	●	Create a simple table containing:
	●	Name
	●	TL
	●	Include all names for whom reporting information is available.
Design
Use a professional corporate style suitable for sharing with HR/management.
	●	Rajat Jain: dark blue/highest-level box
	●	TLs: another professional blue shade
	●	Team members: light blue/grey boxes
	●	Clear hierarchy and spacing
	●	Bold names
	●	Proper alignment
	●	Borders where appropriate
	●	Freeze panes where useful
	●	Auto-adjust column widths
	●	Add a clear title such as "EOXS Recruitment Team – Organizational Chart"
Important: Do not invent reporting relationships for the 19 additional candidates. Keep their TL information blank unless it is explicitly provided.
Finally, provide the completed .xlsx Excel file. make it excel sheet

## Assistant

[Asked craft level via AskUserQuestion: Sketch / Draft / Painting / Commissioned. User selected: Draft.]

[Built EOXS_Recruitment_Org_Chart.xlsx with openpyxl, recalculated via LibreOffice (0 formula errors, 5 formulas), rendered to PDF/PNG and visually verified all three sheets.]

Delivered: EOXS_Recruitment_Org_Chart.xlsx

Note: no screenshot or file actually came through with the message — only the typed text. Everything in the workbook comes from what was typed, nothing else.

Three sheets:

Org Chart — Rajat Jain (dark navy) at top, a horizontal bus dropping to Raj / Ron / Isha / Ayan (medium blue), each TL with a left spine and elbow connectors into their members (light blue). Built from merged cells with border-drawn connector lines, gridlines off, title row frozen, landscape fit-to-width for printing. Legend and a source note at the bottom.

Candidate List — 19 names, TL column left blank, Status column with a dropdown (Applied / Screening / Interview / Offer / Joined / On Hold / Rejected), Remarks free text. Autofilter, banded rows, frozen header. A note below the table states the TL column is intentionally blank.

Reporting Data — Name / TL for all 20 rows where reporting is known: the 4 TLs → Rajat Jain, plus the 16 team members → their TL. Side table computes team size with COUNTIF (Raj 2, Ron 7, Isha 3, Ayan 4, total 16), so it self-corrects if rows are added.

One thing worth flagging: Ron carries 7 of the 16 assigned people — 44% of the assigned team under one TL, versus 2 under Raj. If the 19 unassigned candidates get distributed without accounting for that, the imbalance widens. Worth deciding the split deliberately rather than by default.
