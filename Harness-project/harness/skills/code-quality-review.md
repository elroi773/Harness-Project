# Code Quality Review Checklist

Use this checklist to identify concrete maintenance risks.

- Duplication: repeated logic likely to drift or require synchronized changes.
- Responsibility: functions or modules mixing unrelated concerns.
- Maintainability: hidden assumptions, scattered policy, and brittle change paths.
- Readability: unclear names, control flow, or intent that impedes correct changes.
- Coupling: avoidable dependence between routes, persistence, templates, or global
  state.
- Database access: connection lifecycle, row handling, transaction boundaries,
  repeated queries, and consistency of persistence behavior.
- Dead code: unreachable, unused, redundant, or misleading implementation.
- Coverage discipline: inspect each important module identified by the analyst,
  and explicitly report when no concrete maintainability issue is supported.
- Change scenarios: test each candidate mentally against a realistic maintenance
  task and report the specific drift, coupling, or regression risk it creates.

Do not report formatting taste as a finding. Explain the realistic maintenance or
correctness consequence and recommend the smallest proportionate improvement.
