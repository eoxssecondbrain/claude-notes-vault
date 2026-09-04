---
thread_name: "team-access-management-sop"
user: "humaira"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Team Access Management SOP

**User:**
[Uploaded two screenshots]
Image 1: Notes thread on an Odoo task. Note by Ron - 9 minutes ago: "@Humaira Zainab - Correction, "Only you, Hashir and Aryan should have admin access to the instance."" Note by Ron - 10 minutes ago: "@Humaira Zainab - Who has access to what, you should have full visibility on it, which developer has access to which instance and you need to make a SOP for the same to ensure that we have that aligned across the board for all instances. Only you, Hashir and Aryan should have access to the instance." Note by Humaira Zainab - a day ago: "@Ron - What should be the next steps on this." Maria Naeem - 22 days ago: "Task created."

Image 2: Odoo task detail page. Title: "Create Standard Operating Procedure for Team Access Management". Project: Build Team. Customer: EOXS. Ownership: Ron. Dev State: Developing. QA State: QA. Progress: 0%. Description: "Create a Standard Operating Procedure (SOP) for providing and managing system access for team members. The SOP should clearly document the process for requesting, approving, granting, reviewing, modifying, and removing access, along with the required permissions and access levels. The goal is to ensure team access is provided consistently, securely, and according to the defined process."

Check this and create SOP

**Assistant:**
Two screenshots: an implementation task ("Create Standard Operating Procedure for Team Access Management," owned by Ron, project "Build Team," client EOXS, status Assigned/Developing/QA) and its notes thread. Ron's correction: admin access to "the instance" should be limited to you, Hashir, and Aryan. His ask: full visibility on who has access to what, which developer has access to which instance, and an SOP to align this across all instances.

Building this SOP properly means pulling actual current access data across the EOXS instances (DPS, EOXS Teams, Greer, Sabre Alloys, and whichever others exist) rather than writing generic policy text. That's a real research task, not a lookup, so pick a rigor level:

5ft — Quick: SOP built from the standard access-management template + whatever access info is already documented in wiki/assets, no live per-instance verification.

10ft — Verified: same, but I query each live instance (DPS/EOXS Teams/Greer/Sabre Alloys/etc.) directly for current admin/user access lists and confirm Ron's correction (only you, Hashir, Aryan) against reality before writing the SOP.

50ft — Deep: 10ft plus flagging any access misalignments I find across instances (e.g. someone with admin who shouldn't have it), and checking for an existing access-related SOP asset to avoid duplicating/conflicting with it.

Which level?
