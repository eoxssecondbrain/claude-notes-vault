---
thread_name: "nijam-weekly-tasks"
user: "nizamuddin"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

**User:** hi what are the things i need to work on this week

**Claude:** Before I give you a list — none of the 23 tasks currently in "Assigned" stage show an owner named "nijam" (owners shown: Humaira Zainab, Hashir Saleem, Tapish Sharma, Dhrup, Sourav Sahoo, Akash Deep, Aryan, Rahul Bains, Siddhant, Arpan, Ajith Kumar, Nandish, Jesus R., Ernie, Dev team, or unassigned).

Two possibilities: either you go by a different name in the Odoo `owner` field, or the "Assigned" stage on this board isn't scoped to you individually (i.e. it's the whole Build team's queue and you'd normally scan it manually for your name/client).

[Asked via AskUserQuestion: "Which owner name should I filter on to pull your actual task list from the Assigned stage?" Options: "Show me all 23, unfiltered" / "I go by a different name"]

**User (answer):** name is nijamuddin

**Claude:** You have 4 tasks in "Assigned" stage right now, all under the Build Team project (user_id 353, G. Nijamuddin, confirmed via EOXS Team Live):

| Task | Client | Priority | Opened |
|---|---|---|---|
| Investigate and Fix Unexpected Quantity Change on Delivery | Discount Pipe & Steel | P2 | Aug 3 (3 weeks ago) |
| Quantity Changes When Length Is Edited | Velox | P4 | Aug 11 (2 weeks ago) |
| Improve Inventory Loading Performance | Velox | P4 | Jul 23 (1 month ago) |
| Inventory Adjustment Cost Fix | Sabre Alloys | P5 | Apr 23 (4 months ago) |

None have a deadline set in the system.

Order I'd work them: the Discount Pipe & Steel P2 first — it's the only elevated-priority item. Then the two Velox P4s. The Sabre Alloys P5 has been sitting for 4 months at the lowest priority level — worth checking whether it's still actually needed before you sink time into it, rather than letting it linger as background guilt.

Source: EOXS Team Live (`project_task`), live query.
