# Paperer

## 中文简介

`Paperer` 是一套面向论文处理的 skill-first 工作流。它的目标不是只做 abstract summary，而是把一篇 **readable research PDF** 处理成一份完整的 **paper package**，其中包含：

- `summary.md`
- `report.json`
- `manifest.json`
- extracted text
- header / figure / table / formula assets

现在推荐的标准入口 skill 是：

- `paper-package-runner`

它会负责新电脑启动、关键参数补问、默认值推断，以及调用：

- `literature-summary`
- `paper-asset-extraction`

## English Introduction

`Paperer` is a skill-first workflow for turning a readable research PDF into a complete **paper package**, not just an abstract-level summary. A paper package contains the final literature brief, structured reports, extracted text, and visual assets for figures, tables, formulas, and the paper header.

The recommended primary entry skill is:

- `paper-package-runner`

It handles fresh-machine bootstrap, required-input intake, safe default generation, and the orchestration of:

- `literature-summary`
- `paper-asset-extraction`

## 仓库角色 / Repository Role

| 项目 / Item | 值 / Value |
|------|-------|
| 源仓库 / Source of truth | `Paperer` |
| 镜像仓库 / Mirror repo | `slidegen` |
| 同步方向 / Sync direction | `Paperer -> slidegen` |

## 核心技能 / Core Skills

| Skill | 中文说明 | English role |
|------|----------|--------------|
| [`paper-package-runner`](skills/paper-package-runner/SKILL.md) | 标准入口 skill，负责新电脑 bootstrap、最小参数采集、默认值推断和调用顺序 | Primary entry skill for fresh-machine bootstrap, minimal intake, default derivation, and orchestration |
| [`literature-summary`](skills/literature-summary/SKILL.md) | 主总结 skill，负责 `summary.md`、`report.json`、头图、文本提取 | Main brief-writing skill for `summary.md`, `report.json`, header image, and text extraction |
| [`paper-asset-extraction`](skills/paper-asset-extraction/SKILL.md) | 图表公式提取 skill，负责 `manifest.json` 和视觉资产 | Conservative visual-asset extraction skill for `manifest.json` and figure/table/formula assets |

## 统一术语 / Unified Naming

### 中文

本仓库统一使用 **paper package** 这个术语，表示一篇论文的完整输出目录：

```text
output/papers/<paper-slug>/
```

它包含源 PDF、副产物、最终总结和状态报告。

### English

This repo uses **paper package** as the preferred term for the full output directory of one paper:

```text
output/papers/<paper-slug>/
```

Older notes may still say `bundle`. In this repo, `bundle` and `paper package` mean the same thing, but `paper package` is now the preferred name.

## 新电脑最快路径 / Fastest New-Machine Path

### 中文

如果你在一台新电脑上，想最高效地用这套 skill 处理论文，推荐路径只有 4 步：

1. 确保当前工作区已经有 `Paperer` 的 skill；如果没有，先获取 `https://github.com/QiushanHuang/Paperer.git`
2. 调用 `paper-package-runner`
3. 只提供：
   - 论文 PDF 路径
   - `target_language`
4. 让 runner 自动：
   - 推断 `paper_slug`
   - 默认输出到 `output/papers/<paper-slug>/`
   - 调用 `literature-summary`
   - 让 `literature-summary` 优先调用 `paper-asset-extraction`

### English

On a fresh machine, the fastest normal path is:

1. Make sure the `Paperer` skills are available in the current workspace; if not, fetch `https://github.com/QiushanHuang/Paperer.git`
2. Call `paper-package-runner`
3. Provide only:
   - the paper PDF path
   - `target_language`
4. Let the runner:
   - derive `paper_slug`
   - default the output root to `output/papers/<paper-slug>/`
   - call `literature-summary`
   - require `literature-summary` to prefer `paper-asset-extraction`

## 可复制提示词（中文） / Copyable Prompt (Chinese)

```text
如果当前工作区还没有 `Paperer` 的 skills，请先获取 `Paperer` 仓库，或者先让这些 repo-local skills 在当前工作区可用：
https://github.com/QiushanHuang/Paperer.git

然后调用 `Paperer` 里的 `paper-package-runner` skill，对路径 `/absolute/path/to/your-paper.pdf` 的论文 PDF 生成一个 paper package。

要求：
- target_language: Chinese
- 如果缺少 `paper_slug`，就根据 PDF 文件名自动推断
- 如果缺少 `output_root`，就默认写到 `output/papers/<paper-slug>/`
- 让 `paper-package-runner` 调用 `literature-summary`
- 让 `literature-summary` 优先调用 `paper-asset-extraction`
- 在 `summary.md` 中直接嵌入 header image 以及所有提取到的 figure、table、formula
- summary 内容只聚焦论文本身，不讨论提取流程
- 如果证据不完整，就把 package 标记为 `partial`，不要编造内容

最后请返回：
- 输出目录路径
- `summary.md`、`report.json`、`manifest.json` 的路径
- 最终状态是 `complete`、`partial` 还是 `failed`
```

## Copyable Prompt (English) / 可复制提示词（英文）

```text
If the current workspace does not already contain the `Paperer` skills, first fetch the `Paperer` repository or otherwise make the repo-local skills available from:
https://github.com/QiushanHuang/Paperer.git

Then use the `paper-package-runner` skill from `Paperer` to generate a paper package for the PDF at `/absolute/path/to/your-paper.pdf`.

Requirements:
- target_language: English
- if `paper_slug` is missing, derive it from the PDF filename
- if `output_root` is missing, default to `output/papers/<paper-slug>/`
- have `paper-package-runner` call `literature-summary`
- have `literature-summary` prefer `paper-asset-extraction`
- embed the header image and every extracted figure, table, and formula directly in `summary.md`
- keep the summary focused on the paper itself, not the extraction process
- if evidence is incomplete, mark the package `partial` instead of inventing content

At the end, return:
- the output directory path
- the paths to `summary.md`, `report.json`, and `manifest.json`
- whether the final package is `complete`, `partial`, or `failed`
```

## 实例提示词 / Real Example Prompt

```text
如果当前工作区还没有 `Paperer` 的 skills，请先获取 `Paperer` 仓库，或者先让这些 repo-local skills 在当前工作区可用：
https://github.com/QiushanHuang/Paperer.git

然后调用 `Paperer` 里的 `paper-package-runner` skill，对路径 `/Users/joshua/Downloads/219qiushan.pdf` 的论文 PDF 生成一个 paper package。

要求：
- target_language: Chinese
- 如果缺少 `paper_slug`，就根据 PDF 文件名自动推断
- 如果缺少 `output_root`，就默认写到 `output/papers/<paper-slug>/`
- 让 `paper-package-runner` 调用 `literature-summary`
- 让 `literature-summary` 优先调用 `paper-asset-extraction`
- 在 `summary.md` 中直接嵌入 header image 以及所有提取到的 figure、table、formula
- summary 内容只聚焦论文本身，不讨论提取流程
- 如果证据不完整，就把 package 标记为 `partial`，不要编造内容

最后请返回：
- 输出目录路径
- `summary.md`、`report.json`、`manifest.json` 的路径
- 最终状态是 `complete`、`partial` 还是 `failed`
```

## 实际流程 / Production Flow

### 中文

正常用户的实际流程应当是：

```text
paper-package-runner
  -> literature-summary
     -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```

### English

The normal production flow is:

```text
paper-package-runner
  -> literature-summary
     -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```

## 仓库测试流程 / Repo Test Flow

### 中文

以下流程只给仓库维护者使用，不是普通用户的入口：

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
  -> logs/fix-logs/*.md
```

### English

The following flow is for repo-maintainer testing only, not for normal user runs:

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
  -> logs/fix-logs/*.md
```

## 输出文件说明 / Output File Guide

| File | Produced by | 用途 / Purpose |
|------|-------------|----------------|
| `source.pdf` | runtime assembly or rebuild script | 当前 paper package 对应的源 PDF / Source paper copy |
| `assets/header/paper-header.png` | `literature-summary` | 页面标题区头图 / Header image for the title block |
| `assets/figures/*` | `paper-asset-extraction` | figure 资产 / Figure assets |
| `assets/tables/*` | `paper-asset-extraction` | table 资产 / Table assets |
| `assets/formulas/*` | `paper-asset-extraction` | formula 资产 / Formula assets |
| `assets/pages/*` | rebuild/debug utilities | 调试整页图 / Full-page debug renders |
| `extracted/fulltext.md` | `literature-summary` | 正文提取文本 / Extracted paper text |
| `extracted/metadata.json` | `literature-summary` | 基础元数据 / Paper metadata |
| `extracted/errors.json` | `literature-summary` | 文本提取问题 / Text extraction issues |
| `extracted/asset-extraction-report.json` | `paper-asset-extraction` | 图表公式提取报告 / Visual extraction report |
| `manifest.json` | `paper-asset-extraction` | 资产清单与质量标记 / Structured asset manifest and quality flags |
| `summary.md` | `literature-summary` | 最终论文简报 / Final literature brief |
| `report.json` | `literature-summary` | 最终状态与风险报告 / Final package status and risk report |

## Paper Package Structure / Paper Package 目录结构

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

## 样例预览 / Example Preview

当前 README 的预览使用仓库内置样例 `tan2026`：

- Example input PDF: [`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)
- Example output package: [`output/papers/tan2026/`](output/papers/tan2026/)

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

## 样例输入 / Example Inputs

用于仓库测试的样例 PDF 在 [`examples/papers/`](examples/papers/)：

- [`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)
- [`examples/papers/219qiushan.pdf`](examples/papers/219qiushan.pdf)
- [`examples/papers/Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`](examples/papers/Simulating%20Particle%20Dispersions%20in%20Nematic%20Liquid-Crystal%20Solvents.pdf)

These files are reproducible repo-side test inputs, not a required runtime location for normal users.

## 样例输出 / Example Output Packages

当前提交的 example paper packages 在 [`output/papers/`](output/papers/)：

- [`output/papers/tan2026/`](output/papers/tan2026/)
- [`output/papers/219qiushan/`](output/papers/219qiushan/)
- [`output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/)

These are committed example outputs for testing and regression review.

## 仓库维护工具 / Repo Utilities

这些工具不是技能本身，而是维护者使用的复现和验证工具。

These utilities are not production skills. They are maintainer-facing rebuild and validation helpers.

| File | 中文作用 | English purpose |
|------|----------|-----------------|
| [`scripts/rebuild_tan2026_bundle.py`](scripts/rebuild_tan2026_bundle.py) | 重建 `tan2026` 样例 package | Rebuild the `tan2026` example package |
| [`scripts/rebuild_219qiushan_bundle.py`](scripts/rebuild_219qiushan_bundle.py) | 重建 `219qiushan` 样例 package | Rebuild the `219qiushan` example package |
| [`scripts/rebuild_simulating_bundle.py`](scripts/rebuild_simulating_bundle.py) | 重建 `simulating` 样例 package | Rebuild the `simulating` example package |
| [`scripts/validate_paper_bundle.py`](scripts/validate_paper_bundle.py) | 校验 package 结构和约束 | Validate package structure and contract rules |
| [`logs/fix-logs/`](logs/fix-logs/) | 记录每轮修复与验证 | Record repair and verification history |

## 仓库结构 / Repository Layout

```text
.
├── README.md
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

## 关键文件 / Key References

- [`skills/paper-package-runner/SKILL.md`](skills/paper-package-runner/SKILL.md)
- [`skills/literature-summary/SKILL.md`](skills/literature-summary/SKILL.md)
- [`skills/paper-asset-extraction/SKILL.md`](skills/paper-asset-extraction/SKILL.md)
- [`skills/literature-summary/references/summary-template.md`](skills/literature-summary/references/summary-template.md)
- [`skills/literature-summary/references/bundle-contract.md`](skills/literature-summary/references/bundle-contract.md)
- [`skills/literature-summary/references/failure-rules.md`](skills/literature-summary/references/failure-rules.md)
- [`docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md`](docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md)
- [`docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md`](docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md)
- [`docs/superpowers/specs/2026-03-31-paper-package-runner-skill-design.md`](docs/superpowers/specs/2026-03-31-paper-package-runner-skill-design.md)

## 当前状态 / Current Status

### 中文

当前仓库已经具备：

- `paper-package-runner` 作为标准入口
- `literature-summary` 作为主总结 skill
- `paper-asset-extraction` 作为图表公式提取 skill
- 可复现的 example inputs 和 example outputs
- README 中英双语使用说明

### English

The repo now provides:

- `paper-package-runner` as the standard entry skill
- `literature-summary` as the main brief-writing skill
- `paper-asset-extraction` as the visual-asset extraction skill
- reproducible example inputs and example outputs
- a bilingual README for both fresh-machine onboarding and normal usage
