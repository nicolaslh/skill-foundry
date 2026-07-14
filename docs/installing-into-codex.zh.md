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
