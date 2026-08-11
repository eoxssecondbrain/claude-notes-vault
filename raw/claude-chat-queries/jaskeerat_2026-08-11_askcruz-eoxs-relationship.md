---
thread_name: "askcruz-eoxs-relationship"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# How AskCruz Works With EOXS

## The Relationship Structure

AskCruz (GFC) and EOXS are separate companies with Raj as the common link:

- EOXS: Steel ERP SaaS, 8 clients, ~$27K/mo MRR, profitable/bootstrapped
- GFC (AskCruz): Separate holding company, AI operating system, VC-fueled growth model
- Raj's ownership: 100% equity in both (corrected 2026-08-02)
- Intentional separation: Different funding paths, unit economics, risk profiles

---

## How Data Flows From EOXS to AskCruz

AskCruz's Obsidian Vault ingests multiple sources, including EOXS ERP data:

1. Live ERP data — real-time orders, inventory, customers from EOXS instances
2. Email — client team communications
3. Call transcripts — Fireflies, Fathom
4. Static KB — internal documentation

For clients using both systems: AskCruz sits atop their EOXS instance, querying it via API to pull operational data into the unified Vault.

---

## IRIS Acquisition (Key Transaction)

**IRIS = Natural-language BI over live ERP/CRM**

- Currently: Part of EOXS product
- Moving to: GFC ownership (AskCruz)
- Transaction: $10,000 from GFC to EOXS
- Why: AskCruz owns the IP cleanly rather than licensing
- Result: IRIS + Obsidian Vault + Claude = AskCruz's "Brain" layer

---

## First Pilot Clients (Both From EOXS Base)

**Sabre Alloys** (~$11K/mo from EOXS):
- Running SA2 (IRIS-style pilot) — natural-language queries over live EOXS instance
- Not a full AskCruz deployment yet; testing IRIS layer in isolation
- Proof-of-concept for full rollout

**Monarch Steel**:
- Intended as first full AskCruz build (Brain + Hands + full Vault setup)
- Pulls EOXS data + email + calls + KB

---

## The Critical Tension: Time Split & Conflict

**The biggest issue flagged in vault is organizational, not technical.**

From the $50M vs. $1B path analysis:

**Path A ($50M in 5 years, 55-65 hrs/week):**
- Sustainable split: 60-70% AskCruz, 30-40% EOXS
- EOXS survives on part-time attention + Ron + Ayan
- Can maintain both without one failing

**Path B ($1B in 5 years, 75-90 hrs/week):**
- Full-time capital raising, category building, investor circuit
- EOXS likely cannot survive with founder split 75+ hrs/week to AskCruz
- Must address "EOXS relationship/time-split question"
- Requires either abandoning EOXS or stepping back as AskCruz CEO

**Current team allocation:**
- Ron: 50% Year 1 → full-time (EOXS + AskCruz blend)
- Ayan: Full-time on AskCruz engineering from day one
- Raj: Split between both; decision point coming at scale

---

## Why They're Separate (Not Merged)

Strategic reasons for intentional separation:

1. **Funding trajectories differ** — EOXS bootstrapped/profitable; AskCruz VC-fueled
2. **Unit economics differ** — EOXS recurring licensing vs. AskCruz bespoke builds at $30K ACV
3. **Team leverage differs** — EOXS can run lean; AskCruz requires full-time engineering + sales
4. **Risk profiles differ** — AskCruz failure doesn't kill EOXS (and vice versa)
5. **Investor expectations differ** — VC wants growth; EOXS can stay profitable and small

**Strategic logic:** Keep EOXS alive as profitable defensive base while betting AskCruz on faster growth.

---

## Where They Actually Touch

| Touch Point | Details |
|-------------|---------|
| IP | IRIS moves from EOXS to GFC; core AskCruz component |
| Customers | First pilots (Sabre, Monarch) are existing EOXS clients |
| Data | AskCruz Vault queries live EOXS ERP instances |
| Delivery | Implementation team members work on both; workload split critical |
| Conflict | Founder time split at scale; mutually exclusive at $1B ambition |

---

## Bottom Line

AskCruz uses EOXS as:

1. **Data source** — pulls live ERP data into Vault for dual-platform clients
2. **IP source** — acquires IRIS and makes it core AskCruz component
3. **Customer base** — 8 EOXS clients are first AskCruz pilot targets
4. **Time trade-off** — running both at scale is mutually exclusive; founder must choose path

Integration is operational, not structural. Separate companies sharing a founder and early customers.

Sources: raw/claude-chat-queries/raj_2026-08-04_askcruz-overview-explained.md, raw/claude-chat-queries/raj_2026-08-02_gfc-askcruz-1b-vs-50m-vision.md, raw/claude-chat-queries/jaskeerat_2026-08-10_cruz-askcruz-purpose-explained.md
