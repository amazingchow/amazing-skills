# Semantic Tokens

这里记录“用途”，不是记录“物理值”。

不要把 token 命名成：

- `blue-500`
- `gray-200`
- `big-radius`

优先写成：

- `text/primary`
- `text/muted`
- `surface/base`
- `surface/raised`
- `surface/brand`
- `border/subtle`
- `border/strong`
- `accent/primary`
- `accent/secondary`

## 推荐格式

### Text

- `text/primary` -> 用于正文和主要标题
- `text/secondary` -> 用于辅助信息
- `text/muted` -> 用于标签、注释、时间
- `text/inverse` -> 用于深色底上的文本

### Surface

- `surface/base`
- `surface/subtle`
- `surface/raised`
- `surface/overlay`
- `surface/brand`

### Border

- `border/subtle`
- `border/default`
- `border/strong`

### Accent / Status

- `accent/primary`
- `accent/soft`
- `status/success`
- `status/warning`
- `status/danger`

## 规则

- 一个组件只引用 semantic token，不直接写色值
- 一个 token 可映射到多端实现，但语义必须稳定
- 改风格时优先改 foundations 与 token 映射，不要逐组件修修补补
