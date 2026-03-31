# Paperer Skill Package

This directory is the minimal distributable `Paperer` skill package.

## Included Production Skills

- `skills/paper-package-runner/`
- `skills/literature-summary/`
- `skills/paper-asset-extraction/`

## Default Entry Skill

- `skills/paper-package-runner/SKILL.md`

Start from that skill first. Do not start from maintainer scripts.

## When To Use This Package

Use this package when:

- the current workspace does not already contain the `Paperer` production skills
- the task is to process a readable paper PDF
- the user does not need the full repo

Do **not** fetch the full repo unless the task is repo-maintainer work or the user explicitly asks for full-repo artifacts.

## Source Directory

- `https://github.com/QiushanHuang/Paperer/tree/main/paperer-skill-package`

## One Way To Fetch Only This Directory

```bash
git clone --filter=blob:none --no-checkout https://github.com/QiushanHuang/Paperer.git
cd Paperer
git sparse-checkout init --cone
git sparse-checkout set paperer-skill-package
git checkout main
```

## Minimal Copyable Prompt

```text
If the current workspace does not already contain the `Paperer` skill package, first obtain only this directory from:
https://github.com/QiushanHuang/Paperer/tree/main/paperer-skill-package

After download, the expected local path is:
paperer-skill-package/

Then use the entry skill at:
paperer-skill-package/skills/paper-package-runner/SKILL.md

Do not use repo-maintainer files such as scripts/rebuild_*.py unless the task is repo maintenance.

Generate a paper package for the PDF at /absolute/path/to/your-paper.pdf.
```
