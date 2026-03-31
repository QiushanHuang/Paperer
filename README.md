# Paperer

`Paperer` 是一个面向论文整理、文献总结与后续 slide 化处理的技能仓库。当前核心模块是 `literature-summary` 与 `paper-asset-extraction`：前者负责把**可读论文 PDF**整理成**高质量、结构化、可切换目标语言**的文献综述 Markdown，后者负责更保守地提取图、表、公式资产，并用 `manifest.json` 显式记录质量风险。

> **English summary**  
> `Paperer` is a skill-first repository for turning readable research PDFs into polished literature briefs. Its current core skills are `literature-summary` and `paper-asset-extraction`: one writes a language-switchable `summary.md`, and the other extracts conservative figure / table / formula assets with a `manifest.json` that makes uncertainty explicit.

当前同步约定：

- 源仓库：`Paperer`
- 镜像仓库：`slidegen`
- 同步方向：`Paperer -> slidegen`

## 项目亮点

- 面向**真实论文 PDF**，不是只处理 abstract。
- 输出是**研究简报式**文献总结，而不是粗糙笔记。
- 支持 `target_language`，不强制所有输出保留中文。
- 支持论文头图、关键图、表、公式等资产整理。
- 新增 `paper-asset-extraction`，专门处理图、表、公式分割中的漏割、多割与裁切过紧风险。
- 当提取不完整时，允许输出 `partial`，但必须同时写 `report.json`。
- 为后续 slide 生成保留足够的结构与证据密度。

## 样例预览

下面的图片全部来自仓库内置的真实论文验证样例：

- 论文：`Origin and evolution of the ore-forming fluids in the giant Dongping wolframite-quartz vein-type deposit in the Jiangnan Orogen, South China: fluid inclusions and H-O isotopic constraints`
- bundle 路径：[`output/papers/tan2026/`](output/papers/tan2026/)

### 论文头图区块

<img src="output/papers/tan2026/assets/header/paper-header.png" alt="paper header preview" width="100%">

### 图、表与公式预览

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
    <td align="center">Figure preview</td>
    <td align="center">Table preview</td>
    <td align="center">Formula preview</td>
  </tr>
</table>

这个样例已经验证了：

- 从真实 PDF 提取正文
- 生成论文头图截图
- 生成 figure、table 与 formula 资产
- 输出中文研究简报
- 生成 `manifest.json` 与结构化提取报告

## 仓库结构

```text
.
├── README.md
├── docs/
│   └── superpowers/specs/
│       ├── 2026-03-30-literature-summary-skill-design.md
│       └── 2026-03-30-paper-asset-extraction-skill-design.md
├── examples/
│   ├── README.md
│   └── papers/
│       ├── 219qiushan.pdf
│       ├── Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf
│       └── Tan2026.pdf
├── logs/
│   └── fix-logs/
│       └── *.md
├── scripts/
│   ├── rebuild_219qiushan_bundle.py
│   ├── rebuild_simulating_bundle.py
│   ├── rebuild_tan2026_bundle.py
│   └── validate_paper_bundle.py
├── skills/
│   ├── literature-summary/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   │       ├── bundle-contract.md
│   │       ├── failure-rules.md
│   │       ├── summary-template.md
│   │       └── sync-policy.md
│   └── paper-asset-extraction/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
│           ├── extraction-policy.md
│           ├── integration-contract.md
│           ├── manifest-schema.md
│           └── quality-flags.md
└── output/
    └── papers/
        └── <paper-slug>/
            ├── source.pdf
            ├── manifest.json
            ├── summary.md
            ├── report.json
            ├── extracted/
            └── assets/
```

关键文件：

- 技能定义：[`skills/literature-summary/SKILL.md`](skills/literature-summary/SKILL.md)
- 资产提取技能：[`skills/paper-asset-extraction/SKILL.md`](skills/paper-asset-extraction/SKILL.md)
- 输出模板：[`skills/literature-summary/references/summary-template.md`](skills/literature-summary/references/summary-template.md)
- bundle 契约：[`skills/literature-summary/references/bundle-contract.md`](skills/literature-summary/references/bundle-contract.md)
- 失败处理规则：[`skills/literature-summary/references/failure-rules.md`](skills/literature-summary/references/failure-rules.md)
- 同步策略：[`skills/literature-summary/references/sync-policy.md`](skills/literature-summary/references/sync-policy.md)
- 设计文档：[`docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md`](docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md)
- 资产提取设计文档：[`docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md`](docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md)
- 示例 PDF：[`examples/README.md`](examples/README.md)
- 重建脚本：[`scripts/`](scripts/)
- 修复日志：[`logs/fix-logs/`](logs/fix-logs/)

## 核心概念

### 什么是 bundle

`bundle` 是一篇论文在仓库里的**完整工作包**，路径固定为 `output/papers/<paper-slug>/`。

它的作用是把一篇论文从输入到输出的关键产物放在一起，便于：

- 复查这篇论文到底用了哪份源 PDF
- 查看正文提取、图表公式提取和最终总结是否一致
- 让后续 slide 生成或其他下游模块直接消费这些文件

一个 bundle 通常由两个 skill 共同完成：

- `paper-asset-extraction`
  - 负责图、表、公式资产，以及 `manifest.json`
- `literature-summary`
  - 负责 `summary.md`、`report.json`，并消费上面的资产与文本提取结果

bundle 的典型内容包括：

- `source.pdf`
  - 当前 bundle 对应的原论文 PDF
- `summary.md`
  - 面向阅读和后续 slide 化的论文简报主文件
- `report.json`
  - 记录这次输出是否 `complete / partial / failed`，以及缺失、风险和错误
- `manifest.json`
  - 图、表、公式的结构化清单，供主 skill 和下游模块消费
- `extracted/fulltext.md`
  - 提取出的正文文本
- `extracted/metadata.json`
  - 基础元数据，例如标题、页数、PDF 元数据
- `extracted/errors.json`
  - 文本提取阶段发现的错误和不确定项
- `extracted/asset-extraction-report.json`
  - 图、表、公式提取阶段的结构化报告
- `assets/header/*`
  - 页面标题区域头图
- `assets/figures/*`
  - figure 截图
- `assets/tables/*`
  - table 截图
- `assets/formulas/*`
  - formula 截图
- `assets/pages/*`
  - 调试用整页渲染图，便于复查截图来源

### 什么是重建脚本

`rebuild script` 是放在 `scripts/` 下的**仓库侧复现实验工具**，例如：

- `scripts/rebuild_tan2026_bundle.py`
- `scripts/rebuild_simulating_bundle.py`
- `scripts/rebuild_219qiushan_bundle.py`

它们的作用不是定义 skill 本身，而是：

- 用固定的 example PDF 重建一个完整 bundle
- 让仓库里的验证样例可以重复生成
- 让修复前后能对比输出是否改善

换句话说：

- `skill` 是运行契约和行为规则
- `rebuild script` 是为了仓库测试和样例复现而写的辅助代码

这些脚本通常会做下面几件事：

- 读取 `examples/papers/*.pdf`
- 生成 `source.pdf`
- 提取正文到 `extracted/fulltext.md`
- 生成头图、figure、table、formula、page 级图片
- 写 `manifest.json`
- 写 `report.json`
- 写 `summary.md`

### 什么是修复和验证

这里的 `修复` 和 `验证` 分成两层。

第一层是 skill 侧修复：

- `paper-asset-extraction`
  - 负责修复图、表、公式的漏割、多割、编号不连续、混合裁切、裁切过紧等问题
- `literature-summary`
  - 负责修复总结内容本身，例如遗漏关键结论、把流程信息写进正文、图片未嵌入 Markdown、解释不够完整等问题

第二层是仓库侧验证：

- `scripts/validate_paper_bundle.py`
  - 检查 bundle 结构是否完整
  - 检查 `summary.md` 是否嵌入了所有应嵌入的资产
  - 检查 `report.json` 是否含有关键字段
  - 检查 figure / table 编号是否连续且与文件名一致
  - 检查 summary 是否混入流程侧术语
- `logs/fix-logs/*.md`
  - 记录每一轮修复具体修了什么、为什么修、影响了哪些文件和样例

## 实际调用流程

如果之后是**实际调用 skill 来生成论文简报**，推荐把整个流程理解成下面几步。

### 1. 用户输入

用户提供：

- 一篇 readable paper PDF
- `target_language`
- 可选的 `paper_slug`

### 2. `literature-summary` 启动主流程

主入口通常是 `literature-summary`。

它负责组织整篇论文的最终输出，并优先调用 `paper-asset-extraction` 来处理视觉资产。

### 3. `paper-asset-extraction` 生成视觉资产

这个 skill 主要输出：

- `assets/figures/*`
- `assets/tables/*`
- `assets/formulas/*`
- `manifest.json`
- `extracted/asset-extraction-report.json`

这些文件的作用是：

- 给 `literature-summary` 提供可嵌入的视觉资产
- 给后续模块提供类型、页码、编号、质量标记等结构化信息

### 4. `literature-summary` 补全文本与头图，并写最终简报

这个 skill 继续生成：

- `assets/header/paper-header.png`
- `extracted/fulltext.md`
- `extracted/metadata.json`
- `extracted/errors.json`
- `summary.md`
- `report.json`

这些文件的作用是：

- `paper-header.png`
  - 用在页面标题区，展示标题、期刊、作者、单位
- `fulltext.md`
  - 为总结和证据定位提供正文材料
- `metadata.json`
  - 保存论文基础信息
- `errors.json`
  - 保存提取阶段的问题
- `summary.md`
  - 最终的论文简报主文件
- `report.json`
  - 最终的状态报告，说明这次输出是否完整、缺了什么、有哪些风险

### 5. 可选的仓库侧复现与验证

如果是在仓库里维护 example 或回归测试，而不是一次性运行 skill，就会额外用到：

- `scripts/rebuild_<slug>_bundle.py`
  - 重建指定 example 的 bundle
- `scripts/validate_paper_bundle.py`
  - 对 bundle 做规则检查
- `logs/fix-logs/*.md`
  - 记录这一轮修复和验证的历史

这里要区分清楚：

- end-user 视角，核心是两个 skill
- repo-maintainer 视角，还会用到 scripts 和 fix logs 来保证样例可复现、可验证

### 输出文件与职责一览

| File | Produced by | Purpose |
|------|-------------|---------|
| `source.pdf` | bundle assembly / rebuild script | 保存当前 bundle 对应的源 PDF |
| `assets/header/paper-header.png` | `literature-summary` pipeline | 页面标题区头图 |
| `assets/figures/*` | `paper-asset-extraction` | figure 资产 |
| `assets/tables/*` | `paper-asset-extraction` | table 资产 |
| `assets/formulas/*` | `paper-asset-extraction` | formula 资产 |
| `assets/pages/*` | rebuild / debug pipeline | 整页调试图，方便回看截图来源 |
| `extracted/fulltext.md` | `literature-summary` pipeline | 论文正文文本 |
| `extracted/metadata.json` | `literature-summary` pipeline | 论文元数据 |
| `extracted/errors.json` | `literature-summary` pipeline | 文本提取错误与不确定项 |
| `extracted/asset-extraction-report.json` | `paper-asset-extraction` | 视觉资产提取阶段的结构化报告 |
| `manifest.json` | `paper-asset-extraction` | 图表公式清单和质量标记 |
| `summary.md` | `literature-summary` | 最终论文简报 |
| `report.json` | `literature-summary` | 最终完成度与风险报告 |

## `literature-summary` 技能

这个技能的目标，是把一篇可读论文 PDF 整理成一份**专业研究简报**，而不是只生成摘要，也不是直接生成幻灯片。

### 输入

- 一篇可读论文 PDF
- `target_language`

可选：

- `paper_id` 或稳定 slug
- 用户关注重点

### 输出

主输出：

- `summary.md`

配套输出：

- `report.json`
- `manifest.json` when conservative asset extraction is used
- `extracted/fulltext.md`
- `extracted/metadata.json`
- `extracted/errors.json`
- `extracted/asset-extraction-report.json` when `paper-asset-extraction` is used
- `assets/header/*`
- `assets/figures/*`
- `assets/tables/*`
- `assets/formulas/*`

### 输出质量要求

- 必须是**研究简报式**文献总结，而不是 OCR 笔记堆砌
- 技术部分尽量带页码 / 图号 / 表号 / 公式号锚点
- 图、表、公式不能只贴图，必须有简短解释
- 不使用打分式推荐，而用 prose 做判断
- 如果证据不足，必须明确标记，而不能强行编造

## `paper-asset-extraction` 技能

这个技能专门负责论文里的图、表、公式资产提取，并把结果整理成主 skill 可消费的保守 bundle。

### 设计目标

- 漏割风险高于裁切偏大
- 多余边缘信息优于关键信息被截断
- 不依赖人工修正
- 用 `manifest.json` 显式暴露不确定性

### 主输出

- `assets/figures/*`
- `assets/tables/*`
- `assets/formulas/*`
- `manifest.json`
- `extracted/asset-extraction-report.json`

### 关键约束

- 优先保留完整视觉块，而不是追求过紧裁切
- 对疑似重复、疑似漏割、类型不确定的资产打质量标记
- 当资产集合明显不完整时返回 `partial`
- `literature-summary` 默认优先消费这个 skill 的输出

## 真实论文验证样例

当前仓库包含三篇真实论文的验证 bundle：

- `219qiushan`
  - PDF：[`source.pdf`](output/papers/219qiushan/source.pdf)
  - 总结：[`summary.md`](output/papers/219qiushan/summary.md)
  - 资产清单：[`manifest.json`](output/papers/219qiushan/manifest.json)
  - 报告：[`report.json`](output/papers/219qiushan/report.json)
  - 元数据：[`extracted/metadata.json`](output/papers/219qiushan/extracted/metadata.json)
  - 正文提取：[`extracted/fulltext.md`](output/papers/219qiushan/extracted/fulltext.md)

- `Tan2026`
  - PDF：[`source.pdf`](output/papers/tan2026/source.pdf)
  - 总结：[`summary.md`](output/papers/tan2026/summary.md)
  - 资产清单：[`manifest.json`](output/papers/tan2026/manifest.json)
  - 报告：[`report.json`](output/papers/tan2026/report.json)
  - 元数据：[`extracted/metadata.json`](output/papers/tan2026/extracted/metadata.json)
  - 正文提取：[`extracted/fulltext.md`](output/papers/tan2026/extracted/fulltext.md)
- `simulating-particle-dispersions-in-nematic-liquid-crystal-solvents`
  - PDF：[`source.pdf`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/source.pdf)
  - 总结：[`summary.md`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/summary.md)
  - 资产清单：[`manifest.json`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/manifest.json)
  - 报告：[`report.json`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/report.json)
  - 元数据：[`extracted/metadata.json`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/extracted/metadata.json)
  - 正文提取：[`extracted/fulltext.md`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/extracted/fulltext.md)

这三个样例一起覆盖了当前 skill contract 的关键路径：

- readable PDF -> extracted text
- extracted text + visual assets -> polished `summary.md`
- asset extraction -> explicit `manifest.json`
- partial or complete output -> explicit `report.json`

同时，仓库根目录下的 [`examples/`](examples/) 与 [`examples/papers/`](examples/papers/) 保存了当前用于复现实验的原始 PDF：

- [`examples/papers/219qiushan.pdf`](examples/papers/219qiushan.pdf)
- [`examples/papers/Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`](examples/papers/Simulating%20Particle%20Dispersions%20in%20Nematic%20Liquid-Crystal%20Solvents.pdf)
- [`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)

## 如何新增一篇论文 bundle

下面是当前仓库约定的新增流程。

### Step 1: 准备 PDF 与 slug

先准备一篇**可读** PDF，并为它确定稳定 slug。建议 slug 使用小写英文加连字符，例如：

```text
simulating-particle-dispersions-in-nematic-liquid-crystal-solvents
```

### Step 2: 创建 bundle 目录

在 `output/papers/<paper-slug>/` 下建立标准结构：

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
    ├── figures/
    ├── tables/
    ├── formulas/
    └── pages/
```

说明：

- `assets/tables/` 可以为空，但不能假装检测到了表格
- `assets/pages/` 是可选但推荐保留的调试产物，方便回看截图来源

### Step 3: 放入源 PDF

把原论文保存为：

```text
output/papers/<paper-slug>/source.pdf
```

### Step 4: 生成 `extracted/`

最少需要：

- `extracted/fulltext.md`
- `extracted/metadata.json`
- `extracted/errors.json`
- `manifest.json` when `paper-asset-extraction` is used
- `extracted/asset-extraction-report.json` when visual assets are extracted conservatively

建议：

- `fulltext.md` 按页保存文本，便于之后定位证据
- `metadata.json` 至少包含论文文件名、页数、基础 PDF metadata
- `errors.json` 用来记录提取缺失、不确定公式、截图失败等问题

### Step 5: 生成 `assets/`

应尽量生成：

- `assets/header/paper-header.png`
- `assets/figures/*.png`
- `assets/tables/*.png`
- `assets/formulas/*.png`

要求：

- header 图应覆盖标题、期刊 / 会议名、作者、单位等区域
- figure / table / formula 截图要尽量干净，不要带过多无关正文
- 如果某类资产没有可靠检测到，就保留空目录，并在错误报告中说明

### Step 6: 写 `summary.md`

`summary.md` 应遵守 `literature-summary` 的模板与质量要求：

- 以研究简报为目标
- 深度理解优先
- 技术部分尽量保留证据锚点
- 图、表、公式必须配解释
- 语言跟随 `target_language`
- 非中文目标语言时，不要强制保留中文章节标题

### Step 7: 写 `report.json`

`report.json` 至少应包含：

- `target_language`
- `status`
- `missing_sections`
- `missing_assets`
- `unreadable_regions`
- `asset_manifest_status`
- `notes`
- `errors`

推荐状态值：

- `complete`
- `partial`
- `failed`

### Step 8: 判断是否应标记为 `partial`

以下情况通常应该标记为 `partial`：

- 正文只提取到 abstract 或严重缺页
- 关键公式无法可靠读取
- figure / table / formula 截图缺失较多
- summary 中某些判断只能依据残缺证据得出

原则是：

**宁可输出高质量 partial，也不要伪装成 complete。**

## English Quick View

### What this repo does

`Paperer` stores a skill-first workflow for converting readable research PDFs into polished literature briefs with supporting visual assets.

### Key features

- Readable PDF to structured `summary.md`
- Language-switchable output via `target_language`
- Conservative figure / table / formula extraction with `manifest.json`
- Header / figure / table / formula asset organization
- Explicit completeness reporting through `report.json`
- Source-to-mirror workflow: `Paperer -> slidegen`

### Quick start

1. Prepare a readable paper PDF.
2. Choose a stable paper slug.
3. Run `$paper-asset-extraction` if you want conservative visual-asset extraction.
4. Provide `target_language`.
5. Run `$literature-summary`.
6. Review `summary.md`, `report.json`, `manifest.json`, and the generated assets.

## 同步规则

当前约定是：

- `Paperer` 是源仓库
- `slidegen` 是镜像仓库
- 技能定义与相关参考文档优先在 `Paperer` 编写
- 再镜像同步到 `slidegen`

也就是说，`slidegen` 不应成为这个 skill module 的独立 source of truth。

## 当前状态

目前仓库已经完成：

- `literature-summary` 技能初版
- `paper-asset-extraction` 技能初版
- 对应设计文档
- 三篇真实论文 PDF 示例
- 三篇真实论文的 bundle 验证样例
- README 升级版首页

下一步更合适的工作通常是：

- 用现有样例测试更多非中文目标语言路径
- 收紧图 / 表 / 公式检测规则
- 增加更稳定的提取与截图脚本
- 明确哪些 bundle 产物需要长期留在仓库中，哪些只作为验证样例
