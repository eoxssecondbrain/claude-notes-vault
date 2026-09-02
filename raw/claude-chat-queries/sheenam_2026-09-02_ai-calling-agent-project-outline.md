---
thread_name: "ai-calling-agent-project-outline"
user: "sheenam"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
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

Human: Now I need a name for this agent.

Assistant: A few directions, take what fits:

Steel-industry tie-in (fits EOXS's world)
- Forge — raw applicants go in, a shaped shortlist comes out
- Sieve — filters out the 90% that don't matter
- Foundry — where the real candidates get separated from the rest

Function-first, plain
- Shortlister
- FirstPass
- Gatekeeper

If you want a name that also works as a product/brand later (not just internal), Forge or Sieve carry outside a slide deck better than Gatekeeper or FirstPass, which read as internal tool labels.

Pick one, or tell me if you want it to sound more human/assistant-like (a "Sam" or "Ava" type) instead of function-based — different naming logic entirely.
