---
thread_name: "askcruz-cold-call-script"
user: "yashvir"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

[Continuing from prior saved turns: full strategy build through Sections 1-4, narrowed quotes/inventory script, opener stress-test, expanded pain-point bank, and three persona scripts (CXO / VP Sales / VP Ops) — see earlier revisions of this file for that content.]

User: Are you sure whatever painpoints you mentioned in the scripts can be solved with askcruz?

Assistant: Grounded, yes — but "can be solved" needs a qualifier I glossed over, and it's worth being straight about it.

Every pain point in all three scripts does map to a named capability in the feature file, not something I invented:

Margin erosion → 8.7, verbatim: AskCruz can help investigate why margin changed
Tribal knowledge → 4.4 and the New Employees user group, verbatim: reduces dependence on one person's memory
Quoting delays → 8.4 and 5.2, verbatim: draft a quote using company terms and pricing logic
Call follow-up → 8.5, verbatim: summarize customer calls and connect to account context
Inventory blind spots → 8.3, the "free to sell" concept, verbatim
Order/delivery risk → 8.2, verbatim: identify orders at risk of missing their promised date

So none of these are fabricated. But every single one of those capability descriptions in the source document carries the same qualifier, word for word: "when the necessary information is available to the deployment." That's not boilerplate — Section 14 of the feature file has a standing rule that the AI must use qualified language like this and explicitly must avoid absolute claims like "AskCruz always does this for every customer." That rule exists because these capabilities depend on their systems actually being connected during implementation. Before that integration work happens, none of this runs — it's designed capability, not a live feature they'd see on day one of a demo, let alone on a cold call before any deal exists.

Layered on top of that: zero external customers have any of this working end-to-end today. 3GM is the only external client and is still mid-implementation. So "can be solved" is accurate as "this is what the product is built to do," and inaccurate as "this is proven working for a customer like you" — nobody external has proof of that yet.

Two things I'd actually fix, now that you're pushing on it:

The Sales script's bridge says a rep gets a quote draft or account history "instantly" — that word promises a finished, working experience. Soften it, since it's describing a capability that depends on their systems being integrated, not something instant on day one.

The tribal knowledge pain point (CXO script) needs one caveat you should know even if it doesn't go in the script: Company Brain can only surface knowledge that already exists somewhere accessible to the deployment — emails, documents, call records, systems. It doesn't extract knowledge that was never written down or said anywhere. If a prospect's tribal knowledge really is 100% undocumented and only in one person's head, AskCruz doesn't solve that until someone starts capturing it, which is a heavier conversation than the pain point implies.

Net: keep the pain points, they're real and documented. Swap "instantly" for something like "without hunting across systems," and be ready, if a sharp prospect asks "does this work out of the box," to say it depends on what's already connected — because that's the honest answer per the product's own documentation, and getting caught overclaiming on your first calls with a product that has one implementation total is a bad way to start.

User: How won't we create a script, a standard script, and make a separate list that... of the pain points we can ask, you know, the people based on their job position? Let's say for CXOs, VPs, characters, the one that I shared with you earlier, like, the three most important people will be calling. Right? And let's just create a standard script. Otherwise, it will get a little confusing, and we might actually end up asking the wrong question to the wrong person. What do you say?

Assistant: Agreed — and it's not just simpler, it's actually the better design. Three full parallel scripts means memorizing which document you're on mid-call, and Section 4 already proved the single-script-with-branches pattern works fine for this. Consolidating.

One thing that can't fully collapse into the standard script: the close question. A CXO is usually the economic buyer themselves; a VP of Sales or Ops usually isn't and needs to route it up. That's a real difference in what you ask, not a stylistic one, so it gets its own line in the lookup table rather than forcing one close to fit all three.

Standard script

Cold opener
"Hi [Name], it's Yash — I'll be straight with you, this is a cold call. I've got one specific question about [pain area]. You got 20 seconds?"
[pause]

Gatekeeper path
"Hi, I'm trying to reach [Name] — is this something you handle, or is [Name] the right person for [pain area]?"
If pushed: "Sure — I had a specific question about how [Company] handles [pain area], and wanted [Name]'s take directly."

Reason for the call
"The reason I'm calling — most [title-appropriate peer group] I talk to run into one of two things: [pain 1] or [pain 2]. I wanted to ask how that shows up at [Company], if at all."

Discovery — Situation
"Walk me through how [pain area] works today — is that info in one place or scattered across a few systems?"

Discovery — Problem
[Pull the matching question from the lookup table below.]

Discovery — Implication
"When that happens, what does it actually cost you — time, an annoyed customer, a decision made without the full picture?"

Discovery — Need-payoff
"If that friction just disappeared, what would that be worth to you? Who else feels it the most?"

Insight
"Here's what I've noticed talking to people in your position — the real cost usually isn't the time spent searching, it's decisions getting made without the full picture because nobody wanted to wait for it."

Bridge
"That's the exact problem AskCruz is built around — connecting the systems you're already using so anyone on your team can ask a plain question and get an answer, without hunting across logins. Given what you just described, I think it's worth a real look."
(Not "instantly" — see the earlier caveat on qualified capability language.)

Close
[Pull from the lookup table — this is the one part that genuinely varies by title.]

Pain-point lookup table, by job position

CXO / Owner / President
Reason-for-call pain pair: margin erosion, nobody sure why / tribal knowledge concentrated in one or two people
Discovery — Problem: "When a customer's margin changes, how do you find out why?" / "If your most experienced person left tomorrow, how much of what they know is written down anywhere?"
Close variant: likely the economic buyer — skip the routing question, go straight to timeline or booking. "Is this something you'd want to look at directly — 20 minutes this week or next?"

VP / Director of Sales
Reason-for-call pain pair: quoting delays / call follow-up disappearing after the call ends
Discovery — Problem: "When a customer needs a fast quote, how long does that take end to end?" / "After a call, how much of what's discussed actually makes it into the account versus staying in someone's head?"
Close variant: probably not the sole economic buyer — route explicitly. "Is this a decision you'd make within sales, or would ops or leadership need to be involved too?"

VP / Director of Operations / Inventory
Reason-for-call pain pair: inventory blind spots / orders slipping past their promise date
Discovery — Problem: "How often does someone find out about an inventory issue after a customer's already been promised something?" / "How do you find out an order's at risk of missing its promise date — before or after the customer calls asking?"
Close variant: probably not the sole economic buyer — route explicitly. "Is this something you'd bring to leadership, or is it within your call to move on?"

Reserve list, not yet mapped to a title — pull if the conversation goes there
Lost commitments, issue prioritization — both documented (Commitments, Operational Issues) but didn't have an obvious single-owner title yet. Worth deciding whether these belong to one of the three above or stay general-purpose.

One script, one lookup table, three fewer documents to keep in sync. Ready for objection handling and cadence/tracking whenever you want them.
