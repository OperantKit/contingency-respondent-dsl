# Super-Conditioning

## DSL spelling

`SuperConditioning(phase1_inhibitor=<RespondentExpr>,
                   phase2_target=<RespondentExpr>,
                   test=<RespondentExpr>)`

## Operational definition

A two-phase procedure. **Phase 1:** CS I is trained as a conditioned
inhibitor (e.g., via `ConditionedInhibition`). **Phase 2:** the
compound IX (I co-presented with a novel CS X) is paired with a US.
**Test:** X elicits a CR *larger* than that of a control X trained
without prior inhibitor. Because the compound starts below 0 (I has
negative associative strength), the prediction error at the US is
larger than for a novel compound, giving X extra asymptotic strength.

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1_inhibitor` | `RespondentExpr` | Conditioned-inhibition training of I, typically a nested `ConditionedInhibition(...)`. |
| `phase2_target` | `RespondentExpr` | Compound IX paired with US, typically `Pair.ForwardDelay(Compound([i, x]), us, ...)`. |
| `test` | `RespondentExpr` | Test of X alone. |

## Example

```
SuperConditioning(
    phase1_inhibitor = ConditionedInhibition(
        training = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
        test     = Extinction(i),
        training_trials = 40
    ),
    phase2_target = Pair.ForwardDelay(Compound([i, x]), shock,
                                        isi=10-s, cs_duration=15-s),
    test = Extinction(x)
)
```

## Primary citation

- Rescorla, R. A. (1971). Variation in the effectiveness of
  reinforcement and nonreinforcement following prior inhibitory
  conditioning. *Learning and Motivation*, 2(2), 113–123.
  https://doi.org/10.1016/0023-9690(71)90002-6

## Related primitives

Mirror of `Blocking`: blocking shows *less* learning to X because the
compound starts at λ; super-conditioning shows *more* learning to X
because the compound starts below 0. Depends on
`ConditionedInhibition` for the Phase-1 inhibitor. All three fall out
of Rescorla & Wagner (1972)'s shared-asymptote rule.

