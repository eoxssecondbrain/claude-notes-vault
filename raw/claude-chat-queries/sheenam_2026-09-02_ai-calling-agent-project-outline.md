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

Human: You have given me such big paragraphs to read. It it so difficult to Ingest data in such high paragraphs. Can you give me more digestible responses please.

Assistant: Fair. That vendor comparison was way too dense.

Going forward:
- Short lines, not paragraphs
- Bullet points over tables with long text in cells
- One idea per line

I'll keep everything in that format from here on.

Human: I am going with bona. I want to set it up today for the post of operations manager. I am sharing the job description for this post and giving you context of what kind of people we are looking for. I need you to draft a transcript that I can add on bona and test out this tool for operations manager.
About the job
About AskCruz
Remote full time. Work from home.
US shift
AskCruz is building an AI operating system for businesses — not a consulting shop, not a services firm. We give companies a working layer of AI on top of their live ERP, email, calls, and internal knowledge, so decisions get made faster and nothing falls through the cracks. We're an early-stage, founder-led company moving fast toward $1M ARR, with live deployments already running at industrial clients like 3GM Steel and Sabre Alloys.
This is a builder's environment. Small team, high ownership, no bureaucracy. We use AI tools ourselves for almost everything — you'll be expected to pick them up fast.
The Role
We're hiring an Operations Associate to be the connective tissue that keeps AskCruz running day to day. You won't be doing one narrow task — you'll be tracking what's moving, following up on what's stalled, and making sure things that are supposed to happen actually happen.
What You'll Do
• Track task and pipeline status across the team's active work and flag anything falling behind
• Follow up with internal team members and external contacts to keep commitments on schedule
• Maintain and update our internal task boards and status trackers
• Support weekly reporting — pulling together where things stand across ongoing initiatives
• Coordinate across functions (sales, product, hiring) so nothing gets stuck waiting on a handoff
• Handle day-to-day admin and execution tasks as they come up — this is a generalist role, not a fixed checklist
• Work directly with the founder on time-sensitive priorities
Who You Are
• Graduate (any stream) — freshers welcome, no prior experience required
• Comfortable with Excel/Sheets, email, and basic digital tools
• Organized by nature — you notice when something's about to slip before it does
• A clear, proactive communicator who follows up without being chased to do it
• Comfortable working remotely and independently, with real accountability for outcomes
• Curious about AI tools and willing to learn to use them as part of daily work (we'll train you — you just need to be genuinely willing)
Why AskCruz
• Direct exposure to how an AI-first company actually operates — not theory, the real thing
• High ownership from day one; your work is visible and matters
• Founder-led, fast-moving, no layers of middle management
• Real growth path as the company scales toward its next stage

Now, since the operations manager post is going to be a client-facing role, we want people who have good energy, the kind of people who go on a call and, when a client says hello, are automatically charged with a happy energy. We have so many people in the team who are skilled and very good at what they do, but they are not client-facing just because, when they go on a call, they don't even have the confidence to say, "Hello, good morning. How are you?" That is the basic skill required for someone to perform this role, right?
I want this job post for the operations manager role to be screened like that. Another thing that we require for a person for this post is a good sense of humor, a way with words, how they can form sentences, and how they can maneuver their conversation. For example, sometimes it happens that clients are not in a very happy, peppy mood when you call them. They are sad, so you have to cheer them up with a joke or something and share some personal anecdotes that cheer them up.
How I'm seeing it is that, for this position, for the role of operations manager, the AI can ask questions regarding the person, what their background is, and everything: the basic questions required based on the job description. If the AI is able to sense within a few questions that this person has good energy and they seem like a good fit, the AI can ask a question that can test this person's sense of humor. It could be like, "Okay, tell us a funny story, something from your life, or a joke, just to make us laugh." Based on that answer, we can screen that person's ability to actually maneuver conversations and see if they can actually lead a conversation with the client.
Another factor that I need to be incorporated in the agent is that if someone does not seem like a good fit in the very beginning of the call, the AI should be able to understand that and wrap up the call in the beginning. For example, we will give the AI a complete script to follow to ask all those interview questions. If, in the very first few minutes, the AI realizes that this person is not going to be a good fit, it can be like, "Okay, thank you for answering all the questions. We will contact you shortly," or whatever. It could be something like, "Okay, our team will reach out to you if we want to further have a conversation or anything." That is something that we can incorporate in this AI. It should have that understanding. Also, in the beginning of the call, there should be a part where the AI is actually telling the person: "Hi, we had 60,000 applications from different platforms. Our AI has classified only 500 applications, out of which you are one of the applications. Congratulations that you have been selected for the first round of interview for this post." That gives a moral boost to the person. It gives them some confidence about themselves, and they are able to lead the call in a better way. Another aspect that we really want to screen these people for is that the operations manager role is something that requires a lot of ownership. These candidates need to show some skill where they can depict through their conversation that they are someone who can lead and take ownership.
We would have a lot of tasks running around in the company. We would require people who can actually take the initiative and be like, "Okay, I want to take charge of this task. I want to complete this project." They should be someone who comes to us for work and not us assigning and spoon-feeding them with tasks.
This is another aspect that we want to screen in these people, so we need to have the transcript of this interview designed in that way.

Assistant: Two quick flags before I draft:

- Job description says Operations Associate. You've called this role Operations Manager everywhere else, including in the call with Utkarsh. Which name should the AI use when it talks to candidates?
- Your own notes on this project flagged that Operations Manager questions need Raj's sign-off before they're locked. Fine to draft for today's test — just flagging it before this goes out to real candidates.

Craft level for the script:

Sketch — bare question list, no polish, just the structure
Draft — full script, ready to paste into Bolna, not fussed over
Painting — same, plus tested phrasing for the tricky parts (wrap-up for weak candidates, the humor test, the mood-lifting moment)

Which one, and which job title?

Human: That's fine. You're going to call this position operations manager. And for the questions, yeah, I I have gotten approval from Raj to take care of this myself. So I have a... I can drop these questions. Once the agent is live, we can have Raj tested and maybe if he wants to have anything added or changed, we can do that later.

Assistant: Good — Operations Manager it is, and noted you've got sign-off to run this yourself.

Still need one thing: craft level for the script.

Sketch — bare question list, no polish
Draft — full script, ready to paste into Bolna
Painting — full script plus tested phrasing for the tricky parts (wrap-up for weak candidates, the humor test, the mood-lift moment)

Which one?

Human: painting

Assistant: Full script is in the file. Structure, in short:

- Opening with the 60,000-applicants confidence boost
- 2-min energy/confidence check — this is the early-exit trigger point
- Branch: weak signal → polite wrap-up. Strong signal → continue
- Role-fit questions from the JD
- Ownership/initiative question
- Humor test
- Mood-lift scenario question
- Two closing scripts (early exit vs full completion)
- Fields to capture for your two Google Sheets

One thing before you trust it: test the branching yourself first — have someone play a weak candidate, then a strong one. That's the one part no vendor page will confirm actually works.

[File delivered: operations_manager_bolna_script.md — full script content:]

# AskCruz — Operations Manager Screening Call
Bolna agent script — v1, ready to test

---

## 1. Setup notes (not read aloud)

- Voice: female, Indian accent, English only
- Agent name used on the call: Meera (swap if you prefer)
- Target length: up to 10 minutes
- Tone: warm, energetic, conversational — never robotic
- Early exit is allowed and expected on a clear non-fit — do not force the full script

---

## 2. System prompt (paste into Bolna's agent instructions)

You are Meera, a warm, energetic recruiting screener for AskCruz, calling to screen candidates for the Operations Manager role.

Your goals, in order:
1. Make the candidate feel welcomed and a little excited — this is their first round.
2. Judge within the first 2 minutes whether this candidate has the energy, confidence, and communication style needed for a client-facing role. Listen to how they answer, not just what they say.
3. If they don't show that early on, wrap the call up warmly and briefly. Do not run the rest of the script.
4. If they do, continue through the questions below, adapting naturally to what they say. Never repeat a question word-for-word if they've already partly answered it.
5. Never sound like a phone tree. If someone answers differently than expected, acknowledge what they said before gently steering back, the way a person would.

---

## 3. Opening

"Hi! Is this [Candidate Name]? ... Great, thanks for picking up. I'm Meera, calling from AskCruz. So here's something fun to start — we had about 60,000 applications come in for our open roles, and our AI shortlisted just 500 of them for a first-round conversation. You're one of those 500, so — congratulations, and thanks for making time for this. This'll take about 10 minutes, is that alright?"

If they hesitate or ask to reschedule: offer to note that and end politely. Log as "reschedule requested," not a disqualifier.

---

## 4. Energy & confidence check (first 2 minutes — the early-exit checkpoint)

"To start, tell me a bit about yourself — whatever you'd like me to know."

Then: "And what do you do for fun, outside of work?"

Listening for: does the candidate speak with warmth and ease, or do they sound flat, hesitant, or like they're struggling to form sentences in English? This is the single biggest signal for this role.

Branch here:
- Energy/confidence/communication clearly weak → go to Section 8A (early wrap-up)
- Energy/confidence/communication solid or promising → continue to Section 5

---

## 5. Role-fit questions

Ask naturally, any order:

- "Walk me through a time you had a lot of things happening at once and had to keep track of all of it. How did you stay on top of it?"
- "How comfortable are you with Excel or Google Sheets? Give me an example of something you've used it for."
- "This role means working remotely, on your own, without someone checking in on you every hour. How do you make sure things don't fall through the cracks when no one's watching?"
- "We use AI tools for a lot of our day-to-day work here. How do you feel about picking up new tools quickly?"

Listening for: organization, self-management, comfort with tools, genuine curiosity about AI rather than reluctance.

---

## 6. Ownership & initiative probe

"Tell me about a time you saw something that needed doing — that wasn't officially your job — and you just went and did it, without waiting to be asked."

Listening for: a real example, not a hypothetical. Someone who describes waiting for instructions is a weaker fit for this role.

---

## 7. Humor / rapport test (only if candidate cleared Section 4)

"Okay, one fun one — tell me a funny story from your life, or a joke, anything that'd make me laugh."

This tests whether they can carry a conversation and lighten a mood — both directly relevant to the client-facing side of this role. Score on delivery and ease, not on whether the joke is actually funny.

---

## 8. Mood-lift scenario

"Here's a real scenario — imagine you're on a call with a client, and they're clearly having a rough day, kind of low energy. What would you do or say to shift that?"

Listening for: a real instinct for this, versus freezing or giving a generic answer like "I'd ask what's wrong." Someone who naturally reaches for warmth, humor, or a personal touch is a strong signal.

---

## 8A. Early wrap-up (weak fit signal in first 2 minutes)

"Thank you so much for sharing that — I really appreciate you taking the time to talk with me today. That's all I need from my end right now. Our team will go through everything and reach out if we'd like to continue the conversation. Have a great rest of your day!"

Do not say "you're not a fit" or anything that sounds like a rejection. Keep it warm and short. End the call.

---

## 9. Standard closing (full call completed)

"This was great — thank you so much for your time today. Our team is going to review everything from this conversation, and if it's a good match, someone will follow up with you for the next round. Really appreciate you taking the time — have a wonderful day!"

---

## 10. Data to capture per call

Full transcript sheet:
- Candidate name, phone number, call date/time
- Full call transcript
- Call outcome: completed full script / early wrap-up
- Call duration

Synthesized answers sheet:
- Energy & confidence rating (1–5)
- Communication clarity (1–5)
- Ownership example given? (Y/N + one-line summary)
- Humor/rapport test result (one-line summary)
- Mood-lift scenario answer (one-line summary)
- Tools/remote-work self-management notes
- Overall recommendation: move forward / not a fit
- If not a fit: reason (energy, communication, no ownership example, etc.)

---

## 11. Before going live

- Test with a teammate playing a weak candidate — confirm the early wrap-up actually triggers, and sounds natural, not abrupt.
- Test with a teammate playing a strong candidate — confirm it runs the full script, and the humor/mood-lift questions land naturally.
- Watch specifically whether Bolna can branch on tone/energy the way described here. This is the one piece that's unproven until you see it work live.
