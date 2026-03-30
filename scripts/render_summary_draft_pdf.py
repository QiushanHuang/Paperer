#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

import fitz


FONT_PATH = Path("/System/Library/Fonts/STHeiti Light.ttc")
PAGE_RECT = fitz.paper_rect("a4")
MARGIN = 36
CONTENT_WIDTH = PAGE_RECT.width - (MARGIN * 2)
BOTTOM = PAGE_RECT.height - MARGIN


def parse_markdown(markdown: str) -> list[tuple]:
    blocks: list[tuple] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(part.strip() for part in paragraph if part.strip()).strip()
            if text:
                blocks.append(("paragraph", text))
            paragraph.clear()

    for raw in markdown.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            continue

        heading = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if heading:
            flush_paragraph()
            blocks.append(("heading", len(heading.group(1)), heading.group(2).strip()))
            continue

        image = re.match(r"^!\[(.*?)\]\((.*?)\)$", stripped)
        if image:
            flush_paragraph()
            blocks.append(("image", image.group(1).strip(), image.group(2).strip()))
            continue

        bullet = re.match(r"^- (.*)$", stripped)
        if bullet:
            flush_paragraph()
            blocks.append(("bullet", bullet.group(1).strip()))
            continue

        paragraph.append(stripped)

    flush_paragraph()
    return blocks


def split_long_token(token: str, font: fitz.Font, fontsize: float, width: float) -> list[str]:
    pieces: list[str] = []
    current = ""
    for char in token:
        if not current:
            current = char
            continue
        candidate = current + char
        if font.text_length(candidate, fontsize=fontsize) <= width:
            current = candidate
        else:
            pieces.append(current)
            current = char
    if current:
        pieces.append(current)
    return pieces


def wrap_text(text: str, font: fitz.Font, fontsize: float, width: float) -> list[str]:
    tokens = re.findall(r"\S+|\s+", text)
    lines: list[str] = []
    current = ""

    for token in tokens:
        token_parts = [token]
        if font.text_length(token, fontsize=fontsize) > width:
            token_parts = split_long_token(token, font, fontsize, width)

        for part in token_parts:
            candidate = current + part
            if current and font.text_length(candidate, fontsize=fontsize) > width:
                lines.append(current.rstrip())
                current = part.lstrip()
            else:
                current = candidate

    if current.strip():
        lines.append(current.rstrip())
    return lines or [""]


def make_page(doc: fitz.Document) -> fitz.Page:
    page = doc.new_page(width=PAGE_RECT.width, height=PAGE_RECT.height)
    page.insert_font(fontname="cjk", fontfile=str(FONT_PATH))
    return page


def render_lines(page: fitz.Page, x: float, y: float, lines: list[str], fontsize: float) -> float:
    line_height = fontsize * 1.45
    baseline = y + fontsize
    for line in lines:
        page.insert_text((x, baseline), line, fontname="cjk", fontsize=fontsize)
        baseline += line_height
    return y + (line_height * len(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a simple PDF draft from a summary Markdown file.")
    parser.add_argument("summary_md", type=Path)
    parser.add_argument("output_pdf", type=Path, nargs="?")
    args = parser.parse_args()

    summary_path = args.summary_md.resolve()
    output_pdf = args.output_pdf.resolve() if args.output_pdf else summary_path.with_name("draft.pdf")
    markdown = summary_path.read_text(encoding="utf-8")

    blocks = parse_markdown(markdown)
    doc = fitz.open()
    page = make_page(doc)
    font = fitz.Font(fontfile=str(FONT_PATH))
    y = MARGIN

    for block in blocks:
        kind = block[0]

        if kind == "heading":
            _, level, text = block
            fontsize = {1: 19, 2: 15, 3: 13}.get(level, 12)
            lines = wrap_text(text, font, fontsize, CONTENT_WIDTH)
            needed = (fontsize * 1.45 * len(lines)) + 10
            if y + needed > BOTTOM:
                page = make_page(doc)
                y = MARGIN
            y = render_lines(page, MARGIN, y, lines, fontsize) + 8
            continue

        if kind == "image":
            _, alt_text, image_rel = block
            image_path = (summary_path.parent / image_rel).resolve()
            if not image_path.exists():
                missing = f"[Missing image] {alt_text or image_rel}"
                lines = wrap_text(missing, font, 10, CONTENT_WIDTH)
                needed = (10 * 1.45 * len(lines)) + 8
                if y + needed > BOTTOM:
                    page = make_page(doc)
                    y = MARGIN
                y = render_lines(page, MARGIN, y, lines, 10) + 6
                continue

            pix = fitz.Pixmap(str(image_path))
            max_height = PAGE_RECT.height - (MARGIN * 2) - 20
            scale = min(CONTENT_WIDTH / pix.width, max_height / pix.height)
            width = pix.width * scale
            height = pix.height * scale
            if y + height > BOTTOM:
                page = make_page(doc)
                y = MARGIN
            x = MARGIN + ((CONTENT_WIDTH - width) / 2)
            rect = fitz.Rect(x, y, x + width, y + height)
            page.insert_image(rect, filename=str(image_path))
            y += height + 10
            continue

        if kind == "bullet":
            _, text = block
            fontsize = 11
            indent = 16
            bullet_prefix = "- "
            wrapped = wrap_text(text, font, fontsize, CONTENT_WIDTH - indent)
            lines = [bullet_prefix + wrapped[0]] + [(" " * len(bullet_prefix)) + line for line in wrapped[1:]]
            needed = (fontsize * 1.45 * len(lines)) + 6
            if y + needed > BOTTOM:
                page = make_page(doc)
                y = MARGIN
            y = render_lines(page, MARGIN, y, lines, fontsize) + 4
            continue

        if kind == "paragraph":
            _, text = block
            fontsize = 11
            lines = wrap_text(text, font, fontsize, CONTENT_WIDTH)
            needed = (fontsize * 1.55 * len(lines)) + 8
            if y + needed > BOTTOM:
                page = make_page(doc)
                y = MARGIN
            y = render_lines(page, MARGIN, y, lines, fontsize) + 6
            continue

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc.save(
        output_pdf,
        garbage=4,
        deflate=True,
        deflate_images=True,
        deflate_fonts=True,
        use_objstms=1,
    )
    print(output_pdf)


if __name__ == "__main__":
    main()
