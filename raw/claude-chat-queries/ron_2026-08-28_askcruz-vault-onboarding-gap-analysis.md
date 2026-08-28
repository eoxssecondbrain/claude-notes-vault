---
thread_name: "askcruz-vault-onboarding-gap-analysis"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: What do you know about AskCruz and its implementation? You can review the Teams AskCruz board. We have two customers to onboard: 3GM (new) and EOXS (existing). Please examine all tasks and extract any relevant information, as well as the OB board.
My goal is to ensure you understand what is relevant and what is not. The key points I'm looking for are:
- It's not just about onboarding the customers; the data entering the vault must be properly structured and accurate. All information we store about the ERP and the system must be correct.
- The ultimate goal is to provide the customer with real‑time, clean, accurate data for every prompt they give our product. If the AI is uncertain, it should respond with "flat."
Let's discuss this before accessing the vault. We have observed occasional incorrect data outputs, and I want to identify the possible causes. First, review the current onboarding process and identify any gaps. After pinpointing the gaps, we can address them and streamline the implementation.
Specifically, I need to understand:
- The current implementation process
- The tools being used
- How information is extracted and placed into the vault
- The structure being followed
All of this is new information for me as Ron. I also need to see how we have structured the ERP data and how the system processes it. I know this is a lot to take in, but you do not need to start any work right now. First, let's brainstorm to ensure we are on the same page before moving forward.

Assistant: [Loaded threads-ov and raj-eoxs-vault skills silently, then asked three clarifying questions via AskUserQuestion before touching the vault]

Question 1: "When you say the AI should respond 'flat' if uncertain — what does 'flat' mean here?"
User answer: "I'm using a speech-to-text functionality, so it got flat. I want to say it should respond with that. Instead of it giving wrong information"

Question 2: "Is the 'OB board' the same thing as the Teams AskCruz board (the askcruz Odoo project), or a separate board?"
User answer: "There is the AskCruz board that you are talking about, and then OV Vault is where all the information is stored about AskCruz and also for EOXS. By AskCruz, sorry, I did not mean OV Board. I meant AskCruz's board. There you will find all the tasks that have been created for implementation and to document the process. There is an architecture task that is also created, which has some files and log notes also, which might help."

Question 3: "For 'examine all tasks' — how wide should the first pass go?"
User answer: "Full board"

Assistant: [Asked one more clarifying question per stated rigor-level preference]

Question: "What rigor level for this AskCruz onboarding/vault gap analysis (full board review, architecture task, OV Vault structure)?"
User answer: "50" (50ft — Deep)

Assistant: [Queried the teams-askcruz connector (Odoo project/task tables, task chatter/mail_message for tasks 314 and 272) and the OV Vault/OV2 connector (get_index, search_wiki, search_assets, get_asset on askcruz-self-knowledge) to build the gap analysis, then replied with the following]

Correcting one framing thing first, since it changes how to read everything else: EOXS is not really an "existing AskCruz customer" the way 3GM is. The self-knowledge doc (v1.2, 25 Aug) is explicit that AskCruz currently has exactly one real client, 3GM, mid-implementation. "Customer 1 - EOXS" on the board is EOXS running AskCruz on itself as an internal pilot, not an external deployment with its own tenant boundaries. That matters for your ARR goal: EOXS being 87 tasks deep and mostly Complete tells you the internal build works well enough for EOXS staff daily use. It does not tell you AskCruz is sellable, because 3GM, the only real test of "does this work on someone else's ERP and data," is still mostly sitting in Intake (16 of 21 tasks).

Architecture, as documented (askcruz-self-knowledge asset on the OV Vault, updated 25 Aug):

Source systems (3 Gmail accounts, one shared Zoho support inbox, Fireflies, Fathom, client Odoo instances) feed ingestion (event-driven / scheduled sweeps / fetchers), which goes through filtering plus sensitivity classification (General / Company-Confidential / Raj-Personal, mapping to tier2 / tier2_confidential / tier1, defaulting to the more restrictive tier when unsure) into a central knowledge store, then knowledge generation — raw source becomes a synthesized page with citations, gets a citation check, then human approval, on a documented 6-hour synthesis cycle — before it's retrievable at all.

On your "flat" point specifically: the policy already exists. Section 15 of that same doc instructs AskCruz to say things like "I don't have enough verified information to answer that confidently" whenever information is missing, sources conflict, the question is ambiguous, access is restricted, or evidence is stale, instead of guessing. So what you're asking for is already written down as intended behavior. What I can't confirm from the board or the vault is whether it's actually enforced at answer time or just aspirational documentation — that's a testable question, not a design gap, and I flagged it below as something worth verifying directly.

Here's what the board and vault actually show, gap by gap:

Gap: Raw-to-wiki promotion can silently stall, with nothing watching it. Evidence: Task 314, Architecture File Ingestion: content was written to the vault's raw table on 25 Aug; by 26 Aug the team flagged that the account running ingestion had been suspended and promotion likely never fired. As of today it's only just reached QA. I verified this live — search_wiki for that content returns nothing, while get_asset returns it fine. Four days past the documented 6-hour cycle, unpromoted. Why it matters: This is a currently-live cause of wrong or missing answers: content can be real and sitting in the vault, but invisible to whatever actually answers questions, with no automated signal that it happened.

Gap: Infra fragility, same blind spot. Evidence: Task 272, Threads OV discrepancy: threads stopped saving and users hit error logs; root cause was a detached git HEAD on the Render deployment. Found only because users complained, fixed manually. Why it matters: Same failure class as above — a deployment break drops data silently until a human notices.

Gap: Client implementation data intake is a manual handoff, not a process. Evidence: Task 84, "Put the implementation data in a structured manner": Raj asked Ron to collect it and pass it to Ayan to enter into the vault. Still in Assigned, not done. Why it matters: The step that turns a client's raw implementation history into vault-ready structured data depends on Ron personally collecting and forwarding it — no defined process behind it.

Gap: Access-rights model is incomplete. Evidence: Task 208: no formal tracking system for who has access to which live client instances or AI tools, open since at least 18 Aug ("will look into this when I have bandwidth"). Task 216: Threads OV's own department-level access tiering is still Need discussion. Why it matters: The architecture treats access control as one of two core security layers protecting sensitive data. Parts of it are still undefined.

Gap: 3GM is pre-build, not mid-build. Evidence: 16 of 3GM's 21 tasks are in Intake; its SOP Ingestion task is on Hold; the 3GM-EOXS integration and MCP skill-file tasks have no scope written yet. Why it matters: There's effectively no client-specific structured data for 3GM in the vault right now. Any AskCruz answer for 3GM today is answering from almost nothing — exactly where the "say I don't know" behavior needs to be verified, not assumed.

Gap: No incident log for wrong answers. Evidence: I found no board task or vault page recording a specific "AskCruz answered incorrectly" incident. Why it matters: Without a place these get logged, each bad answer gets diagnosed from scratch instead of building a pattern across the causes above.

Gap: The vault has already stored something wrong about itself once. Evidence: Version history on the self-knowledge doc: v1.2 (25 Aug) had to correct v1.1, which wrongly implied AskCruz was deployed across EOXS's whole client roster (Greer, Eastern States, Discount Pipe & Steel, PPC, Sabre, RW Conklin, Brannon) when only 3GM actually has it configured. Why it matters: Concrete precedent that wrong information can sit in the vault until a person happens to catch it — no check caught it automatically.

Given that picture, the highest-leverage first move probably isn't onboarding either customer yet — it's making the raw-to-wiki promotion step observable (so a stall like the architecture-file one gets caught automatically instead of by luck) and turning the client-data intake handoff into an actual defined process, since both of those feed every future customer, not just these two.

One thing I'd want to do next, if you want it: run a few live test queries against AskCruz where the honest answer is "I don't know" and see whether it actually says that or guesses — that tells us if Section 15 is enforced or just documented. Do you want me to do that next, or go deeper on one of the gaps above first?

Sources: teams-askcruz board — tasks 314, 272, 84, 208, 216, and the project/task-type breakdown for projects 4 (Customer 1 - EOXS), 6 (AskCruz), 14 (Customer 2 - 3GM); e.g. https://teams.askcruz.com/web#model=project.task&id=314. OV Vault (OV2) — asset "AskCruz — Self-Knowledge, Product Definition & System Architecture" (askcruz-self-knowledge, tier2, updated 2026-08-25).
