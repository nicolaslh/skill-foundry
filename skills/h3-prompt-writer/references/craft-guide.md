# Craft Guide

Voice design, shot design, continuity, and the expanded quality checklist.

## Voice Design

Each voice block carries three layers.

Fixed attributes, always present:

- age feel
- gender
- register
- timbre
- pace
- volume
- sentence endings

Dynamic attributes, chosen from the plot:

- 正常 / 紧张 / 怀疑 / 开心 / 生气 / 尴尬 / 被拆穿 / 放松 / 开玩笑 / 犹豫 / 惊讶

Forbidden attributes, always present. Name the styles most likely to drift:

```text
禁止夹子音、幼态撒娇腔、尖叫和播音腔。
```

Keep the fixed layer identical across every shot. Only the dynamic layer reacts to the plot.

## Shot Selection

Pick shot size from intent, not from a desire for more shots.

Two-character interaction:

```text
斜侧双人中景
正面双人中景
双人中近景
```

Single-character dialogue:

```text
正面中近景
正面近景
斜侧近景
```

Emotional reaction:

```text
正面近景
面部特写
```

Prop or environment information:

```text
斜侧近景
局部特写
环境中景
```

## Shot Count

Default split rules:

- one clear action stage = one shot
- one clear emotional turn = one shot
- one new visual focus = one shot
- do not cut inside a single continuous action without reason

If the user fixes a shot count, follow it exactly. If the user fixes a duration, scale shot count and action density to that duration.

## Action Chains

Write continuous action chains, not action lists.

Good:

```text
先回头看向飞机，又立刻转回人物；
双手同时收紧；
身体微微前倾；
眼神带着怀疑。
```

Bad:

```text
看飞机、转头、抓袋子、说话。
```

Preferred internal order:

```text
动作A -> 动作B -> 动作C -> 表情变化 -> 台词
```

## Micro-Action Library

Give each key shot a suitable amount of micro-action, enough for performance continuity without clutter:

手指收紧 / 握紧道具 / 松开道具 / 呼吸变化 / 肩膀放松 / 眼神移动 / 嘴唇张开 / 嘴唇闭合 / 眉毛变化 / 身体前倾 / 身体后仰 / 低头 / 抬头 / 踮脚 / 衣服褶皱 / 道具滑落 / 重新抓稳

Do not stack micro-actions that carry no meaning.

## Continuity

Later shots inherit everything already established: reference-image binding, character position, left/right relationship, clothing, hair, props, prop state, relationships, environment, time, light, eyeline axis.

`<Picture X>` is declared once in the character block and holds for the whole prompt. Do not restate it per shot, and do not reassign a character to a different picture number mid-prompt.

Prop state must progress legibly:

```text
Shot 1：
人物握紧手提袋。

Shot 2：
手提袋仍然存在。

Shot 3：
手提袋从手腕滑落。

Shot 4：
人物重新抓稳手提袋。
```

Do not let the bag reappear in the other hand in Shot 4 without a reason.

## Quality Checklist

Characters:

- [ ] Subject numbers unique
- [ ] `<Picture X>` present for every character that has a reference image
- [ ] picture numbers match the order the user supplied the images
- [ ] position inside the reference image stated
- [ ] left/right positions consistent
- [ ] appearance consistent
- [ ] clothing consistent
- [ ] props consistent

Voices:

- [ ] every speaking character has a unique S number
- [ ] Subject and S correspond
- [ ] fixed voice described
- [ ] emotion variants described
- [ ] forbidden voice styles included

Shots:

- [ ] every shot has explicit visual content
- [ ] shot size is reasonable
- [ ] actions have clear order
- [ ] necessary micro-actions present
- [ ] shots connect to each other

Dialogue:

- [ ] uses `says`
- [ ] uses `<d>[Chinese]... </d>`
- [ ] bound to the correct character
- [ ] no filler narration

Global constraints:

- [ ] forbidden list present
- [ ] subtitles forbidden
- [ ] logo and watermark forbidden
- [ ] readable on-screen text forbidden
- [ ] no background music unless the user explicitly asked
