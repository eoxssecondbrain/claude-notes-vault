---
thread_name: "swic-resume-screening"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

**User:**
You already have access to our company's data, context, business, and hiring needs. Use that knowledge along with the JD below to screen candidates for the Software Implementation Consultant role.

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

**Assistant:**
This is a standalone screening task — it doesn't call for EOXS data lookups (eoxs-data-general doesn't apply here), and threads-ov applies only for its mandatory transcript-save requirement, not as the primary skill for this work. Flagging that per your instruction rather than guessing.

JD and hard requirements are clear. Ready — send the first resume and I'll score it against:

Disqualifiers checked: personally implemented (not just sold/supported) ERP/CRM/similar software, hands-on technical comfort (SQL/APIs/webhooks/data mapping/integrations), ability to train skeptical non-technical users to drive adoption, no significant job-hopping.

Nice-to-have checked: industrial/distribution (steel/metals/building materials), early-stage SaaS, high-ownership environment.

Each candidate gets a score out of 10 and QUALIFY/DISQUALIFY, based only on what's clearly demonstrated in the resume — no credit for adjacent or implied experience.

**User:**
[Uploaded resume PDF: Rizwan Dirisina — NetSuite Functional Consultant — full text as previously logged]

"check this"

**Assistant:**
**Rizwan Dirisina — NetSuite Functional Consultant**

Score: 3/10
Decision: DISQUALIFY

Personally implemented ERP/CRM (hard requirement): Not clearly demonstrated. Nearly every bullet is framed as post-production support, day-to-day admin, monitoring integration logs, break-fix, and BAU maintenance on already-live NetSuite orgs (NetApp, Autodesk, Macy's — large enterprises, not SMB rollouts). One vague line mentions "new implementations, enhancements, and integrations" but it's not backed by any specifics on owning a client from signed contract to live use. This reads as a support/functional consultant profile, not an implementer.

Hands-on technical work: Present but narrower than the JD wants. CSV-based data migration, field mapping templates, custom fields/workflows, script-log debugging, third-party integration monitoring — real technical depth within NetSuite, but no SQL, no API/webhook work mentioned anywhere.

Training skeptical non-technical users / driving adoption: Only generic mentions ("user training on new processes," "training to users on CSV import process," "End User Training Materials"). No evidence of driving adoption or handling resistant users — sounds like documentation handoffs, not adoption ownership.

Job stability: Fine — TCS (Feb 2022–Sep 2023) then Itrope (Oct 2023–present), ~4.5 years total across 2 roles. Not a red flag.

Nice-to-haves: None. Clients are large enterprise (NetApp, Autodesk, Macy's) — no industrial/distribution exposure, no early-stage SaaS, no high-ownership environment signal.

Bottom line: This is an enterprise NetSuite support/BAU profile, not an implementation-owner profile. The core hard requirement — personally driving a client from contract to live adoption — isn't demonstrated. Send the next resume.

**User:**
[Uploaded resume PDF: Kuldeep Sharma — VP Delivery & Support Head — full text as previously logged]

"check this"

**Assistant:**
**Kuldeep Sharma — VP Delivery & Support Head**

Score: 2/10
Decision: DISQUALIFY

Personally implemented ERP/CRM: Not demonstrated. Every role from 2015 onward is a management/oversight title (Delivery & Support Head, AVP/VP Professional Services, Principal Consultant, Business Analyst) with bullets like "delegate the team on ERP implementation," "manage development team," "supported the team on giving training," "serve as liaison between developers and users." This is a person who runs delivery teams and liaises between client/developers — not someone personally configuring systems. The "50+ full life cycle implementations" claim has zero specifics behind it and reads as a generic resume-writer line.

Hands-on technical work: Essentially absent. One buried line — "developed using SQL Reporting services" — is the only concrete technical claim in 8 pages. No APIs, no webhooks, no integration work described as something he personally built. "Proactively explain the template to users for mapping the data" is him talking users through a template, not doing data mapping himself.

Training skeptical non-technical users / driving adoption: Delegated, not personal — "supported the team on giving continuous training," "developed a training plan," "dutifully prepared training manuals/videos." No indication he sat with resistant floor/counter-level users and drove adoption himself.

Job stability: 6 roles across ~15 years (2011–present), with a couple of short stints (~1 year at Octopus, ~1.5 years at Value C). Not extreme hopping, but combined with everything else it doesn't offset the fit problem.

Other red flags: The responsibility bullets are word-for-word identical across three different companies (NorthStar, Octopus, and near-duplicates elsewhere), and the platform list claims deep expertise across virtually every major ERP/CRM (SAP S4 HANA across 6+ modules, Maximo, SuccessFactor, Navision, Dynamics, NetSuite, Salesforce, SAP Business One, a "home grown ERP") — a breadth claim with no depth evidence anywhere, consistent with a templated or padded resume.

Seniority/role mismatch: This is a VP/Delivery-Head profile, not an individual-contributor implementation consultant. Even setting the above aside, someone titled VP Delivery & Support Head for the last 4 years is very unlikely to be a fit — or interested — in a hands-on, single-client-at-a-time IC onboarding role.

Nice-to-haves: None evident — no industrial/distribution vertical, no early-stage SaaS, enterprise IT-services environment rather than high-ownership startup.

Send the next one.

**User:**
[Uploaded resume PDF: Kuldeep Sharma — VP Delivery & Support Head — identical content, byte-for-byte the same resume as the one just submitted above]

"check this"

**Assistant:**
This is the same resume as the previous one — Kuldeep Sharma, identical content word for word. Already scored 2/10, DISQUALIFY. No new evaluation needed; send the next candidate's resume when ready.

**User:**
[Uploaded resume PDF: Deepak Kumar — Implementation Consultant II]

Deepak Kumar
deepakdhawan256@gmail.com
Hyderabad, India
9963936645
linkedin.com/in/deepak-kumar-a8a7811ba/

SUMMARY
Results-driven Implementation Consultant with 4+ years of experience delivering end-to-end B2B SaaS implementations, business analysis, and customer experience optimization. Proven record of reducing post-deployment rework and accelerating client time-to-value through data-driven workflow redesign, SQL-powered system optimization, and rigorous requirements engineering. Adept at bridging technical teams and business stakeholders to design scalable solutions and drive self-service adoption.

SKILLS
Solution Consulting, Requirements Gathering, Customer Workshops, Functional Specifications, Process Flow Documentation, SaaS Implementation, Customer Onboarding, System Configuration, Word, Excel, PowerPoint, Salesforce, Jira, UAT Coordination, Training & Knowledge Transfer, Stakeholder Management, SQL, Data Analysis, REST APIs, Workflow Automation, Change Management, ERP/CRM Integration, Cross-functional Collaboration, Post-Go-Live Support, Agile/Scrum, MySQL, Proof of Concept (POC)

EXPERIENCE
Implementation Consultant II — Highradius — 08/2025 – Current | India
• Monitored implementation KPIs, project scopes, and schedules to track platform performance, delivering workflow improvements that reduced post-deployment rework by 30%, measured across 8 enterprise accounts.
• Own end-to-end implementation lifecycle for assigned accounts — from kickoff and solution design through UAT, go-live, and hypercare.
• Conduct deep-dive analysis of client workflows to identify automation opportunities, reducing manual intervention in AR/AP processes by 35% across 5 enterprise clients.
• Collaborate with product teams to surface client-reported edge cases, directly influencing the product roadmap and reducing support escalations.
• Authored technical solution design documents and self-service training materials that cut average client onboarding time from 12 weeks to 8 weeks.
• Lead structured client onboarding programs for enterprise accounts, defining success criteria, milestones, and escalation paths from day one — ensuring alignment across client IT, finance, and operations teams.
• Build and maintain strong relationships with senior stakeholders at client organizations, conducting regular business reviews to track adoption metrics and proactively address risks before escalation.
• Coordinate cross-functional project teams spanning solutions engineering, product, support, and customer success to deliver implementations on schedule, maintaining 100% on-time go-live rate for assigned accounts.

Implementation Consultant — CRMNEXT — 01/2022 – 03/2025 | India
• Managed 10+ concurrent enterprise SaaS implementations, maintaining 95%+ client satisfaction scores and an average go-live 2 weeks ahead of contracted schedule.
• Drove end-to-end change management initiatives — stakeholder communication plans, training programs, and adoption tracking — ensuring on-time, on-budget delivery.
• Developed and executed complex MySQL queries to optimize CRM data management, reducing average data retrieval time by 40% and improving overall system performance.
• Led discovery workshops and requirements elicitation sessions with C-suite and department heads, producing BRDs, FRDs, and functional specifications for enterprise CRM implementations.
• Authored high-impact technical documentation assets — solution design specs, slide decks, and self-service training videos — ensuring voice and style consistency across clients.

EDUCATION
B.Tech in Computer Software Engineering — Kalinga Institute of Industrial Technology — 2022 | Bhubaneswar, OR — CGPA: 8.3

"check this"

**Assistant:**
**Deepak Kumar — Implementation Consultant II (Highradius), previously CRMNEXT**

Score: 7/10
Decision: QUALIFY

Personally implemented ERP/CRM/SaaS: Clearly demonstrated, in first-person ownership language rather than delegation. "Own end-to-end implementation lifecycle for assigned accounts — from kickoff and solution design through UAT, go-live, and hypercare" (Highradius); "Managed 10+ concurrent enterprise SaaS implementations... average go-live 2 weeks ahead of schedule" (CRMNEXT). This is a real step up from the first two candidates — it reads as someone who actually runs implementations, not someone who supports or oversees them.

Hands-on technical work: The strongest of the three so far. Explicit MySQL/SQL work with a concrete outcome — "developed and executed complex MySQL queries to optimize CRM data management, reducing average data retrieval time by 40%" — plus REST APIs, ERP/CRM integration, and workflow automation listed as active skills, not just familiarity. This is the first resume that ties a specific technical action to a specific result rather than a vague "good exposure" line.

Training skeptical non-technical users / driving adoption: Present and reasonably concrete — self-service training materials, onboarding time reduced "from 12 weeks to 8 weeks," adoption-metric tracking, proactive risk/escalation management. The one gap: his training experience is described as reaching C-suite/department heads and enterprise IT/finance/ops stakeholders, not floor or counter-level staff. The JD specifically needs someone comfortable training the least technical end of the user base (floor/counter staff at a 15-50 person distributor) — this resume doesn't show that population directly, only sophisticated enterprise stakeholders.

Job stability: Solid — CRMNEXT (01/2022–03/2025, ~3.2 years) then Highradius (08/2025–present, ~1 year), a ~5 month gap between them but only two employers across a 4.5-year career. No job-hopping concern.

Nice-to-haves: Weak on the specific ones you care about. Both employers are enterprise B2B SaaS/CRM vendors (Highradius does AR/AP automation, CRMNEXT is a CRM platform) — no industrial/distribution vertical exposure, not early-stage (Highradius and CRMNEXT are both established, well-funded companies with large account books, not scrappy startups), and the environment described (structured onboarding programs, cross-functional coordination across solutions engineering/product/support/customer success) reads as a mature, well-resourced org rather than high-ownership/scrappy.

One flag worth probing in interview: the resume is dense with round, favorable metrics (30%, 35%, 40%, 95%+, 100% on-time) with no sourcing — common in resume writing services and worth pressure-testing rather than taking at face value. But unlike the previous two candidates, the underlying job descriptions here are specific and technically grounded enough that I'd move this one forward, while probing in interview whether he's actually trained frontline/skeptical non-technical users (not just enterprise stakeholders) and whether the SQL/API work was truly hands-on versus directed.

Send the next one.
