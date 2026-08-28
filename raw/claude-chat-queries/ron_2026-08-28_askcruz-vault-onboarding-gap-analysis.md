---
thread_name: "askcruz-vault-onboarding-gap-analysis"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: Can you make me a document and put it in my Downloads folder on my computer? In that Downloads folder, create a separate folder and name it AskCruz Implementation.
In that, I want you to explain the entire process that has been followed in the implementation of EOXS to make that internal tool and to implement it in the system.
After you do that, I want you to take yourself out of that situation and think of yourself as someone who is doing this implementation for the first time. Go online and see whoever the four or five best people are, then use that as a persona and use that persona to review whatever file you created. See what all the gaps are and how that can be improved so that it is done faster.
After you do these two things, you will have information about how it can be improved. Create another document where you will mention all the ways it can be improved, how it can be improved, and why it should be improved.
One thing that I would like to learn more about is this: I saw this post from a guy. I'm going to share that link with you. It's from Kem Klitsch. I will see if there is a way to give you the transcript, but I will definitely give you the link. This guy was talking about how MCP is dead and everything. I want to understand what he's talking about also.
Basically, what I'm trying to do here is see whatever they include in the documentation plan right now: how the files have been structured and what process has been followed. Have someone who is more intelligent on all of the structures on how it could have been done better review the structure that currently is and suggest what the structure could be so that all the answers are correct.
After you do these two things, create a document which has all that information. I want you to think of yourself as if you are doing a 3GM implementation, where you are giving them the ERP data and the Gmail data. How would you do it for them? How would you make the implementation roadmap for them to ensure that their implementation is clean and whenever they ask any question to Claude, it is always, or the majority of the time, able to give them the right answer If they get the wrong answers from Claude, they will stop trusting Claude and the product that we have.

https://www.instagram.com/reel/DcEBQNPNPzs/?igsi=NjA3NjQwaHJpNnZh

Here is the transcript of the call above, 
"00:00:00
Most people use something like Obsidian with a wiki knowledge graph. You could use something like the Graphify open source repo that basically helps your agent build a knowledge graph around a large set of folders and files.
00:00:10
Now, things get more complicated when you want your agent to actually remember specific term I love you Agentic James. I think you're a cool dude. I think you make some awesome videos,
00:00:20
and I've seen some cool stuff and ways that you put together, but you're wrong. You're wrong on this one big time. No, there it, it, it doesn't get more complicated than this. Knowledge graph is the most complicated memory architecture.
00:00:31
The reason people like you and others don't realize that is'cause you haven't had the benefit of fifteen years plus experience implementing knowledge graph at scale in things like investment banks.
00:00:40
Let me tell you what the issue is. You're not doing it right, and I mean that respectfully. It's just frustrating seeing this stuff, and I wanna help, right? In order for knowledge graph to work, you have to ontologically and logically model.
00:00:52
And guess what? It's really hard, right? It's really hard to do. You cannot outsource this stuff to some vibe-coded repo or something like Obsidian, which will just automatically base synthesize from some glob or something tooling, right?
00:01:09
And create some rough YAML and just link everything together. And it's not gonna work if you have no actual multi-hop traversal tooling. If you're just grepping YAML and jumping from bar to bar, that is not knowledge graph. That is a big fucking mess that your
00:01:25
AI needs to read through at minimum. At best, it might just be reading the YAML and jumping through things, right? That you're praying to God have been modeled beautifully so that it can find what it needs. Of course, it's gonna eat up your context.
00:01:37
That is not knowledge graph, and it certainly isn't knowledge graph memory architecture. I am always here to help you if you wanna know how to do this stuff properly and actually experience what real knowledge graph is like, right?
00:01:52
And if you wanna look and explore the ideas of things like graph engineering, which I'm not that big of a fan of, but if you're curious, I can also help you with that, right? Keep making awesome videos. I love them.
00:02:03
I get a lot of inspiration. You have some really cool ideas. Don't fall for this Karpathy hype and stuff. He's am he's amazing. He's incredibly bright, but he's a researcher.
00:02:13
He comes up with vague ideas, loose ideas that are not formally tested by practitioners at scale, right? If you wanna know more about it, always happy to help. Reach out. Chemical Kit Club signing out." 

BEFORE YOU START ANYTHING REPHRASE EVERYTHING THAT I AM LOOKING FOR
Continue from where you left off.

Assistant: [Asked clarifying questions via AskUserQuestion before starting]

Question set 1 — rephrased the request into: Doc 1 "How EOXS Was Implemented"; drop the implementer hat and research 4-5 real experts to build a review persona; Doc 2 "How It Can Be Improved" from that persona review; clarified Kem Klitsch's transcript is entirely about knowledge-graph modeling and never mentions MCP; Doc 3 as a 3GM implementation roadmap informed by that structural critique; all three saved to Downloads/AskCruz Implementation.
User answers: "That's right" (shape); "Use the transcript as-is" (Kem Klitsch mismatch); "The first point is that you can pick as many people as required. Think of yourself as making a team who was doing the implementation. Who would you pick?" (expert persona); "Word docs (.docx)" (file format).

Question 2 — craft level for the three documents.
User answer: "Painting".

Assistant: [Set up a task list; requested and received Downloads folder access on the user's computer; researched Kem Klitsch (no verifiable public profile found under that name, and no "MCP is dead" content from him — confirmed the transcript is entirely about knowledge-graph/ontology modeling); researched and confirmed a real five-person expert panel (Juan Sequeda, Tony Seale, Jerry Liu, Harrison Chase, Zach Wahl); re-queried the teams-askcruz board (EOXS project id 4, AskCruz project id 6, 3GM project id 14) for full task detail and chatter; pulled OV Vault assets including the AskCruz self-knowledge architecture doc, the Development Standards SOP, the Code Review/QA SOP, and the full EOXS Client Implementation and Go-Live SOP; pulled 3GM Steel's client profile (34 implementation tasks since 2022, 956 emails, 14 calls, and live wiki pages including the AskCruz proposal call and an open pricing-error incident); then built three polished Word documents and delivered them]

All three documents are saved in Downloads/AskCruz Implementation on your computer, and attached above:

1. How EOXS Was Implemented — the factual build history: five phases from a repo-based store through to the DigitalOcean-hosted Postgres vault, the documented source-to-answer pipeline, the tools inventory, and a current-state snapshot including two real incidents (a silent ingestion stall on the architecture file, and a git-HEAD outage that broke Threads OV).

2. How It Can Be Improved — reviewed by a five-person panel built from real, currently active practitioners I researched: Juan Sequeda and Tony Seale (enterprise knowledge graphs), Jerry Liu (LlamaIndex, RAG at scale), Harrison Chase (LangChain, agent memory), and Zach Wahl (Enterprise Knowledge, governance/rollout). Their honest read: the infrastructure is more mature than the knowledge model. Eight findings, prioritized, closing with why this matters for the $1M AskCruz ARR goal specifically.

3. 3GM Implementation Roadmap — written as if I'm running it: what's genuinely new (3GM's been an EOXS ERP client since 2022; AskCruz itself was only just confirmed, 12 August, and at a reduced 2-user scope with a shorter term — Travis Lane is being deliberately cautious, which the roadmap treats as the right instinct to build around), a concrete ontology for their data, a phased rollout mapped to their actual 21 board tasks, a right-answer test suite, and an explicit "I don't know" contract.

On Kem Klitsch: the transcript you sent is entirely about knowledge graphs — his point is that Obsidian-style auto-linking isn't real knowledge-graph work because nobody deliberately modeled the ontology. It never mentions MCP, and I couldn't find any "MCP is dead" content from him, or much of a public profile under that name at all — he doesn't appear to be broadly indexed. I used the substance of his argument anyway (it's the backbone of Document 2's top finding and Document 3's ontology section) because it's independently corroborated by Sequeda's and Seale's public work, but I flagged his credentials as unverified in the doc itself. If you find the actual "MCP is dead" post, send it and I'll fold it in.

The one thing worth flagging before you read further: 3GM's own ERP has active, open data-quality issues right now (a pricing error on order S11105, an open inventory bug, a product catalog still mid-correction) — independent of anything AskCruz does. Document 3 treats that as a real input, not background noise.
