# Literature Summary Template

Use this file for the final `summary.md` structure.

The headings must be localized to `target_language`. The Chinese labels below define the section logic, not a requirement to keep Chinese in non-Chinese output.

## Writing standard

- Write as a polished research brief, not as fragmented notes.
- Prefer short paragraphs over bullet dumps where explanation matters.
- Keep a stable heading hierarchy.
- Use evidence anchors mainly in technical sections.
- Avoid ratings. Make judgment in prose.
- When extraction is partial, keep the document polished and mark missing support clearly.
- Keep the prose focused on the paper itself. Do not discuss extraction strategy, crop quality, or other workflow-side details inside `summary.md`.
- Every header image, figure, table, and formula that exists in the bundle must be embedded visibly inside `summary.md`.
- After `summary.md` is written, render a simple `draft.pdf` from it for quick review.
- In `1.3 核心结论速览`, allow multiple problem / method / result / contribution points when the paper clearly contains more than one.

## Recommended structure

### Page Title

Include:

- paper title
- venue or journal
- authors and affiliations
- basic citation metadata
- header screenshot covering title, venue, authors, and affiliations

The header screenshot must be embedded directly in the Markdown, not only described in text.

### 1. 论文概览

Cover:

- 论文定位
- 这篇论文为什么值得关注
- 核心结论速览

This section should help the reader understand what the paper is about and why it matters before going technical.

### 2. 研究问题与动机

Cover:

- 背景与痛点
- 研究问题
- 作者的研究目标

Explain what gap or pain point motivated the work and what the paper is trying to solve.

### 3. 方法与创新

Cover:

- 整体方法框架
- 核心创新点
- 方法为什么可能有效

Explain the method as a coherent mechanism. Do not just restate keywords.

### 4. 实验设计与证据

Cover:

- 实验设置
- 关键结果
- 证据是否充分

Use page, figure, table, or equation anchors here when available.

### 5. 图表与公式解读

Cover:

- 图片解读
- 表格解读
- 公式解读

For each asset:

- place the screenshot
- explain it in complete sentences that answer three questions naturally:
  - what it is
  - what can be observed from it
  - what it shows for the paper's argument

Avoid raw repetition of table values or equations unless needed to explain meaning.
Do not summarize extraction problems here. If the bundle has extraction uncertainty, keep that in `report.json` unless it materially changes what the paper itself can support.

### 6. 作者真正完成了什么

Cover:

- 论文的实际贡献
- 这项工作的价值判断

Separate:

- what the authors claim
- what the paper actually supports

### 7. 局限性与讨论

Cover:

- 论文的不足
- 可以进一步追问的问题

Be analytical, not dismissive.

### 8. 总结与启示

Cover:

- 这篇论文意味着什么
- 一句话总结

End with a strong closing sentence that is precise and defensible.

## Tone guide

Target tone:

- professional
- academic
- concise
- confident only where supported

Avoid:

- checklist-like phrasing
- filler translation
- exaggerated praise
- unsupported certainty
- commentary about your own extraction or rendering process
