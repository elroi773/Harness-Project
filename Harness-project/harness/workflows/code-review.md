# Structured Code Review Workflow

This workflow performs a review-only fan-out/fan-in analysis followed by code
validation. Keep all intermediate artifacts in memory unless the user explicitly
asks to save the report.

## Prerequisite

Read `../rules/review-guardrails.md` first. The guardrails override any conflicting
stage instruction.

## 1. Scope analysis

Use `../agents/analyst.md` to inspect the project and produce a scope brief. Do not
produce findings at this stage.

## 2. Independent fan-out

Run these three passes independently from the same analyst scope brief:

- Security: `../agents/security.md` with `../skills/security-review.md`
- QA: `../agents/qa.md` with `../skills/qa-review.md`
- Code quality: `../agents/code-quality.md` with
  `../skills/code-quality-review.md`

Use parallel workers when the runtime supports them. Otherwise, perform isolated
passes sequentially and do not expose one specialist's output to another.

## 3. Fan-in review

Use `../agents/reviewer.md` to merge the three specialist outputs. Deduplicate
overlaps without creating new findings. Preserve every specialist source ID and
produce a disposition for every source finding. The result is a proposed report,
not the final answer.

## 4. Validation

Use `../agents/validator.md` to check every proposed item against the current code.
Issue exactly one `CONFIRMED` or `REJECTED` decision for every merged finding.
Record the finding ID, code evidence, and concise reason for every decision.

## 5. Final output

Present only the validated result with exactly these headings, in this order. Do
not add an introduction, conclusion, or any other heading at any level.

## Confirmed Findings

For each finding include:

- Merged finding ID and source specialist IDs
- Security severity, or QA type, as applicable
- File/location
- Evidence
- Impact
- Recommended improvement

## QA / Test Gaps

List only confirmed QA findings whose type is `test-gap`. Include merged finding
ID, source IDs, type, file/location, evidence, impact, and recommendation. State
whether tests were executed.

## Code Quality Findings

List only confirmed Code Quality findings. Include merged finding ID, source IDs,
type, file/location, evidence, maintainability impact, and recommendation.

## Validation Summary

Include these four labeled counts:

- specialist findings proposed
- duplicates merged
- findings rejected
- findings confirmed

Then include the reviewer's concise disposition for every specialist source ID,
including the target `REV-###` ID and reason for merges or removals. Follow it
with the validator's concise decision record for every merged finding: finding
ID, `CONFIRMED` or `REJECTED`, code evidence, and reason. Present both ledgers as
lists or tables, not additional headings. Note whether tests or commands were
executed and any review limitations.

Only `CONFIRMED` findings may appear in the first three sections. Put confirmed
Security findings and confirmed QA findings other than `test-gap` in `Confirmed
Findings`; preserve each specialist's defined fields rather than inventing a
common category. If a section has no confirmed items, write `None.` Do not
include raw specialist drafts or hidden chain-of-thought/private reasoning.
