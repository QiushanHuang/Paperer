---
title: Paper Asset Extraction Skill Design
date: 2026-03-30
status: approved-in-chat
source_repo: Paperer
mirror_repo: slidegen
---

# Paper Asset Extraction Skill Design

## 1. Summary

This document defines a new pure skill named `paper-asset-extraction`.

The skill is designed to extract figures, tables, and formulas from readable academic paper PDFs and produce a structured asset bundle for downstream consumption by `literature-summary`.

The design is intentionally skill-first rather than script-first. The skill does not introduce repository-local detection scripts. Instead, it orchestrates available PDF-reading, screenshotting, and visual extraction capabilities, then applies strict normalization, review, and quality-flagging rules.

The key requirement is conservative extraction:

- prefer a larger crop over a crop that misses content
- prefer preserving a questionable candidate over silently dropping a likely asset
- no manual repair loop

## 2. Goals

- Extract figure, table, and formula assets from readable paper PDFs.
- Produce a `manifest.json` that downstream skills can consume.
- Detect and surface extraction risks such as:
  - missed assets
  - duplicate assets
  - overly tight crops
  - oversized crops
  - uncertain classification
- Apply a second-pass review to reduce over-segmentation and obvious duplication.
- Integrate with `literature-summary` as the preferred asset pipeline.
- Support real-paper acceptance testing using `Tan2026.pdf`.

## 3. Non-Goals

- Implement OCR or image segmentation algorithms in repository-local scripts.
- Perform manual correction loops.
- Write the final literature summary.
- Replace all generic PDF or screenshot workflows; this skill is preferred, not mandatory.

## 4. Source Of Truth And Synchronization

### 4.1 Repositories

- Authoring repository: `https://github.com/QiushanHuang/Paperer.git`
- Mirror repository: `https://github.com/isPANN/slidegen.git`

### 4.2 Sync Rule

`Paperer` remains the source of truth.

Synchronization is one-way:

`Paperer -> slidegen`

The new extraction skill and any related reference files should be authored in `Paperer` and mirrored into `slidegen`.

## 5. New Skill Boundary

### 5.1 Skill Name

Recommended new skill name:

`paper-asset-extraction`

### 5.2 Responsibilities

The skill is responsible for:

- extracting candidate figure, table, and formula regions
- normalizing the results into a stable asset bundle
- running a second-pass review to reduce obvious segmentation errors
- producing `manifest.json`
- producing an extraction report suitable for downstream propagation

The skill is not responsible for:

- summary writing
- value judgment
- paper interpretation beyond lightweight labeling
- manual review workflows

### 5.3 Core Principle

The extraction policy must be conservative:

- missing content is worse than extra irrelevant margin
- low false negatives are more important than perfectly neat crops
- uncertainty must be surfaced, not hidden

## 6. Input Contract

### 6.1 Required Inputs

- one readable paper PDF

### 6.2 Optional Inputs

- `paper_slug`
- output root path

### 6.3 Default Policy

The skill should assume these defaults unless explicitly overridden:

- conservative cropping
- second-pass review enabled
- duplicate reduction enabled
- quality flags enabled

## 7. Output Contract

The skill should write:

```text
output/papers/<paper-slug>/
  assets/
    figures/
    tables/
    formulas/
  extracted/
    asset-extraction-report.json
  manifest.json
```

### 7.1 Expected Asset Directories

- `assets/figures/`
- `assets/tables/`
- `assets/formulas/`

### 7.2 Report Files

- `manifest.json`
- `extracted/asset-extraction-report.json`

`manifest.json` is the downstream integration contract.

`asset-extraction-report.json` is a process-facing extraction report with more operational detail.

## 8. `manifest.json` Contract

The manifest should include:

```json
{
  "paper_slug": "example-paper",
  "status": "complete",
  "policy": {
    "crop_bias": "prefer-larger-over-missing",
    "dedupe": true,
    "second_pass_review": true
  },
  "summary": {
    "figure_count": 3,
    "table_count": 1,
    "formula_count": 5
  },
  "assets": [
    {
      "id": "fig-001",
      "type": "figure",
      "page": 3,
      "path": "assets/figures/fig-001.png",
      "caption_hint": "FIG. 1",
      "quality_flags": []
    }
  ],
  "global_flags": []
}
```

### 8.1 Required Top-Level Fields

- `paper_slug`
- `status`
- `policy`
- `summary`
- `assets`
- `global_flags`

### 8.2 Required Per-Asset Fields

- `id`
- `type`
- `page`
- `path`
- `caption_hint`
- `quality_flags`

### 8.3 Status Values

- `complete`
- `partial`
- `failed`

## 9. Quality Flags

The skill should support at least these per-asset flags:

- `oversized_crop`
- `tight_crop_risk`
- `possible_duplicate`
- `possible_missed_sibling`
- `uncertain_type`
- `low_readability`

The skill should support at least these global flags:

- `possible_missing_figures`
- `possible_missing_tables`
- `possible_missing_formulas`
- `page_layout_ambiguous`
- `asset_set_incomplete`

## 10. Extraction Flow

The skill should use a fixed two-pass flow.

### 10.1 Pass 1: Candidate Collection

- collect all plausible figure candidates
- collect all plausible table candidates
- collect all plausible formula candidates
- prefer over-inclusive crops at this stage
- do not discard borderline candidates just because they include extra margin, caption text, or neighboring context

### 10.2 Pass 2: Review And Normalization

- classify each candidate
- merge obvious duplicates
- retain possible alternates when they may preserve otherwise missing content
- re-check for overly tight crops
- re-check for likely missed sibling panels or adjacent formula lines
- write normalized asset files and the final manifest

## 11. Conservative Cropping Rules

The skill must follow these ordering preferences:

- prefer `oversized_crop` over `tight_crop_risk`
- prefer `possible_duplicate` over `possible_missed_content`
- prefer `uncertain_type` over silent deletion
- prefer full content with extra margin over visually clean crops that cut off labels, legends, equation numbers, panel markers, rows, or columns

### 11.1 Figure Rule

Keep the full visual block and enough caption or labels to preserve interpretability.

Do not crop so tightly that:

- axes disappear
- legends disappear
- panel labels such as `(a)` or `(b)` disappear
- the figure body is truncated

### 11.2 Table Rule

Keep:

- full table body
- row and column structure
- visible headers when possible

If the table boundary is ambiguous, crop larger rather than clipping rows or columns.

### 11.3 Formula Rule

Keep:

- the full displayed formula
- nearby equation number when present
- neighboring lines when needed to avoid truncating a multiline equation

If a formula spans multiple lines, prefer treating it as one logical asset unless there is strong evidence otherwise.

## 12. Failure And Partial-Output Rules

This skill should treat partial success as valid.

### 12.1 Partial Conditions

Return `partial` when:

- a major asset class is likely incomplete
- important formulas are unreadable or fragmented
- likely sibling panels or related blocks were missed
- the remaining crops are usable only as rough references rather than strong evidence blocks

### 12.2 Failed Conditions

Return `failed` when:

- the PDF is unreadable for this workflow
- no meaningful asset set can be produced
- both classification and extraction confidence are too poor for downstream use

## 13. Integration With `literature-summary`

The main skill should treat `paper-asset-extraction` as its preferred asset pipeline.

Recommended call order:

1. receive readable PDF and `target_language`
2. try `paper-asset-extraction`
3. if successful, consume:
   - `assets/figures/*`
   - `assets/tables/*`
   - `assets/formulas/*`
   - `manifest.json`
   - `extracted/asset-extraction-report.json`
4. if unavailable or failed, fall back to the generic PDF / screenshot pipeline
5. continue summary generation

### 13.1 What `literature-summary` May Trust

It may trust:

- asset paths
- asset types
- page numbers
- quality flags
- global extraction warnings

It must not blindly trust that every asset is clean enough for strong interpretation.

### 13.2 Propagation Rules

The main skill should propagate extraction uncertainty into its own `report.json`.

Examples:

- `oversized_crop`: usually acceptable, low impact
- `tight_crop_risk`: use cautious explanation, may force `partial`
- `possible_missed_sibling`: indicate possible incomplete visual evidence
- `low_readability`: explain only at a high level
- `uncertain_type`: avoid strong interpretation

## 14. Test Strategy

The skill should be tested against real papers, not synthetic placeholders.

### 14.1 Known Failure Modes To Encode

- oversized crop
- tight crop
- over-segmentation
- under-segmentation / missing extraction
- duplicate extraction
- type confusion

### 14.2 Acceptance Criteria

The extraction is acceptable when:

- no major asset is obviously missing without being flagged
- no critical crop is so tight that key information is lost
- duplicates are removed or explicitly flagged
- ambiguous cases are preserved conservatively and labeled
- downstream `literature-summary` can consume the bundle without unsupported certainty

## 15. New Real-Paper Acceptance Case

Use this paper as the next real validation case:

`/Users/joshua/Desktop/Tan2026.pdf`

This paper should become a second bundle under:

```text
output/papers/<tan2026-slug>/
```

Expected contents:

- `source.pdf`
- `manifest.json`
- `summary.md`
- `report.json`
- `extracted/`
- `assets/figures/`
- `assets/tables/`
- `assets/formulas/`

## 16. Agent-Based End-To-End Validation

After implementation, validate the whole workflow with agents:

1. invoke `paper-asset-extraction` on `Tan2026.pdf`
2. inspect and validate the emitted asset bundle
3. invoke `literature-summary`
4. ensure it consumes the manifest-aware assets
5. verify that uncertainty propagates correctly into the final summary and `report.json`
6. commit the resulting bundle
7. mirror the commit to both `Paperer` and `slidegen`

## 17. Exact Repo Deliverables

### 17.1 New Skill

Create:

```text
skills/
  paper-asset-extraction/
    SKILL.md
    agents/
      openai.yaml
    references/
      extraction-policy.md
      manifest-schema.md
      quality-flags.md
      integration-contract.md
```

### 17.2 Main Skill Updates

Update:

```text
skills/literature-summary/SKILL.md
skills/literature-summary/references/bundle-contract.md
skills/literature-summary/references/failure-rules.md
```

### 17.3 Validation Outputs

Add a second real-paper validation bundle for `Tan2026.pdf`.

## 18. Risks

- As a pure skill, extraction quality still depends on the capabilities of upstream PDF and screenshot tools.
- Conservative cropping may produce noisier visual assets than ideal.
- Formula extraction remains a high-risk class because multiline or symbol-dense equations are easy to fragment.
- Real-paper layout diversity may require future refinement of quality flags and integration rules.

## 19. Guardrails

- Prefer conservative completeness over cosmetic neatness.
- Never hide uncertainty.
- Never silently drop likely assets.
- Keep the extraction-to-summary contract explicit and machine-readable.
- Keep `Paperer` as the source of truth for both skill definitions and validation artifacts.
