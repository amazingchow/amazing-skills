# Design System Template

把这一套目录复制到具体项目中使用。

```text
design-system-template/
  foundations/
    colors/
      README.md
    typography/
      README.md
    spacing-radius-shadow-motion/
      README.md
  tokens/
    semantic/
      README.md
  components/
    README.md
  patterns/
    README.md
  prompts-rules/
    CLAUDE.template.md
    cursor-ui-design.mdc
  utils/
    FIGMA_MCP_SYSTEM_PROMPT.md
    UI_PROMPT_TEMPLATE.md
    REFERENCE_BOARD_CHECKLIST.md
    DEMO_BOARD_CHECKLIST.md
```

## 维护原则

- `foundations` 只写基础规律，不写业务组件
- `tokens/semantic` 只写语义，不写具体品牌色号昵称
- `components` 聚焦可复用 UI 单元
- `patterns` 聚焦 section 级布局和版式关系
- `prompts-rules` 只写给 AI 的行为约束
- `utils` 放流程模板、检查清单、复用 prompt

## 推荐命名

- 使用英文目录名，便于跨工具和跨团队复用
- 内容说明可用中文
- token 命名优先语义化，例如 `text/primary`、`surface/raised`、`border/subtle`
