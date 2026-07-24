"""
Claude Notes Vault MCP Server
Standalone scratchpad service — save_chat_transcript + save_analysis (plus read-back tools).
Isolated from OV2 (raj-wiki-vault): separate repo, separate branch, separate Render service.
Run: python mcp_server.py
"""

import os
import re
import subprocess
from datetime import date, datetime, timezone
from pathlib import Path

from mcp.server.fastmcp import FastMCP

VAULT_ROOT = Path(__file__).parent
WIKI_DIR = VAULT_ROOT / "wiki"
RAW_DIR = VAULT_ROOT / "raw"
CHAT_DIR = RAW_DIR / "claude-chat-queries"
ANALYSES_DIR = WIKI_DIR / "analyses"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO_URL = os.environ.get(
    "GITHUB_REPO_URL", "https://github.com/eoxssecondbrain/claude-notes-vault.git"
)
GIT_BRANCH = os.environ.get("GIT_BRANCH", "data")

# No login — the URL path itself is the credential. Refuse to start on a
# guessable path, same convention as OV2's mcp_server.py.
MCP_URL_SECRET = os.environ.get("MCP_URL_SECRET")
if not MCP_URL_SECRET:
    raise RuntimeError(
        "MCP_URL_SECRET environment variable is not set. Refusing to start an "
        "unauthenticated server. Set MCP_URL_SECRET to a long random value "
        "(e.g. `python -c \"import secrets; print(secrets.token_urlsafe(32))\"`) "
        "in the environment."
    )

PORT = int(os.environ.get("PORT", "8000"))

mcp = FastMCP(
    "Claude Notes Vault",
    host="0.0.0.0",
    port=PORT,
    auth=None,
    sse_path=f"/{MCP_URL_SECRET}/sse",
    message_path=f"/{MCP_URL_SECRET}/messages/",
)


@mcp.custom_route("/", methods=["GET"])
async def health(request):
    from starlette.responses import PlainTextResponse
    return PlainTextResponse("ok")


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading {path}: {e}"


def _all_md(directory: Path) -> list[Path]:
    return sorted(directory.rglob("*.md")) if directory.exists() else []


def _search(directory: Path, query: str, max_results: int = 12) -> str:
    q = query.lower()
    results = []
    for path in _all_md(directory):
        content = _read(path)
        lines = content.splitlines()
        matches = []
        for i, line in enumerate(lines):
            if q in line.lower():
                start = max(0, i - 1)
                end = min(len(lines), i + 3)
                matches.append("\n".join(lines[start:end]))
        if matches:
            rel = path.relative_to(VAULT_ROOT)
            results.append(f"### {rel}\n" + "\n---\n".join(matches[:3]))
    if not results:
        return f"No results for '{query}'."
    return f"Results for '{query}':\n\n" + "\n\n".join(results[:max_results])


# ── Git (shared by both save tools) ─────────────────────────────────────────

def _git(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(VAULT_ROOT)] + args, capture_output=True, text=True)


def _git_commit_and_push(rel_path: Path, commit_message: str) -> str:
    """Commit rel_path and push to GIT_BRANCH. Each write is a single small file,
    so a self-triggered redeploy on push is fine — same tradeoff OV2 accepted."""
    if not GITHUB_TOKEN:
        return "WARNING: GITHUB_TOKEN not set on this server — file was saved locally but NOT pushed to GitHub."

    token_url = GITHUB_REPO_URL.replace("https://", f"https://{GITHUB_TOKEN}@")
    _git(["remote", "remove", "origin"])
    _git(["remote", "add", "origin", token_url])
    _git(["config", "user.email", "notes-mcp-server@eoxs.com"])
    _git(["config", "user.name", "Claude Notes MCP Server"])

    _git(["add", str(rel_path)])
    commit = _git(["commit", "-m", commit_message])
    if "nothing to commit" in (commit.stdout + commit.stderr):
        return "Nothing to commit (file unchanged)."
    if commit.returncode != 0:
        return f"git commit failed: {commit.stderr.strip()}"

    push = _git(["push", "origin", f"HEAD:{GIT_BRANCH}"])
    if push.returncode != 0:
        return f"git commit succeeded locally but push failed: {push.stderr.strip()}"
    return f"Committed and pushed to origin/{GIT_BRANCH}."


# ── Save Chat Transcript ─────────────────────────────────────────────────────

@mcp.tool()
def save_chat_transcript(title: str, content: str) -> str:
    """
    Save a Claude chat conversation transcript into this notes vault and push it to GitHub.
    Writes to raw/claude-chat-queries/YYYY-MM-DD-<slug>.md, then commits and pushes.

    title: short title for the conversation (used to build the filename)
    content: full markdown transcript of the conversation
    """
    today = date.today().isoformat()
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "conversation"
    filename = f"{today}-{slug}.md"
    out = CHAT_DIR / filename

    n = 2
    while out.exists():
        out = CHAT_DIR / f"{today}-{slug}-{n}.md"
        n += 1

    CHAT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    frontmatter = (
        f"---\ntitle: \"{title}\"\ntype: claude-chat\ncreated: {today}\nupdated: {today}\n---\n\n"
    )
    out.write_text(frontmatter + content.strip() + "\n", encoding="utf-8")

    rel_path = out.relative_to(VAULT_ROOT)
    push_result = _git_commit_and_push(
        rel_path, f"chat: save transcript {rel_path.name} ({timestamp})"
    )
    return f"Saved: {rel_path}\n{push_result}"


@mcp.tool()
def search_claude_chat_queries(query: str) -> str:
    """Search saved Claude chat transcripts (raw/claude-chat-queries/) — by topic, keyword, or title."""
    if not CHAT_DIR.exists():
        return "No saved chat transcripts yet."
    return _search(CHAT_DIR, query)


@mcp.tool()
def list_claude_chat_queries() -> str:
    """List all saved Claude chat transcripts, newest first."""
    if not CHAT_DIR.exists():
        return "No saved chat transcripts yet."
    files = sorted(CHAT_DIR.rglob("*.md"), reverse=True)
    if not files:
        return "No saved chat transcripts yet."
    lines = []
    for f in files[:150]:
        rel = str(f.relative_to(VAULT_ROOT))
        try:
            title = f.read_text(encoding="utf-8").split("\n")[0].lstrip("# ").strip()
        except Exception:
            title = f.stem
        lines.append(f"- [{title}]({rel})")
    note = f"\n\n(showing 150 of {len(files)})" if len(files) > 150 else ""
    return "Saved chat transcripts:\n\n" + "\n".join(lines) + note


@mcp.tool()
def get_claude_chat_query(file_path: str) -> str:
    """Return the full content of a saved Claude chat transcript.
    file_path: relative path from vault root, e.g. 'raw/claude-chat-queries/2026-07-24-testing-01.md'
    Get the path from search_claude_chat_queries or list_claude_chat_queries first — don't guess it."""
    p = VAULT_ROOT / file_path
    return _read(p) if p.exists() else f"File not found: {file_path}"


# ── Save Analysis ────────────────────────────────────────────────────────────

@mcp.tool()
def save_analysis(title: str, content: str) -> str:
    """
    Save a synthesized insight as a permanent analysis page and push it to GitHub.
    title: short title (e.g. 'Sabre Alloys Churn Risk Assessment')
    content: full markdown — include ## Question, ## Findings, ## Sources sections
    """
    today = date.today().isoformat()
    safe_title = re.sub(r'[<>:"/\\|?*]', "", title).strip()
    filename = f"{today} {safe_title}.md"
    out = ANALYSES_DIR / filename

    n = 2
    while out.exists():
        out = ANALYSES_DIR / f"{today} {safe_title} ({n}).md"
        n += 1

    out.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    frontmatter = f"---\ntitle: \"{safe_title}\"\ntype: analysis\ncreated: {today}\nupdated: {today}\n---\n\n"
    out.write_text(frontmatter + content.strip() + "\n", encoding="utf-8")

    rel_path = out.relative_to(VAULT_ROOT)
    push_result = _git_commit_and_push(
        rel_path, f"analysis: save {rel_path.name} ({timestamp})"
    )
    return f"Saved: {rel_path}\n{push_result}"


@mcp.tool()
def search_analyses(query: str) -> str:
    """Search saved analysis pages (wiki/analyses/) — by topic, keyword, or title."""
    if not ANALYSES_DIR.exists():
        return "No saved analyses yet."
    return _search(ANALYSES_DIR, query)


@mcp.tool()
def list_analyses() -> str:
    """List all saved analysis pages, newest first."""
    if not ANALYSES_DIR.exists():
        return "No saved analyses yet."
    files = sorted(ANALYSES_DIR.rglob("*.md"), reverse=True)
    if not files:
        return "No saved analyses yet."
    lines = []
    for f in files[:150]:
        rel = str(f.relative_to(VAULT_ROOT))
        try:
            title = f.read_text(encoding="utf-8").split("\n")[0].lstrip("# ").strip()
        except Exception:
            title = f.stem
        lines.append(f"- [{title}]({rel})")
    note = f"\n\n(showing 150 of {len(files)})" if len(files) > 150 else ""
    return "Saved analyses:\n\n" + "\n".join(lines) + note


@mcp.tool()
def get_analysis(file_path: str) -> str:
    """Return the full content of a saved analysis page.
    file_path: relative path from vault root, e.g. 'wiki/analyses/2026-07-24 My Analysis.md'
    Get the path from search_analyses or list_analyses first — don't guess it."""
    p = VAULT_ROOT / file_path
    return _read(p) if p.exists() else f"File not found: {file_path}"


# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Starting Claude Notes Vault MCP Server on port {PORT}")
    print(f"Vault root: {VAULT_ROOT.resolve()}")
    print(f"Saved chat transcripts: {len(_all_md(CHAT_DIR))}")
    print(f"Saved analyses: {len(_all_md(ANALYSES_DIR))}")
    print(f"Write access (GITHUB_TOKEN): {'enabled' if GITHUB_TOKEN else 'DISABLED — saves will stay local only, not push'}")
    print(f"Git branch: {GIT_BRANCH}")
    print(f"SSE endpoint mounted at /<secret>/sse (secret not logged)")
    mcp.run(transport="sse")
