# Which repository owns each skill

**Observed 2026-11-02 from the Skills table in each repository's README.md.** Each repository's checker fails a skill with no row there, so the table lists every skill. `scripts/skill_owner.py check` compares this file with the live READMEs, and the monthly freshness check in iu-research runs it.

A skill name is unique across the family, with one exception during the move to iu-research: `reporting-a-skill-problem` exists in both iu-research and research-technologies. Report a problem with it to iu-research.

| Skill | Repository |
| --- | --- |
| `reporting-a-skill-problem` | iu-research |
| `capturing-a-workflow-as-a-skill` | research-technologies |
| `checking-iu-research-access` | research-technologies |
| `getting-help-from-research-technologies` | research-technologies |
| `iu-research-computing-map` | research-technologies |
| `jetstream2` | research-technologies |
| `managing-python-environments` | research-technologies |
| `managing-rt-projects` | research-technologies |
| `planning-research-computing-work` | research-technologies |
| `requesting-accounts-and-allocations` | research-technologies |
| `running-llms-on-hpc` | research-technologies |
| `searching-the-iu-knowledge-base` | research-technologies |
| `storing-and-moving-research-data` | research-technologies |
| `submitting-hpc-jobs` | research-technologies |
| `using-reallms` | research-technologies |
| `using-research-desktop` | research-technologies |
| `versioning-research-code` | research-technologies |
| `accessing-health-and-clinical-data` | research-data |
| `classifying-research-data` | research-data |
| `finding-iu-research-data` | research-data |
| `getting-help-with-research-data` | research-data |
| `navigating-research-data-policy` | research-data |
| `planning-data-management-and-sharing` | research-data |
| `sharing-research-data` | research-data |
| `using-licensed-and-public-data` | research-data |
| `assembling-required-documents` | research-funding |
| `budgeting-a-proposal` | research-funding |
| `finding-funding-opportunities` | research-funding |
| `getting-help-with-proposals` | research-funding |
| `planning-a-proposal` | research-funding |
| `responding-to-reviews-and-resubmitting` | research-funding |
| `routing-and-submitting-at-iu` | research-funding |
| `using-preliminary-data-and-feasibility` | research-funding |
| `writing-specific-aims` | research-funding |
| `writing-the-research-strategy` | research-funding |
| `acknowledging-research-cores` | research-cores |
| `budgeting-core-services-in-proposals` | research-cores |
| `getting-help-with-research-cores` | research-cores |
| `handling-core-instrument-data` | research-cores |
| `iu-research-cores-map` | research-cores |
| `matching-research-to-cores` | research-cores |
| `using-iu-research-cores` | research-cores |

Every repository is on GitHub as `IUSCA/<repository>`. The checker in iu-research, `tools/check-skills.py`, and the family conventions also belong to iu-research.
