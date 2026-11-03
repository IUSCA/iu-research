# iu-research

The shared home of the IU research skills family. The family is a set of open agent-skill repositories about research at Indiana University, for any IU researcher and their coding agent. Each skill says where every claim came from, so an agent never trusts its own memory of IU.

This repository holds what the family shares: the conventions, the checker, the CI workflows, and a Claude plugin marketplace. It also holds one skill, for reporting a problem with any family skill. The skills about research itself live in the four repositories below.

## The family

| Repository | Covers | Start with |
| --- | --- | --- |
| [research-technologies](https://github.com/IUSCA/research-technologies) | Clusters, storage, data transfer, allocations, and IU's LLM service | `checking-iu-research-access` |
| [research-data](https://github.com/IUSCA/research-data) | Finding, classifying, managing, and sharing research data | `finding-iu-research-data` |
| [research-funding](https://github.com/IUSCA/research-funding) | Planning and preparing grant proposals | `planning-a-proposal` |
| [research-cores](https://github.com/IUSCA/research-cores) | Core facilities, their instruments, and the data they deliver | `iu-research-cores-map` |
| **iu-research** (this repository) | The family's conventions, checker, marketplace, and feedback skill | `reporting-a-skill-problem` |

Each repository draws its edge against the others in its own README. A skill names a companion's skill by repository and skill name, as in "`sharing-research-data` in research-data."

## Install all of them

### Clone them

```bash
git clone https://github.com/IUSCA/research-technologies.git
git clone https://github.com/IUSCA/research-data.git
git clone https://github.com/IUSCA/research-funding.git
git clone https://github.com/IUSCA/research-cores.git
git clone https://github.com/IUSCA/iu-research.git
```

Start your agent in a clone. Claude Code, Codex, OpenCode, and pi all find that repository's skills with no install step. The skills live in `.agents/skills/`. Claude Code reads only `.claude/skills/`, so each repository commits `.claude/skills` as a symbolic link to `.agents/skills`.

To use skills in another project, copy the skill directories you need into that project's `.agents/skills/`. Or use the [`skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/IUSCA/research-data --list
npx skills add https://github.com/IUSCA/research-data --skill finding-iu-research-data --copy
```

### As Claude plugins

This repository is a Claude plugin marketplace that lists all five plugins. Installing them makes every skill available in all your projects, with no clone.

In Claude Code:

```text
/plugin marketplace add IUSCA/iu-research
/plugin install iu-research@iusca-iu-research
/plugin install research-technologies@iusca-iu-research
/plugin install research-data@iusca-iu-research
/plugin install research-funding@iusca-iu-research
/plugin install research-cores@iusca-iu-research
```

Install only the plugins you need. Plugin skills are namespaced by repository, so `finding-iu-research-data` appears as `research-data:finding-iu-research-data`. To update, run `/plugin marketplace update iusca-iu-research`.

Each family repository is also its own marketplace, as its README explains. The manifests here are `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`. Sources for these locations: [Agent Skills specification](https://agentskills.io/specification), [Claude Code plugins](https://code.claude.com/docs/en/plugins), and [plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

## Give feedback

GitHub issues and pull requests are how changes are requested. They are public, so leave out data, identifiers, keys, usernames, and project names.

- **A skill was wrong, out of date, or missing something.** Open an issue on the repository that owns the skill, with its "Skill feedback" form where it has one. Your agent can work out the owner and draft the issue; see `reporting-a-skill-problem`.
- **You have a fix.** Open a pull request on the owning repository. Its `CONTRIBUTING.md` explains how to mark and cite a claim, and `tools/check-skills.py` must print `OK`.
- **The conventions, the checker, the workflows, or the marketplace.** Open an issue or pull request here.

Feedback goes through GitHub, not email. A maintainer answers every issue there.

## Skills

| Skill | Use it when |
| --- | --- |
| [reporting-a-skill-problem](.agents/skills/reporting-a-skill-problem/SKILL.md) | A skill from any family repository was wrong, out of date, or missing something, and you want to report it or send a fix. |

## What the skills trust

The skill here describes the family's own process. Every claim carries one of these markers, or cites its source inline:

| Marker | Meaning | Must cite |
| --- | --- | --- |
| **Observed** | Read from a live page or repository, such as a README's skills table | The date and the URL or command |
| **External** | From a non-IU source, such as the GitHub CLI manual | The source |
| **Practice** | A lesson from experience that no source states | How to check it, where possible |
| **Open item** | No source answers it, or sources conflict | The sources that disagree |

Each family repository defines its own markers in its README. The full set, and what each must carry, is in [docs/research-skills-conventions.md](docs/research-skills-conventions.md).

## Maintaining the family

- [docs/monthly-review.md](docs/monthly-review.md) is the runbook for the monthly review of every family repository. `tools/family-status.sh` shows where each repository stands.
- [docs/research-skills-conventions.md](docs/research-skills-conventions.md) is the guide for any maintainer. It covers scoping, trust markers, sources, freshness, house style, the shared checker, and adding a repository.
- `tools/check-skills.py` is the canonical checker. Every family repository carries an identical copy. Only each repository's `tools/check-skills.toml` differs.
- `tools/sync-checker.sh` reports any family copy of the checker or workflows that differs from this repository's, and `--install` copies them in.
- `.github/workflows/check-skills.yml` and `freshness.yml` are the canonical workflows, identical in every repository.
- [tests/trigger-prompts.md](tests/trigger-prompts.md) checks that agents load the right skill.

## Maintainers

Maintenance is by role, so it can pass from one person to the next. Each role is a GitHub team or account with write access, named here. A role with no one in it falls to the family maintainer.

<!-- Owner: replace each <placeholder> with a GitHub team or role account, not a personal email. -->

| Role | Responsible for | Who |
| --- | --- | --- |
| Family maintainer | This repository: the conventions, checker, workflows, and marketplace; adding a repository to the family | `<github-team-or-account>` |
| Repository maintainer | One family repository: triaging its issues, reviewing pull requests, working its monthly freshness issue, and its quarterly review | `<one per repository>` |
| Reviewer | Reading a pull request's cited sources before it merges | `<github-team-or-account>` |

A maintainer reviews every pull request before it merges. Nothing edits a skill on its own.

## License

Code, meaning scripts and tools, is under the Educational Community License, Version 2.0; see [LICENSE](LICENSE). Written content, including every `SKILL.md` and reference file, is under CC BY 4.0; see [LICENSE-docs](LICENSE-docs). Copyright the Trustees of Indiana University.
