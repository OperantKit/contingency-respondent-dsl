# Overshadowing

## DSL spelling

`Overshadowing(training=<RespondentExpr>, test_a=<RespondentExpr>,
              test_b=<RespondentExpr>,
              training_trials?=<Number>)`

## Operational definition

A single-phase training followed by two element tests. Two CSs of
differing salience (A, B) are presented as a compound paired with the
US. At test, each element is presented alone. The more-salient element
elicits a strong CR; the less-salient element elicits a weaker CR than
it would have achieved if trained alone. The less-salient element is
said to be "overshadowed" by the more-salient one.

## Parameters

| Name | Type | Description |
|---|---|---|
| `training` | `RespondentExpr` | Compound AB paired with US, e.g., `Pair.ForwardDelay(Compound([a, b]), us, ...)`. |
| `test_a` | `RespondentExpr` | Test of A alone, typically `Extinction(a)` or `CSOnly(a, ...)`. |
| `test_b` | `RespondentExpr` | Test of B alone. |
| `training_trials` | `Number` (optional) | Number of compound training trials. |

## Example

```
Overshadowing(
    training = Pair.ForwardDelay(Compound([loud_tone, dim_light]), shock,
                                  isi=10-s, cs_duration=15-s),
    test_a = Extinction(loud_tone),
    test_b = Extinction(dim_light),
    training_trials = 40
)
```

## Primary citation

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Mackintosh, N. J. (1976). Overshadowing and stimulus intensity.
  *Animal Learning & Behavior*, 4(2), 186–192.
  https://doi.org/10.3758/BF03214033

## Related primitives

Closely related to `Blocking` — both are cue-competition phenomena
predicted by Rescorla & Wagner (1972)'s shared-asymptote rule.
Overshadowing is typically reported with a salience asymmetry within a
single training phase; blocking requires prior training of one element
(Kamin, 1969). Related to `OccasionSetting` via Mackintosh (1975)'s
attentional account.

