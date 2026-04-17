# Overexpectation

## DSL spelling

`Overexpectation(phase1_a=<RespondentExpr>, phase1_b=<RespondentExpr>,
                phase2_compound=<RespondentExpr>, test=<RespondentExpr>,
                phase1_trials?=<Number>, phase2_trials?=<Number>)`

## Operational definition

A three-phase procedure. **Phase 1:** two CSs (A, B) are separately
paired with the *same* US to asymptote. **Phase 2:** the compound AB
is paired with the same US; because A and B each individually predict
the US, the compound starts above the asymptote λ. **Test:** A (or B,
or both) is tested; its CR is smaller than at the end of Phase 1 —
"overexpectation" has driven V downward.

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1_a` | `RespondentExpr` | A–US pairing to asymptote. |
| `phase1_b` | `RespondentExpr` | B–US pairing to asymptote. |
| `phase2_compound` | `RespondentExpr` | AB compound paired with the same US. |
| `test` | `RespondentExpr` | Test of A or B alone. |
| `phase1_trials` | `Number` (optional) | Number of Phase 1 trials per element. |
| `phase2_trials` | `Number` (optional) | Number of Phase 2 compound trials. |

## Example

```
Overexpectation(
    phase1_a = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
    phase1_b = Pair.ForwardDelay(b, shock, isi=10-s, cs_duration=15-s),
    phase2_compound = Pair.ForwardDelay(Compound([a, b]), shock,
                                          isi=10-s, cs_duration=15-s),
    test = Extinction(a),
    phase1_trials = 40,
    phase2_trials = 10
)
```

## Primary citation

- Rescorla, R. A. (1970). Reduction in the effectiveness of
  reinforcement after prior excitatory conditioning. *Learning and
  Motivation*, 1(4), 372–381.
  https://doi.org/10.1016/0023-9690(70)90101-3

## Related primitives

Closely related to `Blocking` and `Overshadowing` — all three are
cue-competition phenomena arising from the Rescorla & Wagner (1972)
shared-asymptote constraint. Overexpectation is the "mirror" of
blocking: blocking prevents X from reaching λ, overexpectation drives
A and B below their individual asymptotes when their combined
prediction exceeds λ.

