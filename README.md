# Task Manager — Agile & DevOps Lab

## Product Vision
A lightweight task manager that helps individuals track daily to-dos: add tasks, mark them complete, and remove what's no longer needed, without the overhead of a complex project management tool.

## Data Model

## Product Backlog

| # | User Story | Points |
|---|---|---|
| US1 | As a user, I want to add a new task with a title, so that I can capture something I need to do. | 3 |
| US2 | As a user, I want to view a list of all my tasks, so that I can see everything I need to do at a glance. | 2 |
| US3 | As a user, I want to update a task's status to complete, so that I can track my progress. | 2 |
| US4 | As a user, I want to delete a task, so that I can remove items I no longer need. | 2 |
| US5 | As a user, I want to check the health of the service via a health endpoint, so that I know the system is running correctly. | 1 |

**Total backlog: 10 points**

## Acceptance Criteria

**US1 — Add a task**
* Given a non-empty `title` string, a task is created with `completed = false`.
* Each created task returns an auto-generated integer `id` that is not null.
* Given an empty or missing `title`, the API returns an error response.

**US2 — View all tasks**
* A GET request returns a list of all existing tasks.
* If no tasks exist, an empty list is returned (not an error).

**US3 — Mark a task complete**
* Given a valid task `id`, the task's `completed` field is updated to `true`.
* Given an invalid/non-existent `id`, the API returns a 404-style error.

**US4 — Delete a task**
* Given a valid task `id`, the task is removed from storage and no longer appears in the task list.
* Given an invalid `id`, the API returns an error.

**US5 — Health check**
* A GET request to `/health` returns HTTP 200 with a response body confirming status.

## Definition of Done
1. Code is written and committed to Git with a clear, descriptive commit message
2. Each commit represents a small, working increment
3. At least one automated test covers the story's main behavior
4. The CI pipeline passes (build + test)
5. The feature works exactly as described in its Acceptance Criteria
6. No hardcoded/broken values left in the code

## Sprint Plan
* **Sprint 1:** US1, US2, US3 (7 points) — add → view → complete flow
* **Sprint 2:** US4, US5 (3 points), plus improvements from Sprint 1 retrospective