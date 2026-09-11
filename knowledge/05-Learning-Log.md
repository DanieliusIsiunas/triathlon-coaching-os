# Learning Log

Last updated: 2026-09-09

This file owns hypotheses and durable response conclusions. Current restrictions/queue belong to Active State, protocols/targets to Current Season, and official race evidence to the linked race review. The 2026-09-07 reconciliation uses existing records and user-authorized system changes; it supplies no new live readiness or benchmark results.

## Active investigations

### L1 - Fresh running capacity and bike-to-run cost

- Question/hypothesis: The run is the largest identified Olympic performance opportunity, but its limiting mechanism is unresolved. Fresh capacity, durability, coordination, preceding bike cost and pacing are competing explanations.
- Evidence and alternatives: The [Druskininkai review](../reviews/races/2026-09-05-druskininkai-olympic.md) records a stable first three run loops, a late surge and difficulty accessing faster sustainable pace. Historical half-marathon ability is not a current baseline. Measured race cadence/power is absent; assumed gearing and average speed cannot establish race cadence. The first Favero-recorded ride on 2026-09-09 showed 64 rpm overall and approximately 65 rpm through the first 20 km, including 196 W at 64 rpm over km 5-10. This supports a naturally torque-heavy pedaling pattern, but mixed surface, strong wind, interruptions, new shoes and deliberate intensity changes prevent attribution to race execution or subsequent running. Adequate-feeling effort and tolerated fueling do not exclude bike or nutritional cost.
- Intervention/decision: Once recovery is established, use Current Season's RUN-E/RUN-F references as appropriate, then BRICK-C only if needed. Cadence is now measurable. Before prescribing a correction, compare natural cadence with small controlled increases at similar easy power on a flat, uninterrupted ride and observe heart rate, leg effort, right-foot response and later running. Do not jump directly to a fixed cadence target.
- Expected result and revision criterion: Comparable fresh and post-bike evidence will narrow the limiter. Relatively strong fresh running with poorer post-bike response supports transfer investigation; similarly limited performance fresh weakens bike cost as the sole explanation. Inconsistent conditions leave the result unresolved. Change one major variable in a later trial.
- Review trigger: First relevant activated benchmark pair, then the end of the first adopted development block; earlier if reliable cadence or contradictory evidence arrives.
- Status/outcome: unresolved; protocols are inactive and no new baseline exists.
- Confidence: high that running is an opportunity; low for a specific physiological or gearing mechanism.

### L2 - Session purpose, ceiling and sustainable execution

- Question/hypothesis: Explicit success criteria and ceilings, combined with better prescription fit, may reduce unintended session escalation while preserving enjoyment and key-session quality.
- Evidence and alternatives: Prior records show multiple short/easy prescriptions becoming longer or harder, including the 2026-08-26 bike, 2026-08-28 swim, race-week run and the 2026-09-11 first post-race run, where a 20-minute 2-3/10 impact-tolerance test became 39:38 at 4/10 with a 5:35 kilometre. Immediate tolerance does not establish benefit to the next key session. Underestimated capacity, unclear intent and enjoyment preferences may explain the pattern; do not assume poor discipline.
- Intervention/decision: Use the Coach Rules session contract, explain the reason for the ceiling, and ask about clarity/fit when execution differs. Keep reporting concise and review downstream response.
- Expected result and revision criterion: Intended stimulus is achieved more consistently, next key sessions remain feasible, and reporting/enjoyment are acceptable. If escalation persists, inspect prescription clarity and realism before adding restrictions. If the ceiling is repeatedly too low with favorable evidence, reconsider the future dose through normal progression.
- Review trigger: First weekly review containing relevant sessions and end of the first adopted block.
- Status/outcome: unresolved; implemented as a coaching protocol, not yet demonstrated effective in use.
- Confidence: medium for the observed pattern; low for the intervention effect until reviewed.

## Retained learning and closed historical trials

### L3 - Rolling queue and state architecture

- Question/hypothesis: A rolling queue fits variable family availability; separating knowledge by ownership should prevent stale-state errors.
- Evidence and alternatives: The queue was used across moved/modified sessions and remains the confirmed preference. No controlled comparison establishes improved adherence. The 2026-09-07 audit found old telemetry and expired directions accumulating in Active State despite the 2026-07-25 refactor.
- Intervention/decision: Retain the rolling queue; replace copied policy with canonical routing, compact Active State and review ownership during writes. Architecture history belongs to CHANGELOG.
- Expected result and revision criterion: No contradictory active queue or expired instructions; enough useful history remains to explain decisions. Recurrence of stale state or excessive reading burden weakens implementation effectiveness.
- Review trigger: Every structural validation and the first block review; revisit sooner if an inconsistency affects a decision.
- Status/outcome: weakened for the prior assumption that file separation alone ensured clean state; practical queue suitability is supported by preference/use, not a causal adherence result.
- Confidence: high for the observed architecture defect and confirmed queue preference; low for quantified adherence gains.

### L4 - July calf episode

- Question/hypothesis: The progressive-run dose exceeded calf tolerance more than general aerobic capacity.
- Evidence and alternatives: Mild symptoms followed the July progression. Subsequent easy running and follow-ups in August supported tolerance; Active State already removed the separate easy-running restriction. The precise tissue and mechanism were never diagnosed.
- Intervention/decision: Retain gradual, one-variable progression. The old return-to-run trial is closed; use current symptom gates for post-race decisions.
- Expected result and revision criterion: Historical tolerance does not predict unlimited load. Recurrence opens a current symptom assessment rather than resurrecting expired July instructions.
- Review trigger: New calf symptoms or a relevant progression response.
- Status/outcome: retired as an active July restriction/trial; easy-running tolerance was supported before the race. Current post-race response remains unknown.
- Confidence: high for recorded later tolerance; low for the specific causal/tissue explanation.

### L5 - Fueling tolerance and frequent intake

- Question/hypothesis: Small frequent intakes and pre-swim carbohydrate can be practically tolerated; performance benefit and optimal fluid/sodium doses are separate questions.
- Evidence and alternatives: Early July/August trials tolerated smaller doses. The [race review](../reviews/races/2026-09-05-druskininkai-olympic.md) documents the higher race intake without gastrointestinal problems. Palatability of the earlier pre-swim gel was poor. Changes in readiness, prior food and expectation confound reported energy benefits; fluid loss was not measured.
- Intervention/decision: Retain the tolerated intake rhythm. The old instructions to complete a pre-race higher-dose rehearsal are closed. Use race evidence as an experience reference, not a universal prescription for longer/hotter events; assess fuel/fluid/sodium needs for each new context.
- Expected result and revision criterion: Continued practical tolerance; revise the product/dose/timing if symptoms, palatability or late-session response change. No gastrointestinal symptoms alone does not prove adequate hydration or optimal fueling.
- Review trigger: Next materially longer/different-condition rehearsal or a tolerance problem.
- Status/outcome: supported for practical race tolerance; unresolved for isolated performance benefit and optimal hydration/sodium. Prior dose-rehearsal trials are retired.
- Confidence: high for reported race tolerance; low for isolated causal performance claims and individual fluid/sodium sufficiency.

### L6 - Swimming confidence, technique and transfer

- Question/hypothesis: Swimming practice improved pool capability and open-water confidence; remaining speed opportunity may involve technique/navigation.
- Evidence and alternatives: The race review records calm continuous freestyle instead of the prior stress-driven breaststroke. This supports confidence transfer. Course, wetsuit, conditions and pacing confound split comparison; watch metrics do not isolate technical efficiency. The shoulder/arm-entry link remains an unverified mechanical explanation.
- Intervention/decision: Preserve confidence-building continuous work and use purposeful repetitions when cleared. Use Current Season's SWIM-T only after its activation gates; seek video/in-person evidence for a persistent mechanical question.
- Expected result and revision criterion: Technique and pacing gains transfer to sustained swimming without worsening symptoms. Faster rested repeats alone leave race transfer unresolved.
- Review trigger: Next relevant swim-block review after shoulder reassessment; sooner for symptoms.
- Status/outcome: supported for improved open-water confidence; unresolved for the specific technical mechanism. No independent active swim experiment is added while L1/L2 are prioritized.
- Confidence: high for the athlete's confidence report; medium for overall performance progression; low for an isolated technique cause.

### L7 - Aerobar comfort and performance

- Question/hypothesis: The tested aero position is comfortable and practically useful; its speed gain and handling mastery require separate evidence.
- Evidence and alternatives: Multiple rides and the race supported sustained comfort. Uncontrolled wind, power, surface, drafting and position exposure prevent quantifying aerodynamic gains. Comfort did not fully evaluate traffic handling or next-day shoulder status.
- Intervention/decision: Retain the setup as a useful reference with Coach Rules' handling precautions. Compare position changes only when they answer a meaningful performance/comfort question.
- Expected result and revision criterion: Comfort and control persist during relevant duration. New symptoms or handling problems require reassessment; a faster windy ride is not a validated aerodynamic gain.
- Review trigger: Setup change, handling concern, symptoms or a controlled comparison.
- Status/outcome: supported for reported sustained comfort; unresolved for quantified gain and general handling mastery. Initial comfort trial is closed.
- Confidence: high for reported comfort; low for quantified aerodynamic benefit.

### L8 - August low-energy episode

- Question/hypothesis: Accumulated fatigue contributed to temporary performance suppression.
- Evidence and alternatives: Energy improved after a recovery day and subsequent work was tolerated. This temporal response supports the interpretation but does not isolate fatigue from sleep, nutrition or other factors.
- Intervention/decision: Retain the lesson to investigate subjective suppression despite favorable device scores. Retire the old restriction; respond to current symptoms and trends.
- Expected result and revision criterion: Recurrent suppression prompts reassessment rather than assuming the same cause. Persistent or concerning symptoms require appropriate assessment.
- Review trigger: New low-energy pattern or contradictory evidence.
- Status/outcome: supported as a plausible response pattern; the temporary restriction is retired.
- Confidence: medium for fatigue as a contributor; no diagnosis established.
