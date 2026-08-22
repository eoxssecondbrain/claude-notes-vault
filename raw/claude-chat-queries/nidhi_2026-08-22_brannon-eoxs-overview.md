---
thread_name: "brannon-eoxs-overview"
user: "nidhi"
type: claude-chat
created: 2026-08-22
updated: 2026-08-22
---

## Brannon Steel — Full Overview

**User:** Tell me each and everything you know about Brannon. Their relationship with EOXS, cruz proposal, contacts, open items and contract info

**Assistant:** Compiled from eoxs-db (client profile, wiki, emails, calls). No eoxs-teams/CRM SQL access available in this session, so invoice/pipeline detail is limited to what wiki analysis pages cite.

### Relationship with EOXS
- Brannon Steel = prime steel service center, Brampton, Ontario, Canada. EOXS's first Canadian client and first non-ERP, AI-only engagement (MTR AI product, not full ERP).
- Sales cycle: Raj met David Brannon at SMU Steel Summit (Sep 2025) → Scott Begin (salesperson) followed up → in-person meeting Oct 15, 2025 (14 Tilbury, Brampton) established 3-phase roadmap: Phase 1 MTR AI digitization (current), Phase 2 MRP/SFA replacement, Phase 3 "Iris AI" NLP reporting.
- Nov 11, 2025 technical scoping call (55 min) set architecture: MTR DB + Inventory DB + AI NLP Search Layer, heat number as shared key, manual CSV/Excel upload to start.
- Dec 8, 2025 investment proposal call resolved IP ownership: Brannon owns all data/AI training; EOXS owns core platform.
- Formal proposal sent Dec 9, 2025; deal won Jan 20, 2026.
- Ongoing weekly "Implementation Huddle" calls (28 calls on file, most recent Aug 18, 2026) plus a running MTR Samples data-QA task thread (project.task id 271, brannon.eoxs.com portal) active through at least Aug 14, 2026.

### Contacts
- David Brannon — dbrannon@brannonsteel.com (initial sponsor/exec contact)
- Kevin Brannon (K.R.) — krbrannon@brannonsteel.com
- Manish Trivedi — mtrivedi@brannonsteel.com (Head of Operations, technical lead)
- Ranim Fallaha — ranim.fallaha@brannonsteel.com / rfallaha@brannonsteel.com (APQP Manager, ex-Gerdau)
- Shared task-thread alias: info.brannon@gmail.com

### Contract / pricing info
- Pricing figures are stripped in this session ([restricted]) per access-tier rules — confirmed a formal proposal + signed deal exist, but no dollar amounts visible.
- Two specific dev-work proposals found (Aug 2026 email, Ayan Dutta → Manish/Ranim):
  1. Algoma Join Report Enhancement — heat/batch mismatch matching logic — LIVE in production, billed [restricted], invoice INV/2026/0295 (invoice number could not be independently verified against invoice table).
  2. Pre-Purchase MTR–Spec Verification — matches MTRs to spec before purchase without storing them — PROPOSED, quoted [restricted], pending Brannon sign-off.

### "Cruz" proposal
- No evidence found linking Brannon Steel to "Cruz"/AskCruz (EOXS's separate internal AI-agent/second-brain product being piloted with other clients like 3GM Steel and Ohio Strip Steel). Searches for "Brannon AskCruz" / "Brannon Cruz" returned nothing. If a Cruz-specific proposal exists for Brannon it isn't in the synthesized wiki or wasn't yet promoted — worth checking eoxs-teams/CRM directly (not accessible in this session).

### Open items
- MTR Inventory Module status conflict (unresolved as of Aug 7, 2026 analysis): internal escalation says the module task has been stalled 2+ months; support ticket T06332 (assigned Ayan Dutta, created Feb 4, 2026) shows status "QA Passed" — the two systems appear out of sync, cause not yet determined.
- Pre-Purchase MTR–Spec Verification proposal awaiting Brannon sign-off (see above).
- MTR Samples task thread: as of the most recent ingest (through Aug 14, 2026 19:41 UTC), three spec-matching false negatives/mismatches were reported within a single week (Aug 11, Aug 14 x2), acknowledged by EOXS — ongoing data-quality QA issue.

Sources: eoxs-db get_client_profile, wiki pages (Brannon Steel entity/CRM record, MTR Inventory Module Escalation analysis, Algoma Join Report analysis, MTR Samples task thread), emails/calls list. No eoxs-teams (CRM/invoice SQL) tool was available this session.
