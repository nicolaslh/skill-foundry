# 安装到 Codex

这个仓库分两层：

- `skills/`：Codex 可以自动发现的 skill 目录。
- `harness/`：本地评测、回归测试和开发辅助工具。

Codex 默认会从下面的目录发现已安装 skill：

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

`harness/` 不需要安装到 Codex 里。它保留在本仓库中，用来开发、评测和生成 Codex 任务包。

## 安装单个 Skill

安装 `travel-article-beautifier`：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/travel-article-beautifier "${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
```

安装后，通常下一轮 Codex 对话就可以使用这个 skill。

## 使用本仓库安装脚本

如果希望安装过程更稳定、可重复，可以使用本仓库提供的安装脚本：

```bash
python3 utils/install_skill.py travel-article-beautifier
```

安装全部 skills：

```bash
python3 utils/install_skill.py --all
```

安装到自定义目录：

```bash
python3 utils/install_skill.py travel-article-beautifier --dest /path/to/codex-home/skills
```

替换已有安装前先备份：

```bash
python3 utils/install_skill.py travel-article-beautifier --backup-existing
```

直接覆盖已有安装：

```bash
python3 utils/install_skill.py travel-article-beautifier --overwrite
```

## 开发期软链接安装

如果你正在频繁修改 skill，可以使用软链接安装：

```bash
python3 utils/install_skill.py travel-article-beautifier --method symlink --backup-existing
```

这样 Codex skills 目录会指向当前仓库里的 skill。你在仓库中修改文件后，安装目录会同步看到变化。如果某个 Codex 环境不跟随软链接，则改用 copy 方式。

## 使用 rsync 同步安装

如果希望重复同步，并删除目标目录中已经被源目录删除的旧文件，可以使用 `rsync`：

```bash
dest="${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
mkdir -p "$(dirname "$dest")"
rsync -a --delete skills/travel-article-beautifier/ "$dest/"
```

## 安装全部 Skills

把本仓库 `skills/` 下所有 skill 都安装到 Codex：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
for skill in skills/*; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  cp -R "$skill" "${CODEX_HOME:-$HOME/.codex}/skills/$name"
done
```

## 更新已安装的 Skill

如果目标目录已经存在，建议先备份再覆盖：

```bash
dest="${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
backup="${dest}.backup.$(date +%Y%m%d-%H%M%S)"

if [ -d "$dest" ]; then
  mv "$dest" "$backup"
fi

cp -R skills/travel-article-beautifier "$dest"
```

## 代码变动后如何更新

更新方式取决于你最初的安装方式。

### copy 安装

如果是普通复制安装，代码变动后重新运行安装脚本：

```bash
python3 utils/install_skill.py travel-article-beautifier --backup-existing
```

如果不需要保留旧版本，可以直接覆盖：

```bash
python3 utils/install_skill.py travel-article-beautifier --overwrite
```

更新全部 skills：

```bash
python3 utils/install_skill.py --all --backup-existing
```

### symlink 安装

如果是软链接安装，不需要重新安装：

```bash
python3 utils/install_skill.py travel-article-beautifier --method symlink --backup-existing
```

软链接会让 Codex skills 目录直接指向本仓库里的 skill。之后你改仓库中的文件，安装目录会自动看到最新内容。通常下一轮 Codex 对话即可使用更新后的 skill。

### harness 变动

`harness/` 不安装到 Codex skills 目录。它始终在本仓库中运行：

```bash
python3 utils/check_harness.py
python3 harness/run_case.py --case field-journal-style
```

所以 harness 代码、评测用例、rubric 或 quality gates 变动后，不需要更新 Codex 安装，只需要在仓库中重新运行 harness。

### 推荐流程

开发期推荐 symlink：

```bash
python3 utils/install_skill.py travel-article-beautifier --method symlink --backup-existing
```

稳定使用或发布时推荐 copy：

```bash
python3 utils/install_skill.py travel-article-beautifier --backup-existing
```

每次更新前后建议跑：

```bash
python3 utils/check_skills.py
python3 utils/check_harness.py
```

## 验证安装结果

查看 skill 是否已经复制到 Codex skills 目录：

```bash
ls "${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
```

安装前，可以先检查本仓库里的 skill 结构：

```bash
python3 utils/check_skills.py
```

如果当前 Python 环境安装了 `PyYAML`，也可以使用 Codex 官方 validator 检查单个已安装 skill：

```bash
python3 /Users/nic/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  "${CODEX_HOME:-$HOME/.codex}/skills/travel-article-beautifier"
```

## 运行 Harness

harness 保留在本仓库中运行：

```bash
python3 utils/check_harness.py
python3 harness/run_case.py --case field-journal-style
```

`harness/run_case.py` 会生成一个任务包，其中包含 `codex_task.md`。当你希望 Codex 执行某个评测用例时，把这个 `codex_task.md` 交给 Codex 即可。

## 常见安装位置

默认 Codex home：

```bash
~/.codex/skills/travel-article-beautifier
```

自定义 Codex home：

```bash
CODEX_HOME=/path/to/codex-home
mkdir -p "$CODEX_HOME/skills"
cp -R skills/travel-article-beautifier "$CODEX_HOME/skills/travel-article-beautifier"
```

## 注意事项

- 安装 skill 时，只会复制对应的 skill 目录。
- `harness/` 是仓库级开发和评测工具，不会被 Codex 自动发现。
- 如果要跑评测用例，请继续在本仓库中使用 `harness/run_case.py`。
- 覆盖已安装 skill 前，建议先备份旧目录。

## 未来从 GitHub 安装

如果之后把本仓库推到 GitHub，也可以使用 Codex skill installer 直接从 GitHub URL 安装：

```bash
python3 /Users/nic/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/<owner>/<repo>/tree/main/skills/travel-article-beautifier
```

这种方式适合跨设备或团队共享 skill。
