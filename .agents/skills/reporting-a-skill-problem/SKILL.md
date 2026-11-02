---
name: reporting-a-skill-problem
description: Report a problem with any skill in the IU research skills family (iu-research, research-technologies, research-data, research-funding, research-cores) as a GitHub issue on the IUSCA repository that owns that skill, with a pull request if the person wants one. Works out the owning repository, checks for an existing issue, drafts a public-safe report with the exact problem and how the fix was checked, and files it only with the person's yes. Use when a skill's instructions turned out wrong, out of date, or incomplete during a session, such as an error the skill did not mention, a rule or page that changed, a step that no longer works, or a gap that cost time, or when someone asks how to suggest a change to these skills.
---

# Reporting a skill problem

Verified 2026-11-02 against the family's repositories and the GitHub CLI manual. Sources are listed at the end.

A session can show that a skill was wrong, out of date, or silent. Report it to the repository that owns the skill, so the next researcher at IU does not hit the same problem. Each repository's maintainers check the report against a source and update the skill.

**Practice.** Finish the person's task first. Then tell them in one sentence what the skill got wrong, and offer to draft a report.

## Confirm it is the skill

Report the skill only when it, not the session, was wrong.

- Run the failing step again, so the report quotes a real error or a real page.
- Let the source answer. A live system answers what it can report, such as a partition list or quota. An IU policy, KB article, sponsor notice, or core page answers what it states. Each repository's `CONTRIBUTING.md` names its sources.
- A one-off outage is not a skill problem. Check the service's status page or maintenance window first.
- A question the sources do not answer is still worth reporting. Say so, and the maintainers record it as an open item.

## Find the repository that owns the skill

Every skill belongs to one repository, `IUSCA/<repository>` on GitHub. File the report there, and nowhere else. Work it out in this order:

1. **Plugin namespace.** A Claude plugin skill is named `<plugin>:<skill>`. The plugin name is the repository name, as in `research-data:sharing-research-data`.
2. **Install path.** Look at where the skill's `SKILL.md` was loaded from. In a clone, the git remote names the repository. In a plugin install, the nearest `.claude-plugin/plugin.json` names it. A path often contains the repository name.
3. **The table.** [references/skill-owners.md](references/skill-owners.md) lists every skill in the family and its repository. Use it when the skill was copied into another project, which loses both clues above.

The helper does all three:

```bash
python3 scripts/skill_owner.py <skill-name>
python3 scripts/skill_owner.py <plugin>:<skill-name>
python3 scripts/skill_owner.py <path to SKILL.md>
```

A clone whose remote is not `IUSCA` is a fork. Report to the IUSCA repository unless the fork's owner asks for reports there.

A problem with the family's shared parts goes to iu-research. That means `tools/check-skills.py`, the CI workflows, the plugin marketplace, and the family conventions.

If no clue and no table row matches, the skill is not from this family. Tell the person, and do not file anything.

## Check for an existing issue

```bash
gh issue list -R IUSCA/<repository> --state open --search "<skill-name>"
```

Add a comment to a matching issue instead of opening a new one. Without `gh`, search the issues page, `https://github.com/IUSCA/<repository>/issues`.

## Draft the report

**Practice.** The agent drafts the issue. The person reads it and decides whether to send it. Never send it without their yes.

The issue is public. Leave out:

- Data values, file contents, and model outputs about the data.
- Participant, patient, or sample identifiers.
- Keys, tokens, and passwords.
- Usernames, personal paths, account and project names, and hostnames that are not public. Use placeholders such as `<user>` and `<project>`.
- One person's proposal, budget, fund numbers, quotes, reviewer comments, or scores.
- Anything read only while logged in. Cite a page a guest can open.

A good report has:

- The skill name, its repository, and what the skill said or left out.
- What happened, with the exact error text or the words on the page.
- What fixed it, and how that was checked. Give the command and host, or the page URL, with the date, such as `Observed 2026-11-02 on <page URL>`.
- The KB article, policy, or notice number that backs the fix, if one does.

The repository's "Skill feedback" issue form asks for these.

## Send it

With `gh` signed in to GitHub.com:

```bash
gh issue create -R IUSCA/<repository> \
  --title "<skill-name>: <what was wrong or missing>" \
  --body-file <draft.md>
```

The person runs `gh auth login` themselves; never handle their token. **Practice.** Some clusters provide `gh` as a module. For example, on IU's Quartz it is the `github_cli` module; see `versioning-research-code` in research-technologies.

Without `gh`, open `https://github.com/IUSCA/<repository>/issues/new/choose`. Choose "Skill feedback" if the repository has that form. Otherwise open a blank issue. Paste the draft either way.

## Attach a pull request, if wanted

An issue alone is enough. A person comfortable with GitHub can attach the fix:

1. Fork and clone: `gh repo fork IUSCA/<repository> --clone`.
2. Make a branch, and edit the skill. That repository's `CONTRIBUTING.md` says how to mark and cite each claim.
3. Run `tools/check-skills.py`. It must print `OK`.
4. Open the pull request with `Closes #<issue>` in its description.

A maintainer reviews it before anything merges.

## Keep this file current

- When a family repository adds, renames, or retires a skill, update [references/skill-owners.md](references/skill-owners.md). `python3 scripts/skill_owner.py check` lists the differences. The monthly freshness check in iu-research runs it.
- When a repository joins the family, add it to `REPOS` in `scripts/skill_owner.py`, to the table, and to the list in the description.
- Update this file when the issue form in `.github/ISSUE_TEMPLATE/` or the review process in `docs/family-conventions.md` changes.

## Sources

Checked 2026-11-02.

- The README, `CONTRIBUTING.md`, and `MAINTAINING.md` of each family repository, `https://github.com/IUSCA/<repository>`.
- iu-research's `.github/ISSUE_TEMPLATE/skill-feedback.yml` and `docs/family-conventions.md`.
- External: [GitHub CLI manual](https://cli.github.com/manual/), for `gh issue list`, `gh issue create`, and `gh repo fork`.
- External: [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), for plugin names as skill namespaces.
