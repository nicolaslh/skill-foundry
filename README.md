# Agent Foundry

Agent Foundry is a lightweight workspace for managing reusable skills, prompts, workflows, harness cases, and shared utilities.

## Repository Layout

```text
agent-foundry/
├── skills/      # Codex-style skill folders, each with a SKILL.md
├── harness/     # Evaluation cases and local test harness notes
├── prompts/     # Reusable prompt building blocks
├── workflows/   # Multi-step agent/skill recipes
└── utils/       # Small scripts for validation and maintenance
```

## Conventions

- Name skill folders in hyphen-case, matching the `name` field in `SKILL.md`.
- Keep each `SKILL.md` concise. Put long references in `references/`, deterministic helpers in `scripts/`, and reusable output assets in `assets/`.
- Add harness cases before a skill becomes important enough to rely on repeatedly.
- Prefer workflows for orchestration across multiple skills instead of stuffing orchestration rules into one skill.
- Use harness template registries for AI-readable style prompts, rubrics, and example cases when a skill needs repeatable quality checks.

## Quick Checks

Run the repository sanity check:

```bash
python3 utils/check_skills.py
python3 utils/check_harness.py
```

Build a harness task package:

```bash
python3 harness/run_case.py --case field-journal-style
```

The task package includes `codex_task.md` for running the case inside Codex.

Validate a single Codex skill shape with the upstream validator when `PyYAML` is available in the Python environment:

```bash
python3 /Users/nic/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/travel-writer
```
