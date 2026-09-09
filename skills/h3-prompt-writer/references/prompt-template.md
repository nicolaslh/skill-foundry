# Fixed Prompt Templates

Copy these blocks verbatim and replace only the bracketed content. The tokens `<SubjectX>`, `S X`, `[Shot X]`, `says`, and `<d>...</d>` never change.

## 1. Character Block

Every main character is bound to a `<SubjectX>` token.

```text
<Subject1>[人物名称]是<Picture 1>画面[位置]人物，
保留参考图中的[面部特征]、[发型]、[服装]、
[身材比例]、[道具]以及整体外貌。
```

Example:

```text
<Subject1> Gu Yan是<Picture 1>画面左侧男性，保留参考图中的面部特征、黑色短发、黑色西装、白色衬衫、身材比例以及整体外貌。
```

Rules:

- Do not change character numbers.
- Do not swap left/right positions.
- Prefer reference-image features when a reference image is supplied.
- Keep clothing, hair, and props consistent across the whole video unless the plot changes them explicitly.

## 2. Voice Block

Every speaking character is bound to a unique `S` number.

```text
<Subject1>，S1 永远是说话人。
S1始终使用一种固定的声音：
[年龄感]，[性别]，[音域]，
音色[音色描述]，
常态语速[语速]、音量[音量]，
[句尾特征]；
[情绪状态1]；
[情绪状态2]；
[情绪状态3]。
禁止[声音风格1]、[声音风格2]、[声音风格3]。
```

Example:

```text
<Subject1>，S1 永远是说话人。S1始终使用一种固定的声音：20岁出头男性，中低音，音色干净沉稳，常态语速中等、音量偏低，句尾利落下收；说冷笑话时语气保持认真，只在最后几个字稍微放松；被拆穿后呼吸略微松开，声音中带一点压住的笑意。禁止播音腔、霸总气泡音、夸张精英腔和故作深沉。
```

## 3. Scene Block

```text
<Subject3>是[场景描述]。

人物站位：
[人物1的位置、朝向、手部状态]；
[人物2的位置、朝向、手部状态]。

两人[距离关系]。
[背景主要物体及位置]。
保持两人的左右关系与视线轴线。
[环境声音]。
```

Lock first:

- left/right relationship
- front/back relationship
- distance between characters
- body facing
- eyeline axis
- main prop positions
- main background objects
- ambient sound

## 4. Shot Block

With dialogue:

```text
[Shot 1]
[镜头类型 / 景别 / 机位 / 构图]。
[人物动作1]，[人物动作2]，[人物动作3]。
[表情 / 微表情 / 情绪]。

<Subject X> (SX) says:
<d>[Chinese]对白</d>
```

Without dialogue:

```text
[Shot 3]
[镜头类型 / 景别 / 构图]。
[动作连续变化]。
[表情 / 微动作]。
```

Never force a line into a silent shot.

## 5. Dialogue Block

```text
<Subject X> (SX) says:
<d>[Chinese]对白内容</d>
```

Example:

```text
<Subject 2> (S2) says:
<d>[Chinese]你不是说，订的是经济舱吗？</d>
```

Rules:

- `Subject` and `S` must correspond.
- One speaker per `says`.
- Chinese dialogue always uses the `[Chinese]` tag.
- Do not change the meaning of user-supplied lines.

## 6. Dialogue And Action Sync

Dialogue never floats free of action. Preferred order:

```text
动作 -> 表情 -> 说话
```

Or the longer form:

```text
动作开始 -> 人物看向对方 -> 表情变化 -> 开口说话 -> 说完后的反应
```

Example:

```text
Gu Yan顺着她刚才的视线看向飞机，
抬手整理了一下袖口，
随后重新看向她，
表情认真得没有一丝玩笑：

<Subject 1> (S1) says:
<d>[Chinese]对啊，经济情况允许的舱。</d>
```

## 7. Forbidden List

Always append:

```text
【禁止项】

文字/UI/水印/Logo/角标/可读文字/真实UI
```

Append user-specified additions to the same block:

```text
【禁止项】

文字/UI/水印/Logo/角标/可读文字/真实UI/
畸形手指/多余人物/人物身份漂移/服装变化
```

## 8. Forced Declaration

Always append:

```text
【强制声明】

无背景音乐,仅保留环境音与人声和音效;
画面禁字幕/文字/水印/Logo;
禁止可读文字(指画面字幕文字,不含人声台词)
```

Never add background music unless the user explicitly asks for it.

## 9. Full Output Template

```text
<Subject1>[人物1身份及外貌描述]。
<Subject1>，S1 永远是说话人。S1始终使用一种固定的声音：[声音设定]。[情绪变化]。禁止[声音禁止项]。

<Subject2>[人物2身份及外貌描述]。
<Subject2>，S2 永远是说话人。S2始终使用一种固定的声音：[声音设定]。[情绪变化]。禁止[声音禁止项]。

<Subject3>是[场景描述]。

人物站位：[空间关系描述]。
[连续性约束]。
[环境声音]。

[Shot 1]
[镜头 + 构图 + 动作 + 表情]：
<Subject 1> (S1) says:
<d>[Chinese]对白</d>

[Shot 2]
[镜头 + 构图 + 动作 + 表情]：
<Subject 2> (S2) says:
<d>[Chinese]对白</d>

[Shot 3]
[镜头 + 构图 + 动作 + 表情]。

……

【禁止项】

文字/UI/水印/Logo/角标/可读文字/真实UI

【强制声明】

无背景音乐,仅保留环境音与人声和音效;画面禁字幕/文字/水印/Logo;禁止可读文字(指画面字幕文字,不含人声台词)
```
