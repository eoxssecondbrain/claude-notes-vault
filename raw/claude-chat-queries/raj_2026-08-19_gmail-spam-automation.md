---
thread_name: "gmail-spam-automation"
user: "raj"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

USER: Make me an automation that filters out any spam or promotional emails arriving in my inbox. Label it as trash or spam but do not delete any of them.

ASSISTANT: [Checked threads-ov and raj-eoxs-vault skills per mandatory pre-thread rule. Flagged that this task doesn't clearly match raj-eoxs-vault or sales-strategist.]

[Asked AskUserQuestion: (1) Detection method - Native Gmail filter rules (Recommended) vs Scheduled Claude scan. User picked: Native Gmail filter rules (Recommended). (2) Label to apply - Gmail's built-in Spam label vs custom label. User picked: Use Gmail's built-in Spam label. (3) Scope - New mail only (Recommended) vs New mail + one-time sweep. User picked: New mail only (Recommended).]

[Investigated available Gmail MCP tools via ToolSearch. Found no filter-creation tool exists - only per-message/thread action tools (label, mark spam, trash, etc.), no way to create a native Gmail filter rule.]

Told user: Found a constraint: there's no Gmail filter-creation tool available here — only per-message/thread actions. A true native Gmail filter that runs instantly on Gmail's own servers can't be built through this connector. The only buildable path is the second option you didn't pick: a scheduled Claude scan.

[Asked AskUserQuestion: (1) Confirm proceeding with scheduled scan since native filters aren't available - user answered "no check now, i allowed some tools" (2) Cadence - user picked Every hour (Recommended).]

[User's answer suggested they enabled additional tools/scopes. Ran RefreshMcpTools on Gmail server and re-searched ToolSearch for filter/settings tools. Result: still 22 tools, no filter creation or listing tool added.]

Told user: Checked again after refresh — still 22 Gmail tools, no filter-creation or filter-listing tool present. Whatever you enabled didn't add filter capability; this MCP genuinely doesn't expose Gmail's filter/rules API, only actions on individual messages/threads (label, mark spam, trash, etc.). The only way to build this with what's available is the scheduled scan: a recurring task that reads new inbox mail, classifies it, and marks matches as Spam. Native instant filtering isn't possible here.

[Asked AskUserQuestion: Confirm building scheduled scan hourly. User answered: Yes, build it hourly (Recommended).]

[Searched ToolSearch extensively for Gmail read/search tools (search_threads, get_thread, list_labels, list_messages) needed to discover and read inbox emails before classifying them. None of these tools actually exist in the available toolset, despite being referenced inside other Gmail tool descriptions (e.g. "To find the message ID, use tools like search_threads or get_thread"). Confirmed the full Gmail toolset is exactly 22 tools, all of which are write/action tools requiring a pre-known messageId or threadId (create_draft, create_label, delete_label, forward, label_message, label_thread, mark_message_spam, mark_thread_spam, reply, send_message, trash_message, trash_thread, unlabel_message, unlabel_thread, unmark_message_spam, unmark_thread_spam, untrash_message, untrash_thread, update_draft, update_label, apply_sensitive_message_label, apply_sensitive_thread_label). No search/list/read tool exists to discover which emails are new or read their content.]

Told user: Confirmed and this changes the answer: this Gmail connector has 22 tools total, and none of them can search, list, or read your inbox. Every tool (label_message, mark_message_spam, trash_message, reply, etc.) requires a message ID or thread ID as input — but there's no search_threads, list_messages, get_thread, or list_labels tool actually present to obtain those IDs in the first place. The tool descriptions reference search_threads/get_thread/list_labels as if they exist, but they're not in the toolset I have access to.

Practical effect: I cannot build any working automation right now — scheduled or otherwise — because there's no way to discover which emails are new or read their content to classify them. Every action tool is blind without an ID, and I have no way to get IDs.

Two ways forward:
1. You (or whoever manages the Gmail connector) enables the read/search tools (search_threads, get_thread, list_labels at minimum) on this connector. Once those exist, the hourly scheduled scan is straightforward to build with what's already here.
2. I flag this as a dead end for now and you handle spam filtering through Gmail's own native settings directly, outside Claude.

Let me know which, or check whether those read scopes can be added to the connector.

[Checked list_triggers - found one unrelated existing scheduled task (Weekly AskCruz Board Scrum Report), confirming the scheduling mechanism itself works fine; the blocker is purely the missing Gmail read/search tools, not the scheduling infrastructure.]
