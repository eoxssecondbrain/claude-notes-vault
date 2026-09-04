---
thread_name: "team-access-management-sop"
user: "humaira"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

[Turn 1]

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

[Turn 2]

**User:**
50ft

**Assistant:**
SOP drafted and attached, in the same document format used for your existing GitLab SOP. Key findings from the audit:

Grounding — the task exists because of a real incident: on January 19-20, 2026 a junior EOXS engineer, terminated the prior month, used server credentials that had been shared with him informally via text months earlier, and used them to sabotage the Sabre Alloys database. That's the "why" section in the SOP, and it's why the mandatory rules are strict on credential sharing and same-day revocation.

Current admin access vs. Ron's stated target ("only Humaira, Hashir, and Aryan"):

| Instance | Currently has admin | Aligned? |
|---|---|---|
| Discount Pipe & Steel | Aryan, Hashir, Humaira, Ron, Sheenam | No — Ron, Sheenam extra |
| Ohio Strip Steel (Greer) | Aryan, Hashir, Humaira, Ron | No — Ron extra |
| Sabre Alloys | Aryan, Hashir, Humaira, Ron | No — Ron extra |
| EOXS Team Live (internal) | Ayan Dutta, Danish Lari, Humaira, Rajat Jain, Ron | Not evaluated — internal tool, not a client instance |

One thing worth flagging before you act on this: Ron's own note excludes himself from the "only you, Hashir and Aryan" list, but he currently holds admin on every client instance. Worth confirming with him whether that was intentional before removing his own access — the SOP notes this rather than assuming.

Coverage gap: I could only verify live access on 3 of EOXS's 8 client instances (Discount Pipe & Steel, Greer, Sabre) — no DB connector in this session for 3GM Steel, Brannon Steel, Eastern States Steel, PPC Metals, or RW Conklin Steel. Those still need auditing before you can tell Ron the picture is complete. I flagged this in the document too.

No existing "team access management" SOP was in the asset library — this doesn't duplicate or conflict with anything.

This is read-only research — I didn't and can't change anyone's actual access. Executing the removals (Ron, Sheenam) is a separate action for whoever administers those instances.
