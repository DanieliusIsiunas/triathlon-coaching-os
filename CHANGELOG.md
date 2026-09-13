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
- Project settings integration completed on 2026-09-07: Danielius confirmed replacing the legacy instructions and supplied a screenshot matching the maintained `PROJECT-INSTRUCTIONS.md` body. Removed the pending manual-integration note from README; completion is based on the user report and visible screenshot.
- Integration verification completed: the coaching skill was committed and pushed, fetched back and matched against the saved version; its superseded local decision-policy file is absent. Both existing coaching task prompts now route to canonical policy; readback confirmed their prompts and preserved schedules, timezone, titles and enabled status. Unrelated tasks were unchanged. All 14 revised repository files matched their published content after the atomic revision.

## 2026-09-12 - v1.4 block contract and learning-loop closure

- Added one compact current block contract to Active State. A development block now records its capability, linked investigation, intervention/exposure, expected response, evidence plan, constraints, decision options and a 4-6 week or earlier evidence-based review trigger only after the block and queue are confirmed.
- Kept the existing weekly task as the sole scheduled planner. Standard weekly reviews continue normally; due contracts invoke a deeper block-review mode before the next provisional block and queue are proposed. No separate monthly planner or recurring block-report archive was created.
- Defined block closure as an expected-versus-observed decision review, including actual exposure, benchmark comparability, duration effects, symptoms and delayed recovery, subsequent key-session quality, enjoyment, family fit, reporting burden and coaching usefulness. Noisy evidence supports repeating or revising measurement, not forced progression.
- Reconciled the Current Season benchmark framework and Learning Log with the contract. Removed the duplicate monthly submaximal protocol in favor of the existing RUN-E reference and repaired L1's invalid status while retaining the supported efficiency subfinding and unresolved limiter.
- Compacted Active State, removing completed daily telemetry while preserving current calf, shoulder and right-foot restrictions, the confirmed recovery queue and next decision requirements. This repaired the three pre-change validator errors and the size warning.
- Extended structural validation for one current block contract, allowed contract states, canonical closure policy and weekly block-review fields. Six injected regressions were detected as intended. Reviewed all 14 behavioral scenarios, including four new block-boundary cases. Final local validation passed with zero structural errors, zero size warnings and a clean diff check.
- Updated and read back the existing weekly automation prompt so it checks the block contract and invokes canonical block-review mode only when due. Its title, schedule, timezone and enabled state were preserved; the morning task and unrelated automations were unchanged.
- Runtime limitation: this architecture revision did not establish current recovery, activate a development block or prove the new loop effective. Real-use validation remains pending until the first adopted block closes.

## 2026-09-13 - v1.5 progression and underdosing balance

- Danielius confirmed that the prior coaching balance had become too conservative despite a sustained 4-6 hour weekly allocation, favorable recovery and repeated tolerance of work above prescribed ceilings.
- Added a progression and underdosing guardrail. Target doses now govern normal ready weeks; minimums are continuity fallbacks, and holding a development dose requires concrete evidence.
- Required at least one meaningful progression or planned quality stimulus across each 7-14 day period in an active block, while preserving actual warning-sign and recovery protections.
- Added weekly comparison of available budget, prescribed dose and completed exposure. Repeated favorable overshoot must be considered evidence of underestimated prescription, not only non-adherence.
- Activated the 2026-09-14 through 2026-10-11 run-development and dose-recalibration block at 4 hours minimum, about 5 hours 15 minutes target and 6 hours maximum, with three runs, two swims and one bike per complete cycle.
- Added four behavioral regression scenarios and deterministic checks for the new rule and weekly-review field. Real-use effectiveness remains pending until the 2026-10-11 block review.
