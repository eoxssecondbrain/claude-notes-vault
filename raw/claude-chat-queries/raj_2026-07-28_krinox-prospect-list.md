---
thread_name: "krinox-prospect-list"
user: "raj"
type: claude-chat
created: 2026-07-28
updated: 2026-07-28
---

## User
make me a list of all the prospects i can reach out for krinox.

## Assistant
Offered three rigor-level options (5ft/10ft/50ft) per user preference for research/strategic tasks.

## User
5 ft deep

## Assistant
Queried EOXS Teams Live (crm_lead, crm_stage) for live CRM status of the previously-identified high-confidence Krinox (formerly Podar) prospects: Titanium Industries, HarbisonWalker/Crawford Murton, Horizon Steel/Ryan Ganzer, Modesto Steel, Steel Warehouse/Ted Lerman, Coilplus/Spencer Lysek, Monarch Steel/Marty Socha, FerroSource/Daniel Bain, Ace Steel Supply.

Findings (stage_id mapped via crm_stage table):
- Coilplus: Intent (2026-01-08)
- Horizon Steel: Actions Pending (2025-12-23)
- Modesto Steel: Actions Pending (2025-12-24)
- Steel Warehouse (Ted Lerman): Actions Pending (2025-12-23)
- HarbisonWalker (Crawford Murton): Actions Pending (2026-01-08) — contact-only record, no partner_name linked
- Titanium Industries: Unsure, stale, last touch 2023-11-02
- Monarch Steel (Marty Socha): Unsure (2025-08-07) — but flagged as a data conflict since Raj's context has Monarch already in active Podar-style deployment (AI email-to-Invera AR/AP agent), so live CRM stage is stale/wrong here
- FerroSource: LOST (2025-12-24)
- Ace Steel Supply: LOST (2026-07-15) — most recent touch of the whole set

Recommended straight-line reach-out list: Coilplus, Horizon Steel, Modesto Steel, Steel Warehouse (Ted Lerman), HarbisonWalker (Crawford Murton). Flagged Titanium as cold, Monarch as past-prospect-stage, FerroSource/Ace Steel as LOST needing a reason before re-approach. Noted this was a stage-field-only pass and offered a 10ft deep pass (mail_message/description-level verification) as next step if wanted.

## User
horizon steel is an asshole. we dont want to business with them.

## Assistant
Removed Horizon Steel from the reach-out list per Raj's instruction. Updated straight-line reach-out list: Coilplus, Modesto Steel, Steel Warehouse (Ted Lerman), HarbisonWalker (Crawford Murton). Titanium stays cold, Monarch past-prospect, FerroSource/Ace Steel LOST needing a reason, Horizon Steel now excluded per Raj's call. Note: did not write this exclusion to persistent memory since Raj did not explicitly ask for it to be remembered (per his stated preference) — it's reflected in this thread only.
