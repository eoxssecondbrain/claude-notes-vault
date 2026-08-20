---
thread_name: "askcruz-setup-drawbacks"
user: "nizamuddin"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

USER: Worth flagging: two separate open tasks both titled "Quantity Changes When Length Is Edited" (ids 6564 and 7606) at different stages — same bug reopened, or a duplicate task. Might be worth checking which is stale.

this is done for one customer and now need to do other customer with has different codebase and different codebase

CLAUDE: [Queried eoxs-teams: project_task joined to res_partner for ids 6564 and 7606, confirming partner_id/customer_name and description]

Final response delivered to user:

Confirmed — pulled the two tasks directly: 6564 is PPC Speciality Metals (stage: Can be released, meaning that fix is done and ready to ship), 7606 is Velox (stage: Assigned, not started). Same bug description verbatim, different partner_id, so it's exactly what you said — same fix needed on a separate customer codebase, not a stale duplicate. Not a QA gap, just the next instance of the same rollout.

[Wrote to memory /areas/eoxs-development.md: "[stated] Each EOXS customer runs on a separate codebase/instance. A bug fix built for one customer (e.g. PPC Speciality Metals) has to be separately re-implemented for other customers (e.g. Velox) even though it's the same underlying bug — this shows up as duplicate-looking task titles on the project_task board with different partner_id/stage, not as stale/duplicate tickets." — filed because the user stated this as a durable fact about how their EOXS dev work is structured.]
