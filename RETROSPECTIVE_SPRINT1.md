# Sprint 1 Retrospective

## What Went Well
- All 3 planned backlog items (US1, US2, US3) were delivered successfully, meeting all defined acceptance criteria.
- Commit history stayed clean and incremental throughout, no large "big-bang" commits, each commit represented one function, one endpoint, or one group of tests.
- Test isolation was set up correctly from the start (using pytest fixtures + monkeypatch), meaning every test runs against a fresh, independent database with no shared state between tests.
- The CI pipeline was set up successfully on the first real attempt and passed immediately, confirming the test suite works correctly outside of the local development environment, not just "on my machine."
- Manual testing with curl before writing automated tests helped catch expected behavior early, before formalizing it into pytest assertions.

## What Didn't Go Well / Issues Encountered
- Sprint 0 planning (product vision, backlog, acceptance criteria) was fully decided before any code was written, but the actual `README.md` documentation of that planning wasn't committed until partway through Sprint 1 implementation. This means the commit history doesn't accurately reflect the true order of the Agile process, even though the process itself was followed correctly.
- Two stray, unintended files (`clear`, `reminder`) were accidentally committed to the repository early on, likely from misdirected terminal output and a personal note. This happened because `.gitignore` was briefly placed in the wrong folder, and file additions weren't being carefully reviewed with `git status` before each `git add`.
- One early pytest run failed due to a Python import path issue (`ModuleNotFoundError`), caused by not running pytest through `python -m pytest`. This was resolved by adding a `pytest.ini` file, but it revealed a gap in initially understanding how Python's module resolution works across different invocation methods.

## Improvements for Sprint 2
1. **Document planning before implementation, not during it.** For Sprint 2, backlog updates and any new acceptance criteria will be committed to the repo before writing any new code, so the commit history accurately reflects the real Agile order: plan first, build second.
2. **Review `git status` carefully before every `git add`.** Rather than defaulting to `git add .`, check what's actually being staged first, to catch stray or accidental files before they enter version control, not after.
3. **Address the Node.js deprecation warning in CI.** The pipeline logs surfaced a warning about `actions/checkout@v4` and `actions/setup-python@v5` running on a soon-to-be-unsupported Node version. This will be proactively upgraded in Sprint 2 to prevent a future pipeline failure, rather than waiting for it to break.

## Action Items Carried Into Sprint 2
- [ ] Commit Sprint 2 backlog/planning updates to README before starting implementation
- [ ] Manually review `git status` output before staging changes
- [ ] Upgrade GitHub Actions dependency versions to clear deprecation warning