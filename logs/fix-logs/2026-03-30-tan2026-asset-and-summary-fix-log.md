# Tan2026 Asset And Summary Fix Log

Date: 2026-03-30
Bundle: `output/papers/tan2026/`

## Reported Problems

1. The header screenshot and all visual assets must be embedded in `summary.md`.
2. Figure / table / formula explanations should answer the three questions in full sentences instead of literal labeled bullets.
3. Section `1.3 核心结论速览` must allow multiple problem / method / result / contribution points when the paper supports them.
4. Some figure crops mixed figures and tables in the same image.
5. Figure numbering in the bundle did not stay continuous with the paper and missed `Fig. 3` and `Fig. 7`.
6. `fig-009.png` was cropped from the wrong region instead of the actual `Fig. 12`.
7. `fig-008.png` was cropped through the middle of `Fig. 11` and included too much body text.
8. The summary discussed extraction-side issues in the paper-analysis prose.

## Root Cause

- The earlier Tan2026 rebuild used page-level heuristic crops instead of figure-number-aware crops.
- The extraction workflow had no explicit continuity review for `Fig. N` / `Table N`.
- The summary contract required visual explanation, but did not yet require all assets to be embedded directly in Markdown.
- The summary rules did not explicitly forbid writing about extraction workflow inside the paper-focused prose.
- There was no executable validator to fail on mixed-asset captions, numbering gaps, or missing visual embeds.

## Changes Made

- Added a repair-history folder at `logs/fix-logs/`.
- Tightened `paper-asset-extraction` rules to require:
  - numbering continuity review
  - one labeled figure or table per emitted crop
  - file ids that match paper numbering when labels are detectable
- Tightened `literature-summary` rules to require:
  - embedding the header image and every available figure / table / formula in `summary.md`
  - prose-only visual explanations that still answer what it is, what can be observed, and what it shows
  - paper-focused limitations and discussion
  - `draft.pdf` output
- Added `scripts/validate_paper_bundle.py` to catch:
  - numbering gaps
  - id / caption mismatches
  - mixed figure-table caption hints
  - missing asset embeds in `summary.md`
  - workflow-side terms inside summary prose
- Rebuilt `Tan2026` with corrected figure numbering and separated visual assets.

## Verification

- Baseline validator run failed before the rebuild and reported numbering / mixed-caption errors.
- After the rebuild, `scripts/validate_paper_bundle.py output/papers/tan2026` passed.
- The rebuilt bundle now contains `fig-001` through `fig-012`, plus separate `table-001`, `table-002`, and `formula-001`.
- `summary.md` embeds the header image and all extracted assets.
- `draft.pdf` renders successfully and currently contains 17 pages and 16 embedded images.
