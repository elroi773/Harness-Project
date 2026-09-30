# Review Guardrails

These rules apply to every stage of the code-review workflow.

## Boundaries

- Review only. Never modify application code, templates, schema, tests, fixtures,
  configuration, dependencies, or application behavior.
- Never access, read, quote, summarize, or reference any `ground_truth.md` file.
- Read only files needed to understand and verify the application.
- Do not invent files, runtime behavior, vulnerabilities, test results, or code
  locations.

## Evidence

- Support every finding with current code evidence and an exact file/location.
- Distinguish confirmed defects or risks from optional improvement suggestions.
- Do not infer exploitability or impact beyond what the implementation supports.
- Do not claim that tests, commands, or flows were executed unless they actually
  were. Record what was inspected and what, if anything, was run.

## Review conduct

- Preserve independent specialist analysis until the reviewer merges results.
- Every specialist candidate must have a unique, stable source ID. Use `SEC-###`
  for Security, `QA-###` for QA, and `CQ-###` for Code Quality findings.
- Preserve source IDs unchanged through reviewer and validator artifacts so every
  final item can be traced to its originating specialist finding or findings.
- The reviewer may merge and deduplicate findings but may not create new ones.
- The reviewer must account for every specialist source ID in its merge log. No
  specialist finding may disappear without a recorded disposition and reason.
- The validator must check every merged finding against the current code and
  issue exactly one `CONFIRMED` or `REJECTED` decision for it.
- Reject unsupported, obsolete, duplicate, or materially overstated findings.
- Use severity labels consistently: Critical, High, Medium, or Low.
- Do not expose hidden chain-of-thought or private reasoning. Expose only concise
  code evidence, dispositions, decision reasons, and requested summaries.

## Final report

Use exactly these Markdown headings, once each and in this order. Do not add any
other headings at any level before, between, inside, or after them:

1. `## Confirmed Findings`
2. `## QA / Test Gaps`
3. `## Code Quality Findings`
4. `## Validation Summary`

Only validator-confirmed items may appear in the first three sections. Preserve
the merged finding ID and all source IDs on every displayed item. If a section
has no confirmed items, write `None.` under its heading.

`Validation Summary` must include the counts `specialist findings proposed`,
`duplicates merged`, `findings rejected`, and `findings confirmed`. It must also
include the reviewer's concise source-ID disposition log for every specialist
finding and the validator decision record for every merged finding: finding ID,
`CONFIRMED` or `REJECTED`, code evidence, and reason.
