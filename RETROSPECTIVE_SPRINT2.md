# Sprint 2 Retrospective

## What Went Well
- All 3 Sprint 1 retrospective improvements were successfully applied: Sprint 2 planning was documented in README before implementation began, `git status` was checked carefully before staging throughout the sprint, and the CI deprecation warning was fully resolved (not just partially patched).
- US4 and US5 followed the same established patterns from Sprint 1 (existence-check-then-act for delete, matching the mark_complete pattern), which made implementation faster and more consistent than Sprint 1, since the conventions were already in place.
- Adding logging surfaced a good learning moment: distinguishing `INFO` (expected success) from `WARNING` (expected failure) from `ERROR` (unexpected system failure) in log levels, rather than logging everything at the same level.
- The CI fix required two separate action version upgrades (checkout, then setup-python), not one. Verifying the fix by re-checking logs after each change, rather than assuming the first change resolved it, caught this properly.

## What Didn't Go Well / Issues Encountered
- The Node.js deprecation warning fix initially looked complete after upgrading only `actions/checkout`, but the warning persisted because `actions/setup-python` also needed upgrading. This was a reminder that CI warnings can involve multiple independent causes, and clearing a warning message fully requires re-verifying after each change, not stopping at the first apparent fix.
- AUTOINCREMENT ID behavior during manual testing (IDs not resetting after deletions) briefly looked like a bug during logging tests, but was confirmed to be correct, expected SQLite behavior. A good reminder to verify assumptions about a tool's behavior before treating something as a defect.

## Overall Project Reflection (Sprint 1 → Sprint 2)
Looking across both sprints: the biggest overall improvement was in commit and documentation discipline. Sprint 1 had planning documentation committed after implementation had already started; Sprint 2 corrected this by documenting the plan first. Sprint 1 also had two stray files accidentally committed due to not reviewing `git status` carefully; no such incidents occurred in Sprint 2, directly due to the improved habit of reviewing status before every `git add`.

Technically, the codebase grew in a consistent, predictable way: every new endpoint followed the same structure as earlier ones (input validation → data layer call → status-coded response), and every new feature was matched with both a manual curl test and an automated pytest test before being considered complete, in line with the Definition of Done established in Sprint 0.

## Final Definition of Done — Project-Wide Status

| DoD Item | Met? |
|---|---|
| All commits have clear, descriptive messages | ✅ |
| Commits represent small, incremental progress | ✅ |
| All 5 user stories have automated test coverage | ✅ |
| CI pipeline passes with zero warnings | ✅ |
| All features match their Acceptance Criteria | ✅ |
| No hardcoded/broken values in final code | ✅ |

All 5 backlog items (US1–US5) are complete, tested, and verified working both locally and in CI.