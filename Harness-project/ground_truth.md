# Ground Truth — Intentional Issues

This file is for evaluation only. Do not reference it from the application.

---

## Issue 1: Plaintext Password Storage

- **File:** `app.py` (signup, lines 54–57; login, line 74); `schema.sql` (seed row, line 11)
- **Category:** Security
- **Severity:** Critical
- **Description:** Passwords are stored and compared as plaintext. A database dump immediately exposes every user's password.
- **Expected fix:** Hash passwords with `werkzeug.security.generate_password_hash` on write and `check_password_hash` on verify.

---

## Issue 2: Hardcoded Weak Secret Key

- **File:** `app.py`
- **Line:** 6
- **Category:** Security
- **Severity:** High
- **Description:** `app.secret_key = 'secret'` is trivially guessable. An attacker who knows the key can forge arbitrary session cookies, including `is_admin=True`.
- **Expected fix:** Load a long random key from an environment variable: `app.secret_key = os.environ['SECRET_KEY']`.

---

## Issue 3: Insecure Direct Object Reference (IDOR) on Edit Profile

- **File:** `app.py`
- **Lines:** 107–125
- **Category:** Authorization
- **Severity:** High
- **Description:** `edit_profile()` checks only that the requester is logged in; it does not verify that `session['user_id'] == user_id`. Any authenticated user can modify any other user's profile by visiting `/profile/edit/<victim_id>`.
- **Expected fix:** Add `if session['user_id'] != user_id: return 'Forbidden', 403` before processing the request.

---

## Issue 4: Mass Assignment / Privilege Escalation via Hidden Field

- **File:** `app.py` (line 118); `templates/edit_profile.html` (line 11)
- **Category:** Authorization
- **Severity:** High
- **Description:** The `is_admin` flag is passed as a hidden HTML form field and written back to the database without restriction. Any user can set `is_admin=1` by modifying the hidden field value before submitting the form, granting themselves admin privileges (effective after next login).
- **Expected fix:** Remove `is_admin` from the form and the UPDATE statement; never accept privilege fields from user input.

---

## Issue 5: Stored XSS via Unsanitized Bio

- **File:** `templates/profile.html`
- **Line:** 8
- **Category:** Security
- **Severity:** High
- **Description:** `{{ user['bio'] | safe }}` bypasses Jinja2's auto-escaping. A bio containing `<script>alert(1)</script>` executes in every viewer's browser.
- **Expected fix:** Remove `| safe`; Jinja2's default auto-escaping is sufficient. If rich formatting is needed, use a whitelist-based sanitizer.

---

## Issue 6: Debug Mode Enabled

- **File:** `app.py`
- **Line:** 150
- **Category:** Security / Configuration
- **Severity:** Medium
- **Description:** `app.run(debug=True)` enables the interactive Werkzeug debugger. If an unhandled exception occurs in production, any visitor gets a REPL with arbitrary Python execution capability.
- **Expected fix:** Set `debug=False` (or omit it); control debug mode via the `FLASK_DEBUG` environment variable outside the source file.

---

## Issue 7: Username Enumeration via Distinct Login Error Messages

- **File:** `app.py`
- **Lines:** 76–83
- **Category:** Security / Information Disclosure
- **Severity:** Medium
- **Description:** After a failed login, the app distinguishes "No account with that username." from "Incorrect password." This lets an attacker enumerate valid usernames with a single request per candidate.
- **Expected fix:** Return a single generic message: "Invalid username or password."

---

## Issue 8: Unauthenticated Profile View (Information Disclosure)

- **File:** `app.py`
- **Lines:** 98–104
- **Category:** Authorization
- **Severity:** Medium
- **Description:** `profile()` has no session check. Any unauthenticated visitor can view any user's email, bio, and account metadata by guessing sequential integer IDs (`/profile/1`, `/profile/2`, …).
- **Expected fix:** Add a login guard; or at minimum avoid exposing PII such as email to unauthenticated viewers.

---

## Issue 9: No CSRF Protection on Mutating Endpoints

- **File:** `app.py` (lines 107–125, 137–144); all POST forms in templates
- **Category:** Security
- **Severity:** Medium
- **Description:** None of the POST routes (`edit_profile`, `delete_user`) validate a CSRF token. An attacker can craft a page that silently submits these forms on behalf of a logged-in victim (including admin deletion of other accounts).
- **Expected fix:** Use Flask-WTF or manually generate and validate a per-session CSRF token on every state-changing form.
