---
thread_name: "askcruz-overview-steel"
user: "sebastian"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

**User:**
Give me a two-minute plain-English overview of what AskCruz does and the problem it solves for steel service centers.

**Assistant:**
AskCruz is EOXS's own AI product — an internal knowledge and work-assistant tool that's now being sold externally, and its current deployments are all steel and metals service centers. First external client is 3GM Steel (mid-implementation on a six-week rollout), and the sales push has extended to Sabre Alloys and Three D Metals. Worth flagging up front: EOXS's own documentation formally positions AskCruz as industry-agnostic long-term, not steel-specific — but every real customer today is a steel service center, so the "problem it solves for steel service centers" framing you asked about is accurate to what it's actually doing right now, even if it's not the official permanent scope.

The core problem: at a steel service center, the knowledge needed to run the business well is scattered. A customer's actual delivery promise lives in an email thread, a pricing exception got agreed on a call, true inventory availability sits in the ERP, and the reason a customer's margin moved might only live in one salesperson's head. When that person is out, or nobody remembers where to look, the business stalls or makes a worse decision. AskCruz pulls that scattered information together so anyone can ask an ordinary question and get a grounded answer instead of hunting across systems and people.

It's built around four pieces. Company Brain answers questions using the company's own history — what was promised to a customer, why a margin changed, how quotes are normally priced. Company Hands does practical work with that knowledge — drafting a quote using your actual pricing logic, flagging an order at risk of missing its promise date, summarizing a call against the right account. Digital Workforce is standing responsibilities — watching an order queue or exception and flagging it without being asked. Company Personalization means it reflects how your specific company actually operates — your vocabulary, your pricing exceptions, your tolerances — not generic steel-industry assumptions.

For a steel service center specifically, this maps onto real operational pain: knowing what's genuinely "free to sell" once commitments are netted out, catching orders drifting toward a missed promise date, understanding "true margin" after freight and processing, and not losing a customer's history when the one rep who knew the account leaves.

Boundaries worth knowing: it explicitly does not replace your ERP, isn't guaranteed real-time (there's a sync lag), and doesn't make commercial decisions on its own — it's an assistant layer on top of what you already run.

Want me to go deeper on any one piece — the four-pillar model, the current 3GM/Sabre Alloys deal terms, or that industry-agnostic-vs-steel positioning tension?

Sources: AskCruz — Product Feature File; AskCruz — Comprehensive Client-Facing Product Understanding; AskCruz — Market Positioning, ICP & Product-Market Fit Status (internal EOXS knowledge base, confidential)

**Assistant (follow-up flag):**
Done — answer's above. One thing to flag as your advisor hat, not just the summary: internal docs are actively contradicting each other on whether AskCruz is "industry-agnostic" or "steel-specific," and the timestamps show this got edited same-day (Aug 25) without full resolution across all four asset files. If you're about to pitch or position this externally, that's worth nailing down before it leaks into a deck or a prospect call — right now different internal sources would give a prospect different answers to "is this built for steel or just happens to be running there first."

**User:**
Who are AskCruz's current clients, and what specific outcome did each of them get from using AskCruz?

**Assistant:**
Short answer: only one steel service center has actually signed on as an AskCruz client, and even that deal is too fresh to have a measured outcome. The other two names in the pipeline are still prospects, not clients. If someone told you AskCruz has client outcomes to show, that's not what the record supports right now.

3GM Steel — the only confirmed AskCruz deal. Travis Lane (CCO) confirmed on 2026-08-19 that 3GM is moving forward, but at a reduced 2-user scope (down from what was originally proposed) and with a shortened initial contract term he pushed for. Pricing details are redacted in what I can see, and there were multiple pricing inconsistencies across drafts that had to be corrected before he'd sign off. Notably, the internal record also shows a strategic decision to run this client's "Company Brain" on Claude directly rather than through AskCruz as the client-facing front end — worth understanding before you describe 3GM as a clean AskCruz deployment. There's no record yet of a kickoff date being set or implementation actually starting, so there is no outcome to report — it's a signed intent, not a live result.

Sabre Alloys — not a client, still a prospect. Rajat pitched a 1-page AI transformation proposal on 2026-08-12, a call happened on 2026-08-13, but the internal record flags a real problem: the email that was supposed to carry the proposal document to Sabre's contacts (Michael Mercadante, Tye Webb) went out with no attachment. Whether they ever actually received written terms is unverified. No deal, no outcome.

Three D Metals — also just a prospect. Referred in by Lawrence Tabachnick, pitched by Rajat on 2026-08-13 using 3GM and Sabre as reference points ("running our AI Company Brain on live operational data" — which overstates 3GM's actual status, since 3GM's deal wasn't even confirmed yet at that point). A demo/evaluation call was scheduled for 2026-08-19; whether the prospect has responded since is unverified in the record. No deal, no outcome.

Bottom line: AskCruz has zero documented client outcomes for steel service centers as of today. One signed-not-yet-implemented deal (3GM), two open prospects (Sabre Alloys, Three D Metals), and internally an EOXS pilot with no reported results either. If you're being asked or asking someone to cite "what AskCruz has done for clients," there's currently nothing in the record to back that up — that's a gap worth closing before it gets said out loud externally.

Sources: 3GM Steel — AskCruz (Company Brain) Proposal Call (internal, tier2_confidential); AskCruz Sales Push Extends to Sabre Alloys (internal, tier2_confidential); Three D Metals prospect page (internal, tier2)
