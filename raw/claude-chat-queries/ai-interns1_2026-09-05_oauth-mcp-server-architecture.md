---
thread_name: "oauth-mcp-server-architecture"
user: "ai_interns1"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

## OAuth + MCP Server Architecture Discussion

### User Query
What are the best possible ways to add oauth in the mcp servers whose links can be shared to some other people

### Clarification Questions & Answers

**Q1: Scope** — Are you looking to share MCP server links with external people (customers, partners, integrators) or internal team members?
A: Both — external people (customers, partners, integrators) AND internal team members.

**Q2: Access model** — What are you trying to gate?
A: Each person gets personalized access to specific data/tier within one MCP server.

**Q3: Current state** — What's blocking OAuth implementation?
A: Adding OAuth to MCP servers that currently don't have it.

**Q4: Bearer/auth model** — Do you want these shared links to be:
A: One-time auth that creates a long-lived token for that person.

### Recommendation & Patterns

Four viable patterns presented:

#### Pattern 1: OAuth Provider → Custom Token (Recommended)
- User gets unique shareable link: `yourapp.com/mcp/auth?server=wiki-tier2&client_id=X`
- Redirects to OAuth provider (custom or Google/GitHub)
- Server issues long-lived Bearer token (48+ months) tied to user + tier combo
- User adds token to Claude MCP config: `Authorization: Bearer <token>`
- MCP server validates token on every request, enforces tier permissions

Pros: One-time friction, tier boundaries enforced server-side, revocable, works for internal + external
Cons: Requires building/hosting OAuth server, token management infrastructure

#### Pattern 2: Signed URL + SSO Integration (Enterprise)
- Generate signed, time-limited URL: `yourapp.com/mcp?sig=...&user=alice&tier=tier2&exp=2027-01-01`
- MCP server validates HMAC signature + expiration on first request
- Server generates + caches long-lived token
- Subsequent requests use cached token

Pros: No OAuth provider needed upfront, simple HMAC-based
Cons: Token is global for user once created, harder to revoke individually

#### Pattern 3: Claude Native (Easiest short-term)
- User enables connector with standard OAuth (Google, GitHub, or custom) in Claude.ai
- Claude handles all auth UI + token refresh automatically
- Tier enforcement in MCP tool responses

Pros: No manual token copying, Claude handles lifecycle
Cons: Claude.ai users only, tier boundaries enforced in responses (weaker), revocation requires user disconnect

#### Pattern 4: Hybrid (Recommended Overall)
- Internal EOXS team → Claude's built-in MCP OAuth (Pattern 3)
- Customers/partners → Custom OAuth provider with Bearer tokens (Pattern 1)

### Recommendation for Your Case
Start with Pattern 1 (OAuth → Bearer token):
1. You're building auth anyway since servers lack it now
2. One-time, long-lived tokens fit shareable links perfectly
3. Server-side token validation enforces tier boundaries without Claude involvement
4. Works for both internal (manual token in claude.ai) and external (via shared link)
5. Token granularity = 10 different customers with 10 different tier2 tokens, each seeing only scoped data

Blocker: You need an OAuth provider infrastructure + token storage.

### Pending
- What does current MCP server auth look like? Reverse proxy or direct server-side auth?
