# Installing Into Codex

This repository has two layers:

- `skills/`: Codex-discoverable skill folders.
- `harness/`: local evaluation and regression tooling for developing skills.

Codex automatically discovers installed skills from:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

The harness does not need to be installed into Codex. Keep it in this repository and run it locally.

## Install One Skill

Install `travel-article-beautifier`:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/travel-article-beautifier "${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
```

The skill should be available to Codex on the next turn.

## Install All Skills

Install every skill in this repository:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
for skill in skills/*; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  cp -R "$skill" "${CODEX_HOME:-$HOME/.codex}/skills/$name"
done
```

## Update An Existing Installed Skill

If the destination already exists, back it up first:

```bash
dest="${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
backup="${dest}.backup.$(date +%Y%m%d-%H%M%S)"

if [ -d "$dest" ]; then
  mv "$dest" "$backup"
fi

cp -R skills/travel-article-beautifier "$dest"
```

## Verify Installed Files

Check that the skill exists:

```bash
ls "${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
```

Check the local repo structure before installing:

```bash
python3 utils/check_skills.py
```

Validate one installed skill with the upstream validator when `PyYAML` is available:

```bash
python3 /Users/nic/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  "${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
```

## Run Harness Cases

Harness cases stay in this repository:

```bash
python3 utils/check_harness.py
python3 harness/run_case.py --case field-journal-style
```

The generated task package includes `codex_task.md`. Give that file to Codex when you want Codex to execute a specific harness case.

## Common Install Targets

Default Codex home:

```bash
~/.codex/skills/travel-article-beautifier
```

Custom Codex home:

```bash
CODEX_HOME=/path/to/codex-home
mkdir -p "$CODEX_HOME/skills"
cp -R skills/travel-article-beautifier "$CODEX_HOME/skills/travel-article-beautifier"
```

## Notes

- Installing a skill copies only that skill folder.
- Repository-level harness files are for development and evaluation.
- If a skill relies on harness-managed examples, keep this repository available and use `harness/run_case.py`.
- Avoid copying a skill over an existing destination without backing it up.
