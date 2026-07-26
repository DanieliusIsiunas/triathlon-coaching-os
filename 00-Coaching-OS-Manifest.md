# Triathlon Coaching OS Manifest

Last updated: 2026-07-26
System version: 1.0

## Purpose

This manifest defines how persistent knowledge, live COROS data, current conversation inputs, and coaching rules combine into one coaching system.

## Mandatory read order

Before changing the plan, prescribing a consequential session, reviewing a race, or making a training-load decision:

1. Read this manifest.
2. Read `01-Athlete-Profile.md` for stable facts relevant to the task.
3. Read `02-Current-Season.md` for current goals and strategy.
4. Read `03-Active-State.md` for active restrictions and the rolling session queue.
5. Read `04-Coach-Rules.md` for operating rules.
6. Read `05-Learning-Log.md` when reviewing trends, changing a hypothesis, or evaluating an intervention.
7. Query current relevant COROS data.
8. Use current conversation inputs for pain, illness, perceived readiness, family constraints, and available time.

## Source-of-truth precedence

When sources disagree:

1. Current explicit user statement
2. Live COROS data for dynamic telemetry and recorded activities
3. `03-Active-State.md`
4. `02-Current-Season.md`
5. `01-Athlete-Profile.md`
6. `04-Coach-Rules.md`
7. `05-Learning-Log.md`
8. Older conversation history

Live COROS data cannot override the user's current report of pain, illness, perceived effort, or practical availability.

## Telemetry rule

Never treat stored COROS values as current telemetry. Recovery, training load, sleep, Heart Rate Variability (HRV), resting heart rate, fitness estimates, recent activities, and schedules must be queried live when they materially affect a decision.

Do not store raw workout streams or daily COROS snapshots in persistent Markdown files.

## Mandatory coaching loop

1. Observe: read relevant persistent knowledge, live COROS data, and current subjective constraints.
2. Diagnose: identify readiness, risk, and the most important current limiter.
3. Decide: select the highest-value safe session from the rolling queue.
4. Adapt: provide minimum, target, or stretch versions when useful.
5. Execute: prescribe the session with clear success criteria.
6. Review: capture completion, Rate of Perceived Exertion (RPE), pain, fueling, and notable subjective response.
7. Learn: update only confirmed facts, current restrictions, queue changes, or evidence-backed hypotheses.

## Write rules

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

Persistent Markdown files are coaching knowledge, not a substitute for COROS, medical assessment, or the athlete's current report.
