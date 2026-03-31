# Example Inputs

This folder stores **example input PDFs** used for repo-side testing and reproducible validation.

These files are:

- test inputs for committed example paper packages
- used by `scripts/rebuild_<slug>_bundle.py`
- not special requirements of the skills themselves

If you are doing a real paper run, you can point the skills at any readable PDF path. You do **not** need to copy your paper into this folder first.

## Included Example Inputs

- `219qiushan.pdf`
- `Tan2026.pdf`
- `Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents.pdf`

## Related Test Flow

```text
examples/papers/*.pdf
  -> scripts/rebuild_<slug>_bundle.py
  -> output/papers/<paper-slug>/
  -> scripts/validate_paper_bundle.py
```

## Related Actual Flow

```text
/absolute/path/to/your-paper.pdf
  -> literature-summary
     -> paper-asset-extraction
  -> output/papers/<paper-slug>/
```
