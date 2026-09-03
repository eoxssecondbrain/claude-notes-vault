---
thread_name: "jaee-role-in-askcruz"
user: "jaee-moharir"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

User: what is my role in askcruz

Assistant: Based on internal EOXS records: your role is listed as Product · MBA Business Operations in the August 2026 monthly performance summary — not under the separate "CRUZ" department tag that some other AskCruz-focused staff (Parshant Sharma, Tanya Shrivastava, Nandita Rana, Harsh Yadav) carry.

Beyond that title/department pairing, I found no dedicated role description, task assignments, or scope-of-work document for you specifically in the AskCruz project data (no implementation tasks, no org-chart asset). You do show up as a participant in AskCruz-related internal calls — e.g. the Aug 13 "Claude vs AskCruz" cost-decision meeting (where you proposed a "third/final chance" on an intern-accountability matter) and the Aug 18/19 Claude/MCP access onboarding sessions.

If there's a more specific scope (e.g. what you're supposed to be delivering on AskCruz this month), it isn't captured in what these connectors index — could be in a Slack/Notion/doc system not connected here, or something Raj assigned verbally that hasn't hit email/calls yet.

User: what is my salary

Assistant: This connection strips every monetary figure — salary, payroll, compensation, bonus — before I ever see it, regardless of tier. Even if a record exists, it would come back as [restricted: amount]. I can't get your salary through this connector. Check the salary register directly with HR/Odoo, or ask Raj/whoever manages payroll access.

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

User: tell me in general as compared to other AI organizations what are mandatory trainings for employee

Assistant: Doesn't clearly match either loaded skill (not a save action, not EOXS internal data) — treating as general knowledge, flagging per your rule.

Compared to general orgs, AI companies tend to add a layer specific to model/data risk on top of the standard baseline (security awareness, code of conduct, data privacy, anti-harassment). What's different:

Responsible AI / safety training
- Most frontier AI labs (Anthropic, OpenAI, Google DeepMind) run mandatory training on responsible scaling policies, model risk categories, and escalation paths for anyone touching model development or deployment
- Red-teaming and misuse-awareness training for staff with model access, even non-research roles in some orgs

Confidentiality / IP protection
- Heavier NDA and trade-secret training than typical software companies, because model weights, training data, and safety research are treated as extremely sensitive
- Stricter device and network security requirements (approved hardware, no personal cloud sync of internal docs) — this is often mandatory training + policy, not just policy

Data handling and privacy
- Training on handling user conversation data, PII in training sets, and data retention rules — more rigorous than typical SaaS because the product itself ingests user input at scale
- Some orgs require training specific to regulatory frameworks their models touch (GDPR, HIPAA if in health verticals, export controls if the tech is dual-use)

Export control / national security awareness
- Increasingly common at frontier AI labs given government scrutiny (comparable to what you'd see at defense contractors) — training on what can't be shared with foreign nationals or certain jurisdictions
- Less common at smaller AI startups unless they're building anything with dual-use potential

Bias/fairness and ethics training
- Many AI orgs run mandatory training on bias in datasets/models for anyone doing data labeling, model evaluation, or product decisions — this is less standard outside AI

What's roughly the same as any tech company
- Standard security awareness (phishing, password hygiene)
- Code of conduct, anti-harassment
- Incident response basics

Certifications: individual staff rarely hold formal certs (SOC 2/ISO 27001 stay at company level), but AI orgs increasingly document internal "model access tiers" the way EOXS already does with its own tier1/tier2/tier2_confidential system — that's actually a fairly mature practice you're already running, most smaller orgs don't have it formalized yet.

If you're asking because you're thinking about what AskCruz should adopt as it scales toward enterprise clients: the export-control and IP-protection pieces are the ones companies skip early and regret later once a serious client's procurement team asks about them.

User: is there any external official trainings which has certifications as well

Assistant: Yes — real external certs exist across the areas I listed. Breaking down by category:

Security awareness / general infosec
- CompTIA Security+ — broad, foundational, widely recognized, not AI-specific
- SANS Security Awareness certifications — org-wide training programs, well regarded
- ISC2 Certified in Cybersecurity (CC) — entry-level, free/low-cost, good baseline for non-security staff

Data privacy
- IAPP CIPP (Certified Information Privacy Professional) — CIPP/US, CIPP/E for GDPR — the standard cert for anyone actually responsible for privacy compliance, not typically mandatory for all staff, more for whoever owns privacy at a company
- IAPP CIPM — privacy program management

AI-specific (this space is still young, fewer mature options)
- ISO/IEC 42001 — AI management system standard, org-level certification, not individual, but increasingly what enterprise clients ask vendors to hold
- Responsible AI certifications from individual vendors (Microsoft Responsible AI, Google Cloud's AI/ML governance training) — vendor-specific, useful mainly if you're on their stack
- No universally recognized individual "AI safety" cert exists yet comparable to Security+ — this space is still forming. Most frontier labs run internal training rather than sending staff to external certs, because the field is moving faster than certification bodies can standardize

Export control
- BIS (US Bureau of Industry and Security) training programs — for anyone whose org touches export-controlled tech
- ITAR/EAR compliance training — vendor-run, not a personal certification so much as a compliance course

IT/cloud security (relevant if AskCruz touches infrastructure)
- CISSP — for whoever owns security architecture, not entry-level
- AWS/Azure/GCP security certifications — relevant if AskCruz's infra runs on one of these

Practical read: for a company your size, the ones worth actually pursuing now are CIPP (if you want someone owning privacy formally, which matters once EU or regulated-industry clients show up) and eventually ISO/IEC 42001 at the org level once AskCruz is trying to close enterprise deals where procurement asks "do you have a certified AI governance framework." The individual-employee security certs (Security+, ISC2 CC) are nice-to-have, not typically gating for a startup — internal training covers 90% of the actual risk at this stage.
