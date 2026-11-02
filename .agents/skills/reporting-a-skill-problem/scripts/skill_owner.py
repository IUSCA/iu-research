#!/usr/bin/env python3
"""Find which IU research skills repository owns a skill, or check the table.

Usage:
    skill_owner.py <skill-name>            # look the name up in the table
    skill_owner.py <plugin>:<skill-name>   # a Claude plugin namespace
    skill_owner.py <path>                  # a SKILL.md or skill directory
    skill_owner.py check                   # compare the table with each README

The table is references/skill-owners.md, next to this script's directory.
A path is resolved by its git remote, then by a Claude plugin manifest
above it, then by a family repository name in the path, then by the
skill directory's name in the table.

`check` reads the Skills table of each repository's README.md, which every
repository's checker keeps complete. It reads the local README when this
script runs inside that repository's checkout, and the public README on
GitHub otherwise. It exits 1 when a skill is missing from the table, or a
table row names a skill its repository no longer lists.

Exit status for a lookup: 0 when an owner is found, 2 when none is.
Standard library only; Python 3.9 or newer.
"""

import json
import pathlib
import re
import subprocess
import sys
import urllib.request

ORG = "IUSCA"
REPOS = ["iu-research", "research-technologies", "research-data", "research-funding", "research-cores"]
HERE = pathlib.Path(__file__).resolve().parent
TABLE = HERE.parent / "references" / "skill-owners.md"
ROW_RE = re.compile(r"^\|\s*`([a-z0-9-]+)`\s*\|\s*([a-z0-9-]+)\s*\|", re.M)
README_ROW_RE = re.compile(r"\(\.agents/skills/([a-z0-9-]+)/SKILL\.md\)")
REMOTE_RE = re.compile(r"github\.com[:/]([^/]+)/([^/.]+?)(?:\.git)?/?$")
RAW = "https://raw.githubusercontent.com/{org}/{repo}/main/README.md"


def load_table():
    """Return {skill: repository} from references/skill-owners.md."""
    return dict(ROW_RE.findall(TABLE.read_text()))


def from_git(start):
    """(repo, how) from the git remote of the checkout holding `start`."""
    try:
        url = subprocess.run(["git", "-C", str(start), "remote", "get-url", "origin"],
                             capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None
    m = REMOTE_RE.search(url)
    if not m or m.group(2) not in REPOS:
        return None
    owner, repo = m.groups()
    if owner != ORG:
        return repo, f"git remote {owner}/{repo}, a fork; report upstream unless its owner asks otherwise"
    return repo, f"git remote {owner}/{repo}"


def from_plugin(start):
    """(repo, how) from a .claude-plugin/plugin.json above `start`."""
    for d in [start, *start.parents]:
        manifest = d / ".claude-plugin" / "plugin.json"
        if manifest.is_file():
            try:
                name = json.loads(manifest.read_text()).get("name")
            except (OSError, json.JSONDecodeError):
                return None
            return (name, f"plugin manifest {manifest}") if name in REPOS else None
    return None


def owner_of(arg, table):
    """Return (repo, how), or (None, why)."""
    path = pathlib.Path(arg).expanduser()
    if path.exists():
        path = path.resolve()
        skill_dir = path.parent if path.is_file() else path
        for finder in (from_git, from_plugin):
            found = finder(skill_dir)
            if found:
                return found
        for part in reversed(skill_dir.parts):
            if part in REPOS:
                return part, f"repository name {part!r} in the path"
        arg = skill_dir.name
    elif ":" in arg:
        namespace, _, skill = arg.partition(":")
        if namespace in REPOS:
            note = "" if skill in table else f"; {skill!r} is not in the table yet"
            return namespace, f"plugin namespace {namespace!r}{note}"
        arg = skill
    if arg in table:
        return table[arg], f"table row for {arg!r}"
    return None, f"{arg!r} is not a skill of this family, as far as the table knows"


def readme_skills(repo):
    root = HERE.parents[3]  # scripts -> <skill> -> skills -> .agents -> root
    local = from_plugin(root)
    if local and local[0] == repo and (root / "README.md").is_file():
        text = (root / "README.md").read_text()
    else:
        url = RAW.format(org=ORG, repo=repo)
        req = urllib.request.Request(url, headers={"User-Agent": "iu-research-skill-owner"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode()
    return set(README_ROW_RE.findall(text))


def check(table):
    changed = 0
    for repo in REPOS:
        try:
            live = readme_skills(repo)
        except Exception as err:  # report and keep going
            print(f"ERROR    {repo}: could not read README.md: {err}")
            changed += 1
            continue
        listed = {s for s, r in table.items() if r == repo}
        for skill in sorted(live - listed):
            if skill in table:
                print(f"NOTE     {skill} is in {repo}'s README; the table says {table[skill]}")
            else:
                print(f"ADDED    {skill} in {repo}; add a row to references/skill-owners.md")
                changed += 1
        for skill in sorted(listed - live):
            print(f"REMOVED  {skill} is no longer in {repo}'s README; update the table")
            changed += 1
        print(f"checked  {repo}: {len(live)} skills")
    print("Table matches every README." if not changed else f"{changed} differences.")
    return 1 if changed else 0


def main(argv):
    if len(argv) != 1 or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0 if argv else 2
    table = load_table()
    if argv[0] == "check":
        return check(table)
    repo, how = owner_of(argv[0], table)
    if repo is None:
        print(f"No owner found: {how}.")
        return 2
    print(f"{ORG}/{repo}")
    print(f"  found by {how}")
    print(f"  issues: https://github.com/{ORG}/{repo}/issues")
    print(f"  new:    https://github.com/{ORG}/{repo}/issues/new/choose")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
