# Triathlon Coaching OS

Canonical, versioned coaching knowledge for Danielius's adaptive triathlon system.

## Architecture

The system has three connected components:

1. **ChatGPT Project** — coaching reasoning, current conversation, pain, illness, readiness, family constraints, and available time.
2. **This GitHub repository** — canonical mutable persistent knowledge with full history and CRUD operations.
3. **COROS MCP** — current telemetry, recent activities, recovery, training load, sleep, HRV, resting heart rate, fitness estimates, and schedules.

## Operating contract

Before changing the plan, prescribing a consequential session, reviewing a race, or making a training-load decision:

1. Read `knowledge/00-Coaching-OS-Manifest.md`.
2. Follow its mandatory read order and source-of-truth precedence.
3. Read the relevant current repository files.
4. Query current relevant COROS data.
5. Use the current conversation for subjective symptoms and practical constraints.
6. Update the relevant canonical file after a confirmed durable change.

## Repository structure

- `knowledge/00-Coaching-OS-Manifest.md` — system contract and read/write protocol
- `knowledge/01-Athlete-Profile.md` — stable athlete facts, preferences, history, and equipment
- `knowledge/02-Current-Season.md` — current race, goals, strategy, and durable season assumptions
- `knowledge/03-Active-State.md` — current restrictions, immediate decisions, and rolling session queue
- `knowledge/04-Coach-Rules.md` — coaching decision rules
- `knowledge/05-Learning-Log.md` — meaningful hypotheses, interventions, and validated response patterns
- `reviews/races/` — completed race reviews
- `templates/race-review.md` — race review format
- `templates/weekly-review.md` — weekly review format
- `CHANGELOG.md` — system architecture history
- `PROJECT-INSTRUCTIONS.md` — canonical ChatGPT Project instruction block

## Source-of-truth precedence

1. Current explicit user statement
2. Live COROS data for dynamic telemetry and recorded activities
3. `knowledge/03-Active-State.md`
4. `knowledge/02-Current-Season.md`
5. `knowledge/01-Athlete-Profile.md`
6. `knowledge/04-Coach-Rules.md`
7. `knowledge/05-Learning-Log.md`
8. Historical race reviews
9. Older conversation history and non-canonical artifacts

Live COROS data cannot override Danielius's current report of pain, illness, perceived effort, readiness, or practical availability.

## Telemetry and update rules

Do not store raw workout data or daily COROS telemetry in this repository. Query COROS live whenever current recovery, training load, sleep, HRV, resting heart rate, fitness estimates, recent activities, or schedules materially affect a decision.

GitHub is the canonical mutable store. Update only the file whose responsibility changed. Before updating an existing file, fetch its current content and blob SHA, then replace it with a descriptive commit message.
