---
thread_name: "swi-consultant-resume-screening"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

User: You already have access to our company's data Ask Cruz, context, business, and hiring needs. Use that knowledge along with the JD below to screen candidates for the Software Implementation Consultant role.

Evaluate each resume based on the actual requirements of the role and what would make someone a strong fit for our company.

Hard requirements — disqualify if missing:

- Personally implemented software such as ERP, CRM, or similar; supporting or selling software alone is not enough.
- Comfortable with hands-on technical work such as SQL, APIs/webhooks, data mapping, and software/data integrations, without necessarily being an engineer.
- Able to train and work with skeptical, non-technical users and drive actual software adoption.
- No significant job-hopping pattern; look for reasonable stability in previous roles.

Nice-to-have: Experience with industrial/distribution businesses (steel, metals, building materials), early-stage SaaS, or working in a high-ownership environment.

Give each candidate a score out of 10 and a final decision: QUALIFY or DISQUALIFY.

Be strict and realistic. Do not give credit for skills or experience that are not clearly demonstrated. Prioritize candidates who have actually done implementation work rather than candidates who have only sold, supported, or demonstrated software.

I will share resumes one by one. Evaluate each candidate individually.

JD:

- US shift, work from home.
- Own the full path from signed contract to a client actively using AskCruz: configuration, data ingestion, OV setup, user training, and adoption.
- Onboard raw material distributors (15–50 employees) across steel, fastener, plastics, and lumber verticals.
- Map workflows such as quoting, inventory, and order desk into AskCruz's Company Brain/IRIS layer.
- Set up ERP connections, email/call transcript pipelines, and wiki seeding.
- Train non-technical users from floor/counter staff to operations managers.
- Act as the first escalation point for implementation-stage issues and monitor/report adoption to identify churn risk.

Assistant: Ready. Share the first resume and I'll score it against the hard requirements (implementation experience, technical hands-on work, non-technical user training/adoption, job stability) and the nice-to-haves, then give a score out of 10 and QUALIFY/DISQUALIFY.

[Candidate 1: AAKASH KAUSHIK — DISQUALIFY, 2/10, Program/Delivery Manager with no personal hands-on implementation work, no floor-staff training evidence, level/function mismatch with the role.]

[Candidate 2: PAVAN KUMAR YADAV K — QUALIFY with reservations, 7/10, LeadSquared Implementation Consultant, ~3 years, hands-on CRM implementation/SQL/API-webhook integration/floor-staff training claims all present but single employer, JD-mirroring language, and an odd "May 2026" end date flagged for interview verification.]

[Candidate 3: JEEVAANANTHAM R — QUALIFY, 8/10, Implementation Engineer with 5+ years delivering Focus X ERP implementations (Finance, Production, MRP, Inventory, Sales, Purchase, Fixed Assets modules) across India/US/UK clients, SQL Server & MySQL, custom reports, UAT, end-user training, three employers in 5 years with reasonable tenure and progression, no industrial vertical match but functional module overlap is strong, API/webhook gap and depth of "skeptical user" training to be probed in interview.]

[Candidate 4: KISLAY KUMAR — QUALIFY, 8/10, Senior Implementation Specialist at Apex Analytix (supplier/tax-compliance SaaS) with full implementation lifecycle ownership, strong SQL/REST API/data mapping evidence including a specific Markit/S&P Global integration, prior Infosys DevOps engineering background, only two employers in 6 years (strongest stability so far), but training evidence skews to admin-level users rather than floor/counter staff, no industrial vertical match.]

User: [Uploaded resume PDF: NANDITA JAISWAL]
NANDITA JAISWAL
Implementation Analyst | SaaS | Payroll & ERP Implementation
Bangalore, India | 6304436149 | nanditajaiswal22@gmail.com | LinkedIn

PROFESSIONAL SUMMARY
Implementation Analyst with 4+ years of experience in SaaS payroll implementation, ERP deployments, and enterprise data migration. Experience in onboarding 150+ SMB, mid-market, and enterprise clients across US payroll platforms. Adept at cross-functional collaboration, stakeholder communication, and translating complex technical requirements into seamless go-live outcomes.

PROFESSIONAL EXPERIENCE
Rippling | Implementation Analyst | 2024 – Present
- Led end-to-end payroll data migration for 150+ SMB, Mid-Market, and Enterprise clients, migrating from Gusto, ADP, and Paychex — achieving 95%+ go-live success rate.
- Reduced payroll discrepancy resolution time by ~30% by building structured tax-reconciliation workflows, ensuring compliance with US federal and state payroll regulations.
- Configured earnings, deductions, and employer/employee tax structures across 150+ accounts, supporting compliance across multiple US jurisdictions.
- Resolved 100+ post-go-live escalations on the Re-Import/Escalations team, improving client retention and reducing churn risk on complex payroll issues.
- Mentored 5+ new analysts, cutting average onboarding time by 20% through structured training documentation and shadowing sessions.
- Partnered with Engineering and Support teams to debug escalated issues, contributing to a 15% reduction in repeat escalations.

HighRadius Technologies | Associate Consultant I | 2022 – 2024
- Managed 10+ ERP implementation projects across APAC, EMEA, and North America from requirements through go-live.
- Reduced implementation cycle time by 25% by standardizing requirement-gathering templates and testing frameworks.
- Delivered process improvement recommendations that reduced post-go-live support tickets by 20% across managed projects.
- Developed and executed end-to-end UAT and regression testing strategies, achieving zero critical defects at go-live.

HighRadius Technologies | Associate Techno-Functional Consultant | 2021 – 2022
- Delivered 8+ treasury and cash forecasting implementations, automating financial data processes and reducing manual effort by ~40%.
- Used SQL for data analysis, integration troubleshooting, and data validation across ERP connections, managing the full project lifecycle end-to-end.

TECHNICAL SKILLS
Payroll Platforms: Rippling, Gusto, ADP, Paychex | ERP: SAP | Data & Analytics: MySQL, Power BI, MS Excel | CRM & PM: Salesforce, Jira | Domain: US Payroll Compliance, Payroll Migration, Treasury Implementation, Data Migration, Stakeholder Management, Client Onboarding

EDUCATION
B.Tech in Information Technology | KIIT University | CGPA: 9.3

User: check

Assistant: Nandita Jaiswal — QUALIFY. Score: 8/10.

Hard requirement 1 (personally implemented software) — met, strongly. Explicit hands-on configuration work: "configured earnings, deductions, and employer/employee tax structures across 150+ accounts," managed 10+ ERP implementation projects "from requirements through go-live," delivered 8+ treasury/cash forecasting implementations. This is concrete individual-contributor implementation work at real, identifiable companies (Rippling, HighRadius), not sales or support.

Hard requirement 2 (hands-on technical) — met. SQL for data analysis, integration troubleshooting, and data validation across ERP connections; end-to-end payroll data migration off Gusto/ADP/Paychex onto Rippling for 150+ clients. Migrating live payroll/tax data between systems is genuinely technical, high-stakes work — a stronger data-migration signal than most résumés in this batch.

Hard requirement 3 (training skeptical non-technical users) — the weak point. The only training evidence is mentoring 5+ new internal analysts — that's peer/employee training, not external client-facing training of non-technical end users. Nothing in the résumé explicitly claims she trained client-side HR/finance staff at the SMBs she onboarded, even though that's plausible given the role. This needs to be probed directly in interview since it can't be credited on inference alone.

Hard requirement 4 (job stability) — strong. Effectively two employers: HighRadius 2021–2024 (with an internal promotion from Techno-Functional Consultant to Associate Consultant I — a positive stability and growth signal), then Rippling 2024–present. No hopping.

Nice-to-haves: no industrial/distribution vertical experience — payroll/HR SaaS (Rippling) and treasury/AR automation (HighRadius) are a different domain from steel/fastener/lumber distributors. Not early-stage — both are established, well-funded companies. However, the sheer volume of her onboarding experience (150+ SMB/mid-market clients) is a strong proxy for the repeatable, high-throughput onboarding motion this role needs, and her post-go-live escalation work explicitly ties to reducing churn risk — a direct parallel to the JD's "monitor/report adoption to identify churn risk" line.

This is one of the stronger candidates on paper: real data migration and configuration work, good technical depth, excellent stability, and directly relevant churn-risk/escalation experience. The one thing to verify in interview, not assume, is whether she has actually trained non-technical, resistant end users herself, or whether that work sat with a separate customer-success function at her employers.</content>
