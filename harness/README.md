# Harness

The harness directory holds test cases and lightweight evaluation fixtures for skills and workflows.

Suggested case shape:

- `id`: stable case identifier
- `skill`: target skill folder name
- `input`: user-style request
- `expect`: observable qualities to check in the response

Start with smoke tests, then add realistic examples whenever a skill fails or gets updated.

## Rubrics And Examples

- Put scoring rubrics in `harness/rubrics/`.
- Put skill-specific artifact schemas in `harness/schemas/<skill>-artifacts.yaml`.
- Put realistic input/expected pairs in `harness/examples/<skill>/<case>/`.
- Use examples to catch regressions after changing a prompt template, router, or workflow.

## Template Registries

Style templates are managed under `harness/templates/`. In this repo, style templates are AI-readable prompt templates, not final HTML/CSS layouts. A registry should point to the prompt template file, describe when to use it, and list checks that should remain true after the template is edited.

Run:

```bash
python3 utils/check_harness.py
```

Build a model-independent task package for a case:

```bash
python3 harness/run_case.py --case field-journal-style
```

The generated package includes `codex_task.md`, which can be handed directly to Codex as the execution prompt for that case.
