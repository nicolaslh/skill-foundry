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

## Install With The Local Helper

Use the repository helper when you want repeatable installs:

```bash
python3 utils/install_skill.py travel-article-beautifier
```

Install all skills:

```bash
python3 utils/install_skill.py --all
```

Install to a custom destination:

```bash
python3 utils/install_skill.py travel-article-beautifier --dest /path/to/codex-home/skills
```

Back up an existing install before replacing it:

```bash
python3 utils/install_skill.py travel-article-beautifier --backup-existing
```

Overwrite an existing install:

```bash
python3 utils/install_skill.py travel-article-beautifier --overwrite
```

## Development Install With A Symlink

For active development, install a symlink so Codex reads the skill directly from this repository:

```bash
python3 utils/install_skill.py travel-article-beautifier --method symlink --backup-existing
```

This is convenient while editing, because changes in the repository are reflected in the installed skill path. If a Codex environment does not follow symlinks, use copy mode instead.

## Sync Install With rsync

Use `rsync` when you want repeatable updates with deletion of removed files:

```bash
dest="${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
mkdir -p "$(dirname "$dest")"
rsync -a --delete skills/travel-article-beautifier/ "$dest/"
```

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

## Updating After Code Changes

The update path depends on the original install method.

### Copy Install

If you installed by copying, run the helper again:

```bash
python3 utils/install_skill.py travel-article-beautifier --backup-existing
```

If you do not need the previous installed copy:

```bash
python3 utils/install_skill.py travel-article-beautifier --overwrite
```

Update all skills:

```bash
python3 utils/install_skill.py --all --backup-existing
```

### Symlink Install

If you installed with a symlink, no reinstall is needed:

```bash
python3 utils/install_skill.py travel-article-beautifier --method symlink --backup-existing
```

The Codex skills directory points directly to the skill in this repository. After editing repository files, Codex should see the updated skill on the next turn.

### Harness Changes

The harness is not installed into the Codex skills directory. It runs from this repository:

```bash
python3 utils/check_harness.py
python3 harness/run_case.py --case field-journal-style
```

When harness code, cases, rubrics, or quality gates change, rerun the harness locally. No Codex skill reinstall is needed.

### Recommended Flow

Use symlink mode while actively editing:

```bash
python3 utils/install_skill.py travel-article-beautifier --method symlink --backup-existing
```

Use copy mode for stable installs or sharing:

```bash
python3 utils/install_skill.py travel-article-beautifier --backup-existing
```

Before and after updates, run:

```bash
python3 utils/check_skills.py
python3 utils/check_harness.py
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

## Future GitHub Install

After this repository is pushed to GitHub, a Codex skill installer can install a skill directly from a repo URL:

```bash
python3 /Users/nic/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/<owner>/<repo>/tree/main/skills/travel-article-beautifier
```

Use this for sharing skills across machines or teammates.
