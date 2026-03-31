# Paper Package Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a thin portable runner skill for paper-package generation, tighten the intake contract of the existing summary skill, and rewrite the README as a full bilingual usage guide for both fresh-machine onboarding and normal paper runs.

**Architecture:** Keep production responsibilities split across three layers: `paper-package-runner` for bootstrap and intake, `literature-summary` for the final brief, and `paper-asset-extraction` for conservative visual extraction. Update the docs so normal users start from the runner skill while repo-maintainer rebuild scripts remain explicitly test-only.

**Tech Stack:** Markdown skill specs, YAML agent metadata, repo documentation, existing validation conventions

---

### Task 1: Add the runner skill

**Files:**
- Create: `skills/paper-package-runner/SKILL.md`
- Create: `skills/paper-package-runner/agents/openai.yaml`

- [ ] **Step 1: Create the new skill folder and metadata file**

Create an English wrapper skill with a short description focused on portable paper-package entry.

- [ ] **Step 2: Write the runner skill contract**

Cover:
- required inputs: `paper_pdf_path`, `target_language`
- optional inputs: `paper_slug`, `output_root`, `user_reading_focus`
- preflight checks for fresh-machine usage
- bootstrap behavior when `Paperer` skills are unavailable
- default output path derivation
- invocation order: `paper-package-runner` -> `literature-summary` -> `paper-asset-extraction`
- final return contract

- [ ] **Step 3: Add agent metadata**

Match the existing `agents/openai.yaml` style used by the other two skills.

- [ ] **Step 4: Verify the new skill tree**

Run: `find skills/paper-package-runner -maxdepth 3 -type f | sort`
Expected: shows `SKILL.md` and `agents/openai.yaml`

### Task 2: Tighten the summary skill intake

**Files:**
- Modify: `skills/literature-summary/SKILL.md`

- [ ] **Step 1: Add standard intake behavior**

Document:
- which inputs are required
- which inputs can be derived
- when the agent must ask follow-up questions
- the default output root rule

- [ ] **Step 2: Align the runner handoff**

Make it explicit that:
- `literature-summary` can be entered directly
- but when called from `paper-package-runner`, it should accept derived defaults and prefer `paper-asset-extraction`

- [ ] **Step 3: Verify the new intake wording**

Run: `rg -n "paper_pdf_path|paper_slug|output_root|target_language|paper-package-runner" skills/literature-summary/SKILL.md`
Expected: all intake and handoff terms appear in the skill file

### Task 3: Rewrite the README as a bilingual usage guide

**Files:**
- Modify: `README.md`
- Modify: `examples/README.md`

- [ ] **Step 1: Reframe the primary usage path**

Make the top-level user path:
- fresh machine -> obtain `Paperer` skills if needed
- call `paper-package-runner`
- let it call the other two production skills

- [ ] **Step 2: Make the root README fully bilingual**

For the main usage sections, provide both Chinese and English rather than a Chinese body with only an English summary.

- [ ] **Step 3: Replace the copyable prompt**

Add:
- a portable copyable prompt for fresh-machine use
- a concrete real-path example
- explicit wording that tells the agent to fetch `Paperer` skill support first if it is not already available

- [ ] **Step 4: Keep test flow separate**

Ensure rebuild scripts and example PDFs stay clearly labeled as repo-maintainer tooling, not the user-facing runtime path.

- [ ] **Step 5: Verify README structure**

Run: `rg -n "paper-package-runner|fresh machine|新电脑|Copyable Prompt|实际流程|Actual Flow|Test Flow" README.md examples/README.md`
Expected: bilingual usage guidance and the new runner entry path are visible

### Task 4: Record and verify the documentation change set

**Files:**
- Create: `logs/fix-logs/2026-03-31-runner-skill-and-bilingual-readme-fix-log.md`

- [ ] **Step 1: Write the fix log**

Record:
- what changed
- why the old flow was too implicit
- how the runner skill and bilingual README address fresh-machine onboarding

- [ ] **Step 2: Run final verification**

Run:
- `find skills/paper-package-runner -maxdepth 3 -type f | sort`
- `rg -n "paper-package-runner|paper_pdf_path|output_root|target_language" skills/literature-summary/SKILL.md README.md examples/README.md`
- `git diff -- skills/paper-package-runner skills/literature-summary/SKILL.md README.md examples/README.md logs/fix-logs/2026-03-31-runner-skill-and-bilingual-readme-fix-log.md`

Expected:
- runner skill files exist
- intake terms appear consistently
- README clearly separates fresh-machine use, actual flow, and test flow

- [ ] **Step 3: Commit**

```bash
git add skills/paper-package-runner skills/literature-summary/SKILL.md README.md examples/README.md logs/fix-logs/2026-03-31-runner-skill-and-bilingual-readme-fix-log.md docs/superpowers/plans/2026-03-31-paper-package-runner-implementation.md
git commit -m "Add runner skill and bilingual usage guide"
```
