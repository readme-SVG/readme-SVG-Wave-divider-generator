# Contributing Guide

First of all, thanks for deciding to contribute. Seriously, this project gets better because engineers like you care enough to improve tiny details that compound into real developer experience wins.

This guide explains how to report bugs, propose features, set up local development, and ship pull requests that are easy to review and merge.

## 1. Introduction

Welcome aboard.

Whether you are fixing a typo, patching wave generation logic, improving frontend UX, or hardening deployment docs, your contribution matters. The goal is simple: keep the project fast, deterministic, and frictionless for anyone who needs embeddable SVG wave dividers.

Core principles:

- Keep changes focused and intentional.
- Prefer deterministic behavior over hidden magic.
- Optimize for maintainability and explicitness.
- Leave the codebase cleaner than you found it.

## 2. I Have a Question

Please do not use GitHub Issues for general usage questions.

Issues are for actionable engineering work (bugs, enhancements, regressions), not support threads. If you have a usage question:

- Use **GitHub Discussions** (if enabled).
- Use community channels linked in `README.md`.
- If relevant, search existing Issues/PRs before asking.

When asking a question, include:

- Your goal (what you are trying to build).
- Your current command/URL/config.
- What you expected vs what happened.
- Minimal reproducible context.

## 3. Reporting Bugs

Great bug reports save everyone time.

Before opening a new bug:

- Search open and closed Issues for duplicates.
- Re-test on the latest `main` branch state.

Use this bug report checklist:

1. **Environment**
   - OS and version (`Ubuntu 22.04`, `macOS 14`, etc.)
   - Python version (`python --version`)
   - Deployment target (`local`, `Vercel preview`, `Vercel production`)
   - Browser version (if UI-related)
2. **Steps to Reproduce**
   - Exact commands and/or exact `/wave?...` URL.
   - Input values for all relevant parameters.
3. **Expected Behavior**
   - What should have happened.
4. **Actual Behavior**
   - What actually happened (error output, broken SVG, wrong render, etc.).
5. **Evidence**
   - Screenshots/GIF for UI issues.
   - Full logs or stack traces for backend errors.

High-quality report template:

```markdown
### Environment
- OS:
- Python:
- Deployment target:
- Browser:

### Steps to Reproduce
1.
2.
3.

### Expected Behavior

### Actual Behavior

### Additional Context
- URL/params:
- Logs:
- Screenshots:
```

## 4. Suggesting Enhancements

Feature requests are welcome, but they need product and technical context.

A good enhancement proposal includes:

- **Problem statement**: What pain point exists right now?
- **Proposed solution**: What behavior/API should change?
- **Use cases**: Real scenarios where this provides value.
- **Trade-offs**: Complexity, breaking changes, performance impact.

Examples of solid enhancements:

- New wave profile with deterministic math contract.
- Better parameter validation with clearer error responses.
- Structured test suite for generator output invariants.
- Accessibility and UX improvements in the playground.

## 5. Local Development / Setup

### Fork and clone

```bash
# 1) Fork on GitHub, then clone your fork
git clone https://github.com/<your-username>/readme-SVG-wave-divider.git
cd readme-SVG-wave-divider

# 2) Add upstream remote
git remote add upstream https://github.com/readme-SVG/readme-SVG-wave-divider.git
```

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

### Environment variables

This project currently does not require a `.env` for baseline functionality.

If your change introduces environment config:

```bash
cp .env.example .env
```

Document every added variable in `README.md` and keep defaults safe for local execution.

### Run locally

Because this is Vercel-oriented serverless code, common approaches are:

```bash
# Option A: Vercel local runtime (recommended)
vercel dev

# Option B: direct module sanity checks
python -m py_compile api/index.py api/wavegen.py
```

Then test with:

```bash
curl -i "http://localhost:3000/wave?type=smooth&color_top=0d1117&color_bottom=161b22"
```

## 6. Pull Request Process

### Branch naming strategy

Use explicit, scoped branch names:

- `feature/<short-description>`
- `bugfix/<issue-id-or-topic>`
- `docs/<scope>`
- `refactor/<scope>`
- `chore/<scope>`

Examples:

- `feature/add-triangle-smoothing`
- `bugfix/issue-42-invalid-opacity`
- `docs/rewrite-readme`

### Commit message format

Use **Conventional Commits**:

- `feat: add configurable wave seed`
- `fix: clamp invalid frequency values`
- `docs: improve deployment section`
- `refactor: isolate svg gradient builder`

### Keep your branch fresh

Before opening PR:

```bash
git fetch upstream
git rebase upstream/main
```

### PR description requirements

Every PR should include:

- What changed.
- Why it changed.
- Any behavioral or API impact.
- Linked issue(s): `Closes #123` when relevant.
- Visual proof (screenshots/GIF) for UI-affecting changes.
- Test evidence (commands + outputs).

## 7. Styleguides

### Code quality expectations

- Keep functions single-purpose and readable.
- Avoid hidden side effects.
- Prefer explicit validation and clear errors.
- Do not mix unrelated refactors with functional changes.

### Linters and formatters

Current repository does not enforce a strict formatter/linter pipeline yet. If you add one, propose it in a dedicated PR first.

Recommended baseline for contributors:

- Python: `ruff` + `black` (if introduced by consensus)
- JavaScript/CSS/HTML: `eslint` + `prettier` (if introduced by consensus)

### Architecture expectations

- Keep API HTTP handling in `api/index.py`.
- Keep wave generation logic in `api/wavegen.py`.
- Keep UI behavior in `app.js` and styling in `styles.css`.
- Preserve URL-driven deterministic output behavior.

## 8. Testing

New logic should ship with validation evidence.

Minimum expectation:

```bash
python -m py_compile api/index.py api/wavegen.py
curl -i "http://localhost:3000/wave?type=sine&amplitude=25&frequency=2"
```

When adding non-trivial functionality, include test coverage for:

- Parameter parsing and validation behavior.
- SVG path generation correctness constraints.
- Regression scenarios tied to fixed bugs.

## 9. Code Review Process

Typical flow:

1. Maintainer reviews PR for correctness, scope, and maintainability.
2. Feedback is left inline or as review comments.
3. Contributor pushes follow-up commits addressing comments.
4. Once approved and checks pass, PR is merged.

Guidelines for smooth reviews:

- Keep PRs small and focused.
- Respond to every review comment (even if just acknowledging).
- If you disagree, explain technical trade-offs with data.
- Re-request review after updates.

Depending on repo activity, one maintainer approval is usually enough for straightforward changes. Complex or risky changes may require deeper review.

Thanks again for contributing and helping keep this project sharp.
