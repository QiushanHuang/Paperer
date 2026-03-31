# Paperer Skill Package

Use this file as the machine-facing entry when an agent or installer needs the minimal `Paperer` skills.

## Use This Instead Of The Full Repo

Obtain only the minimal skill package when:

- the current workspace does not already contain the `Paperer` production skills
- the task is to process a readable paper PDF
- the user does not need repo-maintainer rebuild or regression tools

Do **not** obtain the full repo unless:

- the task is repo-maintainer work
- the user explicitly needs `scripts/rebuild_*.py` or `scripts/validate_paper_bundle.py`
- the user wants to edit `Paperer` itself

## Minimal Package Directory

- GitHub directory:
  - `https://github.com/QiushanHuang/Paperer/tree/main/paperer-skill-package`
- Expected local path after download:
  - `paperer-skill-package/`

## One Way To Fetch Only This Directory

```bash
git clone --filter=blob:none --no-checkout https://github.com/QiushanHuang/Paperer.git
cd Paperer
git sparse-checkout init --cone
git sparse-checkout set paperer-skill-package
git checkout main
```

## Included Skills

- Public entry skill:
  - `paperer-skill-package/skills/paperer/`
- Thin orchestration skill:
  - `paperer-skill-package/skills/paper-package-runner/`
- Core production skills:
  - `paperer-skill-package/skills/literature-summary/`
  - `paperer-skill-package/skills/paper-asset-extraction/`

## Default Entry Skill

- `paperer-skill-package/skills/paperer/SKILL.md`

Use that skill first. Do not start from repo README sections or maintainer scripts.

## Minimal Copyable Prompt

```text
Check whether the current workspace already contains the `Paperer` skills. If not, install the minimal skill package from https://github.com/QiushanHuang/Paperer/tree/main/paperer-skill-package at `paperer-skill-package/`. Use Paperer skill to generate a paper package for the PDF at /absolute/path/to/your-paper.pdf.
```

## Expected Production Flow

```text
paperer
  -> paper-package-runner
     -> literature-summary
        -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```
