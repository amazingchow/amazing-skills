# Figma MCP System Prompt

把 Figma 文件链接和下面模板一起交给支持 Figma MCP 的 AI。

```md
请通过 Figma MCP 读取我提供的 Figma 文件。这个文件是 Reference Board，不是最终设计系统。

你的任务不是复刻页面，而是从中抽象出一个可复用的设计系统初稿。

## 工作目标

请基于参考板，输出以下内容：

1. foundations/colors
2. foundations/typography
3. foundations/spacing-radius-shadow-motion
4. tokens/semantic
5. components
6. patterns
7. prompts-rules 建议

## 工作原则

- 保留气质，不保留构图
- 不把任何单一参考网页当成最终规范
- 删除或忽略品牌强识别元素，例如 logo、品牌插画、专有图形、品牌文案
- 不允许生成对某个参考网页的 section-by-section 映射

## 你必须先做的分析

先按参考源分别总结：

- 它贡献了什么视觉特征
- 这些特征适合沉淀到哪个层级
  - foundations
  - semantic tokens
  - components
  - patterns
- 哪些内容必须舍弃，避免形成直接复刻风险

## 输出格式

请严格按以下结构输出：

### A. Visual DNA Summary

- 用 5 到 8 个关键词总结整体气质
- 分别写出应该保留的特征和应该舍弃的特征

### B. Foundations

- Colors
- Typography
- Spacing / Radius / Shadow / Motion

### C. Semantic Tokens

- 给出推荐 token 名称
- 说明每类 token 的语义用途

### D. Component Families

- 列出建议沉淀的组件族
- 说明每个组件族的视觉基线与禁忌

### E. Patterns

- 列出 2 到 5 个可复用的 section pattern
- 明确哪些 pattern 不能直接照搬参考站布局

### F. Guardrails for AI

- 写出适合放进 `CLAUDE.md` 或 Cursor Rule 的关键约束

### G. Originality Check

- 说明为了避免像参考网页，你建议至少刻意改变的 3 个维度

## 额外要求

- 如果发现参考源之间风格冲突，请指出冲突并给出取舍建议
- 如果发现某些模式只适合单一品牌，请明确标记“不要进入设计系统”
- 输出结果必须足够具体，能直接填进设计系统目录模板
```
