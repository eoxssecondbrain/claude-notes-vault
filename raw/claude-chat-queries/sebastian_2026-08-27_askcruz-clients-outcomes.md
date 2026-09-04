---
thread_name: "askcruz-clients-outcomes"
user: "sebastian"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

User: Who are AskCruz's current clients, and what specific outcome did each of them get from using AskCruz?

Assistant: This is a research question — AskCruz is EOXS's internal AI product, and "current clients + specific outcomes" requires cross-referencing prospect/deal records, correspondence, and possibly CRM data, not a one-line lookup. Pick a rigor level:

5ft — Quick: pull whatever the wiki's synthesized AskCruz/prospect pages already say about client status and outcomes. Fast, but relies on what's already been written up.

10ft — Verified: same, but every named client and claimed outcome gets checked against underlying emails/calls/CRM records before I report it, not just the synthesized wiki page.

50ft — Deep: full investigation across eoxs-db (wiki, emails, calls, prospects) and eoxs-teams (CRM/pipeline), verified per 10ft, plus flags on deal-stage ambiguity (e.g. "interested" vs. "signed") and any outcomes that are aspirational rather than realized.

Which level?

User: 50ft

Assistant: AskCruz has one confirmed external client: 3GM Steel. No client has a documented outcome yet.

Details, cross-checked against the underlying deal records (not just the synthesized summary):

- 3GM Steel — deal confirmed Aug 19, 2026 (Travis Lane, CCO) at a reduced 2-user scope, with a shortened initial contract term and a 6-month auto-renew decision point. Currently listed as "mid-implementation." No kickoff-payment confirmation, usage data, ROI, or outcome is in the record — the canonical AskCruz Product–Market Fit doc (revised 25 Aug 2026) explicitly states 3GM's "exact sales pitch, buying criteria, commercial value, measured ROI, usage depth, and retention outcome... were not established," and it names 3GM as AskCruz's "first — and, as of this update, only — external client."

- EOXS itself runs AskCruz internally as its own pilot ("Company Brain" / second-brain deployment) — that's a pilot, not an external client, and the doc is explicit this shouldn't be counted alongside 3GM.

Flag on data quality, since you asked for this: internal sales correspondence contains a claim that Sabre Alloys and 3GM Steel have "been running it for two weeks now and are hooked" — used twice, in pitches to two different prospects (Lawrence Tabachnick and Three D Metals). That claim is contradicted by the record:
- Sabre Alloys never got past proposal stage — a joint 3GM/Sabre proposal call happened Aug 13, but there's no confirmed deal, and it's unverified whether Sabre even received the proposal document (an email claiming an attachment had none attached).
- The canonical PMF doc, written after that pitch, still says 3GM is the only external client.

So "hooked" is sales framing, not a verified outcome — treat it as a red flag on the sales narrative, not as evidence of a second client or of any measured result.

Net: 1 confirmed client (3GM), 0 confirmed outcomes, and pipeline overstatement in at least one outbound pitch. Sources: eoxs-db wiki (AskCruz PMF asset, 3GM proposal-call page, Sabre sales-push page, Lawrence Tabachnick / Three D Metals entity pages); eoxs-teams checked and ruled out (its sale_order records for 3GM/Sabre are unrelated EOXS steel-distribution business, not AskCruz).

User: visualize the 10ft

Assistant: [Rendered an interactive SVG diagram titled "askcruz_client_pipeline_verified" showing a two-row pipeline: 3GM Steel (Pitched Aug 12 → Proposal sent Aug 14 → Deal confirmed Aug 19, 2-user → Outcome: not documented, all stages teal/confirmed except outcome which is gray/not-reached) and Sabre Alloys (Pitched Aug 13 → Proposal sent: receipt unclear (coral/flagged) → Deal confirmed: not reached (gray) → Outcome: not documented (gray)). Legend: teal = confirmed in records, coral = flagged/unverified, gray = not reached. Below, a coral flagged box reads: "Sales claim: both 'running it 2 weeks, hooked' — Made to two prospects — contradicted by the stages above."]

3GM Steel is the only client past deal confirmation, and even it has no documented outcome yet. Sabre Alloys stalled at proposal stage with unconfirmed receipt. The "hooked" claim used in outbound pitches isn't backed by either client's actual record.
