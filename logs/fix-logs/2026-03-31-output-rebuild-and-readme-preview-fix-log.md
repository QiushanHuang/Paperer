# Output Rebuild And README Preview Fix Log

Date: 2026-03-31
Scope:
- `output/`
- `scripts/rebuild_simulating_bundle.py`
- `README.md`
- `skills/literature-summary/references/summary-template.md`

## Reported Problems

1. The entire `output/` directory needed to be cleared and regenerated from scratch.
2. Both example papers needed fresh end-to-end test bundles under `output/papers/`.
3. The repository README preview needed to use the `Tan2026` example instead of the older simulating paper preview.
4. The summary template change from the previous turn needed to remain in place while the example bundles were regenerated.

## Root Cause

- Only `Tan2026` had a stable rebuild script; the simulating example was still effectively a tracked output bundle rather than a reproducible test case.
- The README homepage preview had fallen behind the current primary validation bundle.
- Clearing `output/` would have removed the old simulating bundle with no reproducible path to rebuild it.

## Changes Made

- Added `scripts/rebuild_simulating_bundle.py` so the simulating paper can now be regenerated from `examples/papers/Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`.
- Cleared `output/` and rebuilt both example bundles from source PDFs.
- Regenerated the simulating bundle with:
  - `manifest.json`
  - `extracted/asset-extraction-report.json`
  - refreshed assets, summary, and report files
- Updated `README.md` so the homepage preview now uses `Tan2026` header, figure, table, and formula assets.
- Expanded the README validation-example section to point to both example bundles instead of only the older simulating bundle.
- Kept the latest `summary-template.md` wording change in the same update.

## Verification

- `python3 -m py_compile scripts/rebuild_simulating_bundle.py scripts/rebuild_tan2026_bundle.py scripts/validate_paper_bundle.py`
- `./.venv/bin/python scripts/rebuild_simulating_bundle.py`
- `./.venv/bin/python scripts/rebuild_tan2026_bundle.py`
- `./.venv/bin/python scripts/validate_paper_bundle.py output/papers/simulating-particle-dispersions-in-nematic-liquid-crystal-solvents`
- `./.venv/bin/python scripts/validate_paper_bundle.py output/papers/tan2026`
- `find output/papers -maxdepth 4 -type f | sort`
