---
thread_name: "collier-metals-call-prep"
user: "raj"
type: claude-chat
created: 2026-07-30
updated: 2026-07-30
---

User: we have a call with collier metals right now. ayan spoek with them last week. can you pull up all the info about the people we have a call with, the history of our previous call and then we will create a structure for todays call. give me all the info that i need to prep for this call properly. if we know what technology they use etc.

Assistant: Call: **Collier / EOXS – AI Brainstorming**, today (Thu Jul 30) 12PM EST. Confirmed by both sides via email thread 07-28/29.

**Who's on it**

Collier Metals side:
- Rob Drum (rdrum@colliermetals.com, 205-253-8756) — sales-side, reports to Tripp. Met you at SMU, is the origin of this whole thread.
- Tripp Collier (tcollier@colliermetals.com) — owner, second-generation (father founded the company). Per your own internal CRM note from the SMU conversation, his son takes over the business this coming October — so Tripp may be thinking succession/systems-handoff, not just tooling. Personally deep into AI — built his own slitter setup-calculation tool that reportedly saves the shop ~10 hrs/week. He's the actual decision-maker.

EOXS side: Ayan (led the July 20 demo, scheduled this one), and you're on it too per the thread.

**Company profile**

Steel service center, 25–30 employees. Runs Microsoft Business Central as core ERP, plus PS Data for MTR/quality-cert workflows. Rob volunteered unprompted that PS Data "looks ancient" with a steep learning curve. Currently carries relatively low on-hand inventory — Rob himself flagged the MTR/matching tool as more valuable for larger multi-location service centers than for Collier's current scale, though he still saw value in it.

Leadership is unusually AI-forward for this vault's steel accounts — Rob estimates 3 of 6 execs use AI tools daily.

One real headwind: Collier recently invested in shop-floor scanners/cameras tied into Business Central for run-time tracking. Rob cited this as a reason he's more reluctant to consider switching off Business Central as the core ERP — even while staying open to AI overlay tools. So a full-ERP pitch is a much harder sell than an overlay pitch here.

**What's already been shown (July 20 demo, Ayan solo — you were hospitalized after the bike accident)**

1. MTR AI — live walkthrough of the ~22,000-record MTR database, PDF extraction of chemistry/mechanical properties, spec-matching, and a natural-language MTR chatbot (demoed with a real filtered query, correctly returned 2 matches with full traceability). This directly hits Collier's stated biggest pain point: manually transcribing chemistry/yield/tensile data out of MTR PDFs into PS Data. Rob called this "the biggest thing we can't figure out ourselves."
2. Second Brain / internally codenamed "Turing" — the company-wide Claude-powered knowledge vault, demoed live. Ayan positioned this as C-suite/ownership-only, not for line staff.

Ayan's positioning on that call, worth reusing: EOXS is not a PS Data or Business Central competitor — overlay tools on top of the existing ERP, not a replacement ("Rolex" / "Cadillac you can customize" framing). Reference points he used: Sabre Alloys (full ERP), Brannon Steel (MTR-only overlay on their existing Business Central — this is your closest apples-to-apples precedent for Collier), Gerdau/"AI Joe" (Rob was visibly happy when Gerdau came up).

Rob also asked for a second capability on that call: given a list of chemistries, predict mechanical properties (yield, tensile, elongation). You reportedly told him you'd develop that — worth confirming status before this call if it's come up internally.

Outcome of the July 20 call: no pricing discussed, relationship-building framing throughout. Rob said he'd brief Tripp and gauge interest — that's exactly what produced today's call.

**One flag on your own CRM**

The internal Odoo lead for Collier Metals (Rob Drum, stage "Leads," $0 expected revenue, 21.8% probability) hasn't been touched since Nov 27, 2025, and is still assigned to Scott Begin — not Ayan. It's badly out of sync with the actual relationship, which has clearly moved since. Worth reassigning ownership after today's call so it doesn't sit stale again.

Also on record: Ayan requested and you approved a ₹10,000 internal incentive for converting this cold lead into a discovery call (paid 07-28) — so there's already a completed internal loop tied to getting to today.

One open item the vault hasn't resolved: whether "Rick" at Eastern States Steel (cited by Ayan as a prior PS Data-migration reference) is a usable case study — unverified against ESS's own pages. I'd hold off citing that one until you've confirmed it.

Ready to build the structure for the call whenever you are.

User: so what should my questions on this call be. think from solutions selling. it would make sense to look at it from a high level, erp need, AI need, and then maybe mtr needs. what do you say. 

Assistant: Reverse your order. Leading with "ERP need" walks straight into the wall you already know about — they just bought scanners/cameras wired into Business Central, so an ERP-replacement conversation reads as EOXS not having listened. Start where the pull already exists (MTR/AI), and treat ERP as a background/roadmap question, not a pitch.

Second thing: Tripp isn't a typical buyer, he's a builder — he made his own slitter tool. Selling to a builder means understanding what he built and why before you pitch anything. That's your real opening, not "high level."

Structure I'd use:

1. Tripp's own build (credibility + buy-vs-build intel)
- Walk me through the slitter tool — what does it actually do, what did you build it on?
- What made you build it yourself instead of buying something?
- Where does it stop being useful — what's outside what one person can maintain?
This tells you his technical ceiling and exactly what argument will land later (in-house tools don't scale/aren't maintainable when he's not the one maintaining them).

2. MTR pain (the proven interest — go deep here)
- Roughly how many MTRs come through in a week/month?
- Walk me through what happens today from PDF landing in your inbox to that data being usable in PS Data.
- Where does it actually break — data entry errors, compliance risk, delay to shipping?
- Who touches this process — one person, several?
- What happens when a customer spec needs to be matched against your MTRs today?

3. Broader AI appetite (use the fact you already have — 3 of 6 execs use AI daily)
- Where else internally are people already improvising with AI on their own?
- If you could hand off one manual process to something like this tool, what would it be?

4. ERP/systems posture — light touch, forward-looking only
- How are you thinking about your systems stack over the next few years, especially with the transition to your son?
- Any friction with Business Central today, or is it mostly working for you?
Don't push past what they volunteer here. If BC is fine, let it be fine — you're not selling ERP replacement today.

5. Close
- What would need to be true for this to be worth a real pilot?
- Who else needs to be in the room for that decision — just you two, or anyone else?

One more thing: don't reintroduce the "chemistries → predict mechanical properties" ask unless you've actually got something to show — if that's still vaporware, raising it again costs you credibility with a guy who builds his own tools and will smell a gap.
