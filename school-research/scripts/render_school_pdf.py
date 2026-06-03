#!/usr/bin/env python3
"""Render a single-school research report PDF from structured JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


FONT_NAME = "Helvetica"
BOLD_FONT_NAME = "Helvetica-Bold"


def register_fonts() -> None:
    global FONT_NAME, BOLD_FONT_NAME
    candidates = [
        (r"C:\Windows\Fonts\msyh.ttc", "MicrosoftYaHei"),
        (r"C:\Windows\Fonts\simsun.ttc", "SimSun"),
        (r"C:\Windows\Fonts\arial.ttf", "Arial"),
    ]
    for path, name in candidates:
        if Path(path).exists():
            pdfmetrics.registerFont(TTFont(name, path))
            FONT_NAME = name
            BOLD_FONT_NAME = name
            return


def clean(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "\n".join(clean(item) for item in value if clean(item))
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def as_rows(items: list[dict[str, Any]], columns: list[tuple[str, str]]) -> list[list[str]]:
    rows = [[label for _, label in columns]]
    for item in items:
        rows.append([clean(item.get(key, "")) for key, _ in columns])
    return rows


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName=BOLD_FONT_NAME,
            fontSize=25,
            leading=31,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#1F3A5F"),
            spaceAfter=10,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName=FONT_NAME,
            fontSize=11,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4B5563"),
        ),
        "h1": ParagraphStyle(
            "Heading1",
            parent=base["Heading1"],
            fontName=BOLD_FONT_NAME,
            fontSize=16,
            leading=21,
            textColor=colors.HexColor("#1F3A5F"),
            spaceBefore=8,
            spaceAfter=6,
        ),
        "h2": ParagraphStyle(
            "Heading2",
            parent=base["Heading2"],
            fontName=BOLD_FONT_NAME,
            fontSize=12,
            leading=16,
            textColor=colors.HexColor("#2F5D62"),
            spaceBefore=6,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName=FONT_NAME,
            fontSize=9.5,
            leading=13,
            alignment=TA_LEFT,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName=FONT_NAME,
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#4B5563"),
        ),
    }


def para(text: Any, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean(text).replace("\n", "<br/>"), style)


def table(rows: list[list[Any]], styles: dict[str, ParagraphStyle], widths: list[float] | None = None) -> Table:
    formatted = [[para(cell, styles["small"]) for cell in row] for row in rows]
    tbl = Table(formatted, colWidths=widths, repeatRows=1)
    tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF6")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1F3A5F")),
                ("FONTNAME", (0, 0), (-1, 0), BOLD_FONT_NAME),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return tbl


def bullets(items: list[Any], styles: dict[str, ParagraphStyle]) -> list[Any]:
    story: list[Any] = []
    for item in items:
        story.append(para(f"- {item}", styles["body"]))
    return story


def header_footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont(FONT_NAME, 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(18 * mm, 12 * mm, "School Research Report")
    canvas.drawRightString(192 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(data: dict[str, Any], output: Path) -> None:
    register_fonts()
    styles = make_styles()
    doc = BaseDocTemplate(
        str(output),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=header_footer)])

    story: list[Any] = []
    school = data.get("school", "School")
    program = data.get("program", "")
    context = data.get("applicant_context", "")
    report_date = data.get("report_date", "")
    confidence = data.get("confidence", "")

    story.append(Spacer(1, 35 * mm))
    story.append(para(school, styles["title"]))
    story.append(para(program, styles["subtitle"]))
    story.append(Spacer(1, 6 * mm))
    story.append(para(context, styles["subtitle"]))
    story.append(para(f"Report date: {report_date} | Confidence: {confidence}", styles["subtitle"]))
    story.append(PageBreak())

    story.append(para("Decision Summary", styles["h1"]))
    story.append(para(data.get("bottom_line", ""), styles["body"]))
    story.append(Spacer(1, 4 * mm))
    summary_rows = [
        ["Best-fit reasons", clean(data.get("best_fit_reasons", []))],
        ["Main concerns", clean(data.get("main_concerns", []))],
        ["Next actions", clean(data.get("next_actions", []))],
    ]
    story.append(table(summary_rows, styles, [45 * mm, 120 * mm]))

    scorecard = data.get("fit_scorecard", [])
    if scorecard:
        story.append(para("Fit Scorecard", styles["h1"]))
        story.append(
            table(
                as_rows(scorecard, [("dimension", "Dimension"), ("rating", "Rating"), ("rationale", "Rationale")]),
                styles,
                [38 * mm, 28 * mm, 99 * mm],
            )
        )

    checklist = data.get("admissions_checklist", [])
    if checklist:
        story.append(para("Admissions Checklist", styles["h1"]))
        story.append(
            table(
                as_rows(checklist, [("item", "Item"), ("finding", "Finding"), ("status", "Status")]),
                styles,
                [45 * mm, 90 * mm, 30 * mm],
            )
        )

    timeline = data.get("timeline", [])
    if timeline:
        story.append(para("Timeline", styles["h1"]))
        story.append(
            table(
                as_rows(timeline, [("date", "Date"), ("task", "Task"), ("owner", "Owner"), ("status", "Status")]),
                styles,
                [32 * mm, 83 * mm, 30 * mm, 20 * mm],
            )
        )

    sections = data.get("sections", [])
    for section in sections:
        story.append(para(section.get("title", ""), styles["h1"]))
        story.append(para(section.get("body", ""), styles["body"]))
        if section.get("bullets"):
            story.extend(bullets(section["bullets"], styles))

    risks = data.get("risks", [])
    if risks:
        story.append(para("Risk Register", styles["h1"]))
        story.append(
            table(
                as_rows(risks, [("risk", "Risk"), ("severity", "Severity"), ("evidence", "Evidence"), ("mitigation", "Mitigation")]),
                styles,
                [42 * mm, 24 * mm, 54 * mm, 45 * mm],
            )
        )

    sources = data.get("sources", [])
    if sources:
        story.append(PageBreak())
        story.append(para("Source Log", styles["h1"]))
        story.append(
            table(
                as_rows(sources, [("claim", "Claim"), ("title", "Source"), ("url", "URL"), ("accessed", "Accessed")]),
                styles,
                [42 * mm, 47 * mm, 58 * mm, 18 * mm],
            )
        )

    doc.build(story)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a school research PDF from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_pdf", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
    build_pdf(data, args.output_pdf)


if __name__ == "__main__":
    main()
