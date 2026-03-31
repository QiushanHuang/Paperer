---
name: paper-package-runner
description: Use when a readable paper PDF needs a portable entry workflow that can bootstrap the Paperer skills on a fresh machine, collect the minimum required inputs, and route the run through literature-summary and paper-asset-extraction.
---

# Paper Package Runner

## Overview

Use this as the primary entry skill for generating a paper package from a readable paper PDF.

Core principle: ask only for the truly blocking input, default the rest safely, and route the run through the existing production skills instead of duplicating their logic.

## When to Use

Use this skill when:

- the user wants the fastest normal path for processing a paper PDF
- the user may be on a fresh machine or outside the `Paperer` workspace
- the user should not need to remember which production skill to call first
- the user wants one portable prompt that can be reused across machines

Do not use this skill when:

- the task is repo-maintainer rebuild or regression work
- the user explicitly wants to work from `scripts/rebuild_<slug>_bundle.py`
- the input is not a readable paper PDF

## Required Input

- `paper_pdf_path`

Optional:

- `target_language`
- `paper_slug`
- `output_root`
- `user_reading_focus`

## Fast Preflight

Before asking the user anything beyond the PDF path:

1. Check whether the current environment already has the `Paperer` production skills available:
   - `paper-package-runner`
   - `literature-summary`
   - `paper-asset-extraction`
2. If the skills are already available, do not fetch the repo again.
3. If the skills are not available, first obtain the `Paperer` repo or its skill package from:
   - `https://github.com/QiushanHuang/Paperer.git`
4. Do not send the user into repo-maintainer flows such as:
   - `examples/papers/*`
   - `scripts/rebuild_<slug>_bundle.py`
   - `scripts/validate_paper_bundle.py`

The intended fast path is:

1. ensure the production skills are available
2. collect `paper_pdf_path`
3. default `target_language` to `Chinese` unless the user explicitly asks for another language
4. derive the rest unless the user asks for overrides
5. run the package generation flow

## Intake Rules

- If `paper_pdf_path` is missing, ask for it.
- If `target_language` is missing, default it to `Chinese`.
- If `paper_slug` is missing, derive it from the PDF filename.
- If `output_root` is missing, default to `output/papers/<paper-slug>/`.
- If `user_reading_focus` is missing, continue without it.

Do not ask the user for:

- `target_language` when the user has not requested a different language
- `paper_slug` when it can be derived safely
- `output_root` when the default path is acceptable
- repo-maintainer validation preferences during a normal user run

## Invocation Contract

After preflight and intake:

1. Call `literature-summary` as the main production skill.
2. Require `literature-summary` to prefer `paper-asset-extraction` as the visual-asset pipeline.
3. Let `literature-summary` produce the final paper package under:
   - `output/papers/<paper-slug>/`
4. Return:
   - the output directory path
   - the path to `summary.md`
   - the path to `report.json`
   - the path to `manifest.json` when present
   - the final status: `complete`, `partial`, or `failed`

## Production Flow

The production flow should be treated as:

```text
paper-package-runner
  -> literature-summary
     -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```

The wrapper must stay thin.

It must not:

- rewrite the summary itself
- extract figures, tables, or formulas itself
- redefine the output schema already owned by `literature-summary`

## Quick Reference

- Primary entry skill: `paper-package-runner`
- Main brief-writing skill: `literature-summary`
- Preferred visual-asset skill: `paper-asset-extraction`
- Required user input: `paper_pdf_path`
- Defaulted by the skill: `target_language=Chinese`
- Derived by default: `paper_slug`, `output_root`
- Default output path: `output/papers/<paper-slug>/`
- Fresh machine rule: fetch `Paperer` skills first if they are not already available
- Built-in return contract: output directory, `summary.md`, `report.json`, `manifest.json` when present, and final status

## Common Mistakes

| Mistake | Correction |
|--------|------------|
| Asking the user for every optional field up front | Ask only for `paper_pdf_path`; default `target_language` to `Chinese` and derive the rest unless overrides are needed. |
| Starting normal usage from rebuild scripts | Rebuild scripts are for repo-maintainer testing, not the production entry path. |
| Assuming the `Paperer` skills are already available on a fresh machine | First obtain the `Paperer` repo or its skill package when the production skills are missing. |
| Calling `paper-asset-extraction` as the only user-facing step | Use `paper-package-runner` as the entry and let `literature-summary` orchestrate the final package. |
| Re-implementing summary or extraction logic in the wrapper | Keep this skill thin and delegate all core work to the existing production skills. |
