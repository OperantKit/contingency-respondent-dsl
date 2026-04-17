# Mediated Conditioning

## DSL spelling

`MediatedConditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                    test=<RespondentExpr>,
                    phase1_trials?=<Number>, phase2_trials?=<Number>)`

## Operational definition

A two-phase procedure establishing an association through a mediating
stimulus representation. **Phase 1:** CS A is paired with a
motivationally significant stimulus S (often a flavor or US).
**Phase 2:** CS A is presented in conjunction with a new outcome O,
but *without* S being physically present. **Test:** responses to S
(or to stimuli associated with S) are altered as if S had been
directly paired with O. Under Wagner (1981)'s SOP framework, A
retrieves an A2-mode representation of S during Phase 2, and it is
this representation that supports the A–O association.

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1` | `RespondentExpr` | A–S pairing. |
| `phase2` | `RespondentExpr` | A in conjunction with a new outcome O, without S physically present. |
| `test` | `RespondentExpr` | Test of S (or of S-associated stimuli). |
| `phase1_trials` | `Number` (optional) | Number of A–S pairings. |
| `phase2_trials` | `Number` (optional) | Number of A–O trials. |

## Example

```
MediatedConditioning(
    phase1 = Pair.ForwardDelay(tone, flavor, isi=5-s, cs_duration=10-s),
    phase2 = Pair.ForwardDelay(tone, lithium, isi=5-s, cs_duration=10-s),
    test   = CSOnly(flavor, trials=8),
    phase1_trials = 40,
    phase2_trials = 8
)
```

## Primary citation

- Holland, P. C. (1981). Acquisition of representation-mediated
  conditioned food aversions. *Learning and Motivation*, 12(1),
  1–18. https://doi.org/10.1016/0023-9690(81)90022-9

## Related primitives

Closely related to `HigherOrderConditioning` and
`SensoryPreconditioning` — all three involve chained learning through
intermediate representations. Mediated conditioning is distinctive in
that the mediating *representation* (not the mediating CS) carries the
Phase 2 association — Wagner (1981)'s SOP account is typically
invoked.

