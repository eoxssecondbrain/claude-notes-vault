---
thread_name: "vscode-remote-ssh-connection-error"
user: "nidhi"
type: claude-chat
created: 2026-08-26
updated: 2026-08-26
---

User: [uploaded screenshot, same error] i'm still stuck, uninstalled and reinstalled remote ssh extension

Assistant: Reinstalling the same extension version wouldn't fix a version-mismatch issue anyway — you'd just get the same build back. This specific error (extension declares proposals A,B,C but not the one VS Code core demands) is the classic signature of a non-Microsoft VS Code build — VS Code OSS or VSCodium — rather than a broken extension.

Official Microsoft VS Code ships a product.json that allowlists certain extensions (including Remote-SSH) to use proposed/experimental APIs. OSS/VSCodium builds don't include that allowlist, so any extension trying to use a proposed API throws exactly this error, even freshly installed.

[step_card_display_v0 with steps:]
1. Check which VS Code build you're running — Help > About. Look at the top line. Official Microsoft builds say "Version: 1.9x.x (user setup)" or similar. If it says "Code - OSS" or the About dialog mentions VSCodium, that's the root cause — those builds don't allowlist Remote-SSH for proposed APIs.
2. If it's OSS/VSCodium, switch to official VS Code — Download from code.visualstudio.com and install the official Microsoft build. This is the actual fix in most cases matching this exact error — no combination of extension reinstalls or updates fixes it on a non-Microsoft build, because the allowlist lives in VS Code's own product.json, not in the extension.
3. If it IS official VS Code, check the version is current — Help > Check for Updates. If you're on an old official build, update to latest stable — occasionally the required proposal was added to the extension before VS Code core caught up, or vice versa.
4. As a workaround only, launch with the proposed-API flag — Close VS Code, then launch from a terminal with: code --enable-proposed-api ms-vscode-remote.remote-ssh . This forces it through, but it's a workaround, not a fix — expect it to break again on the next extension update. Only use this if switching build isn't an option right now.

Check Help > About first — if it says "Code - OSS" instead of the official Microsoft branding, that's almost certainly it.
