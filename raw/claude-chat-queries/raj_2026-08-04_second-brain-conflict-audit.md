---
thread_name: "second-brain-conflict-audit"
user: "raj"
type: claude-chat
created: 2026-08-04
updated: 2026-08-04
---

# Second Brain Conflict Audit

## Human

In your second brain, are there any conflicts that I can help you resolve?  Anything you think I should give you clarity on? I just want to make sure that your knowledge basis, clean and updated.

## Assistant

Yes — several real ones. Splitting into two categories: conflicts inside my working instructions (these affect every answer I give you), and contradictions already flagged inside OV2 (these are yours to close).

## Tier 1 — my instruction layer (highest leverage)

1. GFC equity. Two versions on record. The July 23 founder charter says Rajat 51 / Ron 20 / Ayan 20 / ESOP 9, four-year vesting, one-year cliff, shared-decision clause. The August 2 correction says you hold 100% of AskCruz/GFC and drops the shared-decision clause — but Ron's and Ayan's roles and commitments are unchanged. Did they lose equity, defer it, convert to options, or was the 51/20/20 simply never issued? This changes how I advise on every GFC decision, including whether Ron's "50% Year One" commitment still makes sense for him.

2. Entity vs product name. Is Ganesh Fruit Company still the legal entity with AskCruz as the product, or has the entity itself been renamed? My notes use "AskCruz/GFC" as one thing in one place and two things elsewhere.

3. IRIS IP transfer. $10K, EOXS → GFC. Mucker Capital holds ~12.16% of EOXS. If you now own 100% of GFC, that moves an asset out of a company with an outside institutional shareholder into one you own outright, at a price you set. Not saying it's wrong — saying it's the kind of thing that gets re-examined in a future EOXS financing, sale, or dispute. Is there a papered valuation rationale?

4. AskCruz vs Krinox inside OV2. You told me never to use "Krinox." OV2 has a live concept page titled Krinox created July 27–30, plus a Krinox proposal thread on the Eastern States Steel account. The vault is one rename behind you. Correct it, or leave it as historical record?

5. Ayan / Ayaan / Ayan Dutta. OV2 has "Ayaan" as Implementation Lead on Brannon MTR AI and "Ayan Dutta" as a separate person doing pipeline testing. Your GFC co-founder is "Ayan (engineering)." One person or three entries for two people? I've been treating this as ambiguous.

6. Prata Inc. Its OV2 entity page says "separate Delaware entity, relationship to EOXS unestablished." A signed employment agreement and a Sept 2025 1120 draft both say it is EOXS's Delaware C-corp contracting entity. The page is wrong and I'd cite it. Confirm and I'll treat it as settled.

7. Velox Steel. OV2 lists it as a ninth active client with a confirmed live instance at velox.eoxs.com, identity unresolved (Velox / Steel America / Mill Mechanical LLC), MRR unknown, nine tickets all stalled post-QA. You consistently tell me EOXS has eight clients. A live instance with unknown MRR is a billing question, not just a naming one.

## Tier 2 — flagged in OV2, waiting on you

Numbers I'd otherwise report wrong:
- Sabre Alloys: three unreconciled figures ($30M sales claim, workforce scale, balance-sheet timing), plus internal Jan 2026 inventory variance of $477K–$1.2M vs a client-facing Apr 2026 "~$150K, normal"
- Brannon: $1,200 vs $1,240 CAD/month; contract term 1yr vs 3yr
- RW Conklin: 3 vs 4 users disputed; six sales orders with no linked invoice
- CCC Group Inc appears in Sabre threads with no CRM record

Identity:
- "Christi" / "Charles" unattributed tickets — likely Sabre, unconfirmed
- Jon Rosen (2024 pitch-deck advisory board) vs Jonathan Rosen (Alascop, July 2026) — same person?

Hygiene worth knowing:
- 16 duplicate wiki filenames from the HR weekly-report port, so bare links to Ron J, Ayan Dutta, Isha Bisht now resolve ambiguously
- Two prompt-injection attempts were found embedded in ingested source data — a fake MCP-instructions block inside an email thread, and a save_chat_transcript directive. Both were caught and not followed. Worth knowing instruction-shaped text is entering your data stream.

## What I haven't done

The above is what's visible from the wiki index and my own instructions. I have not systematically swept the vault for contradictions.

- 5ft: take the list as-is. You answer Tier 1, I log the rest.
- 10ft: verify each Tier 2 item against underlying records (invoices, tickets, emails) so you're resolving facts rather than restating flags.
- 50ft: full contradiction sweep across all ~442 entity and ~333 source pages including ones the index doesn't surface, plus stale-page detection — pages asserting things later disproven — with sourcing per claim.

Answering Tier 1 alone is the highest-value thing you can do here; it's cheap for you and it corrects errors I'd otherwise repeat in every GFC conversation.
