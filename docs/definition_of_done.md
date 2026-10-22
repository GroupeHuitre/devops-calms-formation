# Definition of Done

This document defines when a Kanban card is considered **Done**, for each type of deliverable we produce. It complements `docs/review_policy.md` (branching, commits, PR process).

---

## 1. General criteria (any card)

A card can only move to **Done** once:

- The corresponding GitHub Issue is linked to a merged PR (`Closes #...`).
- The PR has been reviewed and approved by the day's Product Owner, as defined in `review_policy.md`.
- CI is green on the merged branch (`ci.yml` / `.gitlab-ci.yml`), or the run is explicitly documented as blocked/not demonstrated if runners were unavailable.
- No invented or unverified claim is left in the deliverable: anything not actually executed is labelled **"not tested"** or **"simulated"**, never presented as done.

---

## 2. Research deliverables (`recherches/module-XX/synthese.md`)

Taken directly from the course's own Definition of Done (`plan-travail.md`):

- At least one **verified source** per answer (link, author/publisher, consultation date).
- A **personal explanation**, in our own words, not copy-pasted from an AI answer.
- A **real business example** (not invented), e.g. a documented incident or case study.
- A concrete **action applied to NovaTech**, tied to a fact or hypothesis from the client dossier.
- **Proof or documented limits**: a result that was actually observed, or an explicit statement that it was not tested.
- **Reviewed by another member**, who can reformulate at least one answer without AI (acquisition criterion from `consignes/03_Consignes_3_jours.md`).

---

## 3. Experimentation deliverables (`experiences/*.md`, `novatech/*.md`)

- Hypothesis, protocol, and **actually observed** result (or explicitly marked as not executed / simulated).
- A traceable proof: commit link, CI run, file path, or dated screenshot (`preuves/`).
- Limits documented: what the result does **not** prove.
- Figures and tables trace back to a real source file in the repo (e.g. `donnees-novatech/*.csv`), not an invented number.

---

## 4. Presentation (`presentation/soutenance-10-slides.md`)

- Exactly 10 slides, each backed by a file or proof that is actually in the repo and consultable live during the defense.
- No claim of a result, test, or metric that cannot be pointed to in the repository.
