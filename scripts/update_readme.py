#!/usr/bin/env python3
"""Refreshes the auto-updating block in README.md from the GitHub API.

Only repos listed in FEATURED are shown, so half-finished or private-feeling
experiments never appear by accident. Add a repo name to FEATURED to show it.
Runs daily via .github/workflows/update-readme.yml (no secrets needed;
the built-in GITHUB_TOKEN is used only to avoid API rate limits).
"""
import json
import os
import re
import sys
import urllib.request

USER = "anshiiii-hub"
FEATURED = ["Flask-scraping", "upi-analysis", "web-scraping", "AIML-Bootcamp"]
MAX_ROWS = 5
START, END = "<!--RECENT:START-->", "<!--RECENT:END-->"
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "README.md")


def fetch_repos():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",
        headers={"Accept": "application/vnd.github+json",
                 "User-Agent": "anshita-exe-readme"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def build_block(repos):
    rows = [r for r in repos if r["name"] in FEATURED and not r.get("fork")
            and not r.get("archived")]
    rows.sort(key=lambda r: r["pushed_at"], reverse=True)
    lines = ["```text", "● ● ●  recent_activity.log  (auto-synced daily)"]
    for r in rows[:MAX_ROWS]:
        lang = r.get("language") or "-"
        lines.append(f"{r['pushed_at'][:10]}  {r['name']:<16} {lang}")
    if not rows:
        lines.append("(no featured repos found)")
    lines.append("```")
    return "\n".join(lines)


def update(text, block):
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pat.search(text):
        raise SystemExit("README markers not found")
    return pat.sub(lambda _: f"{START}\n{block}\n{END}", text)


def main():
    try:
        repos = fetch_repos()
    except Exception as e:  # keep the old block if GitHub is unreachable
        print("could not reach GitHub API:", e, file=sys.stderr)
        sys.exit(1)
    text = open(README, encoding="utf-8").read()
    new = update(text, build_block(repos))
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print("README updated")
    else:
        print("no changes")


if __name__ == "__main__":
    main()
