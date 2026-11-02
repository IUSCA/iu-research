#!/usr/bin/env bash
# Compare or install the family's shared checker and workflows.
#
# Usage:
#   tools/sync-checker.sh [repo ...]            # report which copies differ
#   tools/sync-checker.sh --install [repo ...]  # copy this repository's files in
#
# This repository (iu-research) holds the canonical copies, at the same paths
# every family repository uses:
#   tools/check-skills.py
#   .github/workflows/check-skills.yml
#   .github/workflows/freshness.yml
#
# Repos default to the four family checkouts next to this one:
#   ../research-technologies ../research-data ../research-funding ../research-cores
# Never touches a repository's tools/check-skills.toml, which is its own.
# After an install, run tools/check-skills.py in each repository; it must
# print OK. Then commit and open a pull request there, one per repository.
set -euo pipefail

here=$(cd "$(dirname "$0")/.." && pwd)
install=0
if [ "${1:-}" = "--install" ]; then install=1; shift; fi
if [ $# -eq 0 ]; then
  parent=$(dirname "$here")
  set -- "$parent/research-technologies" "$parent/research-data" \
         "$parent/research-funding" "$parent/research-cores"
fi

files=(
  tools/check-skills.py
  .github/workflows/check-skills.yml
  .github/workflows/freshness.yml
)

echo "canonical: $(python3 "$here/tools/check-skills.py" --version 2>/dev/null || echo unknown)"
status=0
for repo in "$@"; do
  if [ ! -d "$repo" ]; then
    echo "MISSING  $repo (no checkout)"
    status=1
    continue
  fi
  for f in "${files[@]}"; do
    src="$here/$f" dst="$repo/$f"
    if cmp -s "$src" "$dst"; then
      echo "same     $dst"
    elif [ $install -eq 1 ]; then
      mkdir -p "$(dirname "$dst")"
      cp "$src" "$dst"
      echo "copied   $dst"
    else
      echo "DIFFERS  $dst"
      status=1
    fi
  done
  [ -f "$repo/tools/check-skills.toml" ] || { echo "MISSING  $repo/tools/check-skills.toml"; status=1; }
done
exit $status
