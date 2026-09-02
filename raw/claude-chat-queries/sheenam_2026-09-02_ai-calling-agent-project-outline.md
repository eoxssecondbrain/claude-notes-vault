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

Human: we are calling this agent siv. I had a call with my team member to give him a full download of how the tool should work. go through the call transcript and save it in your memory. you need to understand how this tool would work:

Impromptu Zoom Meeting - September 02
VIEW RECORDING - 15 mins (No highlights): https://fathom.video/share/mWLbyngV_3Ta4reHjiEWyXuod75A7qvG

---

0:19 - Utkarsh Sharma
  Yes.

0:20 - Sheenam Rawat (sheenam.rawat@gmail.com)
  So let me give you a full picture first, and then maybe you can ask questions. Maybe that'll answer most of the questions.  So the idea is, we need just someone to make the interview calls. So what happens is, we have Yeshu in our team, right?  He makes interview calls to all the applicants who apply for a particular job post. Now, if we have one job post that has 1,500 applications, he has to make a call to all those 1,500 people, right?  Out of those 1,500, 300 won't even answer the calls, right? The remaining who answer the calls, those people might not be a good fit based on their conversation, whatever.  You know, you call someone, you just get a vibe in the very first few seconds that, okay, that person is not going to work, right?  This is something that takes a lot of time, calling 1,500 people, or any person, it takes a lot of bandwidth.  We want to remove that entirely. So we need an agent that can call like a human, talk like a human, and record all the answers in a Google Sheet.  Then later on, data from that Google Sheet can be migrated to our CRM. Now, there would be certain blocks first.  First would be actually training this calling agent. We would give this calling agent a transcript for every job post that it makes a call for.  For example, let's start with operations manager. We would give it a JD for operations manager, that this is the basic criteria.  When you call a person, we already know their name. We already know their education background and everything. So when we call this person, we just need this agent to ask, hi, how are you doing?  Okay. So you applied for this particular post. We know your name and everything. Can you give us an introduction of yourself?  What do you like in general? What kind of hobbies and interests do you have? Then we can get to more detailed, nuanced questions about the job position itself, right?  These questions would be synthesized once we have a tool, and then we can start training, then we can create a questionnaire.  But this tool needs to be a little smart here. So for example, we called someone and in the very first minute, you realize that this person does not have good communication skills, right?  They are poor in sentence formation, their English is maybe not good, and we are high. I for a role that requires a person to have good communication skills because we need client-facing people and a person is going to be client-facing.  If that person can't speak English, they can't be a good fit. Right? So if this tool realizes, okay, this person can't speak English, does not have the confidence to talk, we can wrap up the interview, but it should not be like, you know, disconnect the call abruptly.  could be like, okay, thank you so much for sharing that information with me. We will reach out to you later.  And that's it. Then that call could be whatever discussion happened can be logged in a Google Sheet. I don't want the entire transcript of the call in a Google Sheet.  I don't know how we will, I don't know, manufacture this in a way where only the questions that we are looking an answer for are manufactured in that Google Sheet.  Right? Maybe there could be two levels to this. One Google Sheet can have the entire transcript of the call.  Another one can synthesize data that we need answers. Whatever our question was, what we were looking for, that answer can be logged in that user sheet.  Then another person calls. Another person receives a call, then they start talking. The agent starts asking questions based on the conversation, how it is flowing.  It needs to be attentive. It shouldn't be like, okay, I asked you, what is 2 plus 2? And if you did not answer 2 plus 2 when you said something else, you are constantly saying, sorry, I could not register that.  Can you please tell me what is 2 plus? It shouldn't be like that. That happens, right? When we call these AI, like phone, messenger, something, when you call any customer service, they have an AI number.  And if they don't receive the exact answer they're looking for, they go back with the same script that they have.  It shouldn't be like that, right? It should be smart. should be able to maneuver the conversation. Then based on the conversation, if we do find someone who is actually able to answer the questions properly, all of that data is going in a Google sheet.  And out of- Supposedly called 1,200 people. Now out of this 1,200 people, only 800 might seem like, you know, to be a good fit.  And they can be moved to the next level. In that level, that is up to me and my team to figure out how we want to proceed with that.  But the first level is done. The first round of calling is done with them. This was for one job post.  Now I want another calling agent for another job post. I want a tool where I can configure like two, three different agents within one account or subscription so that you don't have to buy a lot of these accounts because it would be difficult to connect all of that with our CRM also, right?  Now, another thing that I have seen so far is that all the tools that are available in market right now, they do not call manually.  They generate a link. We can share that link to the candidates. And if they click on that link, that is when they would get a call on their number.  They won't get a call unless they don't. to an So we would have to be mindful of that. That is how the calling agent works.  So if we sign that link to 1500 people, 500 might not even open the links. They would feel like, okay, this is spam.  So let's not, you know, risk opening a link or anything else. We would try to keep it via email or LinkedIn, but you never know.  Right? So that is the basic criteria, basic structure of this agent. Now you can ask me questions.

6:32 - Utkarsh Sharma
  My first question is that is, is the agent that we are building, it should call on a number or it should be an interview AI call.  Like the, like the board will ask the questions directly related to the field that a candidate is. Or there should be a sequence like you mentioned that first the AI will judge the vibe of the candidate.  And then it further goes to the technical questions. So this is how the AI has to be worked. So it should be a calling agent on a candidate's mobile phone, basically.  Number. OK. OK. And how would the AI generate the questions, questions and answers? How would we know that that question would it be?  Achai, will keep up.

7:30 - Sheenam Rawat (sheenam.rawat@gmail.com)
  Yeah. When we configure that AI agent, we will give it a set of questions to ask in the interview.  But again, it should not stick to those questions entirely. It should be able to maneuver the conversation on its own if it sees, you know, if the person did not answer the question.  If I ask them, OK, what did you do in your, what do you do in your free time? If that person is not talking about their free time, if they start talking about their work life, it shouldn't be like, OK, I didn't get that answer.  Can you tell me what we do? It shouldn't be like that. should be like, OK. And. Yes, it has to be very smart and diplomatic, or it could be like, okay, I understood what you said, but I asked you a question about how you spend your free time.  Could you get back to that and maybe give me some insight on that? Okay.

8:21 - Utkarsh Sharma
  And all the conversations will be stored in a Google sheet. That's what you want. Yes.

8:28 - Sheenam Rawat (sheenam.rawat@gmail.com)
  Yes. Initially, I want all the conversations to be in a Google sheet. Later, when out of 1000 applicants, we get like 300 good applicants.  I want to move the data of those 300 applicants to our CRM. I don't want to fill our CRM with rejected candidates also.  Right? So I want that whatever candidates we do approve of after this, only those would be moved to our CRM, not all of them.  This is a... be, ah.... Like second layer, we can move to that later and decide how we want to, you know, layer that approval.  But for now, the calling agent needs to be able to put all of that data in a Google Sheet.

9:15 - Utkarsh Sharma
  Okay. And is there any preference of the voice of the bot? Like it should be male or female voice or any, any accent?

9:25 - Sheenam Rawat (sheenam.rawat@gmail.com)
  Female, Indian, Indian accent, because we are going to be running hirings in India, right? So it needs to have an Indian accent.  We, we have options available for Hindi and English, but I would like to go with English only because we hire people for an American company, right?  There is no point in hiring people who can't even speak basic English.

9:50 - Utkarsh Sharma
  Okay. Okay. I get it. And what would be the number from which the bot would call?

9:57 - Sheenam Rawat (sheenam.rawat@gmail.com)
  It would be. How would I get that number? So, I looked for a couple of tools that already do this.  We don't have to build something of our own. It would take a lot of time. It would require a lot of connections, MCPs, plugins, I don't know what not.  So, there are tools available in the market. If you go and like search for a couple of them on Instagram, you would be bombarded with a number of brands, right?  So there is one tool called Ravan AI, which is by Agni. I can share the link with you. Look into that.  Someone in my team tested it as well. I also want to test it myself. If you, Agni AI. Yeah, so it's Raven or Ravan, I don't know how to pronounce.

10:47 - Utkarsh Sharma
  I'm sharing the link with you.

10:50 - Sheenam Rawat (sheenam.rawat@gmail.com)
  Yeah, I'm sharing the link on chat. Right? So if we had a subscription of this tool, it has everything configured.  We just need to train that AI agent and tell it how to make the calls and it has to be done.  Right? Everything has been set up in this tool. The only concerns I have is that it should not be limiting.  Like, okay, you can only make a hundred phone calls in a month, or you can only have like 300 minutes of phone calls in a month, right?  We want to call like thousands of people in a month. We can't have that limitation. And if we do get that sort of, you know, opportunity to call so many people, what is the cost that we will get?  Like how much we would be spending on this application overall? Those are my concerns. And further, I want to see the training capabilities.  How well can we train this? How well can this be integrated with Google Sheet so that it can store data and everything?  So finalizing part intelligence, the question that you asked me in the beginning is something that we will do ourselves with the help of law.  So once we have the data, And data from all these people who would be taking the calls. Once we have the transcripts, they're answered.  We will put all that in Claude and be like, okay, assess this sheet and see all the candidates who have answered, figure out the people who actually seem like a good fit, and then give us their details, and then what should be the next round of questions for them.  That is something that Claude would be able to help us with. For now, we just need to find the right tool that can do this job for us.  So if you test this tool, you'd understand that, okay, everything that we need is already built. We just need to find the right budgeting and, you know, the right training software.

12:41 - Utkarsh Sharma
  Okay. So I just have to find the right tool, which is economically feasible and doing the right job. Yeah.

12:49 - Sheenam Rawat (sheenam.rawat@gmail.com)
  I don't mind spending 20,000 on monthly basis, but it should give us the liberty to call as many people as we want in a month.
  ACTION ITEM: Test Agni AI (Ravan) for Sheenam: create free acct, train agent, run test call, assess training/GSheets, check limits/pricing, compare - WATCH: https://fathom.video/share/mWLbyngV_3Ta4reHjiEWyXuod75A7qvG?timestamp=771.9999  It should not be like, okay, you can call only 100 people or like 100. You can start by testing out Agni.  See how you can train the agent. So you can create a free account on this. can train the agent on the kind of questions you want.  It will give you a link. you click on that link, it will give you a call or it will be directed to talk to that AI and it will ask you all the questions.  Okay.

13:28 - Utkarsh Sharma
  Okay. That's all my questions currently. If you have anything else, if you want me to fill up with any suggestions.

13:39 - Sheenam Rawat (sheenam.rawat@gmail.com)
  The best way of finding the right tool would be on Instagram, right? I would suggest TikTok also, but since TikTok doesn't work in India, like Indian people won't be posting content.  So even your VPN and everything, it won't give you the right content, right? So if you go on Instagram and you type this Ravan there, and then you watch a couple of reads, you'll start getting more suggestions.  You can start testing them out, but I think this is a good one. If we get good budgeting over this, we can start working on this and start training this.  This is the best tool I have seen so far.

14:27 - Utkarsh Sharma
  Okay. I will just explore this Agni that you have sent me and if there are other options as you have told me to look on Instagram and other social medias, then I will also look on that.

14:41 - Sheenam Rawat (sheenam.rawat@gmail.com)
  You can test this out in 30 minutes and after that you can look for other options if you can find any.  If not, then we can start training Agni. Yeah, sure.

14:50 - Utkarsh Sharma
  Yeah, okay. Right? Okay. Okay, thank you sir. Thank you.

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
