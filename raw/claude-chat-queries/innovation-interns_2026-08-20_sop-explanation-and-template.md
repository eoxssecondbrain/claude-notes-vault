---
thread_name: "sop-explanation-and-template"
user: "innovation_interns"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

User: explain me about SOP

Assistant: There are several SOPs in the system, and none jumps out with a clear top score — this is genuine ambiguity, not a confident single match. Which one do you mean?

1. **eoxs-sop** — the general/main "Standard Operating Procedure" doc
2. **Code Review and Technical QA SOP**
3. **Development Standards and Code Structure SOP**
4. **EOXS Client Implementation and Go-Live SOP** (tier2_confidential)
5. **GitLab Branching, Sandbox Deployment, and Production Release Management SOP**
6. **EOXS NEWS SOP**
7. **EOXSplore SOP**
8. **Product Demo Video Library SOP**

If you just mean "the general company SOP," that's #1 (eoxs-sop) — tell me and I'll pull it.

User: [uploaded screenshot: VS Code editor showing OV2-Frontend project file explorer with docker-compose files, and a browser tab open to "Sign in to Open WebUI" at http://127.0.0.1:5173/auth, terminal running ollama with llama3.2:3b]

get me a template of a sop which should be detailed and should be standardised step by step instruction for my application

Assistant: [Created and presented file /mnt/user-data/outputs/SOP_Template.md with the following content:]

# Standard Operating Procedure (SOP) Template

## Document Control
| Field | Value |
|---|---|
| SOP Title | |
| SOP ID | |
| Version | 1.0 |
| Owner | |
| Author | |
| Approved By | |
| Effective Date | |
| Last Reviewed | |
| Next Review Due | |
| Related Docs | (links to other SOPs, wiki pages, repos) |

---

## 1. Purpose
State in 1-3 sentences why this SOP exists and what problem it prevents (e.g. inconsistent deploys, missed steps, onboarding gaps).

## 2. Scope
- What this SOP covers
- What it explicitly does NOT cover
- Which environments/systems/repos it applies to

## 3. Roles & Responsibilities
| Role | Responsibility |
|---|---|
| e.g. Engineer | Executes steps 1-5 |
| e.g. Reviewer | Approves before step 6 |
| e.g. On-call | Handles rollback if failure |

## 4. Prerequisites
- Access/permissions required (repo access, credentials, VPN, etc.)
- Tools/software required (versions if relevant)
- Preconditions that must be true before starting (e.g. "staging is green")

## 5. Definitions / Glossary
Any terms, acronyms, or internal jargon a new reader would need.

---

## 6. Procedure (Step-by-Step)

> Each step should be atomic, testable, and unambiguous. Include exact commands, file paths, or UI actions — not vague descriptions.

### Step 1 — [Action name]
- **What to do:** 
- **Command/Action:** `exact command or click path`
- **Expected result:** 
- **If it fails:** (link to troubleshooting or rollback step)

### Step 2 — [Action name]
- **What to do:** 
- **Command/Action:** 
- **Expected result:** 
- **If it fails:** 

### Step 3 — [Action name]
- **What to do:** 
- **Command/Action:** 
- **Expected result:** 
- **If it fails:** 

*(repeat as needed — number every step, no skipping)*

## 7. Verification / Sign-off Checklist
- [ ] Step outcomes match expected results
- [ ] No errors in logs/console
- [ ] Relevant stakeholders notified
- [ ] Documentation/ticket updated

## 8. Rollback / Failure Handling
- Condition that triggers rollback
- Exact rollback steps
- Who to notify and how

## 9. Exceptions
Any known cases where this SOP does not apply as written, and what to do instead.

## 10. Revision History
| Version | Date | Author | Change Summary |
|---|---|---|---|
| 1.0 | | | Initial version |

---

## Notes on filling this out
- Every step must be something a new team member could follow with zero tribal knowledge.
- Prefer exact commands/screenshots over prose descriptions.
- If a step branches (if X do A, if Y do B), make that explicit — don't bury conditionals in a paragraph.
- Keep ownership current — an SOP with a stale owner rots fast.

[File presented to user: SOP Template, /mnt/user-data/outputs/SOP_Template.md]
