# IU research skills family: conventions

This guide is for anyone who maintains a repository in the family, or starts a new one. It holds the conventions every repository shares. Each repository's own `CONTRIBUTING.md` and `MAINTAINING.md` apply them to its domain.

Read two sibling repositories before writing anything. They are the working examples of everything here.

## Contents

- The family
- Scoping a new repository
- Choosing the skills
- Sources
- Trust markers, Verified dates, and open items
- What stays out
- Freshness checks
- House style
- The shared checker
- Repository layout
- Feedback and review
- Adding a repository to the family
- Lessons

The monthly review has its own runbook, [monthly-review.md](monthly-review.md).

## The family

Each repository is a set of [Agent Skills](https://agentskills.io/specification) about one part of research at IU. Every skill says where each claim came from, so an agent never trusts its own memory of IU.

| Repository | Covers | Leaves to a companion |
| --- | --- | --- |
| research-technologies | Clusters, storage, transfer, allocations, and IU's LLM service | What data may go where (research-data) |
| research-data | Finding, classifying, managing, and sharing data | Where it is computed on and stored (research-technologies) |
| research-funding | Planning and preparing a proposal | The DMS plan (research-data), facilities text (research-technologies), and core quotes (research-cores) |
| research-cores | Core facilities, instruments, and the data they deliver | Proposal drafting (research-funding) and storage (research-technologies) |
| iu-research | The conventions, the checker, the workflows, the marketplace, and the feedback skill | Every research topic (the four above) |

Each repository also states the one rule it exists for, in its README and `CONTRIBUTING.md`. Examples: research-data separates Required from Recommended, and research-funding says the researcher owns the science.

## Scoping a new repository

- Name the domain in one line, and the jobs a researcher brings to it.
- Check every sibling for overlap first. If a topic already has a skill, the new repository points to it rather than repeats it.
- Draw the edge against each companion, one sentence per companion. Example: research-cores covers core quotes and letters; research-funding covers the proposal as a whole.
- Name the repository for its domain, not a document. research-funding was chosen over research-proposals because it covers the whole funding path.
- Find the domain's one rule early.

A skill points across an edge by repository and skill name, as in "`getting-help-with-proposals` in research-funding." Link the first mention in each file to `https://github.com/IUSCA/<repo>/tree/main/.agents/skills/<skill>`. Never use a relative path into a sibling checkout. It breaks wherever the siblings are not cloned side by side.

## Choosing the skills

Every repository has the same four kinds of skill:

1. **A start-here map.** What exists at IU, what it is called now, and what was renamed or retired. Its README row ends with "Start here." It often holds a snapshot script and a renamed-and-retired or catalog file in `references/`. Examples: `iu-research-computing-map`, `iu-research-cores-map`, `finding-iu-research-data`, and `planning-a-proposal`.
2. **A matching or planning skill.** It turns a described research need into the right system, dataset, core, or plan. Examples: `planning-research-computing-work`, `matching-research-to-cores`, and `planning-data-management-and-sharing`.
3. **Access and how-to skills.** One per task a researcher actually does. Examples: `requesting-accounts-and-allocations`, `using-iu-research-cores`, and `budgeting-a-proposal`.
4. **A getting-help skill.** A table of question, office, and shared address, plus what to send. Examples: `getting-help-with-research-data` and `getting-help-with-proposals`.

A skill earns its place when a researcher's question needs more than a line in the map. Otherwise add the line to the map. As of 2026-11-02 the repositories have 17, 8, 10, and 7 skills. Name skills as gerund phrases, such as `using-iu-research-cores`, except the map.

Write descriptions that trigger:

- Start with what the skill does, naming the IU systems, offices, and terms a user would type.
- End with "Use when" and the situations, in a user's words.
- Stay under 1024 characters.
- Write two or more trigger prompts per skill in `tests/trigger-prompts.md`, in a researcher's words, not the skill's vocabulary.

## Sources

Fetch every page. Never write from memory.

What counts as a source:

- IU policies at `policies.iu.edu`, with policy numbers.
- IU KB articles, cited as `[KB0012345](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0012345)`. Old `kb.iu.edu/d/` links lose the article. Read articles with `iukb.py` in research-technologies' `searching-the-iu-knowledge-base`.
- IU unit pages, sponsor pages and notices, and federal regulations.
- Live systems, catalogs, and directories, recorded as Observed.

What does not count:

- Memory, an agent's or a person's.
- Internal working-group drafts. They may guide what to look for. They are never cited and never committed.
- Login-only pages. The repositories are public, so a claim must come from a page a guest can read. `iukb.py` and the checker read the KB without logging in, so an article they return is public. Never quote an article you could read only while logged in. A link to a login-only task, such as a One.IU launch link, is fine; its content is not.
- A person's email, unless recorded as a dated reply from an office, without the name.

Use official office names. Check every one against the office's own page. For example, IU's name is "Office for Research Administration (ORA)," not "Office of Research Administration."

After drafting, run a separate fact-check pass that reads every cited source again. Correct or downgrade each claim it cannot confirm. In the family's first fact-check, a draft written from official sources still had more than 20 wrong or unsupported claims out of about 185. Budget a fact-check pass for every new repository, and before any large commit.

## Trust markers, Verified dates, and open items

| Marker | Use it when | Must carry |
| --- | --- | --- |
| **Required** | A binding source requires it: IU policy, law or regulation, a sponsor notice or terms, an agreement or license, or a core's written policy | The source, named in the same paragraph, list item, or table row |
| **Recommended** | Nothing requires it, and the repository advises it | The reason, and any guidance or peer policy it follows |
| **Observed** | Read from a live system, page, or directory | The date, plus the host, page, or command |
| **External** | From a non-IU source | The source |
| **Practice** | A lesson from experience that no source states | A check, where one exists |
| **Open item** | No source answers it, or sources conflict | The sources that disagree, quoted |

A repository uses only the markers its README defines. `markers` in its `tools/check-skills.toml` lists them, and the checker fails any other. research-technologies uses Observed, External, Practice, and Open item; its KB citations play the Required role.

Never make a recommendation look like a rule, or a rule look optional. A claim cited inline to an IU page or KB article needs no marker.

When the live system and a document disagree on a fact the system reports, keep the Observed value. Note the document as lagging. It is not an open item.

Write a lesson as Practice: state the lesson and the reason, and give a check where one exists. Leave out the incident: no people, hosts, tickets, projects, or dates of failures. If a source backs the lesson, cite it instead.

### Verified dates

Each skill has a `Verified YYYY-MM-DD` line near the top. Change it only after re-reading every source. A partial re-read is written exactly as:

```text
Verified 2026-10-03 (KB0023515 and KB0025747 only). Other sources were verified 2026-10-01.
```

The checker dates the named items with the first date and the rest with the second. STALE uses the older date. A KB article with an entry in `tools/kb-snapshot.json` has its own record of the last reading. The Verified line need not list it.

### Open items

When sources disagree or are silent, write an open item. Do not pick the more plausible value. Every open item also goes in `docs/open-items.md`, grouped by the office that can answer it. Each office gets one ready-to-send message: its shared address, a subject, a short greeting, and numbered questions that each name the skill they came from. Close an item only with a page and date, or a dated reply. Do not name the person who replied.

## What stays out

The skills hold what is true for anyone at IU. They leave out:

- **People.** No names and no personal email addresses. Name the office and its shared address. Each address must be listed in `allowed_emails` after checking it is a role address on an official page.
- **Internal systems.** No internal hostnames, operations details, tickets, incidents, or internal project names. `internal_hosts` in the checker config catches known patterns.
- **Internal platform software.** Describe what a researcher sees, such as "a web data portal." Do not say what software runs it or who operates it.
- **Account names.** Even a generic Slurm account name counts as internal. Say which partition was used, not which account.
- **Prices and rates as examples.** Agents copy examples. Describe how rates are structured, and where to read them now. A cost estimate needs the live rate page or a written quote. Institution-wide rates set by agreement, such as F&A and fringe, may stay if dated and Observed. Add an instruction to check them again each budget year.
- **Links to repositories that are not public.** They return 404. Name a companion in prose until it has a public URL.
- **One person's or one project's details.** Accounts, allocations, a proposal plan, or quotes go in a private file outside the repository. research-technologies uses `~/.config/iu-research/resources.md` or `$IU_RESEARCH_NOTES`.

## Freshness checks

Every repository finds what changed in its own way, from this set:

| Kind | Example | How it runs |
| --- | --- | --- |
| Live system | `describe-cluster.sh` and `check-cluster.sh` in research-technologies | By a person after login, quarterly and after maintenance |
| KB articles | Any repository citing KB | `check-skills.py --kb`, monthly |
| Cited URLs | Every repository | `check-skills.py --links`, monthly |
| Catalog snapshot | `rdc_catalog.py check` in research-data | `[[freshness.commands]]`, monthly |
| Directory scrape | `core_directories.py check` in research-cores | `[[freshness.commands]]`, monthly |
| Skill owners | `skill_owner.py check` in iu-research | `[[freshness.commands]]`, monthly |
| Age | `stale_after_days` | Every run |

A snapshot script is standard-library Python with `check` (exits 1 on any change), `show <id>`, and `snapshot` (writes a dated file into `references/`). It prints names only, never people's contact details.

Two workflows run in every repository. `check-skills.yml` runs the offline checker on every pull request and push to `main`. `freshness.yml` runs `tools/check-skills.py --freshness` on the 1st of each month. When it finds `STALE`, `BROKEN`, `CHANGED`, or `ERROR` lines, it opens an issue labeled `freshness`, or comments on the open one.

Updates stay human-reviewed. A person or their agent works each freshness issue by hand. [monthly-review.md](monthly-review.md) is the family runbook for it: roles, calendar, setup, shared KB articles, the procedure, review, and handing a repository to an agent. Each repository's `MAINTAINING.md` adds only its own monthly items. Nothing edits a skill on its own, because every fixed claim needs someone to read its source. In iu-research, a freshness issue is usually a moved link or a new skill missing from the owner table; fix it in a pull request.

### The KB snapshot

`tools/kb-snapshot.json` records, for each linked KB article, its version, published and updated dates, a sha256 of its text, and the date it was taken. Refresh one article with `--kb-snapshot KB0123456` right after re-reading it, or all with `--kb-snapshot`. Commit it with the skill change it supports.

The KB edits articles in place. ServiceNow's `published` date does not always move when an article changes, but `sys_updated_on` and the version do. The checker reads both.

## House style

### Sentences

- One idea per sentence, under 25 words.
- Plain words. Say "use," not "leverage."
- The serial comma.
- Lead each section with its claim, then support it.
- Second person for instructions; present tense for facts.

### Skill layout

1. Frontmatter: `name` and `description` only, unless a spec field is needed.
2. `# Title` in plain words.
3. The Verified line, then one paragraph with the skill's main claim.
4. Sections that answer questions in the order a researcher asks them. Use tables for "question, office, contact" and "fact, check with."
5. `## Keep this file current`: what changes, how to re-check it, and open items.
6. `## Sources`: "Checked <date>." then one bullet per source.

Keep `SKILL.md` under 500 lines; move catalogs, maps, and templates to `references/`. Put scripts in `scripts/`, in standard-library Python or Bash. A script never prompts for a passphrase or answers Duo.

Skills live in `.agents/skills/<name>/SKILL.md`, with `name` equal to the directory name in kebab-case. `.claude/skills` is a committed symbolic link to `../.agents/skills`, because Claude Code reads only `.claude/skills/`.

### Naming things

- Another skill: its name in backticks.
- A companion's skill: name and repository, as in "`sharing-research-data` in research-data."
- Offices: full official name, then the short form, as in "Office for Research Administration (ORA)."
- Placeholders: `<user>`, `<project>`, and `<id>`.

### Harness neutrality

Do not name a harness's tools. Say "fetch the page" or "run the script," not a tool name. Each README explains how each harness finds the skills.

## The shared checker

`tools/check-skills.py` is one standard-library Python 3.11+ file. It is identical in every repository, and iu-research holds the canonical copy. `tools/check-skills.toml` holds what differs. The first line it prints carries its version and a hash, so copies can be compared.

### Modes

```bash
tools/check-skills.py              # offline; CI runs this on every push and PR
tools/check-skills.py --kb         # look up each linked KB article
tools/check-skills.py --links      # fetch every cited URL, with two retries
tools/check-skills.py --freshness  # the [freshness] checks and commands; monthly
tools/check-skills.py --kb-snapshot [KB...]  # record linked KB articles' text
tools/check-skills.py --version    # version and sha256 of this file
```

It exits 1 on any ERROR, BROKEN, or CHANGED line. STALE, INFO, and WARN never fail.

### Checks

| Check | Level | Config |
| --- | --- | --- |
| Frontmatter present; name matches directory, kebab-case, at most 64 characters | ERROR | no |
| Description 1 to 1024 characters | ERROR | no |
| Description says "Use when" | WARN | no |
| Only spec frontmatter fields | ERROR | no |
| SKILL.md at most 500 lines | ERROR | no |
| Verified line present, and not in the future | ERROR | no |
| Verified older than N days | STALE | `stale_after_days` |
| Ends with "Keep this file current," then "Sources" | ERROR | no |
| An id cited in the text but not in Sources | WARN | `cited_ids` |
| Link to a missing `references/`, `scripts/`, or `assets/` file | ERROR | no |
| Link outside the skill (`../`) | ERROR | no |
| Marker not in the repository's set | ERROR | `markers` |
| Required statement names no binding source | ERROR | `required_source` |
| Observed statement carries no date | ERROR | no |
| Email not an allowed office address | ERROR | `allowed_emails` |
| Internal hostname | ERROR | `internal_hosts` |
| Every skill has a README row and a trigger prompt | ERROR | no |
| Linked KB article retired, login-only, or changed since last read | STALE (INFO when only metadata changed) | `[freshness].checks` |
| Claude plugin manifests parse, agree on name and version, and point at a skills directory that exists | ERROR or WARN | no |
| Cited URL broken | BROKEN | `[links]` |
| Snapshot command found a change | CHANGED | `[[freshness.commands]]` |

Marker and content checks cover `SKILL.md` and `references/*.md`. Content checks also cover scripts (hostnames only), the README, `CONTRIBUTING.md`, `MAINTAINING.md`, `tests/trigger-prompts.md`, and `docs/*.md`. The "Keep this file current" section is not marker-checked, because it talks about markers.

### The per-repository config

| Key | What it sets |
| --- | --- |
| `markers` | The markers the README defines |
| `required_source` | A regular expression for what counts as naming a binding source |
| `cited_ids` | Id patterns, such as KB or NIH notice numbers, that must also appear in Sources |
| `stale_after_days` | The STALE age; 0 turns it off |
| `allowed_emails` | Shared office addresses that may appear |
| `internal_hosts` | A regular expression for hostnames that must never appear |
| `[links]` | `user_agent`, `skip_403_hosts`, and `skip_urls`, each skip with a comment saying why |
| `[freshness]` | `checks` (`kb`, `links`) and `[[freshness.commands]]` with `name`, `run`, and `step` |

An unknown key is an error. A key left out takes the checker's default.

### Changing the checker

1. Open an issue or pull request in iu-research. Edit `tools/check-skills.py` here. Keep it standard-library only, and keep repository specifics in the TOML.
2. Bump `VERSION`.
3. A repository that needs a new behavior gets a new config key, with a default that keeps the others passing. Never fork the file.
4. Run `tools/sync-checker.sh --install`. It copies the checker and both workflows into each family checkout next to this one. It never touches a repository's TOML.
5. Run `tools/check-skills.py` in each repository. Each must print `OK`.
6. Open one pull request per repository with the copied files.
7. `tools/sync-checker.sh` with no flag reports any copy that drifted.

Add a check when a fact-check pass finds a class of mistake. Observed claims without dates, personal emails, internal hostnames, and skills missing from the README all became checks this way.

## Repository layout

Every family repository has these files. Copy them from the most similar sibling, then rewrite each for the domain.

| Path | What it is |
| --- | --- |
| `README.md` | Domain, companion list, quickstart, markers table, what stays out, skills table, install, maintaining, and license |
| `CONTRIBUTING.md` | How to verify and write one claim |
| `MAINTAINING.md` | The review runbook, including "Working a freshness issue" |
| `LICENSE`, `LICENSE-docs` | ECL-2.0 for code, CC BY 4.0 for written content |
| `.gitignore` | `__pycache__/`, `*.pyc`, and `.claude/worktrees/` |
| `.agents/skills/<name>/SKILL.md` | One directory per skill |
| `.claude/skills` | A symbolic link to `../.agents/skills` |
| `.claude-plugin/plugin.json`, `marketplace.json` | The repository as a Claude plugin and its own marketplace, `iusca-<repo>` |
| `.github/workflows/check-skills.yml`, `freshness.yml` | Identical to iu-research's copies |
| `.github/ISSUE_TEMPLATE/skill-feedback.yml` | The feedback form, modeled on iu-research's |
| `tools/check-skills.py` | Identical to iu-research's copy |
| `tools/check-skills.toml` | This repository's settings |
| `tools/kb-snapshot.json` | If the repository cites KB articles |
| `docs/open-items.md` | Every open item, by owning office |
| `tests/trigger-prompts.md` | Two or more prompts per skill |

## Feedback and review

GitHub issues and pull requests are how anyone requests a change. Feedback never goes to a person's email.

- An issue goes to the repository that owns the skill. The `reporting-a-skill-problem` skill in iu-research works out the owner, drafts a public-safe report, and files it only with the person's yes.
- An issue filed on the wrong repository is transferred to the right one, within the IUSCA organization.
- A maintainer reviews every pull request before it merges. The reviewer reads the cited sources, not only the diff.
- Pull requests from forks wait for approval before CI runs. Approve the run, review the diff, then merge.
- Check a contributed claim about a tool against the tool's own documentation before merging.
- Make one focused commit per skill change. Say in the message which sources were re-read.

## Adding a repository to the family

1. Scope it, choose its skills, and research them from official sources, as above.
2. Build it from the layout above. Copy the checker and workflows with `tools/sync-checker.sh --install <path>`.
3. Run the fact-check pass. Then `tools/check-skills.py` must print `OK`, and `--freshness` must run with every BROKEN link fixed or in `skip_urls` with a reason.
4. Have a maintainer review the whole repository before its first push.
5. In iu-research, add the repository to:
   - the family table in `README.md` and in this guide;
   - `.claude-plugin/marketplace.json`, with a `github` source;
   - `.github/ISSUE_TEMPLATE/config.yml` and the dropdown in `skill-feedback.yml`;
   - `REPOS`, the table, and the description in `reporting-a-skill-problem`;
   - the default list in `tools/sync-checker.sh`.
6. Add it to the "Companion repositories" list in every sibling README, so each names all the others.
7. Once it is public, link companion mentions to it on GitHub, and run `--links` everywhere.

## Lessons

These came from building and running the family. Each changed a skill, the checker, or the process.

- **Give parallel agents separate files.** When one agent fact-checks skills while another changes tooling, give one `.agents/` and `docs/`, and the other `tools/`, `.github/`, `tests/`, and top-level files. Each lists what it found in the other's files instead of editing them.
- **Sponsor rules outrun memory.** In 2026, agent memory and many institutional guides had several NIH rules wrong. Examples are prior contact for large budgets, letters of intent, and paylines. Read the current notice every time.
- **Directories disagree and lag.** IU has no single core directory. Snapshot every directory with a script. Treat a name listed only in a directory as an open item until its own page confirms it.
- **One partial Verified date was not enough.** Re-reading one article forced re-reading every other article on the same partial line. The KB snapshot is now the per-article record.
- **GitHub-hosted runners sometimes never start a job.** "The job was not acquired by Runner" is infrastructure, not the checker. Re-run it before debugging.
- **Some hosts refuse GitHub's runners but not people.** Handle links (`hdl.handle.net`) and IU ScholarWorks failed every retry from Actions but resolved from IU and home networks. Confirm by hand, then add the URL to `skip_urls` with a dated comment. Keep the persistent link.
- **Test with the agent where users will run it.** A skill that assumed a laptop needed its own branch for an agent started on a cluster login node.
- **Never put an API key in an agent's environment.** An agent asked to check access can print its environment into its answer. Have the harness read the key from a file per request.
- **Generate model lists from the live service.** Model names in a pasted config are often withdrawn. Read the service's model list instead.
- **Model choice changes skill routing.** The same prompt loaded the expected skill with one model and not with others. Test trigger prompts with the models people use.
- **Copies drift fast.** Copies of the checker drifted within a day, as each new repository added checks. The fix was one canonical file, per-repository TOML, a version and hash line, and the sync script.

## Keeping this guide current

- When a repository adopts a new convention, decide whether it belongs to the family. If it does, add it here in a pull request, and list the repositories that must follow.
- When the checker changes, update the checks and config tables here in the same pull request.
- When work teaches a new lesson, add it under Lessons, without people, hosts, or incidents.
