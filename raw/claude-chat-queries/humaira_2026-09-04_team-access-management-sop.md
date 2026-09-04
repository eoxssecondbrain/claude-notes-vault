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

Grounding — the task exists because of a real incident: on January 19-20, 2026 a junior EOXS engineer, terminated the prior month, used server credentials that had been shared with him informally via text message months earlier, and used them to sabotage the Sabre Alloys database. That's the "why" section in the SOP, and it's why the mandatory rules are strict on credential sharing and same-day revocation.

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

[File attached: Team_Access_Management_SOP.docx]

[Turn 3]

**User:**
Okay, I want to connect this. Can you write on the top? Let's start from the top. Owner Ron, yes. Prepared by Humera Zenab, yes. Version 1. Why are you saying draft? Don't say draft. Effective date from today. Only related task. Management. Okay, define a single procedure for requesting approval, granting access. Why this SOP exists? This is the see, scope. Apply to all your organizations. Don't use word Odoo. We don't need that. Do not use it anywhere. Then, cover admin level setting, administration access. And general user access. Does not you not client side user created and managed by the client don't need to roles in instance access owner instance access owner Ron final approval for any admin level access grant change or removal or any client instance exit administration correct Humera maintain the master access register execute approved access change run the periodic review and it's the point of visibility for who has the access for what develop any york staff granted access to one or more instance to perform assigned work request access through this purpose does not self grant or share credentials next level definition and who typically holds it Admin setting action, full backend access user group, technical setting, developer mode, database level configuration, access owner, access administration, name, develop, developers. We don't need, we don't give a full backend access of any client server to developers. It only as Ron mentioned, Aryan and me and there are specific. But if you are just writing the idea then good. Functional admin. Full access with within one module area, sales, inventory, accounting without system level settings. Standard user, day-to-day operational access scope to, to assign modules. No, day-to-day operational access scope to assign task. Only project module. They standard user is project. They also they only get the uh, um, project module access purpose requesting access approving access granting access reviewing access modifying access removing access everything is good mandatory rule no credential sharing between individual under any circumstances no admin level access without the instance access owner approval logged in regular no access changes made outside this process including by developer with existing admin rights access is revoked the same day on termination without extension correct everything is correct now current state finding as of the of this review in this instance name should be discount pipe and steel ohio stripe formerly greer saber alloys eastern state steel ppc and then york steam live so we need to mention these clients uh, current admin access is whatever i can have access ron can have access aryan can have access hashir can have access raj can have access uh eox team x please remove eox team access from this we don't need that that's internal matter we are right now uh, for clients Client is discount pipe, Ohio, Saber Lois, ESS, Eastern State Steel, and PPC. We have five clients. In five clients, Hashir, Aryan, and me can have access, and Ron can have access. And we will remove all the other people. As Ron mentioned, uh,

**Assistant:**
All changes made:

- Version 1.0, no "Draft," Effective Date September 4, 2026, Related Task shortened to "Team Access Management"
- "Odoo" removed everywhere
- Scope now names the five client instances explicitly and excludes internal EOXS systems
- Admin access level now names the four people (Ron, Humaira, Hashir, Aryan) instead of "developers generally"
- Standard User restricted to Project module only
- Current-State Findings rebuilt for the five clients, EOXS Team Live row dropped, and the approved list now includes Ron — which resolves the earlier open question, so Greer and Sabre are now shown as aligned; only Discount Pipe & Steel has an actual gap (Sheenam)
- Eastern States Steel and PPC Metals are listed but flagged unverified — I still don't have live query access to those two instances in this session, so that gap is real, not just carried over text

One thing to flag: PPC Metals and Eastern States Steel access hasn't actually been checked yet, so "we will remove all the other people" isn't something I can confirm is fully executed until someone pulls their admin lists too.

[File attached: updated Team_Access_Management_SOP.docx]

[Turn 4]

**User:**
[Uploaded file: Team_Access_Management_SOP.docx]

convert it into pdf

**Assistant:**
[Converted the uploaded docx to PDF and attached: Team_Access_Management_SOP.pdf]
