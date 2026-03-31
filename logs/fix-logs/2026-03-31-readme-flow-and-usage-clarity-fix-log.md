# 2026-03-31 README Flow And Usage Clarity Fix Log

## Reported problems

- The README mixed together skills, example outputs, rebuild scripts, and repo test workflows.
- The term `bundle` was overloaded and unclear.
- It was not explicit which paths and files belong to actual skill runs versus repo-maintainer testing.
- The README did not provide a copyable end-to-end prompt for using the skills on a real paper path.

## Root cause

- The README grew incrementally and accumulated both end-user and maintainer explanations in the same sections.
- Example outputs and runtime outputs share the same directory shape, but the README did not explain the difference in purpose.

## What changed

- Rewrote the root `README.md` around a single unified term: `paper package`.
- Explicitly separated:
  - actual flow
  - test flow
  - skills
  - repo utilities
  - example inputs
  - example output packages
- Added a practical “How To Use The Skill In Practice” section.
- Added a copyable prompt and a concrete path-based example prompt for agent use.
- Updated `examples/README.md` so the examples folder is clearly described as test input storage rather than a required runtime location.

## Verification

- Re-read the rewritten README to confirm:
  - the naming is consistent
  - actual flow and test flow are separated
  - the prompt is copyable and path-based
  - the `tan2026` example remains the visible preview case
