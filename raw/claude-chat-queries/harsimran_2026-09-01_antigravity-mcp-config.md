---
thread_name: "antigravity-mcp-config"
user: "Harsimran"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: give me mcp configuration for eoxs data general, teams eoxs live, threads ov all three mcp
i have to paste this in mcp config json file in antigravity

Assistant: Here's the MCP config for all three, in Antigravity's format. Antigravity uses `serverUrl` (not `url`) for remote servers — add these entries inside the existing `mcpServers` object in your `mcp_config.json` (located at `~/.gemini/config/mcp_config.json` globally, or `.agents/mcp_config.json` for a workspace-level setup):

```json
{
  "mcpServers": {
    "eoxs-data-general": {
      "serverUrl": "https://5.223.44.95/mcp/D5RBEh1UUZy8iVw638lFATs7MlDbvKzjxBCoOt_C5-o/sse"
    },
    "team-eoxs-live": {
      "serverUrl": "https://mcpeoxsteamlive.lancerdevops.me/mcp"
    },
    "thread-ov": {
      "serverUrl": "https://claude-notes-vault.onrender.com/mA8sjodhBW8vq7jcpMaxIEqE0iaTrvx6zACgcBs2Hzk/sse"
    }
  }
}
```

Notes:
- If your `mcp_config.json` already has other servers under `mcpServers`, merge these three keys in rather than replacing the file.
- No `headers` block needed — the auth token for each is already embedded in the URL path.
- After saving, restart Antigravity (or use the MCP panel's reload) and check the three show as connected in Manage MCP Servers.
- These URLs are your live connector credentials — treat this file the same as an API key, don't commit it to a shared repo.
