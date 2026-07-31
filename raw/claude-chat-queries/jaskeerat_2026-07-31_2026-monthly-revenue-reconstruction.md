---
thread_name: "2026-monthly-revenue-reconstruction"
user: "jaskeerat"
type: claude-chat
created: 2026-07-31
updated: 2026-07-31
---

# 2026 Monthly Revenue Reconstruction

**User:** tell me my revenue from 2026. monthly.

**Assistant response summary:**
Reconstructed monthly 2026 revenue by pulling per-client Invoice History wiki pages (Sabre Alloys, 3GM Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, Greer Steel/Ohio Strip Steel, RW Conklin Steel, Hansen Metallurgical Services) plus raw Brannon Steel sales-order exports (CAD currency, kept separate).

## Monthly table (USD, ex-Brannon)
| Month | Invoiced (USD) | Notes |
|---|---|---|
| Jan | ~$47,180 | Sabre $12,910; 3GM $15,359 (quarterly Nov'25-Jan'26); Eastern States $2,340; DPS $4,770; PPC $5,064; Greer $3,737 (quarterly); RW Conklin $1,800; Hansen $1,200 |
| Feb | $0 | No invoices dated Feb across any client — billing lag, Feb-period service billed in March |
| Mar | ~$37,504 | Sabre $21,940 (two invoices); Eastern States $4,680; DPS $5,620; PPC $2,864; Hansen $2,400 |
| Apr | ~$1,536 | PPC only (net of billing-error credit) |
| May | ~$60,191 | Sabre $10,720; 3GM $14,558+$14,276 (two quarterly cycles); Eastern States $2,340; DPS $3,120; PPC $2,200; Greer $5,488+$6,288 (two quarterly cycles); Hansen $1,200 |
| Jun | ~$33,860 | Sabre $20,440; Eastern States $4,680; DPS $3,140 net; PPC $4,400; Hansen $1,200 (status uncertain) |
| Jul (partial, thru 7/28) | ~$20,600 | Eastern States $2,340; DPS $6,689; Sabre $9,380 (draft); PPC $2,200 (draft) |
| **Total Jan-Jul 2026** | **~$200,900** | |

Brannon Steel (CAD, separate): Jan $4,320; Mar $10,080 cancelled; May $4,881.60+$11,390.40; Jul $1,356+$3,051 → ~$25,000 CAD total.

## Caveats given to user
- Quarterly billers (3GM, Greer/Ohio Strip) create lumpy month-to-month totals since 3 months are invoiced at once.
- Feb $0 is a billing-timing artifact, not zero revenue.
- Several July items still draft/unbilled (Sabre S00205, PPC S00207).
- RW Conklin invoice history stops Jan 2026 — no later data in vault.
- No data for Aug-Dec 2026 (vault ingest checkpoint ~2026-07-30).
- Mix of Locked/Sales Order (paid/confirmed) vs draft quotations flagged inline.

**Offered follow-ups:** 2025 monthly comparison, CAD-to-USD blended total for Brannon Steel.
