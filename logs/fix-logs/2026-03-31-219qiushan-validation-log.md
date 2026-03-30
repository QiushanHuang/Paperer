# 219qiushan Validation Log

Date: 2026-03-31
Scope:
- `examples/papers/219qiushan.pdf`
- `scripts/rebuild_219qiushan_bundle.py`
- `output/papers/219qiushan/`

## Requested Work

1. Run a real-paper validation on `/Users/joshua/Downloads/219qiushan.pdf`.
2. Generate the corresponding bundle under `output/`.
3. Sync the result back to both GitHub repositories.

## Root Cause

- The paper was outside the repository and had no reproducible rebuild path.
- The repository only had rebuild scripts for the previous example bundles.

## Changes Made

- Added `examples/papers/219qiushan.pdf` so the validation input is versioned inside the repo.
- Added `scripts/rebuild_219qiushan_bundle.py` to make the bundle reproducible.
- Generated a new bundle at `output/papers/219qiushan/` with:
  - `source.pdf`
  - `manifest.json`
  - `summary.md`
  - `report.json`
  - `extracted/*`
  - `assets/header/*`
  - `assets/figures/*`
- Updated `examples/README.md` to list the new source paper.

## Verification

- `python3 -m py_compile scripts/rebuild_219qiushan_bundle.py scripts/validate_paper_bundle.py`
- `./.venv/bin/python scripts/rebuild_219qiushan_bundle.py`
- `./.venv/bin/python scripts/validate_paper_bundle.py output/papers/219qiushan`
