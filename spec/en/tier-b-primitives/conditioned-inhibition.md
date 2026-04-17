# Conditioned Inhibition (Feature-Negative)

## DSL spelling

`ConditionedInhibition(training=<RespondentExpr>, test=<RespondentExpr>,
                      training_trials?=<Number>)`

## Operational definition

A two-element training with two compound types. **Training:** trials of
two kinds are intermixed — (a) CS A paired with US (A+) and (b) compound
AI *without* US (AI−). After training, A elicits a CR, but the presence
of I on AI− trials inhibits that CR. **Test:** a conditioned-inhibition
test (summation or retardation; see `SummationRetardationTest`) confirms
that I has acquired negative associative strength.

## Parameters

| Name | Type | Description |
|---|---|---|
| `training` | `RespondentExpr` | Intermixed A+ and AI− trials. A `Serial` or `Phase` expression is typical in a full program, but any `RespondentExpr` that the surrounding Phase structure can interpret is accepted. |
| `test` | `RespondentExpr` | Summation or retardation test. For summation, this is typically `Extinction(Compound([excitor, i]))` or similar. |
| `training_trials` | `Number` (optional) | Total number of training trials (across both trial types). |

## Example

```
ConditionedInhibition(
    training = Serial(
        [Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
         Pair.ForwardDelay(Compound([a, i]), nothing,
                            isi=10-s, cs_duration=15-s)],
        isi=30-s
    ),
    test = Extinction(i),
    training_trials = 80
)
```

Note: the full conditioned-inhibition paradigm typically requires the
surrounding Phase structure to deliver A+ and AI− trials in randomized
order. The `Serial` form above is a schematic; production programs
typically express the intermixing at the Phase level.

## Primary citation

- Rescorla, R. A. (1969). Pavlovian conditioned inhibition.
  *Psychological Bulletin*, 72(2), 77–94. https://doi.org/10.1037/h0027760

## Related primitives

Precondition for `SuperConditioning`. Verified by
`SummationRetardationTest`. Related to `OccasionSetting`: a
feature-negative occasion setter signals that the target will not be
reinforced, producing inhibitory-like behavior that is nevertheless
formally distinct from conditioned inhibition (Holland, 1983).

