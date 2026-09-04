---
thread_name: "askcruz-rql-sop-icp-review"
user: "raj"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

USER: Can you go through this document and see if it fits well with the ICP of AskCruz as of this stage?

[Uploaded file: /mnt/user-data/uploads/AskCruz_RQL_SOP.pdf — "ASKCRUZ Rapid Qualification of Leads — Standard Operating Procedure, Revision 2 — built from a full pass across Threads OV (Raj-weighted) and the live AskCruz CRM. Prepared for: Data Enrichment Team. Owner: Danish Lari — Data Enrichment & Management, AskCruz / EOXS. Date: September 1, 2026."]

ASSISTANT: I've read the SOP — this is Danish's Rev 2 RQL SOP for AskCruz, dated Sept 1, 2026, gating on operational complexity (headcount/multi-system) rather than industry/product, with mills/manufacturers flipped to Qualify and processors leaning Qualify.

Before I dig in — how deep do you want this?

[Tool call: ask_user_input_v0 — Question: "Rigor level for this ICP-fit review?" Options: "5ft — Quick read against what I already know", "10ft — Verified against CRM/wiki records, not just memory", "50ft — Deep: verified + adjacent risks/blind spots flagged", "100ft — Staged: same as 50ft, delivered section by section"]

USER: 50ft — Deep: verified + adjacent risks/blind spots flagged

ASSISTANT: Rev 2 of Danish's RQL SOP holds up. It's a sound piece of work, and I checked it against the canonical AskCruz docs and actual client data rather than just reading it at face value.

What's right, verified

- The core design choice — gate on operational complexity (headcount, multi-system footprint), not industry or product type — matches the canonical AskCruz Product-Market Fit doc (Aug 25, 2026) almost exactly. That doc states outright: "The ICP should be defined by data fragmentation and value potential, not by industry." There's no separate "AskCruz ICP" asset in the vault — this SOP is effectively filling that gap, and it's aligned with the one canonical source that exists.
- Mills flipping from disqualify (EOXS SOP) to qualify (this SOP) is defensible. EOXS's mill exclusion is about inventory-to-manage, which doesn't apply to a synthesis layer. I don't have evidence contradicting the claim that mills run higher operational complexity than distributors.
- Processors leaning Qualify checks out against your actual paying base — Sabre Alloys is a toll-processing/laser-cutting client, and the live askcruz.com copy explicitly names "service centers, processors, and distributors" as the target segment.
- Criterion 3's tiered size check (enrichment data first, LinkedIn second, facility signals only for the 8–24 ambiguous band) is a more disciplined version of EOXS's flat under-15 cutoff.

Two real gaps, not cosmetic ones

- The size thresholds (25+/under 8/8–24) are explicitly untested — the doc admits this — and it's correct to admit it: you have exactly two paying AskCruz clients (Sabre Alloys, 3GM Steel), and neither was won through an RQL funnel. Both came through existing EOXS relationships. So this SOP has zero closed-deal calibration behind it. That's not a flaw in the writing, it's a flag that the criteria are theory until you have 5–10 more closed or dead deals to check them against.
- The steel-vs-agnostic fork is real and current, not a hypothetical the SOP is hedging on. I pulled the live site just now: it's titled "AI Operating System for Steel" and says Cruz is "trained on steel operations first — not adapted from a generic manufacturing model." That directly contradicts the canonical PMF doc's "industry-agnostic" positioning. The SOP correctly refuses to resolve this itself and escalates it to you — that's the right call, not a punt. But it means every RQL decision made under Criterion 9 (industry as metadata, not gate) is operating on an assumption your own website is currently contradicting in market. Worth resolving soon, because your GTM copy and your qualification logic are pulling in different directions right now.

One thing I'd push back on

Danish built a genuinely rigorous qualification system for a company with ~$84K ARR run-rate against a $1M/12-month target. That's not wrong to build — bad qualification wastes intern hours on dead leads — but it's worth asking whether the highest-leverage next step is refining who counts as qualified, or converting the qualified prospects already sitting in the pipeline (Collier Metals, Leeco Steel, Harbor Pipe, Sabre/3GM expansion). This SOP doesn't cost you anything since it's Danish's lane, not yours — but if RQL throughput isn't currently the bottleneck to $1M ARR, this is optimization on the wrong constraint.

USER: I just want to make sure that my sales and marketing team are fed with good fuel.

ASSISTANT: The logic in the SOP is sound — that's not what determines whether fuel is good. Two things actually will:

Enrichment execution, not criteria. Danish's SOP tells someone what to check. It doesn't guarantee it gets checked consistently across whoever's running RQL day to day — interns, Danish, whoever. A well-designed gate applied inconsistently produces the same noisy pipeline as no gate.

CRM reliability is your real bottleneck, not qualification logic. Real deal activity for your advanced prospects already lives in email and calls, not the CRM. If that's true upstream, it'll be true downstream too — sales gets fed whatever made it into the CRM cleanly, which per your own pattern is not where the signal actually lives.

So: good SOP, untested thresholds, and the fuel-quality question is really "is Data Enrichment output making it into a place sales actually trusts and uses" — not "is the qualification bar right." Worth checking with Danish whether qualified leads are landing somewhere sales checks daily, or somewhere that gets bypassed the way CRM already is for deal tracking.
