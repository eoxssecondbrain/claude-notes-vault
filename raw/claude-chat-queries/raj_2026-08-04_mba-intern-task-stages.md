---
thread_name: "mba-intern-task-stages"
user: "raj"
type: claude-chat
created: 2026-08-04
updated: 2026-08-04
---

# MBA Intern Task Stages

## Human

I'm structuring a big task list for these 50 MBA interns who are coming on board. I wanted to have detailed stages. By detailed, I mean that we need to make sure that we think through every possibility on a stage, and we make 8 to 12 stages. What could those stages be?

1. Task list: everyone joins, and they are able to see all the tasks they have to do. From there, how do we go through all the detailed stages? I don't mind if we have three layers of QA stages by three different people, and every task will have an incentive. The task is considered complete when they are paid.
2. Waiting for approval: this could be the second-to-last stage, which means that the task has been completed and someone needs to approve the payment to the intern as an incentive for that specific task.

## Assistant

Skill routing note: this query matches neither raj-eoxs-vault (not a vault-data lookup) nor sales-strategist (not sales/GTM). It's internal ops design, so I'm answering from context rather than querying a source. Flagging that per your instruction.

Before I build the stage architecture, five things I need:

1. Where does this actually live? EOXS ERP task manager Kanban columns, or a separate tracker? Stage count is constrained by what the project module can enforce (auto-transitions, approval gates, assignee routing).

2. Is the stage list the lifecycle of a task, or the journey of an intern? Your two examples are task-lifecycle stages. Confirming that's what you want, not an onboarding→graduation arc.

3. Who are the three QA people? Named roles, not placeholders. This determines whether 3 layers is real or theatre.

4. Incentive mechanics: per-task bounty on top of the ₹10,000/month stipend, or is the stipend itself the pool? And who holds the payment-approval authority — you, finance, or the function lead?

5. Expected volume: roughly how many tasks per intern per week? 50 interns × N tasks × 3 QA passes is the number that decides whether this design survives week two.

One thing I'd push back on now rather than after building it: three human QA layers on every task is the single highest-risk element in this design. At even 3 tasks/intern/week that's 150 tasks and 450 review actions weekly. If any reviewer is part-time, the whole board jams at QA and interns stop getting paid — which kills the incentive mechanic you're building the system around. There are ways to keep three layers without that outcome (risk-tiered routing, sampling, peer-QA as layer one), but I want your answers before I pick one.

Rigor level for the build:

5ft — a clean 8–12 stage list with names, entry/exit criteria, and owner per stage. Fast, usable this week.

10ft — same, plus throughput math against your actual intern/task volume, QA capacity check, and the incentive-payout rules written out per stage.

50ft — all of the above, plus failure-mode design (what happens on rejection, rework loops, disputes, fraud/gaming vectors), the ERP field/automation spec to implement it, and the reporting layer that feeds your end-of-program permanent-hire analysis.

Tell me the level and answer the five, and I'll build it.
