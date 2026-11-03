#!/usr/bin/env bash
# Show where the monthly review stands in every family repository.
#
# Usage:
#   tools/family-status.sh [owner/repo ...]
#
# For each repository it prints:
#   - the last run of freshness.yml (date and result), so a run that failed
#     or never happened is not mistaken for "nothing to do";
#   - every open issue labeled `freshness`, with its last update;
#   - every open pull request, since a review branch may need to stack on
#     one that touches the same skill or tools/kb-snapshot.json.
#
# Needs the GitHub CLI (`gh`), signed in. Reads only; changes nothing.
# docs/monthly-review.md explains what to do with the output.
set -euo pipefail

if [ $# -eq 0 ]; then
  set -- IUSCA/research-technologies IUSCA/research-data \
         IUSCA/research-funding IUSCA/research-cores IUSCA/iu-research
fi

for repo in "$@"; do
  echo "== $repo"
  if ! gh api "repos/$repo" -q .full_name >/dev/null 2>&1; then
    echo "   not reachable (unpublished, renamed, or no access)"
    continue
  fi
  run=$(gh run list -R "$repo" --workflow freshness.yml --limit 1 \
        --json createdAt,conclusion,status,url \
        -q '.[0] | "\(.createdAt[:10])  \(.status)/\(.conclusion // "-")  \(.url)"' 2>/dev/null || true)
  echo "   last freshness run: ${run:-none found}"
  # The REST API avoids `gh issue view`, which can fail on deprecated
  # Projects (classic) fields.
  issues=$(gh api "repos/$repo/issues?labels=freshness&state=open" \
           -q '.[] | select(.pull_request | not) | "   issue #\(.number)  updated \(.updated_at[:10])  \(.title)"')
  echo "${issues:-   no open freshness issue}"
  prs=$(gh api "repos/$repo/pulls?state=open" \
        -q '.[] | "   PR #\(.number)  \(.head.ref)  \(.title)"')
  echo "${prs:-   no open pull requests}"
done
