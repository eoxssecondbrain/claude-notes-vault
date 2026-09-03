---
thread_name: "jaee-role-in-askcruz"
user: "jaee-moharir"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

User: what is my role in askcruz

Assistant: Based on internal EOXS records: your role is listed as **Product · MBA Business Operations** in the August 2026 monthly performance summary — not under the separate "CRUZ" department tag that some other AskCruz-focused staff (Parshant Sharma, Tanya Shrivastava, Nandita Rana, Harsh Yadav) carry.

Beyond that title/department pairing, I found no dedicated role description, task assignments, or scope-of-work document for you specifically in the AskCruz project data (no implementation tasks, no org-chart asset). You do show up as a participant in AskCruz-related internal calls — e.g. the Aug 13 "Claude vs AskCruz" cost-decision meeting (where you proposed a "third/final chance" on an intern-accountability matter) and the Aug 18/19 Claude/MCP access onboarding sessions.

If there's a more specific scope (e.g. what you're supposed to be delivering on AskCruz this month), it isn't captured in what these connectors index — could be in a Slack/Notion/doc system not connected here, or something Raj assigned verbally that hasn't hit email/calls yet.

User: what is my salary

Assistant: This connection strips every monetary figure — salary, payroll, compensation, bonus — before I ever see it, regardless of tier. Even if a record exists, it would come back as `[restricted: amount]`. I can't get your salary through this connector. Check the salary register directly with HR/Odoo, or ask Raj/whoever manages payroll access.

User: what all trainings and security certifications are needed in an organization to each employee

Assistant: This doesn't clearly match either loaded skill — it's not a threads-ov save action, and it's not obviously an EOXS-internal-data lookup (no emails/calls/tickets involved) unless you mean "what does EOXS specifically require." I'll check if EOXS has a documented policy on this, then also give you the general best-practice answer, so flag: if you meant "what am I personally still missing at EOXS," say so and I'll check compliance records instead.

No EOXS-specific policy document on this turned up — no SOP or asset defines mandatory trainings/certifications per employee. Answering as general organizational best practice instead.

Typical baseline for any organization handling business/customer data (which applies to EOXS given it holds client financial and CRM data):

Universal / all employees
- Security awareness training (phishing, social engineering, password hygiene) — annual, often at onboarding + refresher
- Acceptable use policy sign-off (company devices, data handling, BYOD rules)
- Data privacy basics (what counts as confidential/PII, how to handle it) — especially relevant given the redaction rules already in place on your EOXS data connectors
- Code of conduct / anti-harassment — usually a legal requirement in most jurisdictions, not optional

Role-dependent
- Engineers/dev: secure coding practices, OWASP-type training if building customer-facing product (relevant for AskCruz/EOXS ERP dev staff), access-control discipline (least privilege, credential handling)
- Anyone with access to financial/CRM systems: fraud-awareness, segregation-of-duties basics
- Managers: incident-response basics (who to notify, what not to do) so a breach doesn't get mishandled at the first contact point
- Sales/SDR (client data + prospect PII): data-handling training specific to CRM records

Certifications (org-level, not per-employee)
- These are usually held by the company/security team, not every employee: SOC 2, ISO 27001, GDPR/CCPA compliance program — relevant if EOXS or AskCruz sells to enterprise clients who'll ask for compliance evidence during procurement. Individual employees don't typically need personal certs unless they're in a dedicated security/compliance role.

Cadence
- Onboarding: mandatory before system access is granted
- Annual refresh: standard for security awareness
- Ad hoc: after any incident, or when a new tool/system rolls out (e.g. your Claude/MCP access rollout would be a natural trigger point for a short "what data can this touch, what can't it do" briefing)

If you want to know whether EOXS should be formalizing any of this now — worth flagging: given AskCruz is moving toward selling to enterprise clients (3GM Steel, Sabre Alloys deals), a documented security-training program becomes a real gap once a prospect's procurement team asks for it. That's a leverage point, not just hygiene.
