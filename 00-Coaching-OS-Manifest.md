# Triathlon Coaching OS Manifest

Last updated: 2026-07-26
System version: 1.1
Canonical repository: `DanieliusIsiunas/triathlon-coaching-os`

## Purpose

This manifest defines how persistent GitHub knowledge, live COROS data, current conversation inputs, and coaching rules combine into one coaching system.

## Canonical-store rule

The default branch of `DanieliusIsiunas/triathlon-coaching-os` is the canonical mutable persistent coaching store.

Uploaded Project Sources, prior attachments, sandbox artifacts, downloaded copies, and older conversation excerpts are not canonical when the repository is available. They may be used only as historical evidence or migration inputs.

## Mandatory read order

Before changing the plan, prescribing a consequential session, reviewing a race, or making a training-load decision:

1. Fetch and read this manifest from the canonical GitHub repository.
2. Fetch `01-Athlete-Profile.md` for stable facts relevant to the task.
3. Fetch `02-Current-Season.md` for current goals and strategy.
4. Fetch `03-Active-State.md` for active restrictions and the rolling session queue.
5. Fetch `04-Coach-Rules.md` for operating rules.
6. Fetch `05-Learning-Log.md` when reviewing trends, changing a hypothesis, or evaluating an intervention.
7. Query current relevant COROS data.
8. Use current conversation inputs for pain, illness, perceived readiness, family constraints, and available time.

## Source-of-truth precedence

When sources disagree:

1. Current explicit user statement
2. Live COROS data for dynamic telemetry and recorded activities
3. Current `03-Active-State.md` from the canonical repository
4. Current `02-Current-Season.md` from the canonical repository
5. Current `01-Athlete-Profile.md` from the canonical repository
6. Current `04-Coach-Rules.md` from the canonical repository
7. Current `05-Learning-Log.md` from the canonical repository
8. Older conversation history, Project Sources, attachments, or generated artifacts

Live COROS data cannot override the user's current report of pain, illness, perceived effort, or practical availability.

## Telemetry rule

Never treat stored COROS values as current telemetry. Recovery, training load, sleep, Heart Rate Variability (HRV), resting heart rate, fitness estimates, recent activities, and schedules must be queried live when they materially affect a decision.

Do not store raw workout streams or daily COROS snapshots in persistent Markdown files.

## Mandatory coaching loop

1. Observe: read relevant current repository knowledge, live COROS data, and current subjective constraints.
2. Diagnose: identify readiness, risk, and the most important current limiter.
3. Decide: select the highest-value safe session from the rolling queue.
4. Adapt: provide minimum, target, or stretch versions when useful.
5. Execute: prescribe the session with clear success criteria.
6. Review: capture completion, Rate of Perceived Exertion (RPE), pain, fueling, and notable subjective response.
7. Learn: update only confirmed facts, current restrictions, queue changes, or evidence-backed hypotheses.

## Write protocol

For every persistent change:

1. Identify the single canonical file whose responsibility changed.
2. Fetch its current content and blob SHA from GitHub.
3. Apply the smallest coherent replacement to that file.
4. Update the existing path; do not create duplicates or timestamped substitutes.
5. Use a descriptive commit message that states the confirmed coaching-state change.
6. Re-fetch the file when verification is materially important.

## File ownership rules

- Update `01-Athlete-Profile.md` only after a confirmed stable fact, long-term constraint, injury history, equipment, or preference changes.
- Update `02-Current-Season.md` after a confirmed goal, race, phase, strategy, or durable availability assumption changes.
- Update `03-Active-State.md` after a confirmed current restriction, symptom status, rolling-queue change, or immediate planning decision.
- Update `04-Coach-Rules.md` only when the operating protocol changes.
- Append or resolve entries in `05-Learning-Log.md` after a meaningful hypothesis, intervention, race review, or validated personal response pattern.
- Append system architecture changes to `CHANGELOG.md`.
- Resolve or remove temporary restrictions once they are no longer current.
- Do not preserve uncertainty as fact. Label hypotheses and confidence explicitly.

## Required inputs before higher-risk sessions

Before prescribing a run, hard bike session, brick, long session, or return after pain, collect or infer what remains unknown:

- Sleep quality: 1-5
- Energy: 1-5
- Soreness: 1-5
- Current pain: location and 0-10
- Illness symptoms: yes/no
- Available training time

Do not repeat questions already answered in the current conversation or available from live sources.

## System boundary

GitHub Markdown files are durable coaching knowledge. COROS is the live objective telemetry source. The current conversation is the source for subjective symptoms and practical constraints. None substitutes for medical assessment when warning signs are present.
