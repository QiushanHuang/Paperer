# Paper Package Runner Skill Design

Date: 2026-03-31

## Goal

Add a thin English-language wrapper skill that gives users a portable entry point for generating a paper brief package from a readable PDF, even when they are not already inside the `Paperer` workspace.

This wrapper should make the normal workflow easier to invoke and easier to reuse on another machine, while keeping the existing responsibilities of `literature-summary` and `paper-asset-extraction` intact.

## Problem

The current repo has two production skills:

- `literature-summary`
- `paper-asset-extraction`

They work, but the practical invocation contract is still spread across:

- skill files
- README examples
- repo-specific assumptions

That causes three problems:

1. A user may not know which skill to call first.
2. A user may not know which fields are required versus optional.
3. A user on another machine may not have the `Paperer` skill package already available in the current workspace.

## Proposed Solution

Add a new wrapper skill:

- `paper-package-runner`

This skill is a **portable intake and orchestration layer**.

It should not duplicate the extraction or summary logic. Instead, it should:

1. verify that the required `Paperer` skills are available
2. bootstrap skill access when they are not already available
3. collect the minimum runtime inputs
4. derive safe defaults for optional inputs
5. call `literature-summary`
6. require `literature-summary` to prefer `paper-asset-extraction`

## Role Boundaries

### `paper-package-runner`

Responsible for:

- portable entry behavior
- environment and skill-availability checks
- runtime intake
- default generation
- invocation order
- final return contract

Not responsible for:

- writing the final literature brief itself
- extracting figures, tables, and formulas itself
- redefining output schema

### `literature-summary`

Remains responsible for:

- `summary.md`
- `report.json`
- final paper-level reasoning
- header image generation
- extracted text and metadata outputs

### `paper-asset-extraction`

Remains responsible for:

- conservative visual asset extraction
- `manifest.json`
- `assets/figures/*`
- `assets/tables/*`
- `assets/formulas/*`
- `extracted/asset-extraction-report.json`

## Inputs

### Required runtime inputs

- `paper_pdf_path`
- `target_language`

### Optional runtime inputs

- `paper_slug`
- `output_root`
- `user_reading_focus`

## Intake Rules

The new wrapper skill must enforce the following:

- If `paper_pdf_path` is missing, ask for it.
- If `target_language` is missing, ask for it.
- If `paper_slug` is missing, derive it from the PDF filename.
- If `output_root` is missing, default to `output/papers/<paper-slug>/`.
- If `user_reading_focus` is missing, continue without it.

The goal is that the user only has to supply the paper path and the target language in the common case.

## Bootstrap Rules

The wrapper skill must support portable usage across machines.

If the current environment does not already contain the `Paperer` skill package:

- first obtain the `Paperer` repo or its skill package
- then locate and use:
  - `literature-summary`
  - `paper-asset-extraction`

This behavior should be described inside the skill and reflected in the README copyable prompt.

The wrapper should not assume the repo is already the current working directory.

## Invocation Contract

The wrapper skill should follow this sequence:

1. Check whether `literature-summary` is available.
2. Check whether `paper-asset-extraction` is available.
3. If not available, bootstrap the `Paperer` skill package.
4. Collect missing required inputs.
5. Derive defaults for optional inputs.
6. Call `literature-summary`.
7. Instruct `literature-summary` to prefer `paper-asset-extraction`.
8. Return the final output path and key file paths.

## Final Return Contract

At the end of the run, the wrapper should return:

- the output directory path
- the path to `summary.md`
- the path to `report.json`
- the path to `manifest.json` when present
- the final status: `complete`, `partial`, or `failed`

## Skill Authoring Rules

The new wrapper skill itself must be written in English.

This includes:

- the `SKILL.md` file
- any supporting references
- quick-reference text
- common-mistake guidance

This does **not** change the runtime output language behavior of the literature brief itself, which still follows `target_language` except for the fixed Chinese page-title rule already defined in `literature-summary`.

## README Changes

The README should be updated so that:

1. the primary copyable prompt calls `paper-package-runner`
2. the prompt explicitly says:
   - if the `Paperer` skills are not available in the current workspace, fetch the `Paperer` skill package first
3. the prompt remains path-driven and portable
4. the prompt still makes clear that:
   - `literature-summary` is the main brief-writing skill
   - `paper-asset-extraction` is the preferred visual-asset skill

## Files To Add Or Update

### New files

- `skills/paper-package-runner/SKILL.md`
- `skills/paper-package-runner/agents/openai.yaml`
- `skills/paper-package-runner/references/*` only if the wrapper needs supporting guidance that would make `SKILL.md` too heavy

### Files to update

- `skills/literature-summary/SKILL.md`
- `README.md`
- `examples/README.md` only if the new entry flow needs to be referenced there

## Non-Goals

This change should **not**:

- merge the existing two skills into one large skill
- duplicate the logic of `literature-summary`
- duplicate the logic of `paper-asset-extraction`
- turn rebuild scripts into production entry points

## Acceptance Criteria

This design is successful if:

- a user can start from one wrapper skill instead of remembering two production skills
- the wrapper asks for missing critical inputs instead of silently assuming them
- the wrapper works as a portable entry prompt across machines
- the wrapper keeps production flow separate from repo test flow
- the README copyable prompt now reflects the wrapper-based entry path
- the implementation remains thin and does not fork core logic

## Risks

### Risk: wrapper duplicates too much logic

Mitigation:

- keep all writing and extraction behavior delegated to existing skills

### Risk: bootstrap wording becomes environment-specific

Mitigation:

- describe bootstrap behavior at the skill-contract level, not as a single hardcoded shell flow

### Risk: users still confuse production flow with rebuild scripts

Mitigation:

- keep the README explicit that rebuild scripts are for repo-maintainer testing only
