# Triathlon Coaching OS

Danielius's canonical coaching knowledge. Start with [the manifest](knowledge/00-Coaching-OS-Manifest.md); it owns the current version, authority and file inventory. [Coach Rules](knowledge/04-Coach-Rules.md) owns coaching decisions and review behavior.

## Navigation

- [Athlete Profile](knowledge/01-Athlete-Profile.md): stable facts and preferences.
- [Current Season](knowledge/02-Current-Season.md): targets, strategy and inactive benchmark designs.
- [Active State](knowledge/03-Active-State.md): current restrictions and confirmed queue.
- [Learning Log](knowledge/05-Learning-Log.md): questions, evidence, outcomes and review triggers.
- [Race reviews](reviews/races/): historical evidence.
- [Weekly template](templates/weekly-review.md) and [race template](templates/race-review.md): output fields.
- [Project entry point](PROJECT-INSTRUCTIONS.md): the short instruction block for Project settings.
- [Changelog](CHANGELOG.md): architecture changes and verification history.

## Validation

Run `python3 scripts/validate_os.py` from the repository. The checker uses Python's standard library and validates owned paths, internal file links, version ownership, compact entry points, learning fields and selected telemetry/legacy-state regressions. It exits nonzero on structural errors and reports size warnings.

Then evaluate [coaching scenarios](tests/coaching-scenarios.md), inspect the full diff for changed safety/authority semantics and verify the saved revision. These are complementary checks: a structural pass does not prove correct coaching or predict training outcomes. No automatic remote check is claimed; run the checker before architecture changes and during relevant maintenance.

## Integration boundary

The personal coaching skill and existing morning/weekly tasks should fetch the manifest and use the canonical rules. Their schedules are independent of policy revisions. The root manifest pointer remains for older entry points.

`PROJECT-INSTRUCTIONS.md` is the maintained replacement text for ChatGPT Project settings; editing this repository file does not edit the actual Project settings. The currently supplied legacy Project instructions still route through the root manifest and are compatible, but contain redundant rules. Replacing that settings text with the short entry point is a manual integration step when no Project-settings tool is available.

## Maintenance scope

Keep one owner per responsibility. Git history retains removed detail; do not create backup state files. Daily telemetry stays in COROS; conversation supplies current subjective state. Benchmarks remain designs until activated in a confirmed queue through current readiness gates.
