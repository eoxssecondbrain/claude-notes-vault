---
thread_name: "askcruz-setup-drawbacks"
user: "nizamuddin"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

USER: give me total task i worked on

CLAUDE: [Called AskUserQuestion to clarify which task source] Which tasks do you want listed? Options: My EOXS/AskCruz project board tasks / This conversation's task list / Something else.

USER (via AskUserQuestion): you know i am developer? i am asking about related to development

CLAUDE: [Checked memory (empty), searched EOXS_data_general search_implementation_tasks for "Nijam" (no results), queried eoxs-teams via Team_EOXS connector: describe_table project_task, describe_table res_users, then queried res_users/res_partner to find user_id=353 (login nijam.eoxs@gmail.com, partner_name "G. Nijamuddin"), then queried project_task joined to project_task_type and project_project for all tasks where user_id=353, then a count query grouping by active status confirming 29 total, all active.]

Final response delivered to user:

Pulled directly from EOXS Team Live (eoxs-teams, current by definition) — project_task rows assigned to your user account (nijam.eoxs@gmail.com / G. Nijamuddin, user_id 353). 29 total tasks, all active, no archived ones.

By project: Build Team 22, EOXS Support 6, Daily Snippet 1.

Completed/paid (5): BOL Showing Incorrect Value in Weight Column, FR0444, INV/2026/0954 (Verbal - Joe), Add Vendor Delivery field, Add Pivot Table Functionality to Invoices and Bills in Accounting Module.

Still in the pipeline (24), grouped by stage:

| Task | Project | Stage |
|---|---|---|
| Nijam's Snippet | Daily Snippet | Jr. Dev |
| Re:Quote -02416 - J & I Manufacturing | EOXS Support | Need Developer |
| Quantity Changes When Length Is Edited | Build Team | Assigned |
| Investigate and Fix Unexpected Quantity Change on Delivery | Build Team | Assigned |
| Improve Inventory Loading Performance | Build Team | Assigned |
| Inventory Adjustment Cost Fix | Build Team | Assigned |
| Incorrect Delivered Quantity. | Build Team | Code QA/AI Review |
| Re: 51555 | EOXS Support | QA |
| Update Packing List PDF | Build Team | QA Failed |
| Fix Report Filters Not Persisting | Build Team | On Sandbox/Functional QA |
| Fix Google Maps Customer Selection Error | Build Team | Ready for Sandbox |
| IRIS AI Module | Build Team | Ready for Sandbox |
| Add "Days Past Due" Column to Invoice List View | Build Team | Communicated |
| Add New Cutting Method: "Toll Processing" | Build Team | Communicated |
| Fix Profit & Loss Balance Sign | Build Team | Communicated |
| Add Vendor Delivery Address Field on Purchase Order Header | Build Team | Communicated |
| Implement OTP-Based Login Verification | Build Team | QA Passed |
| Add Sales Order Column in Processing Lines | Build Team | QA Passed |
| Enable Transaction Search by Dollar Amount or Vendor | Build Team | QA Passed |
| Quantity Changes When Length Is Edited (dup task) | Build Team | Can be released |
| Fix Processing Line Reset | Build Team | Can be released |
| Invoice Due Date Not Updating After Changing Payment Terms | Build Team | Can be released |
| Fix General Ledger Print Failure | Build Team | Revert code/Update Gitlab |
| Install Google Authenticator Login Security | Build Team | Revert code/Update Gitlab |

Worth flagging: two separate open tasks both titled "Quantity Changes When Length Is Edited" (ids 6564 and 7606) at different stages — same bug reopened, or a duplicate task. Might be worth checking which is stale.

Source: eoxs-teams, project_task joined to res_users/res_partner, live query.

[Also wrote to memory /profile.md: "[stated] Developer at EOXS, working on the Build Team / EOXS Support project boards (Odoo, EOXS Team Live)." — filed because the user stated their occupation/role directly during this exchange.]
