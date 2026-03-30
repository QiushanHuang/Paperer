# Failure Rules

This skill treats partial success as a valid outcome.

## Non-negotiable rules

- Do not invent unsupported claims.
- Do not silently omit missing evidence.
- Do not make the document look unfinished when output is partial.
- Do not over-explain formulas or visuals that were not extracted clearly.

## Required partial-output behavior

If extraction is incomplete:

- still write `summary.md`
- keep the full section structure where possible
- state which evidence is missing or unclear
- record the same issue in `report.json`

## Visual handling rules

If a figure, table, or formula screenshot is missing:

- keep the section heading
- note the missing asset cleanly
- explain only what the surviving evidence supports

If the screenshot exists but interpretation is uncertain:

- say that the interpretation is limited
- avoid pretending the visual proves more than it does

## Formula-specific caution

Formula blocks are high-risk for hallucination.

If a formula cannot be read reliably:

- explain its apparent role only at a high level, if defensible
- otherwise mark it as unreadable
- do not fabricate variable meanings

## Example disclosure language

Examples of acceptable wording:

- "The paper appears to use this equation as the main optimization objective, but the extracted notation is incomplete, so the variable-level interpretation is uncertain."
- "The figure is referenced in the paper, but the extracted screenshot is missing, so this section relies on the surrounding text only."
- "The experimental claim is partially supported by Table 2, but the ablation evidence appears incomplete in the extracted materials."
