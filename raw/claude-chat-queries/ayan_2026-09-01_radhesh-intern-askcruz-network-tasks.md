---
thread_name: "radhesh-intern-askcruz-network-tasks"
user: "ayan"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: I have an new intern named Radhesh, who comes from IT background. He wants to gain experience on network management, troubeshoot, and manaing admin role.

As an intern for Askcruz what kind of tasks can i assign to him on his domain. Where does his expertise fit into.

Assistant: This falls between the two skills — it's not a straightforward data lookup, and it's ambiguous whether you want it tied to Askcruz's actual current work or general advisory guidance:

1. General advisory — how a network/IT background intern's skills map onto typical Askcruz-type work (network admin, troubleshooting, sysadmin tasks), independent of what's actually in the pipeline right now.
2. Tied to real Askcruz data — pull actual open tasks/tickets from teams-askcruz (and eoxs-teams if relevant) to see what real network/infra/admin work exists that he could be assigned to, then map his skills to that backlog.

Which one do you want? If it's #2, this is a strategic/analysis task, so pick a rigor level too:

- 5ft deep — quick pull of current askcruz tasks/stages, match against his skillset.
- 10ft deep — same, but verify task details against underlying records rather than summary listing.
- 50ft deep — full pass: current tasks, plus adjacent risks (e.g. is this too much access/responsibility for an intern, onboarding gaps, supervision needs).
- 100ft depth — same as 50ft, delivered in sections.

User: 10ft.

Assistant: Pulled live from teams-askcruz (project_task, project_project, hr_employee). Verified against the underlying task rows, not a summary view.

Key finding: Askcruz doesn't have a "network management" function in the classic sense (no routers/switches/AD/firewall tickets exist in this system). What exists is DevOps-style server/infra admin work, scattered across two project boards — "Customer 1 - EOXS" and "AskCruz." That's the domain his IT background actually maps to here.

Open tasks currently on the board that fit network/server/admin/troubleshooting:

| Task | Project | Stage | Currently on |
|---|---|---|---|
| Server Setup - Knowledge | Customer 1 - EOXS | Intake | Ayan |
| O-Auth credentials for MCP | Customer 1 - EOXS | Requirements | Ayan |
| Create Read Only TeamAskCruz MCP | Customer 1 - EOXS | Assigned | Ayan |
| Create write MCP for Ron | Customer 1 - EOXS | Assigned | Ayan |
| Fix MCP write attribution (mcpwrite@cruzai.com) | AskCruz | Intake | Talal |
| PPC EOXS MCP connection | AskCruz | Intake | Ayan |
| AskCruz Complete Write Access MCP | AskCruz | Intake | Ayan |
| Server Setup - Live (3GM) | Customer 2 - 3GM | Intake | Ayan |
| Staging db structure (3GM) | Customer 2 - 3GM | Assigned | Ayan |
| Access tier on threads ov db structure | Customer 1 - EOXS | Need discussion | Ayan |

Where his skillset actually fits:

- Server administration: DigitalOcean/Hetzner box setup, resource monitoring, cleanup (there was already a real incident — task 191, stale tmux sessions eating RAM, server optimization). This is straightforward sysadmin/troubleshooting work he can own.
- DNS/domain admin: askcruz.com subdomain and DNS record management on GoDaddy (already done once for 3GM — task 300/288). Good first assignment, low-risk, clearly scoped.
- Access/auth admin: OAuth credential setup, MCP whitelisting, tiered access control on the Postgres db. This is closer to "admin role" work he's asking for — user/access provisioning and revocation.
- Basic troubleshooting: the MCP connection issues (task 397, 396) are exactly network/connectivity debugging — diagnosing why a connector fails to authenticate or connect.

Two things worth flagging before you assign anything:

1. No hr_employee record exists for him yet — only a res_partner contact (created today) and an auto-generated "Radhesh Tinani" task under the Daily Snippets project. He's set up to log work, not yet formally onboarded as an employee record. If that matters for your process, it's a gap.
2. Every open infra task above currently sits on Ayan or Talal, not idle/unassigned. Assigning to Radhesh means reassigning ownership, not picking up something nobody's doing — worth deciding whether he's additive help or taking something off their plate.

Sources: teams-askcruz (Ask-Cruz connector) — project_task, project_project, hr_employee tables, queried live 2026-09-01.
