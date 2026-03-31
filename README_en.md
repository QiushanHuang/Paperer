# Paperer

For the Chinese version, see [README.md](README.md).

`Paperer` is a skill-first workflow for processing research papers. Its goal is not limited to abstract-level summarization. Instead, it turns a **readable research PDF** into a complete **paper package** that includes:

- `summary.md`
- `report.json`
- `manifest.json`
- extracted text
- header / figure / table / formula assets

The recommended standard entry skill is:

- [`paper-package-runner`](skills/paper-package-runner/SKILL.md)

It is responsible for:

- fresh-machine bootstrap
- checking whether the `Paperer` skills are already available
- collecting the minimum required input
- defaulting `target_language = Chinese`
- deriving `paper_slug`
- defaulting the output path to `output/papers/<paper-slug>/`
- calling [`literature-summary`](skills/literature-summary/SKILL.md)
- requiring [`literature-summary`](skills/literature-summary/SKILL.md) to prefer [`paper-asset-extraction`](skills/paper-asset-extraction/SKILL.md)

## Repository Role

| Item | Value |
|------|-------|
| Source of truth | `Paperer` |
| Mirror repo | `slidegen` |
| Sync direction | `Paperer -> slidegen` |

## Core Skills

| Skill | Role |
|------|------|
| [`paper-package-runner`](skills/paper-package-runner/SKILL.md) | Standard entry skill for fresh-machine bootstrap, minimal intake, default derivation, and orchestration |
| [`literature-summary`](skills/literature-summary/SKILL.md) | Main brief-writing skill for `summary.md`, `report.json`, header image, and text extraction |
| [`paper-asset-extraction`](skills/paper-asset-extraction/SKILL.md) | Visual-asset extraction skill for `manifest.json` and figure/table/formula assets |

## Unified Naming

This repo uses **paper package** as the preferred term for the full output directory of one paper:

```text
output/papers/<paper-slug>/
```

It contains the source PDF, extracted artifacts, the final brief, and the status report.

Older notes may still say `bundle`. In this repo, `bundle` and `paper package` mean the same thing, but `paper package` is now the preferred term.

## Fastest New-Machine Path

If you want the fastest successful path on a new machine, use this flow:

1. Make sure the current workspace already has the `Paperer` skills; if not, fetch `https://github.com/QiushanHuang/Paperer.git`
2. Call `paper-package-runner`
3. Provide only the paper PDF path
4. Let the runner apply all built-in defaults and generate the paper package

The following defaults are embedded in the skill:

- `target_language = Chinese`
- automatic `paper_slug` derivation
- default output root
- default invocation order
- built-in return contract

## Minimal Copyable Prompt

You can now use only the following prompt:

```text
If the current workspace does not already contain the `Paperer` skills, first fetch the `Paperer` repository or otherwise make the repo-local skills available from:
https://github.com/QiushanHuang/Paperer.git

Then use the `paper-package-runner` skill from `Paperer` to generate a paper package for the PDF at `/absolute/path/to/your-paper.pdf`.
```

That prompt is enough. The following are already embedded in the skill and do not need to be restated:

- default `target_language = Chinese`
- automatic `paper_slug` derivation
- default output root
- default invocation order
- default return fields

## Real Example Prompt

```text
If the current workspace does not already contain the `Paperer` skills, first fetch the `Paperer` repository or otherwise make the repo-local skills available from:
https://github.com/QiushanHuang/Paperer.git

Then use the `paper-package-runner` skill from `Paperer` to generate a paper package for the PDF at `/Users/joshua/Downloads/219qiushan.pdf`.
```

## Production Flow

The normal user-facing production flow is:

```text
paper-package-runner
  -> literature-summary
     -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```

This flow is:

- user-facing
- skill-driven
- meant for real paper processing
- not dependent on rebuild scripts

## Repo Test Flow

The following flow is only for repo-maintainer testing:

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
  -> logs/fix-logs/*.md
```

In other words:

- normal users start from `paper-package-runner`
- maintainers start from `rebuild_*.py` and the validator

## Output File Guide

| File | Produced by | Purpose |
|------|-------------|---------|
| `source.pdf` | runtime assembly or rebuild script | Source PDF copy for the current paper package |
| `assets/header/paper-header.png` | `literature-summary` | Header image for the title block |
| `assets/figures/*` | `paper-asset-extraction` | Figure assets |
| `assets/tables/*` | `paper-asset-extraction` | Table assets |
| `assets/formulas/*` | `paper-asset-extraction` | Formula assets |
| `assets/pages/*` | rebuild/debug utilities | Full-page debug renders |
| `extracted/fulltext.md` | `literature-summary` | Extracted paper text |
| `extracted/metadata.json` | `literature-summary` | Paper metadata |
| `extracted/errors.json` | `literature-summary` | Text extraction issues |
| `extracted/asset-extraction-report.json` | `paper-asset-extraction` | Visual extraction report |
| `manifest.json` | `paper-asset-extraction` | Asset manifest and quality flags |
| `summary.md` | `literature-summary` | Final literature brief |
| `report.json` | `literature-summary` | Final package status and risk report |

## Paper Package Structure

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

## Example Preview

The current preview uses the committed `tan2026` example:

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

## Example Inputs

The repo-side test PDFs live in [`examples/papers/`](examples/papers/):

- [`examples/papers/Tan2026.pdf`](examples/papers/Tan2026.pdf)
- [`examples/papers/219qiushan.pdf`](examples/papers/219qiushan.pdf)
- [`examples/papers/Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`](examples/papers/Simulating%20Particle%20Dispersions%20in%20Nematic%20Liquid-Crystal%20Solvents.pdf)

These files are test inputs for repo reproducibility, not a required runtime location for normal users.

## Example Outputs

The committed example paper packages live in [`output/papers/`](output/papers/):

- [`output/papers/tan2026/`](output/papers/tan2026/)
- [`output/papers/219qiushan/`](output/papers/219qiushan/)
- [`output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/)

These are committed example outputs for regression checking and review.

## Repo Utilities

These tools are not production skills. They are maintainer-facing rebuild and validation helpers.

| File | Purpose |
|------|---------|
| [`scripts/rebuild_tan2026_bundle.py`](scripts/rebuild_tan2026_bundle.py) | Rebuild the `tan2026` example package |
| [`scripts/rebuild_219qiushan_bundle.py`](scripts/rebuild_219qiushan_bundle.py) | Rebuild the `219qiushan` example package |
| [`scripts/rebuild_simulating_bundle.py`](scripts/rebuild_simulating_bundle.py) | Rebuild the `simulating` example package |
| [`scripts/validate_paper_bundle.py`](scripts/validate_paper_bundle.py) | Validate package structure and contract rules |
| [`logs/fix-logs/`](logs/fix-logs/) | Record repair and verification history |

## Repository Layout

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

## Key References

- [`skills/paper-package-runner/SKILL.md`](skills/paper-package-runner/SKILL.md)
- [`skills/literature-summary/SKILL.md`](skills/literature-summary/SKILL.md)
- [`skills/paper-asset-extraction/SKILL.md`](skills/paper-asset-extraction/SKILL.md)
- [`skills/literature-summary/references/summary-template.md`](skills/literature-summary/references/summary-template.md)
- [`skills/literature-summary/references/bundle-contract.md`](skills/literature-summary/references/bundle-contract.md)
- [`skills/literature-summary/references/failure-rules.md`](skills/literature-summary/references/failure-rules.md)
- [`docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md`](docs/superpowers/specs/2026-03-30-literature-summary-skill-design.md)
- [`docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md`](docs/superpowers/specs/2026-03-30-paper-asset-extraction-skill-design.md)
- [`docs/superpowers/specs/2026-03-31-paper-package-runner-skill-design.md`](docs/superpowers/specs/2026-03-31-paper-package-runner-skill-design.md)

## Current Status

The repo now includes:

- `paper-package-runner` as the standard entry skill
- `literature-summary` as the main brief-writing skill
- `paper-asset-extraction` as the visual-asset extraction skill
- reproducible example inputs and example outputs
- a Chinese primary README and a separate English README
