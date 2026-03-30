#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


PROCESS_TERMS = [
    "ocr",
    "截图",
    "裁切",
    "crop",
    "workflow",
    "提取版本",
    "截图质量",
]

DISALLOWED_VISUAL_LABEL_PATTERNS = [
    r"(?m)^\s*[-*]\s*是什么[:：]?\s*$",
    r"(?m)^\s*[-*]\s*可以发现什么[:：]?\s*$",
    r"(?m)^\s*[-*]\s*说明了什么[:：]?\s*$",
]


def extract_markdown_images(summary_text: str) -> list[str]:
    return re.findall(r"!\[[^\]]*\]\(([^)]+)\)", summary_text)


def find_label_numbers(text: str, label: str) -> list[int]:
    if label == "figure":
        pattern = r"Fig\.\s*(\d+)"
    elif label == "table":
        pattern = r"Table\s*(\d+)"
    else:
        return []
    return [int(match) for match in re.findall(pattern, text)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a literature-summary paper bundle.")
    parser.add_argument("bundle", type=Path)
    args = parser.parse_args()

    bundle = args.bundle.resolve()
    errors: list[str] = []

    manifest_path = bundle / "manifest.json"
    report_path = bundle / "report.json"
    summary_path = bundle / "summary.md"
    header_path = bundle / "assets" / "header" / "paper-header.png"
    deprecated_draft_path = bundle / "draft.pdf"

    for required in [manifest_path, report_path, summary_path, header_path]:
        if not required.exists():
            errors.append(f"Missing required file: {required.relative_to(bundle.parent)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    report = json.loads(report_path.read_text(encoding="utf-8"))
    summary_text = summary_path.read_text(encoding="utf-8")
    embedded_images = extract_markdown_images(summary_text)

    expected_embeds = ["assets/header/paper-header.png"] + [asset["path"] for asset in manifest["assets"]]
    missing_embeds = [path for path in expected_embeds if path not in embedded_images]
    extra_embeds = [path for path in embedded_images if path not in expected_embeds]
    if missing_embeds:
        errors.append(f"Summary is missing embedded assets: {missing_embeds}")
    if extra_embeds:
        errors.append(f"Summary embeds unexpected assets: {extra_embeds}")

    lowered = summary_text.lower()
    bad_terms = [term for term in PROCESS_TERMS if term in lowered]
    if bad_terms:
        errors.append(f"Summary contains workflow-side terms that should stay out of summary.md: {bad_terms}")

    if "asset_manifest_status" not in report:
        errors.append("report.json is missing asset_manifest_status")

    if deprecated_draft_path.exists():
        errors.append("Bundle still contains deprecated draft.pdf output")

    for pattern in DISALLOWED_VISUAL_LABEL_PATTERNS:
        if re.search(pattern, summary_text):
            errors.append("Summary still uses literal visual QA labels instead of prose explanations")
            break

    by_type: dict[str, list[tuple[int, dict]]] = {"figure": [], "table": [], "formula": []}
    for asset in manifest["assets"]:
        asset_id = asset["id"]
        asset_type = asset["type"]
        match = re.match(r"^(fig|table|formula)-(\d+)$", asset_id)
        if not match:
            errors.append(f"Asset id does not follow expected pattern: {asset_id}")
            continue
        number = int(match.group(2))
        by_type.setdefault(asset_type, []).append((number, asset))

        if asset_type == "figure":
            if "Table" in asset["caption_hint"]:
                errors.append(f"Figure asset mixes table caption hint: {asset_id} -> {asset['caption_hint']}")
            figure_nums = find_label_numbers(asset["caption_hint"], "figure")
            table_nums = find_label_numbers(asset["caption_hint"], "table")
            if len(set(figure_nums)) != 1:
                errors.append(f"Figure asset must map to exactly one figure number: {asset_id} -> {asset['caption_hint']}")
            elif figure_nums[0] != number:
                errors.append(f"Figure asset id does not match caption number: {asset_id} -> {asset['caption_hint']}")
            if table_nums:
                errors.append(f"Figure asset must not contain table numbering in caption hint: {asset_id} -> {asset['caption_hint']}")

        if asset_type == "table":
            if "Fig." in asset["caption_hint"]:
                errors.append(f"Table asset mixes figure caption hint: {asset_id} -> {asset['caption_hint']}")
            table_nums = find_label_numbers(asset["caption_hint"], "table")
            figure_nums = find_label_numbers(asset["caption_hint"], "figure")
            if len(set(table_nums)) != 1:
                errors.append(f"Table asset must map to exactly one table number: {asset_id} -> {asset['caption_hint']}")
            elif table_nums[0] != number:
                errors.append(f"Table asset id does not match caption number: {asset_id} -> {asset['caption_hint']}")
            if figure_nums:
                errors.append(f"Table asset must not contain figure numbering in caption hint: {asset_id} -> {asset['caption_hint']}")

    for asset_type in ("figure", "table"):
        ids = sorted(number for number, _asset in by_type.get(asset_type, []))
        if ids:
            expected = list(range(1, ids[-1] + 1))
            if ids != expected:
                errors.append(f"{asset_type} numbering is not continuous: have {ids}, expected {expected}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Bundle {bundle.name} passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
