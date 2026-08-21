---
thread_name: "mcp-server-icon-howto"
user: "Harsimran"
type: claude-chat
created: 2026-08-21
updated: 2026-08-21
---

**User:** how to add photo , icon image on mcp server, custom mcp server

**Assistant:** This doesn't match the threads-ov or eoxs-data-general skills (it's a general MCP dev question), so answered directly.

There are two separate places an "icon" can go:

1. Protocol-level icon (shows up in MCP clients like Claude Desktop's tool picker) — recent MCP spec added an `icons` field set when building the server. FastMCP (Python) example:
```python
from fastmcp import FastMCP
from mcp.types import Icon

mcp = FastMCP(
    name="MyServer",
    icons=[Icon(src="https://example.com/icon-48.png", mimeType="image/png", sizes=["48x48"])]
)
```
Can embed as base64 data: URI instead of hosting. Individual tools/resources/prompts can take their own icons too.

2. Desktop Extension (.mcpb) icon — for a one-click-install local server packaged for Claude Desktop. In manifest.json:
```json
"icon": "icon.png"
```
pointing to a PNG bundled at the root of the .mcpb package (or an https:// URL). Newer manifests support an icons array for light/dark and multiple sizes.

If listing on a directory (Smithery, Glama, an org's plugin marketplace), icon usually comes from that platform's own listing metadata/plugin.json, not the server code.

Sources: FastMCP icons docs, MCPB Manifest.json Spec, MCP GitHub discussion #2573, fastmcp discussion #2112.
