---
thread_name: "siv-bolna-calling-vs-link-approach"
user: "sheenam"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Human
As you know, I have created an AI hiring agent on Bolna AI, and I've named it Siv. You can go through the chat in this Claude account to get more context.
Now I have set up the agent for the post of operations manager. There are a couple of things that I would like to clarify. Raj said that, instead of having this agent called AI, these calls would work on Bolna like this: I will upload a CSV-format file of all the people that need to be called. For example, I have 818 applicants for the post of operations manager. I will upload the sheet with 818 applicants' phone numbers on Bolna, and Bolna will automatically start calling all of these numbers. Whichever numbers are called and answered, the interview would be conducted. All the data of the interview, the transcript, would be saved in Bolna. I can download it and export it however I need.
Now Raj said that, instead of having this agent call each of these numbers, he suggests that we should have a mechanism where we can share a link with all these applicants over LinkedIn (because they applied for the job post on LinkedIn). We can share this link with them, and then these applicants can click on that link, and then they would get a call.
I understand this idea, and that is initially what I thought, but that would require a lot of manual configuration. Someone would have to sit and send that link to all those 818 candidates, and they will open that link and then conduct the interview.
The second concern that I have with this is that a lot of people are skeptical about opening links on their systems because everyone sees that as dicey. If I were to get a link on my LinkedIn and it would ask me to click on a link to set up the interview, I would also not click it. I would also try to verify the website and the person who has sent me the link.
If I don't have the mandate to send these links, whoever would send these links to each of these people would also need to have a verifiable background. If they go and check about the company (for example, we are doing this for Askcruz), there is no surety that they would even believe it because we don't have a website yet. It kills our credibility to some level.
Another thing that I worry about with this method is that a lot of people use LinkedIn on their computers. If they use it on a computer and click on that link on their computer, they won't be able to receive the call because the call is required to be on the phone number, and the phone number needs to be available to make this call. It does not seem feasible to me. I need to explain this to Raj because he asked me: instead of having this agent call all these people, people should get the link.
Lastly, another concern that I have is that the rate of these interviews being actually conducted will totally depend upon the people actually clicking the link. If they don't click on the link, we don't get an interview. These are my concerns. What do you think about them? I need to send Raj back an update on this, and I would like to make this agent live today to conduct the post for operations manager.

# Assistant
Read threads-ov and raj-eoxs-vault skill files, pulled the eoxs-db index, checked memory notes on the Siv project, and searched past chats for prior Bolna context (nothing indexed yet on Bolna specifically — the last recorded state was the Sept 2 decision to test Agni AI for async link-based screening, so this Bolna/CSV-calling setup is new since then).

Your concerns are legitimate, not just resistance to Raj's idea — the manual workload, the link-trust problem (especially with no AskCruz website yet), the desktop-vs-phone issue, and the click-dependent conversion rate are all real operational risks with the link approach.

This needs a proper side-by-side before I hand you something to send Raj, and it ends in a message to him — so two quick picks first:

1. How deep should the comparison go
2. How polished should the update to Raj be

Rigor:
5ft deep - quick, fastest read on the tradeoffs
10ft deep - verified, checked against real numbers where possible
50ft deep - full investigation, plus angles you didn't ask about
100ft deep - staged, delivered section by section

Craft (for the Raj update):
Sketch - bare structure, one pass
Draft - styled, presentable, not fussed over
Painting - custom, detail-checked
Commissioned - full polish

[ask_user_input_v0 called: Q1 "How deep should the comparison go?" options 5ft deep / 10ft deep / 50ft deep / 100ft deep. Q2 "Craft level for the update to Raj?" options Sketch / Draft / Painting / Commissioned]
