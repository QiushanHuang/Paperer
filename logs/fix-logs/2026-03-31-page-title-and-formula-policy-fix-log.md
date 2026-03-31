# 2026-03-31 Page Title And Formula Policy Fix Log

## Reported problems

- The top displayed page title in `summary.md` was not explicitly constrained to be the Chinese translation of the paper's English title.
- Formula extraction policy was too loose and could admit paragraph-level math fragments or under-audited equation crops.
- Formula numbering continuity was not reviewed as strictly as figure and table numbering.

## Root cause

- The `literature-summary` template described the title block contents, but did not force a single title rule across languages.
- The `paper-asset-extraction` policy treated formulas conservatively for crop size, but not conservatively enough for formula qualification and numbering review.
- The bundle validator checked formula ids loosely and did not enforce manifest/report consistency around formula numbering gaps.

## What changed

- Updated `literature-summary` so the displayed page title is always the Chinese translation of the paper's English title, while the rest of the prose still follows `target_language`.
- Tightened `paper-asset-extraction` so formulas must be standalone displayed equation blocks outside paragraph flow and must preserve an explicit equation cue when available.
- Added formula numbering continuity language to the extraction skill, extraction policy, manifest schema, and quality-flag guidance.
- Updated `validate_paper_bundle.py` to:
  - require formula caption hints to preserve an explicit equation cue
  - compare formula ids against visible equation numbering when present
  - require explicit partial-state flags when numbered formulas have gaps
  - check `report.json.asset_manifest_status` against `manifest.json.status`
- Downgraded the `simulating-particle-dispersions-in-nematic-liquid-crystal-solvents` example manifest from `complete` to `partial` because its recovered numbered formulas skip `Eq. (8)`.

## Verification

- Reviewed the updated skill files and reference files for consistent title and formula rules.
- Updated the validator so future bundle checks will catch formula-gap and title-policy drift earlier.
- Realigned the `simulating` example manifest/report so the repository examples no longer contradict the stricter formula policy.
