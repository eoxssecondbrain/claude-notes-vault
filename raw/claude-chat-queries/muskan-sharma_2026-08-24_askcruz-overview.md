---
thread_name: "askcruz-overview"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

User: tell me about ask cruz

Assistant: I don't have anything on AskCruz yet — memory only has your name on file, and the two skills I just loaded (threads-ov, eoxs-data-general) are scoped to EOXS data, not AskCruz. Neither matches this query.

So: what do you want here? A few options —

1. You tell me what AskCruz is/does and I file the basics to memory for future reference.
2. You have documents, a connector, or files about AskCruz you want me to pull from.
3. You want me to search the web for public info (only useful if AskCruz has an external presence).

Which one, or something else?

User: name all the clients we've worked with since the company started

Assistant: Which company — EOXS or AskCruz? I only have a data connector for EOXS client records; there's no AskCruz data source connected yet (per your last question, we hadn't settled where AskCruz info would come from).

User: eoxs

Assistant: 8 clients in the registry, visible in this session:

| Client | Domain |
|---|---|
| Sabre Alloys | sabrealloys.com |
| 3GM Steel | 3gmsteel.com |
| Eastern States Steel | easternstatessteel.com |
| Discount Pipe & Steel | discountpipesteel.com |
| PPC Metals | ppcmetals.com |
| Ohio Strip Steel (formerly Greer Steel) | ohiostripsteel.com / greersteel.com |
| RW Conklin Steel | conklinsteel.com |
| Brannon Steel | brannonsteel.com |

This is the full client registry as visible in this connection — not a subset. Brannon Steel and RW Conklin Steel have no Odoo instance listed, which usually means they're either pre-go-live or off-platform for some other reason; I haven't checked their implementation status. Say the word if you want that pulled per client.

Source: eoxs-db client registry (get_index, list_clients).

User: who are our top 3 competitors

Assistant: [AskUserQuestion tool call] Asked: "Competitors for which company?" (EOXS vs AskCruz) and "Rigor level for this?" (5ft Quick / 10ft Verified / 50ft Deep). User answered: Company = EOXS, Rigor = 50ft — Deep.

Assistant (final answer): Direct software competitors, per EOXS's own materials: three names appear together as "direct software competitors" in EOXS's Oct 2022 investor teaser deck, and each is independently corroborated by external sources.

| Competitor | What they are | Why they're a threat |
|---|---|---|
| Invera | Largest metals-industry ERP vendor globally — STRATIX and eSTELPLAN, deployed at 600+ sites across 14+ countries. CEO Peter Doucet. | Scale and incumbency — the market leader EOXS positions against. Public press releases (American Piping Products, Southwest Steel Coil, United Performance Metals, others) confirm a large, active install base. EOXS even lists Invera as an "integration partner" for its AI layer, which tells you how entrenched it is. |
| P.S. Data Services (PS Data / mysteelsoftware.com) | Steel-specific ERP/CRM/BI vendor. | Most operationally live threat right now — beat EOXS outright for the Ray Neff Metal Fabrication account (2024), and is the incumbent system at prospect Collier Metals as of a July 2026 call, where Rajat was actively positioning against it ("good product for the 90s," structural technical-debt weakness). |
| Enmark Systems | Metal-service-center software vendor, backed by PE firm Accel-KKR (confirmed via PE Hub, PR Newswire, Accel-KKR's own site). | Unusual case — a real 2023 acquisition/partnership negotiation happened between Enmark/Accel-KKR and EOXS (Rajat was offered a "stronger operational role, including CEO" in a potential combination). Outcome of those talks isn't recorded in the archive. So Enmark is competitor and prior M&A counterparty at once. |

Caveats worth having in view, since this was a deep pass, not a quick one:

The "top 3" framing itself comes from a 2022 investor deck — nearly 4 years old against today's date. No internal document explicitly ranks current competitors; I built this from which names recur most and most directly across wiki, calls, and emails through 2026. By recency and frequency of actual deal contact, PS Data reads as the sharper day-to-day threat; Invera reads as the bigger brand/scale threat.

There's a second, different category I excluded: steel marketplace competitors — Reibus and Felux — which compete on trading/marketplace, not ERP software. If "competitors" means anyone contesting EOXS's space broadly rather than software specifically, those belong in the conversation too. Also surfaced but thinner: Steel Plus (called out in a Jan 2026 call as "not friendly with us") and RealSteel (used in one client's benchmarking) — neither has enough documented depth to rank in a top 3.

Source: EOXS data connector (eoxs-db) — wiki entities for Invera, Ps Data Services, Enmark, Reibus; Mucker Capital analysis page (2022 teaser deck reference); Analysis: Sales Coach Knowledge Base; sales call transcripts (Collier/EOXS AI Brainstorming, 2026-07-20 and 2026-07-30). Cross-checked externally via web search — PRWeb/StreetInsider press releases for Invera, mysteelsoftware.com for PS Data, PE Hub/PRNewswire/Accel-KKR for Enmark.
