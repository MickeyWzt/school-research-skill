# School Research Skill

`school-research` is a Codex/Claude-style skill for deep research on one specific school, college, university, boarding school, international school, or academic program.

It is designed for application planning tasks where a user names a school and wants a source-backed profile covering admissions, program fit, cost, scholarships, student life, outcomes, risks, and next actions.

## What It Does

- Confirms the exact school, campus, program, applicant category, and entry cycle.
- Prioritizes official sources such as admissions, department, tuition, financial aid, international student, student life, and official data pages.
- Attempts a minimum deep-research source set before calling a report "deep research."
- Labels facts as `verified`, `inferred`, or `unclear`.
- Produces quick school profiles, deep due-diligence reports, application checklists, source logs, and risk registers.
- Outputs in Chinese when the user writes in Chinese, while preserving official English names.

## Included Files

```text
school-research/
  SKILL.md
  assets/
    single_school_profile.csv
  references/
    output-templates.md
    research-standards.md
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

## License

MIT
