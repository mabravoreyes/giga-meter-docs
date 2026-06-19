"""
Summarize the latest Giga Meter release with Claude and inject it into README.md.

Called by .github/workflows/sync-releases.yml. Expects:
  /tmp/release_body.txt  — raw GitHub release body (markdown)
  ANTHROPIC_API_KEY      — Claude API key (from repo secret)
  RELEASE_TAG            — e.g. v2.0.2
  RELEASE_NAME           — e.g. "Giga Meter 2.0.2"
  RELEASE_DATE           — YYYY-MM-DD

Injects between <!-- release-start --> / <!-- release-end --> markers in README.md.
If markers are absent on first run, inserts after the opening H1 line.
"""

from __future__ import annotations
import json, os, re, urllib.request
from pathlib import Path

TAG   = os.environ["RELEASE_TAG"]
NAME  = os.environ["RELEASE_NAME"]
DATE  = os.environ["RELEASE_DATE"]
BODY  = Path("/tmp/release_body.txt").read_text().strip()
KEY   = os.environ["ANTHROPIC_API_KEY"]

RELEASES_URL = (
    f"https://github.com/unicef/project-connect-daily-check-app/releases/tag/{TAG}"
)

PROMPT = (
    "Summarize this Giga Meter software release in 1–2 plain-English sentences "
    "for a non-technical audience (school IT staff, ministry officials). "
    "Focus on what changed for the end user — skip internal implementation details. "
    "No bullet points, no markdown, no filler phrases like 'This release introduces'.\n\n"
    f"Release notes:\n{BODY}"
)


def summarize() -> str:
    payload = {
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 150,
        "messages": [{"role": "user", "content": PROMPT}],
    }
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode(),
        headers={
            "x-api-key": KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    return data["content"][0]["text"].strip()


def build_block(summary: str) -> str:
    return (
        f"<!-- release-start -->\n"
        f"<!-- release:{TAG} -->\n"
        f"> **{NAME}** — {DATE}\n"
        f">\n"
        f"> {summary}\n"
        f">\n"
        f"> [Full release notes →]({RELEASES_URL})\n"
        f"<!-- release-end -->"
    )


def inject(readme: str, block: str) -> str:
    pattern = r"<!-- release-start -->.*?<!-- release-end -->"
    if re.search(pattern, readme, re.DOTALL):
        return re.sub(pattern, block, readme, flags=re.DOTALL)
    # First run — no markers yet. Insert after the opening H1 + blank line.
    return re.sub(r"(# .+\n\n)", rf"\1{block}\n\n", readme, count=1)


readme_path = Path("README.md")
readme = readme_path.read_text()

print(f"Summarizing {TAG}...")
summary = summarize()
print(f"Summary: {summary}")

block   = build_block(summary)
updated = inject(readme, block)

readme_path.write_text(updated)
print("README.md updated.")
