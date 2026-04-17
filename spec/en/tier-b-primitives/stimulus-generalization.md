# Stimulus Generalization (Pavlovian)

## DSL spelling

`StimulusGeneralization(training=<RespondentExpr>,
                       test_gradient=[<StimulusRef>, <StimulusRef>, ...],
                       training_trials?=<Number>,
                       test_trials?=<Number>)`

## Operational definition

A two-phase procedure. **Training:** a CS is paired with a US to
asymptote. **Test:** a set of test stimuli varying parametrically
along a sensory dimension (typically including the trained CS and
several off-training values) is presented in extinction. Plotting CR
magnitude against the test-stimulus value yields the generalization
gradient, classically peaked at the trained value and declining as
test values depart from it (Hovland, 1937). The gradient is itself
the datum.

## Parameters

| Name | Type | Description |
|---|---|---|
| `training` | `RespondentExpr` | CS–US pairing. |
| `test_gradient` | list of `StimulusRef` | Test stimuli, including (usually) the trained CS and several neighbors along the dimension. |
| `training_trials` | `Number` (optional) | Number of training trials. |
| `test_trials` | `Number` (optional) | Number of test trials per gradient point. |

## Example

```
StimulusGeneralization(
    training = Pair.ForwardDelay(tone_1000hz, shock,
                                  isi=10-s, cs_duration=15-s),
    test_gradient = [tone_500hz, tone_750hz, tone_1000hz,
                     tone_1250hz, tone_1500hz],
    training_trials = 40,
    test_trials     = 8
)
```

## Primary citation

- Hovland, C. I. (1937). The generalization of conditioned responses:
  I. The sensory generalization of conditioned responses with varying
  frequencies of tone. *Journal of General Psychology*, 17(1),
  125–148. https://doi.org/10.1080/00221309.1937.9917977

## Related primitives

Related to Tier A `Differential` (differential conditioning plus
generalization testing yields the post-discrimination gradient).
Related to `OccasionSetting` — occasion-setting tests often
parametrically vary the target along a sensory dimension.

