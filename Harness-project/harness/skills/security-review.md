# Security Review Checklist

Use this checklist as a focused aid, not as evidence by itself.

- Authentication: credential storage, login checks, account lifecycle, and
  user-enumeration behavior.
- Authorization: ownership and role checks on every protected read or mutation.
- Sessions: secret handling, session contents, invalidation, and trust boundaries.
- Input handling: type, length, format, allow-listing, and server-side validation.
- Injection: SQL, command, template, path, header, and other interpreter boundaries.
- XSS: escaped output, explicitly trusted markup, and stored or reflected content.
- CSRF: state-changing requests, tokens, HTTP methods, and cookie assumptions.
- Sensitive data: secrets, credentials, personal data, logs, and seeded defaults.
- Configuration: debug settings, production defaults, error disclosure, and secure
  deployment assumptions.

For every candidate issue, trace attacker-controlled input to the affected sink
or trust decision. Downgrade uncertain concerns to suggestions and state what
evidence would be needed to confirm them.

