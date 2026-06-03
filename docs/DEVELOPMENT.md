# Development

This guide describes local checks and contribution expectations for School Research Skill.

## Repository Shape

- `school-research/SKILL.md` contains the skill instructions.
- `school-research/references/research-standards.md` defines evidence expectations.
- `school-research/references/output-templates.md` defines report structures.
- `school-research/references/pdf-report-design.md` describes PDF layout expectations.
- `school-research/scripts/render_school_pdf.py` renders structured report JSON to PDF.
- `school-research/assets/sample_pdf_report.json` is the sample renderer input.

## Local Checks

Run these from the repository root:

```powershell
python -m py_compile school-research/scripts/render_school_pdf.py
python -c "import json; json.load(open('school-research/assets/sample_pdf_report.json', encoding='utf-8'))"
```

If ReportLab is installed, render the sample PDF:

```powershell
python school-research/scripts/render_school_pdf.py school-research/assets/sample_pdf_report.json output/sample_school_report.pdf
```

## Evidence Expectations

Changes should preserve:

- Official-source-first research.
- Clear source logs.
- Explicit handling of missing or unclear evidence.
- `verified`, `inferred`, and `unclear` labels when appropriate.
- No private applicant records in public examples.

## Renderer Notes

When changing PDF output, include:

- The sample JSON used.
- The output file path.
- Any visible layout changes.
- Any limitations that remain.
