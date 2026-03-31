# 2026-03-31 Runner Skill And Bilingual README Fix Log

## Reported problems

- The repo still expected users to know the production skill order themselves.
- Fresh-machine usage was possible but not optimized.
- The copyable prompt was not yet centered on a dedicated runner skill.
- The root README was not a full bilingual usage guide.

## Root cause

- The production logic was already split well between `literature-summary` and `paper-asset-extraction`, but there was no thin portable entry layer.
- README guidance still mixed direct-skill invocation, repo-maintainer flows, and new-machine assumptions.

## What changed

- Added a new English wrapper skill:
  - `skills/paper-package-runner/SKILL.md`
  - `skills/paper-package-runner/agents/openai.yaml`
- Updated `literature-summary` so its intake rules are explicit about:
  - required inputs
  - derived defaults
  - runner handoff behavior
- Embedded the default runtime behavior into the skills:
  - `target_language = Chinese` when omitted
  - automatic `paper_slug` derivation
  - default output-root derivation
  - built-in return contract
- Rewrote `README.md` back into a Chinese-primary guide with:
  - the minimal fresh-machine prompt
  - runner-first production flow
  - the shortest practical invocation path
  - a clearer split between production flow and repo test flow
- Added `README_en.md` as the separate English guide.
- Rewrote `examples/README.md` so example PDFs are clearly labeled as test inputs rather than required runtime files.

## Verification

- Verified the new runner skill tree exists.
- Verified `literature-summary` now references `paper-package-runner`, `paper_pdf_path`, `paper_slug`, and `output_root`.
- Verified the README now surfaces:
  - `paper-package-runner`
  - fresh-machine usage
  - copyable prompts
  - production flow versus repo test flow
