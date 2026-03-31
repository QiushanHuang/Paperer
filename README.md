# Paperer

英文版请见 [README_en.md](README_en.md)。

`Paperer` 是一套面向论文处理的 skill-first 工作流。它的目标不是只做 abstract summary，而是把一篇 **readable research PDF** 处理成一份完整的 **paper package**，其中包含：

- `summary.md`
- `report.json`
- `manifest.json`
- extracted text
- header / figure / table / formula assets

当前推荐的标准入口 skill 是：

- [`paper-package-runner`](skills/paper-package-runner/SKILL.md)

它会负责：

- 新电脑 bootstrap
- 自动检查 `Paperer` skills 是否已可用
- 收集最少必填信息
- 默认 `target_language = Chinese`
- 自动推断 `paper_slug`
- 默认输出到 `output/papers/<paper-slug>/`
- 调用 [`literature-summary`](skills/literature-summary/SKILL.md)
- 让 [`literature-summary`](skills/literature-summary/SKILL.md) 优先调用 [`paper-asset-extraction`](skills/paper-asset-extraction/SKILL.md)

## 仓库角色

| 项目 | 值 |
|------|----|
| 源仓库 | `Paperer` |
| 镜像仓库 | `slidegen` |
| 同步方向 | `Paperer -> slidegen` |

## 核心技能

| Skill | 作用 |
|------|------|
| [`paper-package-runner`](skills/paper-package-runner/SKILL.md) | 标准入口 skill，负责新电脑 bootstrap、最小参数采集、默认值推断和调用顺序 |
| [`literature-summary`](skills/literature-summary/SKILL.md) | 主总结 skill，负责 `summary.md`、`report.json`、头图、文本提取 |
| [`paper-asset-extraction`](skills/paper-asset-extraction/SKILL.md) | 图表公式提取 skill，负责 `manifest.json` 和视觉资产 |

## 统一术语

本仓库统一使用 **paper package** 这个术语，表示一篇论文的完整输出目录：

```text
output/papers/<paper-slug>/
```

它包含源 PDF、副产物、最终总结和状态报告。

旧文档里如果出现 `bundle`，在本仓库里与 `paper package` 是同义词，但现在统一优先使用 `paper package`。

## 新电脑最快路径

如果你在一台新电脑上，想最高效地用这套 skill 处理论文，推荐路径只有 4 步：

1. 确保当前工作区已经有 `Paperer` 的 skills；如果没有，先获取 `https://github.com/QiushanHuang/Paperer.git`
2. 调用 `paper-package-runner`
3. 只提供论文 PDF 路径
4. 让 runner 自动补全默认项并生成 paper package

默认行为已经内嵌在 skill 内：

- `target_language = Chinese`
- 自动推断 `paper_slug`
- 默认输出到 `output/papers/<paper-slug>/`
- 自动返回输出目录、`summary.md`、`report.json`、`manifest.json` 路径和最终状态

## 最简调用提示词

你现在可以只输入下面这段提示词就直接使用：

```text
If the current workspace does not already contain the `Paperer` skills, first fetch the `Paperer` repository or otherwise make the repo-local skills available from:
https://github.com/QiushanHuang/Paperer.git

Then use the `paper-package-runner` skill from `Paperer` to generate a paper package for the PDF at `/absolute/path/to/your-paper.pdf`.
```

上面这段提示词已经足够。下面这些默认行为都写进了 skill 里，不需要你再写：

- 默认 `target_language = Chinese`
- 自动推断 `paper_slug`
- 默认输出路径
- 默认调用顺序
- 默认返回结果字段

## 实际示例提示词

```text
If the current workspace does not already contain the `Paperer` skills, first fetch the `Paperer` repository or otherwise make the repo-local skills available from:
https://github.com/QiushanHuang/Paperer.git

Then use the `paper-package-runner` skill from `Paperer` to generate a paper package for the PDF at `/Users/joshua/Downloads/219qiushan.pdf`.
```

## 实际流程

普通用户的实际流程应当是：

```text
paper-package-runner
  -> literature-summary
     -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```

这个流程是：

- 用户入口
- skill 驱动
- 面向真实论文处理
- 不依赖 rebuild scripts

## 仓库测试流程

以下流程只给仓库维护者使用，不是普通用户的入口：

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
  -> logs/fix-logs/*.md
```

也就是说：

- 普通用户从 `paper-package-runner` 开始
- 维护者才从 `rebuild_*.py` 和 validator 开始

## 输出文件说明

| 文件 | Produced by | 用途 |
|------|-------------|------|
| `source.pdf` | runtime assembly or rebuild script | 当前 paper package 对应的源 PDF |
| `assets/header/paper-header.png` | `literature-summary` | 页面标题区头图 |
| `assets/figures/*` | `paper-asset-extraction` | figure 资产 |
| `assets/tables/*` | `paper-asset-extraction` | table 资产 |
| `assets/formulas/*` | `paper-asset-extraction` | formula 资产 |
| `assets/pages/*` | rebuild/debug utilities | 调试整页图 |
| `extracted/fulltext.md` | `literature-summary` | 正文提取文本 |
| `extracted/metadata.json` | `literature-summary` | 基础元数据 |
| `extracted/errors.json` | `literature-summary` | 文本提取问题 |
| `extracted/asset-extraction-report.json` | `paper-asset-extraction` | 图表公式提取报告 |
| `manifest.json` | `paper-asset-extraction` | 资产清单与质量标记 |
| `summary.md` | `literature-summary` | 最终论文简报 |
| `report.json` | `literature-summary` | 最终状态与风险报告 |

## Paper Package 目录结构

```text
output/papers/<paper-slug>/
├── source.pdf
├── manifest.json
├── summary.md
├── report.json
├── extracted/
│   ├── fulltext.md
│   ├── metadata.json
│   ├── errors.json
│   └── asset-extraction-report.json
└── assets/
    ├── header/
    │   └── paper-header.png
    ├── figures/
    ├── tables/
    ├── formulas/
    └── pages/
```

## 样例预览

当前 README 的预览使用仓库内置样例 `tan2026`：

- 样例输入 PDF：[`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)
- 样例输出 package：[`output/papers/tan2026/`](output/papers/tan2026/)

### Header Preview

<img src="output/papers/tan2026/assets/header/paper-header.png" alt="paper header preview" width="100%">

### Figure / Table / Formula Preview

<table>
  <tr>
    <td width="33%">
      <img src="output/papers/tan2026/assets/figures/fig-008.png" alt="figure preview" width="100%">
    </td>
    <td width="33%">
      <img src="output/papers/tan2026/assets/tables/table-001.png" alt="table preview" width="100%">
    </td>
    <td width="33%">
      <img src="output/papers/tan2026/assets/formulas/formula-001.png" alt="formula preview" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center">Figure</td>
    <td align="center">Table</td>
    <td align="center">Formula</td>
  </tr>
</table>

## 样例输入

用于仓库测试的样例 PDF 在 [`examples/papers/`](examples/papers/)：

- [`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)
- [`examples/papers/219qiushan.pdf`](examples/papers/219qiushan.pdf)
- [`examples/papers/Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`](examples/papers/Simulating%20Particle%20Dispersions%20in%20Nematic%20Liquid-Crystal%20Solvents.pdf)

这些文件是仓库测试输入，不是普通用户运行 skill 时必须使用的固定目录。

## 样例输出

当前提交的 example paper packages 在 [`output/papers/`](output/papers/)：

- [`output/papers/tan2026/`](output/papers/tan2026/)
- [`output/papers/219qiushan/`](output/papers/219qiushan/)
- [`output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/)

这些是提交到仓库里的测试样例输出，用于回归检查和结构复查。

## 仓库维护工具

这些工具不是 skill 本身，而是维护者使用的复现和验证工具。

| 文件 | 作用 |
|------|------|
| [`scripts/rebuild_tan2026_bundle.py`](scripts/rebuild_tan2026_bundle.py) | 重建 `tan2026` 样例 package |
| [`scripts/rebuild_219qiushan_bundle.py`](scripts/rebuild_219qiushan_bundle.py) | 重建 `219qiushan` 样例 package |
| [`scripts/rebuild_simulating_bundle.py`](scripts/rebuild_simulating_bundle.py) | 重建 `simulating` 样例 package |
| [`scripts/validate_paper_bundle.py`](scripts/validate_paper_bundle.py) | 校验 package 结构和约束 |
| [`logs/fix-logs/`](logs/fix-logs/) | 记录每轮修复与验证 |

## 仓库结构

```text
.
├── README.md
├── README_en.md
├── docs/
│   ├── superpowers/specs/
│   └── superpowers/plans/
├── examples/
│   ├── README.md
│   └── papers/
├── logs/
│   └── fix-logs/
├── scripts/
│   ├── rebuild_219qiushan_bundle.py
│   ├── rebuild_simulating_bundle.py
│   ├── rebuild_tan2026_bundle.py
│   └── validate_paper_bundle.py
├── skills/
│   ├── paper-package-runner/
│   ├── literature-summary/
│   └── paper-asset-extraction/
└── output/
    └── papers/
```

## 关键文件

- [`skills/paper-package-runner/SKILL.md`](skills/paper-package-runner/SKILL.md)
- [`skills/literature-summary/SKILL.md`](skills/literature-summary/SKILL.md)
- [`skills/paper-asset-extraction/SKILL.md`](skills/paper-asset-extraction/SKILL.md)
- [`skills/literature-summary/references/summary-template.md`](skills/literature-summary/references/summary-template.md)
- [`skills/literature-summary/references/bundle-contract.md`](skills/literature-summary/references/bundle-contract.md)
- [`skills/literature-summary/references/failure-rules.md`](skills/literature-summary/references/failure-rules.md)
- [`docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md`](docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md)
- [`docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md`](docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md)
- [`docs/superpowers/specs/2026-03-31-paper-package-runner-skill-design.md`](docs/superpowers/specs/2026-03-31-paper-package-runner-skill-design.md)

## 当前状态

当前仓库已经具备：

- `paper-package-runner` 作为标准入口
- `literature-summary` 作为主总结 skill
- `paper-asset-extraction` 作为图表公式提取 skill
- 可复现的 example inputs 和 example outputs
- 中文主 README 与单独英文版 README
