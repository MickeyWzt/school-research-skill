# Examples

These examples show how to prompt and package source-backed school research.

## Example 1: Quick School Profile

Use this when you need a first-pass view before deciding whether a school is worth deeper research.

```text
Research NYU for an international student applying to economics for 2027 entry. Give me a quick school profile, official source links, admissions requirements, estimated costs, and risks.
```

Expected result: a concise profile with clear source links and uncertainty notes.

## Example 2: Deep Due-Diligence Report

Use this when the school is already on a serious application list.

```text
Create a deep research report for Phillips Exeter Academy for a boarding applicant entering grade 10 in 2027. Include admissions timeline, academics, residential life, costs, aid, fit risks, and next actions.
```

Expected result: a structured report that separates verified facts from inferred or unclear items.

## Example 3: Program-Specific Research

Use this for universities where requirements differ by faculty, campus, or major.

```text
Research the University of Toronto computer science application path for an international student entering in 2027. Focus on campus differences, prerequisites, deadlines, tuition, scholarships, and official source links.
```

Program-specific context prevents the report from mixing requirements across campuses or departments.

## Example 4: PDF Report Workflow

After research is converted into structured JSON, render a PDF:

```powershell
python school-research/scripts/render_school_pdf.py school-research/assets/sample_pdf_report.json output/sample_school_report.pdf
```

Use the sample JSON as a shape reference, then replace the sample data with the researched school profile.

## Example 5: Compare Schools Safely

The best comparison workflow is:

1. Produce one source-backed report per school.
2. Keep source logs separate for each school.
3. Compare the final reports on fit, cost, admissions risk, program strength, and deadlines.

This avoids shallow multi-school summaries that hide missing or outdated source evidence.
