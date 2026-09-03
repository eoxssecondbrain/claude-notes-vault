---
thread_name: "eoxs-deep-dive-analysis"
user: "innovation_interns"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

## What Claude Knows About EOXS - Deep Dive

**User Request:**
"so, what do you know about EOXS?"

Then after initial response asking for more details:
"yes pull some actual data and not only its sources . i need some content about the recent companies that EOXS worked with and also what exactly EOXS is"

---

## My Response

I pulled actual data from EOXS's internal databases using the EOXS-DATA-GENERAL connector and retrieved:
1. EOXS Company Overview asset
2. Client contact lists
3. Detailed client profiles for Sabre Alloys and Ohio Strip Steel (Greer Steel)

### What EOXS Is

**EOXS (legal name: Prata Inc.) is a vertical SaaS + AI company built exclusively for the steel and metals industry.** They position themselves as the first AI-native ERP built for steel companies.

**Company Details:**
- Founded: ~2021 (not publicly disclosed)
- Headquarters: 125 Maywood Road, New Rochelle, NY 10804
- Tagline: "Where Steel Meets Technology"
- Market: Steel service centers, processors, tube mills, warehouses, metal distributors
- Positioning: "Top ERP software company in North America" for steel service centers
- Competitor positioning: Against SAP, NetSuite, Epicor (generic ERPs), and Invera/Stratix (metals-specific but older)

**Core Problem Solved:** Generic ERPs don't understand steel's unique business model — costing structures, inventory management, production processing, batch vs. continuous manufacturing, material specifications, grade variations, multiple planning strategies (make-to-order vs. make-to-stock). EOXS built specifically for these needs.

---

## EOXS Product Architecture

**Two Distinct Product Lines:**

### 1. Core ERP Modules
- **EOXS Books** — Cloud accounting, invoicing, inventory (multi-warehouse, serial/batch tracking, BOMs, stock transfers)
- **EOXS CRM** — Sales pipeline automation, contact management, lead generation, email campaigns
- **EOXS People** — HR/payroll, employee self-service portal, manager workflows, appraisals
- **EOXS Shop** — No-code website and e-commerce storefront builder with integrated inventory
- **EOXS Report Builder** — Custom BI; "President's Cockpit" shows all KPIs on single executive screen

### 2. AI Co-Pilots Suite (12+ AI Workers)
Positioned as ERP-agnostic — can run standalone or alongside Invera, Stratix, SAP, Epicor, or EOXS ERP.

Deployment: under 2 weeks for cloud environments; 4-6 weeks for complex/on-premise integrations.

| AI Worker | Primary User | Problem Solved |
|---|---|---|
| SmartQuote AI | Sales, estimators | Generates complete quotes from customer emails instantly; eliminates slow manual quoting |
| Steel Brain AI | Technical sales, support | Digital metallurgist; instant expert answers without specialist availability (modeled on Gerdau expert) |
| Contract Review AI | Sales ops, order entry | Compares sales orders vs. customer POs in one click; eliminates costly mismatches |
| WiseQuote AI | Sales managers, pricing | AI-driven pricing by quote history, customer tier, target margin; protects margins |
| Iris | Leadership, analysts | Real-time AI answering business questions by connecting live data across silos |
| SnapReceive AI | Warehouse, receiving | Extracts tags from packing lists; receives material with zero manual typing |
| ViewStock AI | Inventory, supply chain | Forecasts demand; optimizes stock levels and purchase timing |
| RevTrack AI | Account managers, sales | Monitors customer activity; flags churn risks and upsell opportunities |
| Order Review AI | Purchasing, AP | Compares internal PO vs. vendor SO; flags mismatches |
| SnapPO AI | Purchasing | Auto-creates internal POs from vendor sales orders |
| Prompt PO AI | Purchasing | Generates complete POs from typed request |
| SteelSynk AI | Sales, procurement | Matches mill lists to customer requirements in seconds |

**Claimed Accuracy:** 90%+ on price recommendations, 98%+ on quote generation

---

## EOXS's Current Clients (8 Active)

### 1. Sabre Alloys
**Implementation Status:** Mature, active
- **Contacts:** Charles White, Christi, Ernie Valdez, Jesus Rios, Jim Zeigler, Juan Deshon, Michael Mercadante, Tye Webb
- **Engagement:** 200+ implementation tasks, 1,443 emails, 113 calls tracked
- **Recent work (as of Sept 2026):**
  - Processing order errors (weight calculations, stage automation, cancellation issues)
  - Landed cost distribution bugs on multi-line receipts
  - Inventory valuation discrepancies
  - Control tag automation and child-tag processing
  - Margin/Gross Profit calculation implementation
  - "Fully Billed" purchase order status feature
  - Accounting reconciliation (AR/AP discrepancies)
  - Recent security incident: hack investigation with legal case evidence package
- **Recent Strategic Discussion:** Sept 2, 2026 call on "Sabre 2" AskCruz proposal scope
- **AI Access:** Claude AI recently provisioned for Juan and Tye (Sept 1, 2026)
- **Call topics:** Toll processing business discussion, AI transformation proposals

### 2. Ohio Strip Steel (formerly Greer Steel)
**Implementation Status:** Lighter touch than Sabre
- **Contacts:** Aronn Palmer, Joe Brom, Matt Hopkins, Michelle Pierce, Nathan Cale, Todd Daenzer
- **Engagement:** 106 implementation tasks, 278 emails, 23 calls tracked
- **Recent work (2024-2026):**
  - Sales order view customization (default views, field additions)
  - Contact module management
  - Distribution method configuration
  - Map functionality debugging
  - User license management
  - KPI module discussion (Aug 2025)
  - Document module review (Aug 2025)
  - Sales order accounting, contract cost model review
- **Recent Contact:** Aug 10, 2026 AskCruz intro call

### 3-8. Other Clients (Lighter Engagement)
- **Brannon Steel** — 7 contacts tracked
- **3GM Steel** — 3 contacts tracked
- **Discount Pipe & Steel** — 8 contacts, Alt Digital AI consultants (Jamie Vernon, Tina Valdez) involved
- **Eastern States Steel** — 7 contacts tracked
- **PPC Metals** — 10 contacts tracked, relay inbox monitored
- **RW Conklin Steel** — 4 contacts tracked

---

## Database Statistics (as of Sept 3, 2026)

- **1,453 wiki pages** — synthesized from client work, bugs, feature requests, analyses
- **30,460 email threads** — support, implementation, strategy
- **2,200 Fireflies call transcripts** — implementation and leadership discussions
- **140 Fathom calls** — additional recorded meetings
- **824 implementation tasks** — Odoo Kanban tasks across all clients

---

## Key Observations

1. **Sabre Alloys is the flagship/most mature implementation** — 200+ tasks, deep engagement over multiple years, recent AI enhancements being explored

2. **AskCruz is actively being evaluated as an enhancement** — Multiple recent calls titled "AskCruz AI Discussion" suggest EOXS is considering licensing/integrating AskCruz AI capabilities for their clients

3. **EOXS operates as a full-service implementation partner, not just software vendor** — They handle training, support, custom development, data migration, and ongoing optimization per client

4. **Steel Brain AI is explicitly built on Gerdau knowledge** — Suggests a significant enterprise reference and potential partnership

5. **Thought leadership is part of their motion** — Book ("Making Steel Sexy Again"), structured blog, video series ("Stories on Steel"), Innovation Lab

6. **Security matters are escalated** — Sabre Alloys hack incident received legal case evidence packaging, suggesting enterprise-grade security and compliance posture

7. **Implementation is customized per client** — Each client has unique tasks around field names, workflow stages, report structure, approval processes

---

## How This Connects to Your Role

You're QA testing MCPs, particularly the HR MCP at AskCruz. Given that:
- EOXS is actively evaluating AskCruz AI
- Sabre Alloys (EOXS's biggest client) is exploring AI enhancement
- Recent discussions are happening on integrations

It's likely that AskCruz is building connectors or MCP integrations to hook into EOXS's data or workflow systems. Your QA work on MCPs is probably foundational to whether AskCruz can successfully sell/implement with EOXS clients like Sabre Alloys.
