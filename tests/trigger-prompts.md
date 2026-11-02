# Trigger prompts

Use these in a fresh session to check that each skill loads when it should. Each prompt names the skill that should load first. Others may load too. `tools/check-skills.py` fails a skill with no row here.

| Prompt | Expected skill |
| --- | --- |
| The data management skill told me to use a form that doesn't exist anymore. Can we let whoever maintains it know? | `reporting-a-skill-problem` |
| That Slurm advice was wrong, the partition is gone. How do I suggest a fix? | `reporting-a-skill-problem` |
| I'd like to send a pull request to improve one of these IU skills. Where does it go? | `reporting-a-skill-problem` |
