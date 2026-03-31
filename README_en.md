# Paperer

For the Chinese version, see [README.md](README.md).

`Paperer` is a skill-first workflow for processing research papers. Its goal is not limited to abstract-level summarization. Instead, it turns a **readable research PDF** into a complete **paper package** that includes:

- `summary.md`
- `report.json`
- `manifest.json`
- extracted text
- header / figure / table / formula assets

## Human Entry vs Agent Entry

- Humans should start with this `README_en.md`
- Agents and installers should start with [SKILL_PACKAGE.md](SKILL_PACKAGE.md)
- The minimal distributable folder is [paperer-skill-package/](paperer-skill-package/)
- The public default entry skill is [`paperer`](skills/paperer/SKILL.md)

If the goal is simply to process a paper with the skills, do not start from maintainer docs and do not start by searching for `scripts/rebuild_*.py`.

## Core Skills

| Skill | Role |
|------|------|
| [`paperer`](skills/paperer/SKILL.md) | Public entry skill for short prompts and fresh agents |
| [`paper-package-runner`](skills/paper-package-runner/SKILL.md) | Thin orchestration skill behind `paperer` |
| [`literature-summary`](skills/literature-summary/SKILL.md) | Main brief-writing skill for `summary.md`, `report.json`, header image, and text extraction |
| [`paper-asset-extraction`](skills/paper-asset-extraction/SKILL.md) | Visual-asset extraction skill for `manifest.json` and figure/table/formula assets |

## Minimal Installation Rule

Normal users and fresh agents should obtain the minimal skill package, not the full repo.

- Minimal directory URL:
  - `https://github.com/QiushanHuang/Paperer/tree/main/paperer-skill-package`
- Expected local directory name:
  - `paperer-skill-package/`
- Default entry file:
  - `paperer-skill-package/skills/paperer/SKILL.md`

Only obtain the full repo if:

- you are doing repo-maintainer rebuild or regression work
- you need `scripts/rebuild_*.py` or `scripts/validate_paper_bundle.py`
- you are editing `Paperer` skills, docs, or committed examples

## Fastest New-Machine Path

If you want the fastest successful path on a new machine, use this flow:

1. Check whether the current workspace already has the `Paperer` skills
2. If not, obtain only `paperer-skill-package/`
3. Call `paperer`
4. Provide only the paper PDF path

The following defaults are already embedded in the skills:

- `target_language = Chinese`
- automatic `paper_slug` derivation
- default output path
- built-in return contract

## Minimal Copyable Prompt

```text
Check whether the current workspace already contains the `Paperer` skills. If not, install the minimal skill package from https://github.com/QiushanHuang/Paperer/tree/main/paperer-skill-package at `paperer-skill-package/`. Use Paperer skill to generate a paper package for the PDF at /absolute/path/to/your-paper.pdf.
```

That prompt is enough. The following are already embedded in the skill and do not need to be restated:

- default `target_language = Chinese`
- automatic `paper_slug` derivation
- default output root
- default invocation order
- default return fields

## Production Flow

The normal user-facing production flow is:

```text
paperer
  -> paper-package-runner
     -> literature-summary
        -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```

## Repo Test Flow

The following flow is only for repo-maintainer testing:

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
  -> logs/fix-logs/*.md
```

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
- [`examples/papers/Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`](examples/papers/Simulating%20Particle%20Dispersions%20in%20Nematic%20Liquid-Crystal%20Solvents.pdf)

These files are test inputs for repo reproducibility, not a required runtime location for normal users.

## Example Outputs

The committed example paper packages live in [`output/papers/`](output/papers/):

- [`output/papers/tan2026/`](output/papers/tan2026/)
- [`output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/`](output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents/)

These are committed example outputs for regression checking and review.

## Repo Utilities

These tools are not production skills. They are maintainer-facing rebuild and validation helpers.

| File | Purpose |
|------|---------|
| [`scripts/rebuild_tan2026_bundle.py`](scripts/rebuild_tan2026_bundle.py) | Rebuild the `tan2026` example package |
| [`scripts/rebuild_simulating_bundle.py`](scripts/rebuild_simulating_bundle.py) | Rebuild the `simulating` example package |
| [`scripts/validate_paper_bundle.py`](scripts/validate_paper_bundle.py) | Validate package structure and contract rules |
| [`logs/fix-logs/`](logs/fix-logs/) | Record repair and verification history |

## Repository Layout

```text
.
├── README.md
├── README_en.md
├── SKILL_PACKAGE.md
├── paperer-skill-package/
├── docs/
├── examples/
├── logs/
├── output/
├── scripts/
└── skills/
```
