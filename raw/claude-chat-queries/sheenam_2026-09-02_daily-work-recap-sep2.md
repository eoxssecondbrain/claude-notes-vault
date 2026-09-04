---
thread_name: "daily-work-recap-sep2"
user: "sheenam"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

User: This is concerning. why aren't these 2 chat threads saved in the vault

Assistant: Fair to flag. A few real reasons this happens, not just one:

1. It's best-effort, not enforced. The auto-save rule tells me to call a save function at the end of every turn — but nothing outside that instruction checks whether I actually did it. If the Claude instance running those two chats skipped the call, nothing catches it.

2. Those chats might not have had the vault connector active. If Thread_OV wasn't connected in that specific conversation or project context, there was no tool to call at all.

3. Timing. If those chats happened before this save-rule was set up in your preferences, they'd never have been saved in the first place.

4. Project-level settings can differ. The "Hiring" project shown in your screenshot may be configured differently (different connectors enabled) than the session you're in right now.

I can't diagnose which of these it actually was — that requires looking inside those two claude.ai sessions directly, which I don't have access to from here.

What I can do: if you paste the content of those two chats here, I'll save them into the vault right now, and going forward I'd flag it if I ever fail to call the save function myself.
