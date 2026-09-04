---
thread_name: "ron-technical-background"
user: "ron"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

User: Tell me everything you know about Ron and his technical background. What role did he play in EOXS? I wanted to really focus on what he knows in technical terms and his skill set.

Assistant: Ron — EOXS role and technical background, per the employee directory and internal wiki (eoxs-db):

Official role
- Title: Sr. Implementation Consultant, Product department, full-time since 2022-08-31, reporting to Raj (CEO). Not a founder or equity holder.
- Managed other Product-team members directly, not just an individual contributor: Danish Lari (Implementation Intern, still active), plus former reports Yash Motghare (Jr. Implementation Consultant), Nandish (Project Manager), Arpan Singh (Jr. Product Developer), Lukman (Software Dev Intern), and Shazeb (Outreach Executive, Marketing). So the role blended implementation consulting with people management.
- Day to day: primary client-facing point of contact for DPS, Sabre Alloys, Greer Steel, and PPC Specialty Metals — account relationships, AR, release coordination.

Technical skill set, evidence-based rather than self-reported
- Odoo 13: hands-on work in custom module architecture across several EOXS modules — m5_sale_order, m7_freight, m13_processing, m14_account. This is functional/config-level depth, not necessarily writing production Python from scratch.
- Financial/data reconciliation: CFO-level reporting (AR aging, cash flow verification, inventory valuation) including SVL vs AML discrepancy analysis — closer to data analysis than engineering.
- Infrastructure: PostgreSQL diagnostics, Contabo server management, explored a personal dev server (Contabo VPS + GitHub + webhook auto-deploy), backup architecture design (Contabo object storage plus a Backblaze B2 evaluation), Mailcow mail server migration for AskCruz.
- Process/DevOps: led a full redesign of EOXS's Git workflow and deployment process — one-task-one-branch rule, versioning scheme, branch/commit conventions — and scoped a custom Odoo-GitLab integration after finding all App Store options only support Odoo 17-19, not 13.
- AI/automation tooling: building a GitLab + Teams.eoxs MCP workflow for AI-assisted development, an Apollo integration for prospect filtering, a job-title classifier for B2B targeting, and a suite of internal Claude skills (raj-eoxs-vault, war-room strategist, dps/sabre account strategists, client-email-tone-scale). Uses Claude Code and Codex CLI for coding.
- Knowledge systems: designed the Obsidian + Google Drive "Second Brain" client knowledge base and a 12-vault/4-group AI knowledge architecture spec tied to PostgreSQL and the codebase.

One data point worth stating plainly: a tier2_confidential internal email archive (2024-05 to 2024-09) records Ron accidentally purchasing a $150 production-tier Contabo server and having to get it refunded. Not disqualifying, but it's a real signal that the infra work has been "figured out live on production" rather than formally trained sysadmin practice.

Net read: not a software engineer by title or credential — the job title and reporting line are implementation/consulting/account management. But the work history shows a genuinely technical operator: comfortable in a live production Odoo/Postgres environment, able to scope and partially build integrations, and now building AI tooling (MCP workflows, Claude skills) rather than just consuming it. That combination of domain depth plus self-directed tooling is more relevant to the AskCruz implementation-and-product role than either a pure account-manager or a pure-engineer background would be.

Sources: EOXS employee directory (eoxs-db, employee id 89) and wiki page "Internal Email Archive — Infrastructure, Security and Server Incidents (batch 1, 2024-05-05 to 2024-09-29)" (eoxs-db, tier2_confidential); prior-conversation memory files (odoo-13-technical-work, git-workflow-redesign, infrastructure-security, gitlab-teams-mcp-workflow, second-brain-knowledge-base, claude-skills-suite, tools).
