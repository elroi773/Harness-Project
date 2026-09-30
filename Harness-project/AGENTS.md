# Code Review Harness

This repository includes a review-only harness under `harness/`.

## Trigger

Automatically activate the full `harness/workflows/code-review.md` workflow for
any ordinary project-wide code-review request that asks to identify problems,
risks, defects, vulnerabilities, test gaps, maintainability issues, or ways the
code should be improved. The user does not need to mention the harness or ask for
a structured review.

This exact request must trigger the full workflow: "Review this project and
identify problems in the code and how they should be improved."

Every triggered review must run all stages in order: Analyst, independent
Security / QA / Code Quality passes, Reviewer, Validator, then Final Report.

The final report must use exactly these sections in order:

- `## Confirmed Findings`
- `## QA / Test Gaps`
- `## Code Quality Findings`
- `## Validation Summary`

Specialist source IDs, reviewer merge dispositions, and validator decisions must
remain traceable in the final `Validation Summary` as defined by the workflow.
Only validator-confirmed findings may appear in the first three sections.

Do not activate the workflow when the user is only creating, editing, or
explaining the harness and has explicitly said not to perform the review yet.

## Required instructions

Before running the workflow, read and follow:

1. `harness/rules/review-guardrails.md`
2. `harness/workflows/code-review.md`

The workflow identifies the role and review-skill files required for each stage.
Treat those files as instructions for their stage, not as application source.

## Scope

- The harness is for review only. Do not modify application code or behavior.
- Do not access, read, quote, summarize, or reference any `ground_truth.md` file.
- Keep specialist passes independent until the reviewer stage.
- Require the validator stage before presenting a final review.
- Every confirmed finding must cite evidence from the current application code.
