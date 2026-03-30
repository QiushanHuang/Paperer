---
title: Literature Summary Skill Design
date: 2026-03-30
status: approved-in-chat
source_repo: Paperer
mirror_repo: slidegen
---

# Literature Summary Skill Design

## 1. Summary

This document defines a pure skill for generating polished literature summaries from readable PDFs.

The skill is authored in `Paperer` and mirrored into `slidegen` as part of its module set. The skill itself does not own low-level PDF extraction or screenshotting. Instead, it orchestrates existing PDF-related skills or online skills that can:

- read a text-extractable PDF
- capture the paper header region
- extract screenshots for figures, tables, and formulas

The skill then normalizes those inputs, applies a strict literature-summary contract, and produces a polished Markdown research brief in a user-specified target language.

## 2. Goals

- Accept one readable PDF as the source paper.
- Accept any user-specified target language.
- Produce a polished, publication-ready Markdown literature summary.
- Preserve enough structure and evidence density for later slide generation.
- Extract and organize screenshots for:
  - paper header
  - every detected figure
  - every detected table
  - every detected formula
- Produce partial output when extraction is incomplete.
- Emit an explicit machine-readable error/completeness report.
- Mirror the skill source from `Paperer` to `slidegen`.

## 3. Non-Goals

- Implement OCR, PDF parsing, or rendering internals inside this skill.
- Force bilingual output when the selected output language is not Chinese.
- Turn the Markdown summary directly into slides inside this skill.
- Use rating labels such as "strongly worth reading" or "not a priority".

## 4. Source Of Truth And Synchronization

### 4.1 Repositories

- Authoring repository: `https://github.com/QiushanHuang/Paperer.git`
- Mirror repository: `https://github.com/isPANN/slidegen.git`

### 4.2 Sync Rule

`Paperer` is the source of truth.

Synchronization is one-way:

`Paperer -> slidegen`

`slidegen` should not become an independent source of truth for mirrored files belonging to this skill.

### 4.3 What Gets Mirrored

The mirrored content should include the entire skill module and its supporting files, including:

- `SKILL.md`
- `agents/openai.yaml`
- `references/*`
- `assets/*`
- any module files added later that belong to this skill package

Generated paper bundles are runtime artifacts and should remain outside the skill source tree.

## 5. System Boundary

This is a pure orchestration skill with an explicit contract.

The skill is responsible for:

- receiving the paper input and target language
- coordinating upstream extraction and screenshotting skills
- validating extracted content
- applying the literature-summary format
- writing polished output
- writing explicit failure/completeness metadata

The skill is not responsible for:

- OCR fallback
- low-level PDF image segmentation
- screenshot rendering internals
- slide rendering

## 6. Input Contract

### 6.1 Required Inputs

- one readable PDF
- `target_language`

### 6.2 Optional Inputs

- stable paper slug or `paper_id`
- user notes or reading focus, if added in future

### 6.3 Upstream Extraction Requirements

Before the skill can generate the final summary, upstream PDF-related skills or tools must provide:

- extracted full text, as complete as possible
- paper metadata when available
- one screenshot covering the title, venue, authors, and affiliations area
- screenshots for every figure that can be detected
- screenshots for every table that can be detected
- screenshots for every formula that can be detected
- extraction issues and failures when content is missing or unreadable

## 7. Normalized Bundle Contract

Upstream results should be normalized into a stable paper bundle:

```text
paper-bundle/
  source.pdf
  extracted/
    fulltext.md
    metadata.json
    errors.json
  assets/
    header/
      paper-header.png
    figures/
      fig-001.png
      fig-002.png
    tables/
      table-001.png
      table-002.png
    formulas/
      formula-001.png
      formula-002.png
```

This skill then produces:

```text
paper-bundle/
  source.pdf
  summary.md
  report.json
  extracted/
  assets/
```

## 8. Output Requirements

### 8.1 Canonical Output

The canonical output is a polished `summary.md`.

This summary is a research brief first, not a slide deck outline. It should remain rich enough to support later slide extraction.

### 8.2 Language Behavior

- The output language follows `target_language`.
- The skill accepts any user-specified target language.
- If the selected language is not Chinese, the report should not retain Chinese section headings by default.
- Original paper metadata may remain in its original form when appropriate.

### 8.3 Quality Bar

The final report must be publication-ready rather than note-like.

Required quality properties:

- stable heading hierarchy
- fluent, professional academic prose in the selected language
- concise but informative section transitions
- polished screenshot placement
- clear captions and short explanations for images, tables, and formulas
- no placeholders such as `TBD`, `TODO`, or broken references
- partial outputs must still look intentional and finished

### 8.4 Machine-Readable Report

The skill must also write `report.json` containing:

- selected target language
- extraction completeness
- missing sections
- missing screenshots
- unreadable source regions
- whether output is full or partial
- explicit errors

## 9. Recommended Skill Layout

The authoring repository should organize the skill like this:

```text
skills/
  literature-summary/
    SKILL.md
    agents/
      openai.yaml
    references/
      summary-template.md
      bundle-contract.md
      failure-rules.md
      sync-policy.md
    assets/
      examples/
```

Generated paper bundles should live outside the skill definition, for example:

```text
output/papers/<paper-slug>/
```

## 10. Execution Flow

1. User provides a readable PDF and a `target_language`.
2. The skill invokes or depends on an existing PDF-reading and screenshotting capability.
3. Extracted text, metadata, and screenshots are normalized into the agreed paper bundle.
4. The skill validates completeness across:
   - full text
   - metadata
   - header screenshot
   - figures
   - tables
   - formulas
5. The skill writes a polished `summary.md` using the approved literature-summary format.
6. The skill writes `report.json` describing completeness and failures.
7. If extraction is partial, the skill still emits a clean partial summary plus explicit reporting.

## 11. Failure Handling

### 11.1 Required Behavior

- Do not hallucinate unsupported content.
- If extraction is partial, still generate a usable summary.
- Mark unsupported claims or missing evidence clearly.
- Keep the reader-facing summary separate from machine-readable errors.

### 11.2 Asset Failures

If a figure, table, or formula screenshot is missing:

- record the issue in `report.json`
- keep the Markdown section stable
- indicate the missing visual evidence cleanly in prose

### 11.3 Interpretation Limits

If a formula or visual cannot be interpreted reliably:

- avoid overclaiming
- explain the uncertainty
- preserve the document's polished style instead of exposing raw extraction noise

## 12. Evidence Anchoring Policy

The summary should remain editorial and readable, but technical sections should include evidence anchors when available.

Use anchors primarily in:

- method explanation
- experiment sections
- figure/table/formula interpretation

Possible anchors include:

- page numbers
- figure numbers
- table numbers
- equation numbers

Avoid cluttering the front summary with dense inline anchors.

## 13. Literature Summary Format

The report structure should follow this improved professional research-brief format.

### 页面标题

- 论文标题
- 期刊 / 会议名称
- 作者与单位
- 文献基本信息
- Header 截图
  - 截取论文标题、期刊名、作者、单位所在区域

### 一、论文概览

#### 1.1 论文定位

- 用一句话说明这篇论文在研究什么
- 说明它属于什么问题域、解决哪一类核心问题

#### 1.2 这篇论文为什么值得关注

- 这篇论文试图回答什么关键问题
- 它相对已有工作的潜在价值在哪里
- 为什么这项工作值得继续往下读

#### 1.3 核心结论速览

- 问题
- 方法
- 结果
- 贡献
- 用一小段自然语言串起来，不做机械罗列

### 二、研究问题与动机

#### 2.1 背景与痛点

- 研究背景是什么
- 现有方法的主要不足是什么
- 作者为什么认为这个问题值得解决

#### 2.2 研究问题

- 论文明确要解决的问题是什么
- 问题的边界和适用场景是什么
- 如果论文里有假设条件，要明确写出

#### 2.3 作者的研究目标

- 作者希望达到什么目标
- 评价成功的标准是什么

### 三、方法与创新

#### 3.1 整体方法框架

- 用一段完整的话解释方法框架，而不是只堆术语
- 说明输入、核心机制、输出分别是什么
- 必要时补充方法流程解释

#### 3.2 核心创新点

- 创新点 1
- 创新点 2
- 创新点 3
- 每一点都要回答“新在哪里，为什么重要”

#### 3.3 方法为什么可能有效

- 从机制层面解释作者的方法为什么能解决前述问题
- 如果论文提供理论动机或设计直觉，要吸收进去

### 四、实验设计与证据

#### 4.1 实验设置

- 数据集 / 任务 / 对比基线
- 评价指标
- 实验设置中最关键的部分

#### 4.2 关键结果

- 作者最重要的结果是什么
- 哪些结果真正支撑了核心论点
- 这里开始适度加入证据锚点，如页码、图号、表号、公式号

#### 4.3 证据是否充分

- 结果是否和结论匹配
- 有哪些证据特别强
- 有哪些地方论证还不够充分

### 五、图表与公式解读

#### 5.1 图片解读

- 逐一放入检测到的图片截图
- 每张图说明它展示了什么
- 解释它在论文论证链条中的作用

#### 5.2 表格解读

- 逐一放入检测到的表格截图
- 每张表说明比较对象、关键指标、最值得注意的结果
- 避免重复抄表，只解释其意义

#### 5.3 公式解读

- 逐一放入检测到的公式截图
- 说明公式的作用，而不是只转写符号
- 如果公式很多，优先解释核心公式及其变量含义
- 对无法可靠解释的公式要明确标注，不强行分析

### 六、作者真正完成了什么

#### 6.1 论文的实际贡献

- 这篇论文最终做成了什么
- 是提出了新方法、给出新证据、还是重新定义了问题
- 要区分“作者声称的贡献”和“从论文内容看真正成立的贡献”

#### 6.2 这项工作的价值判断

- 这项工作的学术价值或应用价值体现在哪里
- 哪些读者最可能从中受益
- 价值判断只用分析性 prose，不使用打分或评级

### 七、局限性与讨论

#### 7.1 论文的不足

- 方法上的限制
- 实验上的限制
- 适用范围上的限制
- 作者自己承认的不足与我们额外看到的问题都可以写

#### 7.2 可以进一步追问的问题

- 还有哪些关键问题没有被回答
- 哪些设定可能影响结论外推
- 后续研究可以沿什么方向推进

### 八、总结与启示

#### 8.1 这篇论文意味着什么

- 它对该方向意味着什么
- 它对研究实践或应用意味着什么

#### 8.2 一句话总结

- 用一句自然、准确、有判断力的话收束全文

## 14. Rationale For The Format

This format is preferred because it:

- supports deep understanding first
- remains reusable for slide generation later
- reads like a professional literature brief rather than a checklist dump
- separates problem, method, evidence, interpretation, limitations, and judgment clearly
- creates stable places for visual assets and explanations

## 15. Main Risks

- Output quality depends on upstream PDF extraction quality.
- Figure/table/formula detection may be inconsistent across papers.
- Formula explanation is especially vulnerable to partial extraction and ambiguous notation.
- Cross-repo mirroring can drift if the source-of-truth rule is not enforced.

## 16. Design Guardrails

- Treat upstream extraction as variable-quality input.
- Keep the normalized bundle contract explicit and stable.
- Favor polished partial output over brittle hard-fail behavior.
- Never let the summary pretend certainty where the source extraction is weak.
- Preserve the separation between skill source and runtime artifacts.
