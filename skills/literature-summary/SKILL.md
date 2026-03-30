---
name: literature-summary
description: Use when a readable academic paper PDF needs to be turned into a polished literature brief in a user-specified language, especially when figures, tables, and formulas must be explained and missing extraction must be reported explicitly.
---

# Literature Summary

## Overview

Turn a readable paper PDF into a polished research brief.

Core principle: polished partial output is better than confident fabrication.

## When to Use

Use this skill when the user wants a structured literature summary from a readable paper PDF, in a specified language, with visual explanation blocks and explicit handling of missing extraction.

Do not use this skill when:

- the input is not a paper PDF
- the PDF is image-only or unreadable and no other extraction skill can recover it
- the user only wants a short abstract-level summary

## Required Inputs

- one readable PDF
- `target_language`

Optional:

- stable paper slug or paper id
- user reading focus

If `target_language` is missing, ask for it before writing.

## Workflow

1. Build the evidence bundle.
   Prefer installed PDF-reading and screenshotting skills. If `pdf` is available, use it for extraction and visual checks. Gather:
   - full extracted text
   - metadata when available
   - one header screenshot
   - every detectable figure, table, and formula screenshot

2. Validate the bundle against [references/bundle-contract.md](references/bundle-contract.md).

3. Read [references/summary-template.md](references/summary-template.md) and write `summary.md`.
   The output must:
   - follow the selected language
   - read like a professional research brief
   - explain visuals instead of dumping them
   - keep evidence anchors mainly in technical sections

4. Apply the failure rules from [references/failure-rules.md](references/failure-rules.md).

5. Write `report.json`.
   Record completeness, missing assets, unreadable regions, and explicit errors.

6. If this skill is being authored in `Paperer`, follow [references/sync-policy.md](references/sync-policy.md) for mirroring into `slidegen`.

## Quick Reference

- Output language follows `target_language`.
- Do not keep Chinese headings when the selected language is not Chinese.
- Do not use ratings; explain judgment in prose.
- Technical sections should include page, figure, table, or equation anchors when available.
- Every figure, table, and formula block needs a short explanation.
- Separate the authors' claimed contribution from the paper's supported contribution.
- If extraction is partial, still produce a clean summary and an explicit `report.json`.

## Final Checks

Before finishing, confirm:

- `summary.md` is polished rather than note-like
- section hierarchy is stable
- no placeholders or broken references remain
- every included visual has explanation text
- missing visuals or unreadable sections are disclosed cleanly
- `report.json` matches the actual completeness of the bundle

## Common Mistakes

| Mistake | Correction |
|--------|------------|
| Summarizing only the abstract | Read the full available paper text and use the visuals. |
| Keeping Chinese headings for every language | Localize the whole report to `target_language` unless the user asks for bilingual output. |
| Dumping screenshots without interpretation | Every visual block needs a short explanation and its role in the argument. |
| Guessing missing method or formula details | Mark uncertainty explicitly and record it in `report.json`. |
| Writing a rough note dump | Rewrite into publication-ready prose with stable structure. |
