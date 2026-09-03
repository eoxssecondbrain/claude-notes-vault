---
thread_name: "ai-calling-agent-project-outline"
user: "sheenam"
type: claude-chat
created: 2026-09-02
updated: 2026-09-03
---

Human: I think it's high time that we clarify the role of this agent, the calling agent that we are developing. I'm going to give you a complete outline of how I want this agent to work.
The idea is that, instead of us having to call hundreds and thousands of applicants for a particular job post, we get a subscription to a tool that can make those calls for us. So far, how I have understood that these tools work is that we send these applicants a link. They click on that link, and an AI agent conducts the interview and asks some questions that are preset by us for particular job posts. We don't want these questions to be set for just one job post. We would be hiring for multiple positions, and all these positions need to be live at the same time.
We need a tool that can provide us with the ability to make thousands of calls in a month. The idea of having this tool live is that we would not have to spare people from our team to make hiring calls, to make interview calls with people who might not even be a good fit for us. What happens is that we call 500 people for a particular job posting, and out of that 500, you only have 10 to 15 people who were actually worth calling. That wastes a lot of time for the person who actually makes those calls, who could have spent that time on something else, doing something productive in the company, so we don't want that anymore.
I would like to see if we can have a tool that also has a machine learning aspect. For example, if we are making calls, this tool should not only stick to the provided transcript and keep conducting their interview. Maybe in the first two to three minutes, the tool understands the person's answers, the way they are talking, and realizes that this person is not a good fit. There is no point in spending time with that person on the call, so it can literally shorten the call and wrap it up, right?
Ideally, we would be providing a 10-minute transcript to this tool to ask questions for a particular job post. If that is not continuing with each and every individual, the tool should have the ability to shift its answers. It should not be a rigid tool that does not have the ability to understand and maneuver the conversation as it goes.
This is the project that I have at hand. Give me a project outline and the task description. Keep it short, but cover all the points that I have talked about.

Assistant: This is a planning task, not a data lookup — doesn't touch the EOXS connectors or sales-strategist skill, so I'm proceeding as a straight write-up.

Pick a depth before I draft it:

5ft — structure what you just told me into an outline + task description, nothing else.

10ft — same, cross-checked against what's already logged for this project (the async-link decision, 100-candidate deliverable, 7-8 day timeline) so nothing contradicts it.

50ft — same as 10ft, plus I flag risks/blind spots you haven't raised (consent/recording-law compliance for calling candidates in India, vendor evaluation criteria, ATS integration, edge cases in the early-exit logic).

Which one?

Human: 100 ft

Assistant: Sections for this analysis:

1. Project outline
2. Task description
3. Consistency check against what's already logged for this project
4. Risks and blind spots

Section 1: Project Outline

Objective
Replace manual recruiter screening calls with a subscription AI voice-interview tool. Recruiters currently make 2-3 rounds of calls per applicant. Most of that time is wasted — out of 500 applicants for one posting, maybe 10-15 are worth a human's time.

Scope
- Multi-job-post support: several positions live at the same time, each with its own question set. Not a single fixed script.
- Volume: capacity for thousands of interviews a month.
- Delivery method: async, link-based. Candidate gets a link (email/LinkedIn), clicks it, AI conducts the interview on their own time. No proactive outbound dialing.
- Output: structured answers per candidate, logged somewhere the team can review (sheet or dashboard).

Core value
Team stops spending hours on applicants who were never going to be a fit. Only the shortlist that clears screening reaches a human.

Adaptive behavior requirement
- Each job post gets up to a 10-minute question set.
- Tool is not a rigid script-reader. In the first 2-3 minutes, it should judge fit from the candidate's answers and how they're answering.
- If a candidate is clearly not a fit, the tool should shorten the call and wrap up early rather than running the full script.
- Tool should be able to adjust its line of questioning based on the conversation, not just march through a fixed list regardless of what's said.

Next: task description — what actually needs to get done to build/select and stand this up.

Human: give me the task description

Assistant: Task Description

1. Define requirements doc
   - List every job post that needs a question set live at launch
   - For each post: 5-8 core screening questions, pass/fail criteria, target call length (up to 10 min)
   - Define what "not a fit" looks like per role, in concrete terms — this is what the tool's early-exit logic needs to detect

2. Vendor shortlist and evaluation
   - Confirm this is off-the-shelf (per Raj's direction), not built in-house
   - Shortlist 3-4 tools that do async link-based AI interviews
   - For each, check: multi-job-post/multi-script support, monthly call volume limits and pricing, adaptive/early-exit capability (not just fixed-script playback), transcript/answer export format, India-based candidate support (call quality, language)

3. Pilot setup
   - Pick one live job post as the test case
   - Load its question set into the shortlisted tool(s)
   - Send the link to a small batch of real applicants first, not the full 500-1000

4. Validate the adaptive/ML behavior
   - Confirm the tool actually shortens calls for weak candidates instead of running the full script every time
   - Check it against real transcripts — does it correctly judge fit early, or does it cut off people who were still worth hearing out
   - This is the one piece vendors are most likely to oversell — needs hands-on testing, not just a sales demo

5. Output and logging
   - Confirm answers land in the format needed for the team to review (sheet/dashboard)
   - Match this to the existing deliverable structure already committed to Raj (100 candidates logged in a Google Sheet)

6. Rollout
   - Once pilot checks out, load all live job posts' question sets
   - Turn on for full applicant volume
   - Set a review cadence to check the tool's fit-judgment quality isn't drifting over time

Human: we are calling this agent siv. I had a call with my team member to give him a full download of how the tool should work. go through the call transcript and save it in your memory. you need to understand how this tool would work: [Impromptu Zoom Meeting - September 02 call transcript between Sheenam Rawat and Utkarsh Sharma, ~15 min, covering: current manual calling process via team member Yeshu (1500 applicants, 300 no-answer, most others not a fit); need for a human-like calling agent that logs answers to a Google Sheet then migrates approved candidates to CRM; training the agent per job post starting with Operations Manager, using JD + basic criteria; interview flow of intro/rapport questions before nuanced role questions; requirement that the agent recognize poor English/communication skills early for client-facing roles and wrap up politely rather than disconnect abruptly; two-tier Google Sheet idea (full transcript sheet + synthesized answer sheet); the agent must not rigidly re-ask questions when a candidate answers differently, must maneuver the conversation intelligently, unlike typical customer-service IVR bots; only approved candidates get moved to CRM, not all; wanting multiple agents configurable within a single tool subscription/account to simplify CRM integration; confirmation that available market tools work via a generated link rather than manual dialing, and that opening the link is optional for the candidate; concern about candidates treating unsolicited links as spam, preferring distribution via email/LinkedIn; voice preference of female, Indian accent, English only, since hiring is for a US company; uncertainty about the outbound caller ID/number setup; naming Agni AI (product "Ravan"/"Raven") as the first vendor to test, with a team member already having tried it and Sheenam wanting to test it herself; explanation that off-the-shelf tools are being used rather than building in-house due to time and technical complexity; core concerns being no hard cap on call volume/minutes and overall monthly cost; wanting to see training capabilities and Google Sheets integration; noting that final candidate assessment and next-round questions will be handled separately by feeding transcripts into Claude, not by the calling tool; a stated budget of up to $20,000/month with no volume limitation; an action item for Utkarsh to test Agni AI - create a free account, train the agent, run a test call, assess training and Google Sheets integration, check pricing/limits, and compare against alternatives found via Instagram, since TikTok isn't accessible/relevant in India; closing exchange confirming Utkarsh will explore Agni and look for other options on social media before reporting back.]

Assistant: Saved. Logged to the Siv project file and created a file for Utkarsh, since he's now working this with you.

What's new from this call that matters for the outline:

- Current baseline: Yeshu manually calls everyone today — this is what Siv replaces.
- Two-tier sheet output: raw transcript sheet + synthesized-answers sheet (not one sheet).
- Only passed candidates go to CRM, rejects stay out.
- One subscription, multiple agents configured inside it — not separate tool accounts per job post.
- Voice: female, Indian accent, English only.
- Budget ceiling: $20k/month, no volume cap.
- First vendor being tested: Agni AI (product "Ravan") — Utkarsh is running that test now.
- Claude does the post-call candidate assessment/next-round-question work, not the calling tool itself.

This changes what section 3 (consistency check) and 4 (risks) need to cover — want me to continue with those now, folded in with this new detail?

Human: we have two candidates right now - raven and bolna ai
Compare the two

Assistant: Comparing vendor claims against actual product info — that's a research task. Pick a depth:

5ft — quick pass: compare Raven and Bolna AI using what's on their sites/marketing (pricing, features, claims), no deeper checking.

10ft — same, but I verify pricing/limits against at least one more source per vendor (docs, reviews, other write-ups) rather than trusting the sales page.

50ft — same as 10ft, plus I check both against your actual must-haves (multi-agent under one subscription, no volume cap at $20k/month ceiling, Google Sheets export, Indian English female voice, adaptive/early-exit behavior) and flag anything that looks oversold or unverifiable from outside.

Which one?

Human: 50 ft

Assistant: Compared using public vendor info, cross-checked against your must-haves. Both claims should still be pilot-tested — marketing pages oversell in different ways for each.

Requirement | Agni (Ravan.ai) | Bolna
Built for recruiting | General voice-AI platform (sales, collections, support); recruiting is one listed "AI employee" role, not the core product | Recruiting is a named product line, with specific screener personas and recruiting-focused case studies — it markets a dedicated recruitment agent that runs structured phone screening, captures notice period, shift and location fit, and routes shortlisted/rejected outcomes back into the hiring workflow
Link-based delivery (click link, get called) | Not confirmed anywhere public — site shows outbound dialing from contact lists plus a browser "talk to the AI" demo widget | Not confirmed either — public material shows Google-Sheets-triggered outbound dialing, not click-a-link inbound. Need to ask both vendors directly before assuming either works the way you described in the call
Multiple agents, one subscription | Not confirmed publicly for this exact setup | Confirmed on their own pricing page — the Pilot plan explicitly includes sub-accounts access, which maps well to "one agent per job post, one account"
Google Sheets output | No Google Sheets integration found anywhere in Agni's public docs — only Salesforce, HubSpot, custom APIs, DB sync — their CRM integration list is Salesforce, HubSpot, Custom APIs, Database Sync | Confirmed multiple ways — native Zapier connector, Pabbly, and a documented direct-API + Apps Script setup — a Zapier template connects Bolna call-completion data straight into a Google Sheet
Voice: female, Indian accent, English only | Strong Hindi/Hinglish focus in their marketing — the agent code-switches between Hindi and English mid-sentence the way real Indian callers do — "English only" isn't a mode they advertise | Uses ElevenLabs' voice library giving recruiters full control over tone and persona from a wide range of available voices — an Indian-accent, English-only female voice is plausible but not explicitly confirmed
Adaptive early-exit behavior | Not a named feature on either vendor's site. Both are LLM-based agents — this gets built through your own prompt/instructions, not a toggle you switch on. This is the one thing that has to be pilot-tested with a real call, not taken on faith from a demo
Pricing at your volume | All-in rate starts around ₹2/min, with a platform subscription from roughly ₹2,999/month | Standard rate is about 6 cents/min, dropping toward 4.5 cents/min at higher spend tiers, with a bundled Pilot plan around 12,000 minutes. Both land well under your $20k/month ceiling even at a few thousand calls a month
India compliance | Their own terms put TRAI/DLT registration, do-not-disturb scrubbing, a 9am-9pm call window, and 24-hour opt-out handling on you as the customer, not the vendor | Same category of obligation applies to any outbound-calling vendor in India — not Bolna-specific, but not mentioned prominently on their site either

Two things worth flagging before you pick one:

- An independent (non-vendor) blind test scored Bolna notably lower on response latency than two other tools it was tested against — a 350ms vs 1.8-second response gap was described as the difference between a natural exchange and talking to a malfunctioning IVR — not Agni in that specific test, but worth listening to a live Bolna call yourself, not just the pitch.
- A rival's comparison page claims Bolna is fundamentally an open-source framework that needs developer setup and self-hosting — that's a competitor's framing so treat it skeptically, but Bolna's own site does lean heavily on API docs and "Agent Studio," so it may take more setup effort than a pure no-code tool.

Recommendation: run the same test protocol on both — Utkarsh is already doing this for Agni, worth having him mirror it for Bolna. Load the Operations Manager JD into each, run one real test call, check what actually lands in a Google Sheet, and specifically try to trigger an early-exit by giving a deliberately weak answer. That settles the one thing neither company's marketing will honestly tell you.

Sections 3 and 4 from the earlier outline (consistency check, risks) are still open if you want those next.

Human: Sections 3 and 4 are still open whenever you want them.

[Note: this was Claude's own prior-turn closing line, restated here for record continuity]

Human: You have given me such big paragraphs to read. It it so difficult to Ingest data in such high paragraphs. Can you give me more digestible responses please.

Assistant: Fair. That vendor comparison was way too dense.

Going forward:
- Short lines, not paragraphs
- Bullet points over tables with long text in cells
- One idea per line

I'll keep everything in that format from here on.
