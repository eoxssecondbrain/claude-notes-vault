---
thread_name: "ai-hiring-call-agent"
user: "sheenam"
type: claude-chat
created: 2026-08-30
updated: 2026-08-31
---

Human: Raj had a new idea today to automate our entire hiring funnel. Currently, we manually call the people who have applied for a certain job post, do 2-3 rounds of interviews with them, and then hire them. What we have seen is that it takes a lot of time to make calls for even the first interview round, get a vibe check with the candidates, see if they are available for the second round of interviews, and check their soft skills and everything over the call.
What we want is to build an AI calling agent that can do this first round of interviews for us. How it will work is that this AI agent will be trained to understand how every job post needs to be scanned. It will have a complete understanding of the job description, all the things that we require in an employee, and the expectations that we have. We will train the agent on how to ask questions and what questions to ask, and then that agent can keep adding the answers of the candidates in a Google Sheet.
For example, we have an opening for an Operations Manager, and 1,000 people have applied for it. This agent knows what kind of people we want in the Operations Manager team and calls these 1,000 people. It has a list of their names and their phone numbers. It makes a call and has Google Sheet access to it. This agent asks all the questions. This agent has already been provided with a transcript, which it is going to use for this call. It will ask the questions that can gauge how that person is, their attitude, and everything, and then all of these answers are logged in the Google Sheet. We then put this Google Sheet into the cloud and assess how the people have responded and everything.
This is the base idea that we have right now. Raj has given me the stars to build this agent and give him a list of 100 people and their answers that have been derived from this agent. My first delivery on this task to Raj is a list of 100 people whom the agent has called and logged their answers in a Google Sheet.
Give me a realistic timeline for how much time it would take for me to build this agent. We are not going to build this agent per se. We are going to see if we have tools available in the market. Yes, we do have tools available in the market that can do this job. I just need to find the right tool, teach it how to make calls, what expectations we have, and everything, and then see how it works.
Give me a realistic timeline for how much time it would take for me to get this task done and give Raj the first delivery. Since these tools are already available in the market, we literally just need to scan the tools, create the transcript for these agents, and then test it out, so it should not take a lot of time. The timeline should be really realistic. Think of yourself as a professional AI automation builder and scavenger. You have knowledge of all the AI automations, tools, and applications that are available in the market for different things. You need to do a 100-foot deep dive and think about how much time it would take to build something, find something like this, and submit the first delivery. I think my expectation is that it should not take more than a week for me to find the right tool, train it how it needs to start the hiring process, and then create the first delivery. I want to know what you think. This task does not need you to dive into the OV vault and our ERP.

Assistant: Quick flag before I dig in: this doesn't cleanly match raj-eoxs-vault (it's market research on external tools, not EOXS's own data) or sales-strategist (not a sales/GTM/deal question) — so just the standard thread save applies, no vault query needed, as you said.

You've already specified 100 ft depth, so I'll run it staged: outline first, then one section at a time, waiting for "next" between them.

One thing forks the whole analysis before I write that outline: where these applicants actually are. Almost every serious vendor in this space right now — Ribbon, Classet, Apriora/Alex, Ringlyn, Rebecca AI — is a US-market product built around US telecom rules. Outbound AI calls to US numbers need documented consent under the TCPA (informational calls need "prior express consent," not written, but it's still a real requirement — violations run $500–1,500 per call with no cap, and it's the calling business that's on the hook, not the vendor). If these Operations Manager applicants are India-based instead, the compliance frame is completely different (TRAI/DND, DPDP Act) and I'd be checking a different — or at least differently-weighted — shortlist of vendors for actual India calling quality.

[Presented clarifying question via interactive options: "Where are these Operations Manager applicants (and future roles) based?" — options: United States / India / Mix of both or other countries]

Human: [Selected option] India

Assistant: Since it's India, here's how I'll structure the 100 ft pass:

1. Reality check on the plan as described — where Raj's framing (and the "just find a tool" assumption) needs pressure-testing before you pick anything
2. The actual India-relevant vendor shortlist — outbound-calling tools that fit "call from a list, log structured answers," with real pricing and onboarding speed
3. Day-by-day realistic timeline to the first 100-candidate delivery, where the one-week target holds up and where it doesn't, plus my recommendation

Section 1:

The plan as you've described it has one structural ambiguity that determines almost everything downstream: is this agent supposed to proactively dial out to all 1,000 applicants (what you actually described — "it has a list of their names and phone numbers... calls these 1,000 people"), or is it an async link the candidate clicks and completes on their own time? Most of what gets marketed as "AI interview tools" in 2026 is the second thing — Talview's Ivy, iMocha's Tara, most of the India players — the candidate gets a link, does the interview whenever, and it scores itself. That's not what you described, and it's not what Raj is picturing either — he's picturing the recruiter's job (dialing, getting someone live) done by an agent. That narrows the field a lot, to genuine outbound-calling platforms, not screening links.

Second, the compliance layer is not optional homework you do after the tool works — it has to be in the call script from the first test call. Two Indian frameworks apply simultaneously and separately: TRAI's DND/TCCCPR rules mainly govern promotional/commercial calls, and a call to someone who applied to your own job posting almost certainly qualifies as a service/transactional contact rather than promotional — so the DND-registry blocking probably doesn't bite you here, though that's a five-minute confirmation, not a certainty I'd bet Raj's name on without checking. The DPDP Act 2023 applies regardless of that classification: you need a clear notice at the start of the call that it may be recorded, a stated and limited purpose for the data, and the ability to honor a deletion or access request. This isn't a big lift, but it's a line or two of scripted disclosure that has to be in your very first test call, not retrofitted after 100 people are already in the sheet.

Third — and this is the part of the plan I'd actually push back on — Google Sheets as the destination is a non-issue. Every one of these tools either writes to an ATS/webhook natively or connects to Sheets in under an hour through Zapier, Make, or a native Sheets action. Don't spend any evaluation time on "does it support Google Sheets" — that's not a differentiator between tools, it's solved by all of them.

What actually matters, and what changes your timeline more than anything else: does EOXS have an ATS today, or is the applicant list genuinely just a raw spreadsheet of names and numbers? From how you've described the current process — manual calls, no system mentioned — I'm assuming the latter. That matters because most of the India-market vertical tools (BabbleBots, HirePro, iMocha, Talview) are built to trigger off an ATS event ("candidate applied in Darwinbox/Keka → call fires"). If you don't have an ATS, you either need a tool that also accepts a plain CSV/sheet of numbers as its calling list directly, or you're doing a two-piece build: an outbound voice-AI platform plus a thin no-code layer (Zapier/Make/webhook) that feeds it your list and pulls results back. That second scenario is one real extra step Raj's "just find a tool" framing skips over — someone still wires that connection, even with everything off the shelf.

Next: the actual vendor shortlist for India-based outbound calling, with pricing and setup speed.

Human: Okay, I do not know about this right now. I will have to sit with you and do deeper research on this before actually determining it.
For the question on how these candidates will be approached, I think we can go the route where we can send them a link over email or LinkedIn, and they can click on that link, and the call is being shortlisted. That works, that's fine. We don't have to have this agent manually do a call, but I need to give him a timeline. I am on a deadline. I need to tell him how much time it is going to take to test this whole thing out and actually run it. Give me a number. I need to send it to him. Give me a buffer of two to three days extra, but I need to send it to him right now.

Assistant: That changes things in your favor — async link-based screening is the more mature, faster-to-deploy category, and it sidesteps most of the outbound-calling compliance overhead I flagged (DPDP notice-and-consent still applies to whatever gets recorded, but you're no longer fighting DND/dialer classification).

Number for Raj: 7 to 8 working days from kickoff to the 100-candidate delivery.

That's 5 working days of real sequential work, plus the 2-3 day buffer you asked for. The 5:

- Day 1-2: shortlist and trial 2-3 async AI-interview tools, and lock the actual question set/scoring rubric with Raj. This second part is the one genuinely at risk of running long — it needs his sign-off on what "good" looks like for an Operations Manager, not just your judgment call.
- Day 3: configure the chosen tool — load the question set, wire the Sheets export (an hour of work with any of these, not a real cost), add the DPDP recording-consent line at the start of the interview.
- Day 3-4: test on a small batch, then send the link to enough of the 1,000 applicants (email/LinkedIn) to realistically net 100 completions.
- Day 4-5: completions come in, you spot-check quality, clean the sheet before sending to Raj.

The buffer covers the one thing you don't control: how fast people who already applied actually click the link and finish it. If it's a role people want, you clear 100 completions in a day or two of sending. If it's slower, that's what the extra days absorb.

If you start tomorrow, tell Raj he'll have it around September 8-9.

Whenever you want to actually sit down and pick the tool, the India shortlist with real pricing and setup speed is ready to go through.

Human: I am giving you an update on how I will be proceeding with this. I have a deadline for 3 days. Within these 3 days I need to find the tool, test it thoroughly, and deploy it. My first deliverable is now the tool ready and functioning. Here is how Raj has set an incentive on this - 
If I setup and deploy the tool by 3 Sept, thursday 5PM EST, - Gold Medal - incentive of ₹25000
4 Sept, Friday, 5 PM EST - Silver medal - incentive of ₹15000
7 Sept, Monday, 9 AM EST - Bronze medal - incentive of ₹1000 (KPI - data of 50 calls in the CRM)
This is how we are going to ensure that the task is completed in time.
Ingest this information and give me a heads up. Then lets proceed with brainstorming how we want to start the search, what are the exact features that we are looking for.

Assistant: Heads up, straight reaction first, then let's brainstorm.

Today's Monday Aug 31. Gold is Thursday Sept 3 5pm EST — effectively 3 working days out. Silver is Friday Sept 4. Bronze is Monday Sept 7 9am EST, tied to an actual KPI (50 completed calls), not just setup.

Good news: redefining the deliverable as "tool ready and functioning" instead of "100 candidates done" makes Gold genuinely plausible — it's basically my original day 1-3 estimate (shortlist + rubric lock + configure + test), and that's entirely inside your control. The one thing that can still blow up Gold is the same thing I flagged before: getting Raj to sign off on the actual question set/rubric fast. If that drags past tomorrow, Gold is dead regardless of how good the tool is. I'd get that locked today if at all possible — it's the highest-leverage single hour you'll spend this week.

One thing I need nailed down before this is a real target rather than a guess: what does "ready and functioning" mean for Gold/Silver — configured and tested with dummy runs, or actually live with real candidates already flowing through it? Those are different bars. The first is fully in your control and hits Thursday easily. The second depends on how fast real applicants click a link, which is not in your control and is really what Bronze's 50-call KPI is testing. I'd assume Gold/Silver = configured, tested, and live (link is out and working) — not "X real completions" — unless you tell me otherwise, since that's the only version of "functioning" that doesn't depend on candidate behavior.

Second thing: you said "50 calls in the CRM" for Bronze. Is there an actual CRM already in play here, or is that just Raj's shorthand for wherever this data ends up (the Sheet)? I'm not going to go digging into your systems for this since you scoped that out earlier — but if there's a real CRM you're expected to land this in, that changes what "export" needs to support, so worth a one-line confirmation from you or Raj before I build the feature list around Sheets.

Now, the feature brainstorm — what actually matters for a tool search, given async link, sent via email/LinkedIn, professional-track Operations Manager candidates (not high-volume multilingual field/BPO screening, which is what most of the India vendor market is actually optimized for):

1. Self-serve signup, published pricing, no "book a demo" wall — this alone probably cuts your realistic shortlist in half and is non-negotiable for a 3-day timeline.
2. Same-day setup — configure and go live in hours, not a guided multi-day onboarding.
3. Custom question builder — your own Operations Manager questions and rubric, not locked into a generic template.
4. Structured scoring output per candidate — a number or tier per answer, not just a raw transcript you'd have to grade by hand.
5. Bulk candidate upload from a raw CSV/list — has to accept 1,000 names/emails directly, since there's no ATS triggering this.
6. Shareable link per candidate, sendable via email or LinkedIn — not gated behind requiring the candidate to already be inside some system.
7. Live or near-real-time export to Sheets — native or one Zapier/Make hop, so you can watch completions land rather than waiting on a batch pull.
8. A place to insert a DPDP consent/recording-disclosure line at the start of the interview — small thing, but needs to be checkable in the tool, not something you're told isn't supported after you've already sent 1,000 links.
9. Typical completion-rate/time-to-complete data from the vendor — tells you whether Bronze's 50-in-a-week is realistic with that specific tool's usual candidate behavior, versus you finding out the hard way on day 5.
10. Per-completed-interview or pay-as-you-go pricing — not an annual contract, since this is a one-role pilot, not a committed rollout yet.

What would you add or cut from that list before we start naming actual tools against it?
