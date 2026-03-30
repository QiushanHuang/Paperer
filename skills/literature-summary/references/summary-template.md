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
- In `1.3 核心结论速览`, allow multiple problem / method / result / contribution points when the paper clearly contains more than one.
- Treat the section bullets below as compact writing prompts: cover each point directly, but answer in polished prose rather than checklist fragments.

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

#### 1.1 论文定位

- 用一句话说明这篇论文在研究什么。
- 交代它属于什么问题域，在解决哪一类核心问题。

#### 1.2 这篇论文为什么值得关注

- 说明这篇论文试图回答什么关键问题。
- 说明它相对已有工作的潜在价值在哪里。
- 说明为什么这项工作值得继续往下读。

#### 1.3 核心结论速览

- 用一小段自然语言串起问题、方法、结果、贡献，不做机械罗列。
- 如果这四类信息里任何一类存在多个关键点，完整覆盖，不要为了整齐压缩成单点。

### 2. 研究问题与动机

#### 2.1 背景与痛点

- 说明研究背景是什么。
- 说明现有方法的主要不足是什么。
- 说明作者为什么认为这个问题值得解决。

#### 2.2 研究问题

- 明确论文要解决的问题是什么。
- 交代问题的边界和适用场景。
- 如果论文有前提假设或约束条件，要明确写出。

#### 2.3 作者的研究目标

- 说明作者希望达到什么目标。
- 说明评价成功的标准是什么。

### 3. 方法与创新

#### 3.1 整体方法框架

- 用一段完整的话解释方法框架，而不是堆术语。
- 交代输入、核心机制、输出分别是什么。
- 必要时补充方法流程解释。

#### 3.2 核心创新点

- 提炼出最关键的 1-3 个创新点。
- 每一点都要回答“新在哪里，为什么重要”。

#### 3.3 方法为什么可能有效

- 从机制层面解释作者的方法为什么能解决前述问题。
- 如果论文给出理论动机或设计直觉，要吸收进去。

### 4. 实验设计与证据

#### 4.1 实验设置

- 交代数据集 / 任务 / 对比基线。
- 交代评价指标。
- 点出实验设置里最关键的部分。

#### 4.2 关键结果

- 提炼作者最重要的结果是什么。
- 说明哪些结果真正支撑了核心论点。
- 这里开始适度加入页码、图号、表号、公式号等证据锚点。

#### 4.3 证据是否充分

- 判断结果是否和结论匹配。
- 点出哪些证据特别强。
- 点出哪些地方论证还不够充分。

### 5. 图表与公式解读

#### 5.1 图片解读

- 每张图先嵌入截图，再用完整句子解释。
- 解释这张图是什么、可以从中观察到什么、它在论文论证链条中承担什么作用。
- 不要只复述标题，也不要只描述画面。

#### 5.2 表格解读

- 每张表先嵌入截图，再用完整句子解释。
- 说明比较对象、关键指标、最值得注意的结果。
- 避免重复抄表，只解释其意义。

#### 5.3 公式解读

- 每个核心公式先嵌入截图，再用完整句子解释。
- 说明公式的作用，而不是只转写符号。
- 如果公式很多，优先解释核心公式及其变量含义。
- 对无法可靠解释的公式要明确标注，不强行分析。

Do not summarize extraction problems here. If the bundle has extraction uncertainty, keep that in `report.json` unless it materially changes what the paper itself can support.

### 6. 作者真正完成了什么

#### 6.1 论文的实际贡献

- 说明这篇论文最终做成了什么。
- 说明它是提出了新方法、给出新证据，还是重新定义了问题。
- 区分“作者声称的贡献”和“从论文内容看真正成立的贡献”。

#### 6.2 这项工作的价值判断

- 说明这项工作的学术价值或应用价值体现在哪里。
- 说明哪些读者最可能从中受益。
- 价值判断只用分析性 prose，不使用打分或评级。

### 7. 局限性与讨论

#### 7.1 论文的不足

- 分析方法上的限制。
- 分析实验上的限制。
- 分析适用范围上的限制。
- 作者自己承认的不足与从论文内容中额外看到的问题都可以写。

#### 7.2 可以进一步追问的问题

- 点出还有哪些关键问题没有被回答。
- 点出哪些设定可能影响结论外推。
- 点出后续研究可以沿什么方向推进。

### 8. 总结与启示

#### 8.1 这篇论文意味着什么

- 说明它对该方向意味着什么。
- 说明它对研究实践或应用意味着什么。

#### 8.2 一句话总结

- 用一句自然、准确、有判断力的话收束全文。

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
