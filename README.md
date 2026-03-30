# Paperer

`Paperer` 是一个以论文整理与文献总结为核心的技能仓库。当前仓库的重点模块是 `literature-summary`：它面向**可读 PDF 论文**，输出**高质量、结构化、可切换目标语言**的文献综述 Markdown，并配套生成截图素材与显式错误报告。

该仓库同时作为源仓库使用，相关内容会镜像同步到 `slidegen`。

## 当前包含内容

### 1. 文献总结技能

路径：

- `skills/literature-summary/SKILL.md`
- `skills/literature-summary/references/*`
- `skills/literature-summary/agents/openai.yaml`

这个技能的目标是把一篇可读论文 PDF 整理成一份**专业研究简报**，而不是只生成摘要，也不是直接生成幻灯片。

核心约束：

- 输入为可读论文 PDF
- 输出语言由 `target_language` 指定
- 输出主文件为 `summary.md`
- 支持论文头图、图、表、公式截图整理
- 当提取不完整时，允许输出 `partial` 结果，但必须写出 `report.json`
- 不允许在缺失证据时强行编造内容

## 仓库结构

```text
.
├── README.md
├── docs/
│   └── superpowers/specs/
│       └── 2026-03-30-literature-summary-skill-design.md
├── skills/
│   └── literature-summary/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
│           ├── bundle-contract.md
│           ├── failure-rules.md
│           ├── summary-template.md
│           └── sync-policy.md
└── output/
    └── papers/
        └── simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/
            ├── source.pdf
            ├── summary.md
            ├── report.json
            ├── extracted/
            └── assets/
```

## 设计文档

技能设计文档位于：

- `docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md`

该文档定义了：

- 技能边界
- 输入输出契约
- bundle 结构
- 失败处理规则
- `Paperer -> slidegen` 的单向同步策略
- 改进后的文献综述格式

## 输出格式目标

`literature-summary` 的输出不是简陋笔记，而是**研究简报式**文献总结。当前格式重点覆盖：

- 论文概览
- 研究问题与动机
- 方法与创新
- 实验设计与证据
- 图表与公式解读
- 作者真正完成了什么
- 局限性与讨论
- 总结与启示

它强调：

- 深度理解优先
- 保留足够证据密度，便于后续转成 slides
- 技术部分尽量带页码 / 图号 / 表号 / 公式号锚点
- 不用打分式推荐，而用 prose 做判断

## 真实论文验证样例

当前仓库已经包含一篇真实论文的验证 bundle：

- `output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/source.pdf`
- `output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/summary.md`
- `output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/report.json`

该样例验证了：

- 从真实 PDF 提取正文
- 提取论文头图区块
- 提取关键图和关键公式截图
- 输出中文研究简报
- 在公式文本提取不完全时，正确降级为 `partial`，并在 `report.json` 中记录不确定性

## 如何使用这个技能

在支持技能调用的环境中，可以按如下方式使用：

1. 提供一篇可读论文 PDF
2. 指定 `target_language`
3. 调用 `$literature-summary`
4. 根据需要联动 PDF 提取 / 截图相关技能，先构建证据 bundle
5. 输出 `summary.md` 与 `report.json`

如果 PDF 是图片型扫描件、无法读出正文，或者截图提取严重缺失，则不应把结果伪装成完整输出。

## 同步关系

当前约定：

- `Paperer` 是源仓库
- `slidegen` 是镜像仓库
- 同步方向为 `Paperer -> slidegen`

也就是说，技能定义、参考文档与后续模块更新应优先在 `Paperer` 编写，再镜像到 `slidegen`。

## 当前状态

目前仓库已完成：

- `literature-summary` 技能初版
- 技能设计文档
- 一篇真实论文的验证样例

下一步更合适的工作通常是：

- 用第二篇论文继续做非中文目标语言测试
- 收紧图 / 表 / 公式检测规则
- 增加更稳定的提取与截图脚本
- 决定是否将验证 bundle 进一步适配为 `slidegen` 的直接输入
