# Monthly review of the research skills

This runbook keeps every family repository true to its sources, month by month. Anyone with write access to the repositories can run it, with or without an agent. It assumes no knowledge beyond this file, [research-skills-conventions.md](research-skills-conventions.md), and each repository's `MAINTAINING.md`.

The general procedure is here. Each repository's `MAINTAINING.md` adds only what is specific to it, such as the catalog in research-data or the cluster check in research-technologies.

## Roles

| Role | Does |
| --- | --- |
| Coordinator | Opens the month's tracking issue, assigns each repository, checks the shared KB articles, and closes the tracking issue. Usually the family maintainer. |
| Repository reviewer | Works one repository's freshness issue and opens its pull request. May hand the work to an agent. |
| Approver | Reads the pull request's sources, not only its diff, and merges it. Should not be the person who opened it, whenever a second person is available. |

The README's Maintainers table names who fills each role. A role with no one in it falls to the family maintainer.

## Calendar

| When | What | Who |
| --- | --- | --- |
| 1st of the month, 13:00 UTC | `freshness.yml` runs in every repository. GitHub often starts scheduled runs hours late. | Automatic |
| First week | Tracking issue, then one review per repository | Coordinator, reviewers |
| By the 15th | Every review pull request merged, or its delay noted on the tracking issue | Approvers |
| Day after HPC maintenance (second Monday) | Cluster check in research-technologies; needs a login with Duo | A person with a Quartz and Big Red 200 account |
| January, April, July, October | The full quarterly review in each `MAINTAINING.md`, after the monthly one | Coordinator, reviewers |
| As announced | Event triggers in each `MAINTAINING.md`, such as an NIH notice, a new PAPPG, a new research data policy | Whoever watches the feed (see "Watching for events") |

## Before you start

You need:

- The GitHub CLI, `gh`, signed in to an account with write access to the IUSCA repositories.
- Python 3.11 or newer. The checker reads its settings with `tomllib`.
- A checkout of every family repository, side by side in one directory. The KB reader lives in research-technologies, at `.agents/skills/searching-the-iu-knowledge-base/scripts/iukb.py`. Run it as `python3 -I <path> read KB0123456`.
- About ten minutes of machine time per repository. `--freshness` takes 2 to 5 minutes and prints nothing for long stretches. `--kb-snapshot` takes a minute or more. Neither is hung.

Save checker output with `| tee file`, not a bare `> file`. A bare redirect has produced a file of NUL bytes at least once.

`gh issue view` fails in this organization with a "Projects (classic)" error. Use the REST API instead:

```bash
gh api repos/IUSCA/<repo>/issues/<n> -q .body
gh api repos/IUSCA/<repo>/issues/<n>/comments -q '.[].body'
```

## 1. See where things stand

From an iu-research checkout:

```bash
tools/family-status.sh
```

For each repository it shows the last `freshness.yml` run and its result, any open `freshness` issue, and every open pull request. Then:

- **A run failed, or did not run.** Open the run in Actions and fix the cause first. `gh run view --log` can print nothing; `gh api repos/IUSCA/<repo>/actions/jobs/<job-id>/logs` works.
- **No open issue.** The run found nothing to report. Still read the run's log for `INFO` lines (see step 3). They never open an issue.
- **An open issue.** The workflow adds a comment on each run with work in it. Work from the latest comment. It repeats every earlier line that has not cleared, so earlier comments can be ignored.
- **A run that finds nothing posts nothing.** It never closes the issue either. An old issue can look current when every line has cleared. Re-running the check (step 3) is the only way to know.

Open a tracking issue on iu-research titled `Monthly review YYYY-MM`, with the "Monthly review" form. It lists each repository with its issue, its reviewer, and its pull request. It is the month's record, and the place to note anything left for a person.

## 2. Plan around shared KB articles and open pull requests

**Shared articles.** Several KB articles are cited in more than one repository. For example, KB0023515 is cited in research-technologies and research-data, and KB0025237 in research-technologies and research-cores. When the same article is STALE in two repositories, one reviewer reads it once. They post a short note on the tracking issue: what changed, and whether it is substantive. The other reviewer still checks the claims in their own repository, but starts from that note.

**What changed in an article.** The snapshot holds only a hash of each article's text, not the text. To learn what changed before reading the whole article:

- Compare the hash in each repository's `tools/kb-snapshot.json`. If another repository already recorded the new hash, its commit message usually says what changed.
- Look at the article's version and updated date. A new updated date with an unchanged hash is an `INFO` line: the KB touched the article but not its text.

**Open pull requests.** A review branch made from `main` will conflict with an open pull request that also changes `tools/kb-snapshot.json` or the same skill. Either merge that pull request first, or stack the review branch on it:

```bash
git -C <repo> fetch origin
git -C <repo> worktree add ../<repo>-freshness-YYYY-MM -b freshness-YYYY-MM origin/<their-branch>
```

A stacked pull request targets the other branch. GitHub closes the freshness issue only when a pull request merges into `main`. After the base merges, check that the stacked pull request now targets `main`. GitHub retargets it only when the base branch is deleted on merge.

If an open pull request already re-read an article, say so in the review, and do not redo it. The approver of that pull request is responsible for its reading.

## 3. Work one repository

Name the branch `freshness-YYYY-MM`. Fetch first, so the base is current.

1. Re-run the check: `tools/check-skills.py --freshness | tee freshness.txt`. Lines may have cleared since the issue was written.
2. Work every line by kind. That includes `INFO`. An unrecorded `INFO` line comes back every month.
   - **STALE, KB article changed.** Read the whole article with `iukb.py read`. Find every citing claim with `grep -rn KB0123456 .agents/skills docs`. Citations also live in `references/`, in `scripts/`, and in quotes in `docs/open-items.md`. Check the claims in every citing skill, not only the first one. Fix what changed. Then re-run `--kb` and confirm the hash has not moved since you read it. Then record it with `tools/check-skills.py --kb-snapshot KB0123456`.
   - **INFO, text unchanged.** Record it with `--kb-snapshot KB0123456`. No skill changes.
   - **STALE, not found by KB search.** The article was retired, renumbered, or made login-only. Search for a replacement. If there is none, name the article without a link, with the date it went missing.
   - **STALE, Verified date too old.** Re-read every source the skill cites, then update its Verified line.
   - **BROKEN.** Run `--links` again. A single failure is often transient. If it passes, record it in the pull request as "transient", with no change.
   - **BROKEN twice.** Test whether the host refuses scripts: request it several times with the checker's user agent and with a browser's. If a browser's works, add the host to `skip_403_hosts`, or the URL to `skip_urls`, in `tools/check-skills.toml`, with a comment saying how and when you checked. If neither works, find the page's new address. If the page is gone, find another source, or make the claim an open item.
   - **CHANGED.** Run the snapshot script the line names. Update the file it compares against, and every skill that names what changed.
   - **SKIP.** Expected. A `skip_urls` entry whose comment says "check by hand" is checked by hand in the quarterly review, not monthly.
3. Do the repository's own monthly items, from its `MAINTAINING.md`.
4. A claim the new source no longer supports is fixed, cut, or made an open item in `docs/open-items.md`. A question the source now settles leaves the open items.
5. Run `tools/check-skills.py --freshness` until no `STALE`, `BROKEN`, `CHANGED`, or `INFO` line remains, or each remaining line is explained.

### Rules that trip people up

- **Never run `--kb-snapshot` without article numbers.** With none, it records every article as re-read.
- **Snapshot after checking every citing skill.** A snapshot is per article, but a `STALE` line is per skill. One snapshot clears the line in every skill that cites the article.
- **Login-only articles.** `iukb.py read` reads as a guest. If it cannot read an article, the article is login-only. Never quote or summarize a login-only article, even if you can read it while signed in.
- **Verified lines.** Change a skill's Verified line only when you edit the skill, or re-read every source it cites. A partial re-read uses the exact form the checker expects: `Verified YYYY-MM-DD (<what> only). Other sources were verified YYYY-MM-DD.` A partial re-read does not reset the 120-day STALE clock, which follows the older date. A `references/` file with its own Verified line follows the same rule. An article recorded with `--kb-snapshot` does not also need to be named in the Verified line.
- **Second-hand Sources.** A Sources entry that says "as cited by <repo>" may be rewritten once you have read the source yourself. That counts as an edit.

### Commits

- One skill per commit. Put a snapshot in the commit of the skill change it supports.
- If no skill changed, put the snapshot in a snapshot-only commit. Name the articles and the skills that cite them in the message.
- If an article is cited by several skills and only one changed, the snapshot goes in that skill's commit.
- Changes outside the skills each get their own commit: `tools/check-skills.toml`, `docs/open-items.md`, and pruning `allowed_emails`.
- Say in each message which sources were re-read.

### The pull request

Title it `Monthly freshness review, <Month YYYY>`. In the body:

- `Closes #<issue>`, and the base pull request, if the branch is stacked.
- A table grouped by article or URL: the line, the skills it names, and what was done. Say whether the line was fixed, unchanged with a snapshot, transient, or opened as an item. Collapse many unchanged `INFO` lines into one row.
- Open items opened or closed.
- Anything left for a person.

Add the pull request to the tracking issue.

**Nothing to change.** Close the freshness issue with a comment. Give the date, the checker version, and a line saying `--freshness` was clean.

## 4. Review and merge

The approver:

- Reads each changed claim's source, not only the diff. For a fixed claim, finds the sentence in the source that supports it.
- For an "unchanged" line, spot-checks at least one citing claim against the article.
- Confirms CI passed, and that the freshness issue will close (the pull request targets `main`, or will after its base merges).
- Merges, then ticks the repository on the tracking issue.

## 5. Close the month

When every repository is ticked, the coordinator:

- Lists anything left for a person on the tracking issue, with a date and an owner, such as the cluster check.
- Opens issues for tooling gaps found this month (see "Known gaps").
- Closes the tracking issue.

## Handing a repository to an agent

An agent can do steps 2 and 3 for one repository. It cannot do the cluster check, approve its own pull request, or send anything to an office. Give it this prompt, filled in. Run one agent per repository, at the same time if you like:

```text
Run the <Month YYYY> freshness review for IUSCA/<repo>, checked out at <path>.
Follow iu-research's docs/monthly-review.md, steps 2 and 3, and this
repository's MAINTAINING.md. Work issue #<n>; read the latest comment.

Make a worktree:
  git -C <path> fetch origin
  git -C <path> worktree add ../<repo>-freshness-YYYY-MM -b freshness-YYYY-MM origin/<base>
where <base> is main, or the branch of open pull request #<m> if it also
changes tools/kb-snapshot.json or the skills this issue names.

Shared articles already read this month (from the tracking issue): <notes, or none>.
Already settled by open pull requests: <list, or none>.

Do not edit tools/check-skills.py; it is shared. Do not push or open a pull
request. Report: the branch and commits; a table of every line and what you
did; a draft pull request body in the runbook's format; anything left for a
person; and every place this runbook or MAINTAINING.md was unclear or wrong.
```

The person who gave the prompt reviews the branch, pushes it, and opens the pull request. Fold the agent's "unclear or wrong" list into this runbook.

## Watching for events

Some triggers come from outside, and no script notices them. Each repository's `MAINTAINING.md` lists its own. The family maintainer makes sure someone subscribes to each feed, and records who on the tracking issue each quarter:

- The NIH Guide table of contents and NSF news, for research-funding and research-data. The NIH Guide's weekly index cannot be paged back by script. Use its search page, or read each week's issue as it arrives.
- IU policy changes on `policies.iu.edu`, and the Research Data Commons news page, for research-data.
- HPC maintenance announcements, for research-technologies.
- CTSA and S10 award news, for research-cores.

## Known gaps

These were found in the November 2026 review. Each needs a change to the shared checker or workflows, made in iu-research and synced to the family. Until then, follow the workaround.

| Gap | Workaround |
| --- | --- |
| `freshness.yml` does not report `INFO` lines, so they never reach the issue | Read the run's log, or re-run the check |
| A clean run does not close or comment on the open issue | Re-run the check before working an old issue |
| The KB snapshot stores a hash, not text, so nothing shows what changed | Compare hashes across repositories; read the whole article |
| `--kb` cannot be limited to one article or skill | Run it whole |
| `--kb-snapshot KB0123456` reports "Wrote N KB articles", though only the named one changed | Check the diff of `tools/kb-snapshot.json` |
| The link check probes loopback and private addresses, such as `127.0.0.1` | Add each example address to `skip_urls` |
| `iukb.py` can print malformed links, such as `https://servicenow.iu.eduKB0023488` | Read the KB number by eye |
| The workflows use actions that run on Node 20, which GitHub has deprecated | None needed yet; update `actions/checkout` and `actions/setup-python` |

## Keeping this runbook current

After each month, fold in what the reviewers found unclear or wrong. Do it in a pull request on iu-research, linked from the tracking issue. When a gap above is fixed, remove its row in the same pull request as the fix.
