# Paperer

`Paperer` 是一个面向论文简报生成的 skill-first 仓库。它的目标不是只做 abstract summary，而是把一篇 **readable research PDF** 组织成一份可读、可复查、可继续 slide 化的论文简报 package。

> **English summary**  
> `Paperer` is a skill-first repository for turning readable research PDFs into polished literature briefs with structured visual assets. The main skills are `literature-summary` and `paper-asset-extraction`.

## Repository Role

| Item | Value |
|------|-------|
| Source of truth | `Paperer` |
| Mirror repo | `slidegen` |
| Sync direction | `Paperer -> slidegen` |

## What This Repo Contains

This repo contains three different layers. They serve different purposes and should not be confused.

| Layer | What it is | Used in actual paper runs | Used in repo testing |
|------|------------|---------------------------|----------------------|
| Skills | Reusable behavior contracts | Yes | Yes |
| Example inputs | Real PDF files committed for repeatable checks | No | Yes |
| Rebuild / validation scripts | Repo-maintainer utilities for reproducing example outputs | No | Yes |

## Unified Naming

This repo now uses **paper package** as the unified term.

### `paper package`

A `paper package` is the full output directory for one paper:

```text
output/papers/<paper-slug>/
```

It contains the source PDF copy, extracted text, visual assets, the final summary, and the status report.

Older notes may still say `bundle`. In this repo, `bundle` and `paper package` refer to the same thing, but **`paper package` is now the preferred name**.

Some existing script filenames still use `bundle` for backward compatibility. The naming rule above is about repo terminology, not a forced rename of every existing file.

### `example paper package`

An `example paper package` is a committed, reproducible sample under `output/papers/<paper-slug>/` that exists for validation and regression checking.

Examples in this repo:

- `tan2026`
- `219qiushan`
- `simulating-particle-dispersions-in-nematic-liquid-crystal-solvents`

### `runtime paper package`

A `runtime paper package` is what the agent produces when you actually run the skill on a real paper path.

In other words:

- `example paper package` = repo-maintainer test artifact
- `runtime paper package` = actual output of a real skill run

The directory shape is the same. The difference is **why it exists**.

## Core Skills

| Skill | Role | Used directly by user | Main outputs |
|------|------|-----------------------|--------------|
| [`literature-summary`](skills/literature-summary/SKILL.md) | Main paper-brief generation skill | Yes | `summary.md`, `report.json`, header image, extracted text |
| [`paper-asset-extraction`](skills/paper-asset-extraction/SKILL.md) | Conservative figure / table / formula extraction skill | Usually called by `literature-summary` first | `manifest.json`, `assets/figures/*`, `assets/tables/*`, `assets/formulas/*`, `asset-extraction-report.json` |

## Repo Utilities

These are **not skills**. They are repo-maintainer utilities for example regeneration and validation.

| File | Type | Purpose |
|------|------|---------|
| [`scripts/rebuild_tan2026_bundle.py`](scripts/rebuild_tan2026_bundle.py) | rebuild script | Rebuild the `tan2026` example paper package |
| [`scripts/rebuild_219qiushan_bundle.py`](scripts/rebuild_219qiushan_bundle.py) | rebuild script | Rebuild the `219qiushan` example paper package |
| [`scripts/rebuild_simulating_bundle.py`](scripts/rebuild_simulating_bundle.py) | rebuild script | Rebuild the `simulating` example paper package |
| [`scripts/validate_paper_bundle.py`](scripts/validate_paper_bundle.py) | validator | Check whether a paper package matches repo rules |
| [`logs/fix-logs/`](logs/fix-logs/) | fix history | Record what was fixed, why, and how it was verified |

## Preview

The preview below uses the committed **example paper package** for `tan2026`.

- Example source PDF: [`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)
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

This example demonstrates:

- readable PDF -> extracted text
- header crop generation
- conservative figure / table / formula extraction
- manifest-driven visual audit
- polished Chinese literature brief

## Actual Flow Vs Test Flow

### Actual Flow

This is the flow you care about when you want the agent to process a new paper.

```text
Your paper PDF
  -> literature-summary
     -> paper-asset-extraction (preferred visual pipeline)
  -> output/papers/<paper-slug>/
     -> summary.md
     -> report.json
     -> manifest.json
     -> extracted/*
     -> assets/*
```

Characteristics:

- user-facing
- skill-driven
- meant for real papers
- does not require rebuild scripts

### Test Flow

This is the flow the repo maintainer uses to keep committed examples reproducible.

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
  -> logs/fix-logs/*.md
```

Characteristics:

- repo-maintainer-facing
- script-driven
- meant for regression checks and examples
- not the recommended way for normal end-user runs

## How The Actual Skill Run Works

### Step 1: Input

Provide:

- one readable paper PDF
- `target_language`
- optionally a stable `paper_slug`
- optionally a reading focus

### Step 2: Main entry is `literature-summary`

The normal entry point is [`skills/literature-summary/SKILL.md`](skills/literature-summary/SKILL.md).

It is responsible for the final paper brief and the final package shape.

### Step 3: `literature-summary` prefers `paper-asset-extraction`

Before writing the summary, the main skill should call [`skills/paper-asset-extraction/SKILL.md`](skills/paper-asset-extraction/SKILL.md) as the preferred visual pipeline.

That skill produces:

- `assets/figures/*`
- `assets/tables/*`
- `assets/formulas/*`
- `manifest.json`
- `extracted/asset-extraction-report.json`

### Step 4: `literature-summary` completes the package

The main skill then completes the rest of the paper package:

- `assets/header/paper-header.png`
- `extracted/fulltext.md`
- `extracted/metadata.json`
- `extracted/errors.json`
- `summary.md`
- `report.json`

### Step 5: Final output

A complete or partial paper package is written to:

```text
output/papers/<paper-slug>/
```

## Output File Guide

| File | Produced by | Purpose |
|------|-------------|---------|
| `source.pdf` | runtime assembly or rebuild script | The source paper copied into the package |
| `assets/header/paper-header.png` | `literature-summary` | Header image for the title block |
| `assets/figures/*` | `paper-asset-extraction` | Figure assets |
| `assets/tables/*` | `paper-asset-extraction` | Table assets |
| `assets/formulas/*` | `paper-asset-extraction` | Formula assets |
| `assets/pages/*` | rebuild/debug utilities | Full-page debug renders for review |
| `extracted/fulltext.md` | `literature-summary` | Extracted paper text |
| `extracted/metadata.json` | `literature-summary` | Paper metadata |
| `extracted/errors.json` | `literature-summary` | Text extraction issues |
| `extracted/asset-extraction-report.json` | `paper-asset-extraction` | Visual extraction report |
| `manifest.json` | `paper-asset-extraction` | Structured asset manifest and quality flags |
| `summary.md` | `literature-summary` | Final literature brief |
| `report.json` | `literature-summary` | Final package status and risk report |

## Package Structure

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

## Example Inputs

Committed example inputs live in [`examples/papers/`](examples/papers/):

- [`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)
- [`examples/papers/219qiushan.pdf`](examples/papers/219qiushan.pdf)
- [`examples/papers/Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`](examples/papers/Simulating%20Particle%20Dispersions%20in%20Nematic%20Liquid-Crystal%20Solvents.pdf)

These are **test inputs for reproducible repo examples**, not special files required by the skills themselves.

## Example Output Packages

Committed example output packages live in [`output/papers/`](output/papers/):

- [`output/papers/tan2026/`](output/papers/tan2026/)
- [`output/papers/219qiushan/`](output/papers/219qiushan/)
- [`output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/)

These are **example paper packages used for testing and regression review**.

## How To Use The Skill In Practice

### If you are working inside this repo

You do not need a separate install step for the repo-local skills. Ask the agent to use:

- `literature-summary`
- `paper-asset-extraction`

The recommended pattern is:

1. start from `literature-summary`
2. let it call `paper-asset-extraction` first for visual assets
3. write the final package under `output/papers/<paper-slug>/`

### Copyable Prompt

Use the prompt below as a starting point when you want the agent to process a real PDF path.

```text
Use the `literature-summary` skill to generate a complete paper package for the PDF at `/absolute/path/to/your-paper.pdf`.

Requirements:
- target_language: Chinese
- paper_slug: replace-this-with-your-slug
- use `paper-asset-extraction` as the preferred visual-asset pipeline
- write the output to `output/papers/replace-this-with-your-slug/`
- the displayed page title must be the Chinese translation of the paper's English title
- embed the header image and every extracted figure, table, and formula directly in `summary.md`
- keep the summary focused on the paper itself, not the extraction process
- write `summary.md`, `report.json`, `manifest.json`, `extracted/fulltext.md`, `extracted/metadata.json`, `extracted/errors.json`, and `extracted/asset-extraction-report.json`
- if evidence is incomplete, mark the package `partial` instead of inventing content
- run package validation if the validator is available

At the end, return:
- the output directory path
- the paths to `summary.md`, `report.json`, and `manifest.json`
- whether the final package is `complete`, `partial`, or `failed`
```

### Example With A Real Path

```text
Use the `literature-summary` skill to generate a complete paper package for the PDF at `/Users/joshua/Downloads/219qiushan.pdf`.

Requirements:
- target_language: Chinese
- paper_slug: 219qiushan
- use `paper-asset-extraction` as the preferred visual-asset pipeline
- write the output to `output/papers/219qiushan/`
- the displayed page title must be the Chinese translation of the paper's English title
- embed the header image and every extracted figure, table, and formula directly in `summary.md`
- keep the summary focused on the paper itself, not the extraction process
- write `summary.md`, `report.json`, `manifest.json`, `extracted/fulltext.md`, `extracted/metadata.json`, `extracted/errors.json`, and `extracted/asset-extraction-report.json`
- if evidence is incomplete, mark the package `partial` instead of inventing content
- run package validation if the validator is available

At the end, return:
- the output directory path
- the paths to `summary.md`, `report.json`, and `manifest.json`
- whether the final package is `complete`, `partial`, or `failed`
```

## Quality Rules

The current contract expects:

- polished research-brief output, not note dumps
- explicit `complete / partial / failed` status
- manifest-driven visual asset handling
- conservative extraction for figures, tables, and formulas
- no process-side commentary inside `summary.md`
- header, figure, table, and formula assets embedded directly in the summary

## Repo Structure

```text
.
├── README.md
├── docs/
│   └── superpowers/specs/
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
│   ├── literature-summary/
│   └── paper-asset-extraction/
└── output/
    └── papers/
```

## Design References

- [`skills/literature-summary/SKILL.md`](skills/literature-summary/SKILL.md)
- [`skills/paper-asset-extraction/SKILL.md`](skills/paper-asset-extraction/SKILL.md)
- [`skills/literature-summary/references/summary-template.md`](skills/literature-summary/references/summary-template.md)
- [`skills/literature-summary/references/bundle-contract.md`](skills/literature-summary/references/bundle-contract.md)
- [`skills/literature-summary/references/failure-rules.md`](skills/literature-summary/references/failure-rules.md)
- [`skills/literature-summary/references/sync-policy.md`](skills/literature-summary/references/sync-policy.md)
- [`docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md`](docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md)
- [`docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md`](docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md)

## English Quick View

### What is production flow

- Start with `literature-summary`
- Prefer `paper-asset-extraction` for visuals
- Write a runtime paper package under `output/papers/<paper-slug>/`

### What is test flow

- Use committed PDFs in `examples/papers/`
- Rebuild example paper packages with `scripts/rebuild_<slug>_bundle.py`
- Validate them with `scripts/validate_paper_bundle.py`

### What should users actually run

- Use the skills
- Do not start from rebuild scripts unless you are maintaining repo examples

## Current Status

This repo currently includes:

- the first working version of `literature-summary`
- the first working version of `paper-asset-extraction`
- committed example paper inputs
- committed example paper packages
- validation and fix-log utilities
- a README that separates actual skill usage from repo testing workflow
