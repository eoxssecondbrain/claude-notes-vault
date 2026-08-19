---
thread_name: "company-hierarchy-query"
user: "talal"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: Where we are with company heirarchy?

Assistant: I checked the company overview asset and searched the wiki, chat-summaries, and past saved threads for "company hierarchy" — nothing came back. It also isn't a clean match for the eoxs-data-general skill (that's scoped to correspondence, calls, implementation tasks, tickets, invoices, CRM).

"Company hierarchy" is ambiguous to me here. It could mean:

1. Odoo's technical company hierarchy — parent/child company records across the multi-instance fleet (Sabre, Eoxteams, velox, etc.)
2. EOXS/AskCruz org structure — reporting lines, who sits where
3. Status of a specific project or task literally named "company hierarchy" that I haven't found yet

Which one are you asking about, or is it something else entirely?

User: Which of those three did you mean?

User: AskCruz org structure — reporting lines, who sits where

Assistant: No formal org chart document exists for AskCruz that I could find. What follows is inferred from task-board activity, the weekly scrum report, and entity notes, not from a stated hierarchy document.

Rajat Jain (President, EOXS) sits at the top and manages AskCruz directly. He's not delegating through a middle layer, he pings individual contributors directly on tasks (Ron, Ayan Dutta, Sheenam), including pointed escalations when something's late.

Below him, no formal titles, but functional roles are clear from who does what:

Ayan Dutta — de facto technical and product lead. Heaviest task load across every board (AskCruz, Customer 1 - EOXS, Idea Board), owns backend, MCP integration, and access-rights work. His own account of his EOXS trajectory: started as Junior LDR, moved through product and implementation, and by January 2026 was operating as Rajat's Associate on broader sales operations. Separately holds an EOXS-side title as Project Lead for Brannon Steel.

Ron — legal, ops, and admin. Owns company formation (Delaware C-Corp registration), banking (SVB account), email infrastructure setup, and the 3GM proposal. Reports directly to Rajat.

Nidhi Rana — technical/infra work, closely paired with Ayan Dutta. Architecture audits, MCP identity builds, staging server work. Also compiles the weekly AskCruz board report.

Sheenam — marketing and content (website, LinkedIn, lead-gen messaging).

Yashvir Singh Thakur — hiring and SDR sourcing (works the Hiring Funnels board).

Jaskeerat Singh, Priyanshu Sinha — QA, mostly on the Customer 1 - EOXS board, working off Ayan's task assignments.

Isha Bisht — HR/admin, handles mailbox provisioning and onboarding logistics.

Below that sits a rotating MBA intern cohort (their own board), plus Muskan Sharma and others feeding into hiring.

Net shape: flat, founder-managed, with Ayan Dutta functioning as the operational second-in-command on product/tech and Ron covering the legal/ops side. No management layer is documented between Rajat and individual contributors.

Assistant: This is inferred structure, not a documented org chart — worth confirming with Rajat if you need it as an official reference.

User: Is Talal in this?

Assistant: No — Talal (you) don't show up in the AskCruz internal team roster or task boards as an org member. What the data shows is that you're external to AskCruz's internal structure, engaged through Aetos Technology / lancerdevops.me as a DevOps/infrastructure vendor for EOXS: server migration, uptime monitoring, backup verification, security audits.

One relevant note: task #124 "Security" on the AskCruz board (08-17) has Rajat asking Sheenam/Ayan why an ID hasn't been created for you yet. So there was an open item to provision you access into AskCruz's systems, but as of that scrum report it was still unresolved, not done.

So the honest answer: you're a vendor providing infra/security services to EOXS, with a pending, unfinished step to get you formal access on the AskCruz side. You're not part of the reporting-line structure I laid out above.
