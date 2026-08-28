---
thread_name: "jarvis-ai-agent-video-transcript"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: 00:00:00
Here's how you can build your own Jarvis AI agent in one weekend in nine steps. Step number one, we're gonna give Jarvis a home. You can use an old computer or a Mac Mini, but my recommendation is to use a virtual private server

00:00:11
because it stays on twenty-four/seven, and it's always secure. Step number two is to install an agentic harness. This is the infrastructure around your AI agent. My recommendation is to install Hermes as the agentic harness.

00:00:23
Step number three is to install an AI model. This is like the brain of your Jarvis. You can use Anthropic's Claude, you can use OpenAI's ChatGPT, and you can even use open source models. Step number four, we're gonna get Jarvis to interview us.

00:00:36
So have your Jarvis ask you questions to know about your business, your life, and your goals. Step number five, we're gonna give our Jarvis a memory, so I recommend building an AI second brain. Step number six, we're gonna start creating skills for Jarvis.

00:00:47
This is gonna teach Jarvis how to execute tasks really well, and you can create skills for all sorts of different job roles that you have inside of your business. Step number seven, we're gonna start connecting our Jarvis to tools. So I like connecting it to my Google Worksuite

00:01:00
so it can access my calendar, my email, and my tasks, and I also connect it to creative tool to create content. Step number eight, we're gonna connect Jarvis to our communication channels, so you can use Telegram, iMessage, WhatsApp.

00:01:10
And finally, step number nine, we're gonna build our AI dashboard. This is our command center so that we can access Jarvis. If you're looking for a step-by-step course on how to actually set up your Jarvis from scratch without having to code, I put together the entire course as well as guides, prompts,

00:01:23
and copy-and-paste templates inside of my community. If you wanna join, just comment the word Jarvis, and I'll go ahead and send it over to you. As always, if you wanna stay ahead in the world of AI, make sure that you give me a follow.

Assistant: This doesn't clearly match any of the configured skills — it's a pasted video transcript on building a "Jarvis" AI agent (VPS, agentic harness, model, memory, skills, tools, comms, dashboard), with no explicit question attached. It's tangentially close to your Atlas/Poder AI framework work, but I don't want to guess.

What do you want done with this — a critique of the approach, a mapping of these 9 steps against what you're already doing with EOXS/AskCruz Claude skills and infra, or something else?

User: I want to build this this weekend: buy a server in India and set up all of this infrastructure. Can you tell me which server I should buy?

The second step he's talking about is a harness. Can you brief me on what that is? I know the third step is having an AI layer on it, but I don't know what the second step is.

I want to have a discussion with you on:
- Which server to buy
- What the harness is
- How to set it up
- How much time this will take
- Whether I would be able to make something like this over a weekend and then give it access to everything

Assistant: This is a research/strategic task (server choice, harness explanation, setup plan, feasibility), so per your rigor-level rule, pick one:

- 5ft deep — Quick: direct answer using well-known options (e.g. common VPS providers, what "Hermes" harness likely is), no deep verification.
- 10ft deep — Verified: same, but I check current pricing/specs, actual harness options, and cross-check at least one source before reporting.
- 50ft deep — Deep: full investigation — verified, plus explore alternatives the video didn't mention (other harnesses, hosting options in India specifically, security/compliance angles), flag risks and blind spots (e.g. giving an agent broad tool access unattended), realistic time estimate.
- 100ft depth — Staged: same as 50ft but delivered section by section (server choice → harness → setup steps → time/feasibility), you say "next" between each.

Which level?

User: Can you please tell me first what a harness is, and then we can get to this level of depth? I would like a 10-foot-deep analysis for now.

Assistant: What a harness is

The video's "step 2" is the plumbing around the model, not the model itself. A raw LLM (step 3) is stateless — it takes text in, gives text out, forgets everything between calls. A harness is the software layer that wraps the model and gives it:

- Memory (short-term scratchpad plus a persistent store)
- Tool execution (letting it actually run commands, hit APIs, edit files)
- State management (tracking where it is in a multi-step task)
- Guardrails (what it's allowed to touch, sandboxing)
- Orchestration (deciding when a task is done, handling errors/retries)

The model is "the brain," the harness is "the nervous system and hands." Hermes (from Nous Research) is a real, actively maintained open-source harness — self-hosted, model-agnostic (works with Claude, GPT, open models), with built-in memory, skills, and gateways to Telegram/Discord/Slack/WhatsApp. It's a legitimate pick, not vaporware — verified against independent sources, not just the video.

Server — verified pick

For India specifically, the well-established, non-marketing-blog options are:

- Vultr Mumbai — ~₹590/mo for 1GB, hourly billing, good for testing before committing
- DigitalOcean Bangalore — ~₹350-400/mo entry, reliable, huge community docs (matters when you get stuck)
- AWS Lightsail Mumbai — ~₹295-590/mo, integrates with S3/RDS if you expand later
- Hetzner (Germany, not India) — best specs-per-rupee (2 vCPU/4GB for ~₹460/mo) but 40-60ms latency from India — fine since a home-assistant agent isn't latency-sensitive

I'd skip the "best VPS India 2026" listicle picks (GigaNodes, AIC Cloud) — several of those articles are self-published by the provider itself, which is a red flag for objectivity, and you have no track record with them.

For your use case (Hermes + Claude API + a handful of tool integrations, not heavy compute), DigitalOcean Bangalore or Vultr Mumbai at the 4GB/2vCPU tier is enough. Don't over-buy compute — the bottleneck will be your API costs and integration work, not CPU.

Setup, realistically

1. Provision server, harden it (SSH keys only, firewall, fail2ban) — 1-2 hrs
2. Install Hermes, point it at Claude via API key — 1-3 hrs (depends how much its docs match your OS/version)
3. Connect one tool (e.g. Gmail or Calendar via OAuth) — 2-4 hrs, this is usually where people lose a weekend, OAuth flows and scopes are fussy
4. Basic memory/skills config — 2-4 hrs
5. Messaging channel (Telegram is easiest) — 1-2 hrs
6. Dashboard — skip this weekend, it's polish, not function

Time and feasibility — my honest read

A working skeleton (server up, Hermes running, talking to Claude, one tool connected, reachable via Telegram) is a realistic weekend for someone technical. Nine fully-working steps with a dashboard and multiple tool/comms integrations, tested and reliable, is not — that's a 2-3 weekend project once you hit real integration friction, and the video is selling a course/community, so it has an incentive to make it sound like a weekend.

The bigger flag: "give it access to everything" on day one is the wrong move regardless of timeline. An unattended agent with broad tool access (email, calendar, files) run by a fresh harness install is exactly the failure mode the harness articles warn about — errors compound when nobody's watching. Start with one connected tool, watch it operate for a few days, then expand scope. Given you're mid-exit from EOXS and starting AskCruz next week, I'd also flag this is a side project competing for weekend hours right before a real transition — worth being honest with yourself about whether this is exploration you want, or a distraction from ramping into AskCruz.
