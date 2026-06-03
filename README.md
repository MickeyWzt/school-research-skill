# School Research Skill

[![CI](https://github.com/MickeyWzt/school-research-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/MickeyWzt/school-research-skill/actions/workflows/ci.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

`school-research` is a Codex/Claude-style skill for deep research on one specific school, college, university, boarding school, international school, or academic program.

It is designed for application planning tasks where a user names a school and wants a source-backed profile or polished PDF report covering admissions, program fit, cost, scholarships, student life, outcomes, risks, and next actions.

## At a Glance

| Field | Details |
| --- | --- |
| Project status | Working research skill with sample assets and a PDF report renderer. |
| Best for | Deep due diligence on one specific school, campus, program, or application path. |
| First thing to try | Ask for one named school and include applicant type, entry year, and target program. |
| Important caveat | Final requirements, costs, dates, scholarships, and visa rules must be verified with official sources. |

## Project Links

- [Development guide](docs/DEVELOPMENT.md)
- [FAQ](docs/FAQ.md)
- [Examples](docs/EXAMPLES.md)
- [Support and troubleshooting](SUPPORT.md)
- [Changelog](CHANGELOG.md)
- [Roadmap](ROADMAP.md)
- [Contributing guide](CONTRIBUTING.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Security policy](SECURITY.md)
- [Research standards](school-research/references/research-standards.md)
- [PDF report design](school-research/references/pdf-report-design.md)

## What It Does

- Confirms the exact school, campus, program, applicant category, and entry cycle.
- Prioritizes official sources such as admissions, department, tuition, financial aid, international student, student life, and official data pages.
- Attempts a minimum deep-research source set before calling a report "deep research."
- Labels facts as `verified`, `inferred`, or `unclear`.
- Produces quick school profiles, deep due-diligence reports, application checklists, source logs, and risk registers.
- Produces readable visual PDF reports with a cover, decision summary, fit scorecard, admissions checklist, timeline, risk register, and source log.
- Outputs in Chinese when the user writes in Chinese, while preserving official English names.

## Included Files

```text
school-research/
  SKILL.md
  assets/
    sample_pdf_report.json
    single_school_profile.csv
  references/
    output-templates.md
    pdf-report-design.md
    research-standards.md
  scripts/
    render_school_pdf.py
dist/
  school-research.skill
```

## Installation

Use the packaged skill file:

```text
dist/school-research.skill
```

Or install/copy the source folder:

```text
school-research/
```

## Example Requests

- "Research NYU for an international student applying to economics."
- "Make a deep school profile for Phillips Exeter Academy."
- "Check whether USC still requires SAT/ACT for 2027 entry."
- "Research the University of Toronto computer science application requirements."
- "Help me decide whether this one school is worth applying to."
- "Make the final school research report as a polished PDF."

## Deep Research Standard

For a deep profile, the skill asks the agent to attempt:

1. Official school profile or facts page.
2. Admissions requirements and deadlines.
3. Program, department, curriculum, or catalog pages.
4. Tuition, cost of attendance, aid, and scholarships.
5. International admissions or applicant support.
6. Student life, housing, safety, and advising.
7. Official outcomes, Common Data Set, career, or annual-report evidence.
8. External context only after official sources.

If a category cannot be found, the report should say so instead of silently omitting it.

## PDF Output

The skill includes a ReportLab renderer:

```powershell
python school-research/scripts/render_school_pdf.py school-research/assets/sample_pdf_report.json output/sample_school_report.pdf
```

Agents can use this script after converting research findings into structured JSON. The PDF mode emphasizes readability: the first pages are decision-oriented, while detailed evidence and source logs come later.

## License

MIT
