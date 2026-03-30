# Summary Prompt And PDF Output Fix Log

Date: 2026-03-30
Scope: `skills/literature-summary/`, `scripts/rebuild_tan2026_bundle.py`, `output/papers/tan2026/`

## Reported Problems

1. `draft.pdf` should no longer be part of the output contract.
2. The section requirements should be rewritten into shorter, more efficient skill prompts.
3. Section 5 needed stronger guidance for figure, table, and formula interpretation.
4. Section 8.1 needed explicit direction-level and practice / application-level meaning.
5. Sections 6 and 7 needed the fuller contribution / limitation prompts restored.
6. Sections 1 to 4 needed the fuller overview, motivation, method, and evidence prompts restored.

## Root Cause

- The summary contract had grown across several iterations and mixed high-level guidance with execution details.
- `draft.pdf` removal had not yet been propagated into the bundle contract or the Tan2026 rebuild path.
- Some section prompts were present in earlier design discussions but not encoded concisely in the live skill files.

## Changes Made

- Removed `draft.pdf` from the live `literature-summary` contract.
- Rewrote `summary-template.md` into tighter subsection prompts that keep the same structure but are easier to execute consistently.
- Expanded Section 5 prompts so figure, table, and formula analysis stays more specific and paper-facing.
- Expanded Sections 6, 7, and 8.1 to match the intended contribution, limitation, and implication coverage.
- Updated `scripts/rebuild_tan2026_bundle.py` to stop generating `draft.pdf`.
- Deleted the unused `scripts/render_summary_draft_pdf.py` helper.
- Updated `scripts/validate_paper_bundle.py` so it now fails if:
  - a bundle still contains `draft.pdf`
  - the summary uses literal `是什么 / 可以发现什么 / 说明了什么` label bullets

## Verification

- `python3 -m py_compile scripts/rebuild_tan2026_bundle.py scripts/validate_paper_bundle.py`
- Rebuilt `output/papers/tan2026/`
- Re-ran `scripts/validate_paper_bundle.py output/papers/tan2026`
- Confirmed `output/papers/tan2026/draft.pdf` no longer exists
