# Review Policy & Git Workflow

This policy defines our rules for branch management, commits, Pull Request (PR) creation, and code reviews to ensure clarity and quality in our deliverables.

---

## 1. Task Management (Kanban)

- Before starting work on any feature or fix, always create the corresponding issue on the GitHub Project Kanban board.
- Ensure the issue is properly detailed and scoped before starting development.

---

## 2. Branching Strategy

Our team workflow is structured around daily branches created from the `main` branch (`J1`, `J2`, `J3`, etc.).

### Local Workflow:

1. Start from the active daily branch of the day (e.g., `J1`).
2. Create a sub-branch dedicated to your feature:
   ```bash
   git checkout -b feature/<feature-name> J1
   ```
3. Once the work is complete, open a Pull Request (PR) from your feature branch to the daily branch (e.g., `feature/...` -> `J1`).

---

## 3. Commit Messages

We enforce the Conventional Commits standard to maintain a clear and readable history.

- **Mandatory format:** `<type>: <description>`
- **Main types:** `feat`, `fix`, `docs`, `refactor`, `ci`, `test`, `chore`.
- **Example:**
  ```bash
  git commit -m "fix: correct authentication token expiration handling"
  ```

---

## 4. Pull Requests & Review Process

### PR Submission

- Fill out the project's PR Template.
- **Mandatory Issue Linking:** Link the corresponding ticket in the PR using a GitHub keyword to automatically close the issue upon merging (e.g., `Closes #123` or `Fixes #123`).

### Review & Validation

1. **Assigning the Reviewer:** The PR must be assigned to today's Product Owner (PO).
2. **Review & Approval:** Merging into the daily branch is only permitted once the PR has been approved by the PO.
3. **Merge:** Merging will automatically close the linked issue on the Kanban board.