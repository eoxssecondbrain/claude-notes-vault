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

Ready when you are — answer Tier 1 in whatever order suits you, or pick a rigor level for the deeper sweep.

## Human

1. That was just a discussion I had with you.  At this point, I will own hundred percent equity in gfc.

2. Ganesh food company is the legal entity and ask Cruz is the Product.

3. I understand this point, but don't worry about it.

4. Can you replace krinox with Ask Cruz everywhere.

5. Ayan where is multiple hats. Think of a SOLUTIONS architect  remember this

6. Confirmed.

7. Velox is our demo instance. It has the base code of our product and we use it for demonstration in life sales calls.

Don't worry about Sabre Alloys

I am not sure if it is 1200 or 1240.

RW Conklin churned a year ago. We don't have any business transaction with them.

I don't know anything about cCC group

Cristi and Charles are from Sabre Alloys

Nod two different people. Jonathan Rosen and Jon Rosen.

Regarding the 16 duplicate file names, can you write an email that I can send to Ayan Ron and Isha.

Regarding the two prompt injected attempts that were found embedded. Add this also in the email.

50

## Assistant

Two things before the findings.

Krinox → AskCruz replacement: I can't do it. My OV2 tools are read-only — get_index, get_wiki_page, search_*. There's no write or edit tool exposed on that connector. The only OV2 write path I have is apply_ov2_xref, which appends a one-line pointer and nothing else. This needs Nidhi to run a find-and-replace across the vault and rename `wiki/concepts/products/Krinox.md`. I've added it to the email below.

Also: you wrote "Ganesh Food Company." My record says Ganesh Fruit Company, named after your grandfather's fruit business. Which is the registered name?

## 50ft sweep — findings

I prioritised by what would make me give you a wrong number, since ARR is the decision filter.

### Stale revenue records — fix these first

RW Conklin. OV2 still lists them as an Active client, $450 MRR, LOW-MODERATE risk. That's wrong per your answer, but your timing is also off: last sales order is S00154 (2026-01-06, December 2025 licensing). Churn is ~January 2026, not a year ago. The live question is money: six consecutive orders Jul–Dec 2025 ($10,800 total) show no linked invoice in the Odoo export, and an October 1, 2025 arrears notice from Ron shows $5,400 already outstanding for Jul–Sep. Nothing in the vault records whether that AR was ever collected. If they walked owing, that's real cash and nobody closed the loop.

Hansen Metallurgical Services. $1,200/month "Joe 2.0" Gerdau licensing, 16 orders through June 2026 (S00195, no invoice raised). Jamie Hansen flagged May 2026 as likely the last month Gerdau is contracted. Outcome never recorded. This is ~$14.4K/year that isn't on your eight-client list and has an open live-or-dead question.

Velox. Confirmed as your demo instance — but nine support tickets are logged against it, all stalled post-QA, one QA-Failed. Dev hours are being spent on a non-revenue instance, and it's inflating client-level ticket analytics. Separately, the "Steel America" and "Mill Mechanical, LLC" name variants have no explanation if it's purely internal.

### Resolved this pass

Brannon: it is $1,200 CAD/month, $1,356 with HST (S00203, July 2026). The figure $1,240 appears nowhere in actual billing — the CRM record page is simply wrong. Fix the page.

But a worse finding fell out of it. Both July invoices — INV/2026/0295 ($3,051 implementation) and INV/2026/0289 ($1,356 subscription) — are Posted, Unpaid, and flagged "Invoice Sent: No." That's $4,407 CAD raised and apparently never delivered to the client. Combined with the multi-month AR backlog already flagged on the Brannon page, you likely have a mechanical cause for a collections problem, not a client-behaviour one. Worth checking whether the same flag is set on other accounts.

### Pages that would make me cite wrong facts

- Prata Inc — you confirmed it; the page still says "separate entity, relationship unestablished."
- Sachin (Kumar) — unresolved contradiction between a success-story framing and a First Advantage record showing involuntary termination ~March 2024.
- Vitco Steel — contradicts a January 2022 internal claim that Vitco was "already paying us 50k for implementation." Either inflated or a deal that churned in five weeks. Flagging it because inflated internal revenue claims show up more than once in your history and investors read those.
- Alliance Trading Inc — an 84% payroll-time-reduction case study, flagged UNVERIFIED, reused verbatim across at least three 2021 proposal decks. If that number is still in circulating sales material, verify it or retire it.

### One process finding worth more than the rest

Discount Pipe & Steel. On April 22–23, 2026, Zana Williams tested the reservation-reallocation logic and reported it works with two SOs and fails completely with three or more plus partial bundles. She retested with four and confirmed. One week later, on April 30, Aryan Bakshi's formal QA summary concluded "all tested scenarios performing in line with expected behavior... reliable data integrity under both standard and edge case conditions." Never reconciled.

The June 26 overselling incident on S05460 was exactly the multi-order partial-delivery scenario she had already demonstrated broken. That is not a documentation conflict — it's a QA sign-off that overrode a client's own test result and then cost you an incident on a HIGH-risk account with a legal letter already on file. If you fix one thing from this sweep, make it that pattern rather than any of the page edits.

Also: 3GM sits at LOW risk with the coil zero-value bug and a declined Aug 2024 tax-calc fix both recorded as chronic and open. Worth knowing what's still broken before you push IRIS expansion to Travis Lane.

### Can't close without you

CCC Group Inc — appears in Sabre support threads, no CRM record, you don't recognise it. Suggest asking Tye Webb directly rather than leaving it flagged indefinitely.

## The email

One note first: you named Ayan, Ron and Isha, but Nidhi leads OV2 development. The rename and the pipeline change both land on her. I'd add her.

[Email drafted via message_compose_v1 — subject: "OV2 — three fixes needed: duplicate page names, injected instructions in source data, Krinox rename"]

Ayan, Ron, Isha (cc Nidhi) —

Three issues in OV2. None are on fire; all of them degrade the vault if we leave them.

1. Duplicate page filenames (16)

When the 41 HR weekly-report pages were ported from main to data on 29 July, 16 landed with filenames identical to existing pages under wiki/entities/eoxs-team/ — including Ayan Dutta, Ron J, Isha Bisht, Azra Saleem, Hashir Saleem, Mahesh Mudiraj and Sakshi.

Effect: any bare [[Name]] link to those people now resolves by path proximity rather than intent. A link meant for someone's entity page can silently land on their weekly-report page instead. Eleven of these collisions already existed on main; five are new on data.

Proposed fix: suffix the report pages — e.g. "Ayan Dutta — Weekly Reports.md" — and update the link list on the HR Weekly Team Reports overview page.

Nidhi to own the rename and re-link. Isha, confirm the naming convention you want before it's applied, since these are your reports.

2. Instruction-shaped text found inside our own ingested data

During the 28–30 July ingest, two separate items in raw data contained text written to look like instructions to an AI system:

- a fake "MCP server instructions" block embedded inside an email thread (surfaced on the Re: S00204 thread)
- a save_chat_transcript directive surfaced via a connected MCP server

Both were identified during ingest and not acted on. No harm this time.

The concern is structural, not incidental. Anything we ingest — client emails, ticket bodies, attachments, call transcripts — can carry text that a reading model treats as a command. As more of the business sits behind AI query layers, that surface grows, and relying on the reading agent to notice is not a control.

Ayan: confirm whether the ingest pipeline has any detection for this today. If not, what would it take to add a flag-and-quarantine step at ingest rather than at read time?

Ron: one of these landed on a live client thread. Worth establishing whether the source was the client, a vendor tool in the chain, or something we generated ourselves.

3. Krinox → AskCruz rename

The product is AskCruz. OV2 still carries a concept page titled Krinox (created 27–30 July) plus references on the Eastern States Steel thread. Nidhi, please run a find-and-replace across the vault and rename wiki/concepts/products/Krinox.md to AskCruz, keeping a one-line note that Podar and Krinox were earlier names so the history stays traceable.

Please come back with owners and rough timing by end of week.

Raj
