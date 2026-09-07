# Coaching Operating System Changelog

## 2026-07-26 - Coaching integration migration

- Migrated the `coach-triathlon` skill from the retired Library state-file model to the canonical GitHub manifest workflow.
- Migrated morning and weekly scheduled coaching tasks to the version 1.2 read order and source-of-truth precedence.
- Added higher-risk session gates for current subjective readiness, pain, illness, and available time.
- Required scheduled outputs to audit manifest version, active-state freshness, latest COROS activity, and rolling-queue confirmation.
- Kept weekly queue proposals provisional until explicit athlete confirmation.

## 2026-07-26 - v1.2 finalized operating structure

- Moved canonical coaching knowledge into `knowledge/`.
- Kept `README.md`, `PROJECT-INSTRUCTIONS.md`, and `CHANGELOG.md` at the repository root.
- Added `templates/race-review.md` and `templates/weekly-review.md`.
- Defined `reviews/races/` as the location for completed race reviews.
- Updated all operating references to use canonical repository paths.
- Activated Coaching Operating System version 1.2 as the ready-to-use structure.

## 2026-07-26 - v1.0

- Promoted the modular Coaching Operating System from prototype v0.2 to canonical v1.0.
- Added explicit source-of-truth precedence including `04-Coach-Rules.md`.
- Confirmed that current user reports govern pain, illness, perceived effort, and practical availability.
- Removed all stored live COROS telemetry from the canonical knowledge set.
- Confirmed Druskininkai as Olympic distance: 1.5 km swim, 40 km bike, 10 km run.
- Retired all monolithic `Triathlon-Coach-State.md` files and the compatibility index.
- Retired `06-Project-Instructions-Patch.md` after its content was installed as Project Instructions.
- Added canonical inventory and migration rules.

## 2026-07-26 - GitHub persistence migration

- Established `DanieliusIsiunas/triathlon-coaching-os` as the canonical mutable persistent knowledge store.
- Defined the ChatGPT Project, GitHub repository, and COROS MCP system boundary.
- Project Sources are no longer the canonical state store.

## 2026-09-07 - v1.3 evidence-driven coaching and instruction consolidation

- User approved methodical implementation of the Bu-informed recommendations with tidy, non-competing instructions.
- Established one detailed policy owner in Coach Rules and one version/authority owner in the manifest. Project entry text is a thin router; root manifest compatibility remains.
- Replaced accumulated Active State telemetry and expired pre-race directions with the confirmed recovery queue, unresolved symptoms and next decisions. Preserved session ceilings and recovery dependencies; no training block or benchmark activated.
- Reconciled calf, fueling, swim confidence, aerobar and fatigue outcomes; distinguished observed tolerance from unproven mechanisms. Corrected the historical review's cadence inference and removed its competing live prescriptions.
- Added session purpose/success/ceiling/progression, limited active investigations, falsification/review triggers, and expected-versus-observed coaching accountability.
- Added capability mapping and inactive standardized benchmark designs to Current Season without changing race targets, running frequency ceiling or confirmed recovery status.
- Updated existing review templates; no backup state or parallel policy document created.
- Added `scripts/validate_os.py` and `tests/coaching-scenarios.md`. Structural checks passed, including four injected regressions (missing owner, broken link, duplicated version and telemetry leakage). Ten cases were reviewed against the policy; four were independently exercised through the thin skill using an offline snapshot, with no live mutations, and met the required behaviors.
- Runtime limitations: no current telemetry or symptom clearance obtained during this architecture revision. Behavioral evaluation is not deterministic validation of clinical judgment or proof of training effectiveness. First real adopted-block effectiveness review remains pending.
- Integration boundary: the supplied legacy Project settings still resolve the manifest and are compatible. The replacement `PROJECT-INSTRUCTIONS.md` must be applied manually to settings when no settings-edit capability is available. External skill/task save verification is recorded below when completed.
