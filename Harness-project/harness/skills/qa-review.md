# QA Review Checklist

Use this checklist to review observable behavior and missing verification.

- Trace each normal user flow from request through response and persisted state.
- Build a coverage matrix from the analyst's important execution paths and check
  every path for normal, invalid, boundary, unauthorized, not-found, and failure
  behavior where applicable.
- Check invalid, missing, duplicate, malformed, and boundary inputs.
- Check unauthenticated, unauthorized, and stale-session behavior where relevant.
- Inspect not-found, database-error, and unexpected-state handling.
- Compare validation and behavior across related create, read, update, and delete
  paths.
- Identify ambiguous or inconsistent status codes, redirects, and user feedback.
- Locate existing tests before describing coverage gaps.
- Tie every proposed test to a concrete behavior, branch, or regression risk.
- Check cross-flow consistency, including create/update validation, stale state,
  redirects, status codes, and user-visible error behavior.

Do not equate missing tests with a confirmed runtime bug. Report those items in
QA/Test Gaps unless the code itself demonstrates incorrect behavior.
