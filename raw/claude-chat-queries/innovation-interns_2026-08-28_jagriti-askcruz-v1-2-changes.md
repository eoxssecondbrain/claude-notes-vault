---
thread_name: "jagriti-askcruz-v1-2-changes"
user: "innovation_interns"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

# Jagriti - AskCruz Latest Changes (Version 1.2)

## User Query
"Which is the latest changes which is done in AskCruz?"

## Latest Version: 1.2 (August 25, 2026)

### Major Changes in V1.2:

#### 1. EOXS Client Roster Clarification (Section 4.1)
- **Corrected Distinction:** EOXS's general client base ≠ AskCruz deployment base
- **Named EOXS Clients:** Greer Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, 3GM Steel, Sabre Alloys, RW Conklin Steel, Brannon Steel
- **AskCruz Actual Deployment:** ONLY 3GM (mid-implementation)
- **Impact:** No other EOXS client currently has AskCruz configured

#### 2. Access Tier Mapping Standardization (Section 6)
- **Confirmed Mapping:**
  - `tier1` → Raj-Personal (most restricted)
  - `tier2_confidential` → Company-Confidential (internal-team-only)
  - `tier2` → General (broad visibility)
- **Impact:** Now the authoritative reference for access control

#### 3. Support Ticket & Invoice Data Handling (Section 4.1)
- **Reframed As:** Per-client configurable choice (not fixed limitation)
- **EOXS Approach:** Data stays in live Odoo (not ingested into vault)
- **Other Clients:** Can choose vault ingestion if ERP doesn't support reliable live retrieval
- **New Operational Rule:** AskCruz should only claim access when connection/ingestion is actually configured

#### 4. Naming Standardization
- **Product Name:** Standardized on "AskCruz" (not "Cruz" alone)
- **"Cruz":** Reserved for internal/technical component naming only

#### 5. Industry-Agnostic Positioning Clarity
- **Reinforced:** AskCruz NOT limited to EOXS or steel industry
- **Clarified:** EOXS and 3GM involve steel, but doesn't define product scope
- **Key Point:** Made explicit throughout documentation

#### 6. Internal-Only Content Protection (Sections 10 & 22)
- **Added:** Explicit "internal-only" flags
- **Purpose:** Prevent EOXS-specific access config from leaking to client-facing docs
- **Prevented:** Accidental exposure in client materials

### Version History Summary:
| Version | Date | Focus |
|---|---|---|
| 1.0 | Aug 2026 | Initial self-knowledge specification; product launch |
| 1.1 | Aug 21, 2026 | Added metadata, attributes, data completeness, primary users |
| 1.2 | Aug 25, 2026 | Clarifications, corrections, standardization (CURRENT) |

### Nature of Changes:
- **Type:** Clarifications and corrections (not new features)
- **Focus:** Accuracy, terminology standardization, data governance
- **Strategic Impact:** Clearer product positioning, better multi-tenant isolation preparation, prevention of information leakage
