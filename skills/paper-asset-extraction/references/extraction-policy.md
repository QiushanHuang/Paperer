# Extraction Policy

Use a fixed two-pass extraction flow.

## Pass 1: Candidate Collection

Collect all plausible candidates for:

- figures
- tables
- formulas

At this stage:

- prefer over-inclusive crops
- do not reject a candidate only because it includes extra caption text, surrounding whitespace, or nearby body text
- keep possible sibling panels visible when you are unsure whether they are separate assets

## Pass 2: Review And Normalization

For every candidate:

- classify as `figure`, `table`, `formula`, or `uncertain`
- merge obvious duplicates
- keep alternates only when they preserve otherwise missing content
- widen crops that look too tight
- flag likely missed siblings or adjacent formula lines

## Conservative Ordering Rules

Prefer these outcomes in this order:

1. full content with extra margin
2. questionable but preserved candidate
3. neatly cropped but potentially incomplete candidate

Never choose visual tidiness over content preservation.

## Type-Specific Guidance

### Figures

Keep:

- axes
- legends
- panel labels such as `(a)` and `(b)`
- nearby caption text when needed to disambiguate the figure

### Tables

Keep:

- full row and column structure
- headers when visible
- enough surrounding context to avoid clipping edges

### Formulas

Keep:

- the full displayed formula
- equation numbers when present
- neighboring lines when needed for multiline expressions

If the formula is hard to segment cleanly, prefer one larger block over multiple clipped fragments.
