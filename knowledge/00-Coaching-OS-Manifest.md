# Triathlon Coaching OS Manifest

Last updated: 2026-09-13
System version: 1.5
Canonical repository: `DanieliusIsiunas/triathlon-coaching-os`

## Authority and ownership

The default branch is the canonical mutable coaching store. Current explicit user instructions govern. Uploaded Project Sources, attachments, old conversations, skill copies and local artifacts are historical evidence only when GitHub is available.

Each responsibility has one owner:

| Path | Responsibility |
|---|---|
| `knowledge/00-Coaching-OS-Manifest.md` | Authority, read/write contract, file ownership and integration contract |
| `knowledge/01-Athlete-Profile.md` | Stable facts, preferences, constraints, injury history and equipment |
| `knowledge/02-Current-Season.md` | Goals, season strategy, capability targets and benchmark protocols |
| `knowledge/03-Active-State.md` | Current restrictions, active block contract, confirmed rolling queue and next decision requirements |
| `knowledge/04-Coach-Rules.md` | Coaching policy, live-input requirements, safety, output and review rules |
| `knowledge/05-Learning-Log.md` | Current hypotheses, interventions, benchmark conclusions and retained learning |
| `reviews/races/` | Official results, contextualized historical race evidence and review conclusions |
| `templates/weekly-review.md` | Standard weekly and due block-closure output fields; no independent coaching policy |
| `templates/race-review.md` | Race-review fields; no independent coaching policy |
| `PROJECT-INSTRUCTIONS.md` | Thin project entry point to this manifest |
| `README.md` | Human navigation, validation and integration status |
| `scripts/validate_os.py` | Deterministic structural checks, not a coaching decision engine |
| `tests/coaching-scenarios.md` | Behavioral evaluation cases, not athlete state or session prescriptions |
| `CHANGELOG.md` | Architecture history and validation record |

The root `00-Coaching-OS-Manifest.md` is a compatibility pointer only. Keep detailed policy in its owner; entry points, templates and historical reviews must not become alternative live rulebooks. System version is declared only here.

## Mandatory read order

For a plan change, consequential session, race review, training-load decision or system revision:

1. Fetch this manifest from the default branch; follow the root pointer if that was the entry point.
2. Fetch `knowledge/01-Athlete-Profile.md`.
3. Fetch `knowledge/02-Current-Season.md`.
4. Fetch `knowledge/03-Active-State.md`.
5. Fetch `knowledge/04-Coach-Rules.md`.
6. Fetch `knowledge/05-Learning-Log.md` for trends, hypotheses, interventions, race reviews, weekly reviews or system revisions. Read relevant reviews/templates when needed.
7. Query the live COROS data required by Coach Rules when dynamic telemetry materially affects the decision. An instruction-only revision does not itself clear symptoms, establish readiness or activate a training block.
8. Use current conversation inputs for subjective state and practical constraints.

If required canonical knowledge is inaccessible, name the missing source, do not reconstruct durable state from memory, and avoid the affected plan-level decision. Continue useful read-only work or conservative general guidance with the limitation stated. Apply Coach Rules' degraded-data behavior if COROS is unavailable.

## Source-of-truth precedence

For conflicting athlete facts and state:

1. Current explicit user statement.
2. Live COROS for dynamic telemetry and recorded activities, except official timing is authoritative for race results and verified course information for race distances.
3. Current Active State.
4. Current Season.
5. Athlete Profile.
6. Coach Rules as general defaults, not evidence of an athlete fact.
7. Learning Log.
8. Historical race reviews.
9. Older conversation, Project Sources, attachments or generated artifacts.

Live data never overrides the user's current pain, illness, effort, readiness or availability. A proposed queue cannot override a confirmed queue. A historical review does not prescribe today's session. Rules belong to Coach Rules; the precedence above is not permission for stale prose to override safety or operating policy.

## Coaching loop

Observe -> distinguish facts from hypotheses -> establish a confirmed block contract when development begins -> choose the highest-value safe feasible stimulus -> define purpose, success, ceiling and progression -> review actual execution and next-day response -> close the block against its expected result when due -> update the owning file.

Evaluate whole-race capability and sustainable participation. Coach Rules defines the decisions and evidence standards for this loop.

## Persistence and cleanup

- Persist confirmed durable changes to goals, strategy, constraints, symptoms, equipment, preferences, hypotheses, intervention outcomes and race reviews. A direct user report confirms that report; do not ask again merely to record it. New training queues require confirmation unless the user has already authorized that exact change.
- Fetch each target's current content and blob SHA before writing. Update the same path with the smallest coherent replacement. Reconcile intervening edits; never overwrite them blindly.
- For a multi-file architecture revision, validate the complete revision and prefer one atomic commit based on the current tree. Verify target blob SHAs, recheck the branch head, and use a non-forced fast-forward update; rebuild on concurrent changes. For single-file updates use its current blob SHA.
- Use descriptive commits as the audit trail. Append architecture changes to `CHANGELOG.md`; verify saved content before claiming success.
- Do not store raw workout streams, daily wellness values or daily COROS telemetry in Markdown. Keep dates/references and the minimum contextual evidence needed for durable learning or a benchmark conclusion. Race results and race-specific fueling evidence belong in race reviews.
- Active State holds only unresolved restrictions, the current block contract, the confirmed queue and immediate decisions. Remove completed sessions and expired calendar instructions after retaining any durable conclusion in its owner. Close or replace a completed block contract rather than accumulating block history there. Absence of a new symptom report is not proof of recovery.
- Update learning entries in place; reconcile superseded conclusions across affected owners in the same change. Retain useful historical outcomes compactly; Git history preserves removed detail. Do not create timestamped state copies or append a competing instruction patch.
- Distinguish supported outcomes from untested mechanisms. Do not label an unavailable benchmark as failed or an unobserved outcome as passed.

## Integration and validation contract

The coaching skill, project instructions and existing morning/weekly task prompts fetch this manifest and follow Coach Rules. They contain only routing, task intent and delivery language, not copied policy or athlete state. The weekly task remains the sole scheduled planner and uses block-review mode only when the active contract's trigger is due. Preserve existing task schedules unless the user requests a schedule change.

For architecture changes: run `python3 scripts/validate_os.py`, evaluate `tests/coaching-scenarios.md`, inspect the diff for lost constraints and conflicting instructions, and verify remote read-back. Structural checks catch known file/format regressions; behavioral evaluations and real-use review assess judgment. None guarantees training safety or performance.

After the first adopted training block under this revision, use its due weekly block review to evaluate decision usefulness, session execution, benchmark evidence, symptom handling, family fit and reporting burden. Keep validation pending until observed. Do not create a parallel scheduled planner or an extra task solely for this checkpoint.
