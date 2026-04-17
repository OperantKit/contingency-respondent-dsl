# Occasion Setting

## DSL spelling

`OccasionSetting(feature=<StimulusRef>, target=<StimulusRef>,
                us=<StimulusRef>,
                mode=("FeaturePositive" | "FeatureNegative"),
                training_trials?=<Number>)`

## Operational definition

An occasion setter is a stimulus that modulates the predictive status
of a target CS, without itself acquiring excitatory or inhibitory
strength. In **feature-positive** training, trials alternate
Feature→Target→US versus Target-alone (no US); the feature gates
reinforcement. In **feature-negative** training, trials alternate
Target→US versus Feature+Target (no US); the feature gates the absence
of reinforcement. Occasion setters differ from conditioned inhibitors
in their summation-test behavior: they fail to inhibit a separately
trained excitor (Holland, 1983).

## Parameters

| Name | Type | Description |
|---|---|---|
| `feature` | `StimulusRef` | The occasion-setting CS (F). |
| `target` | `StimulusRef` | The target CS whose reinforcement is modulated (T). |
| `us` | `StimulusRef` | The unconditional stimulus. |
| `mode` | `"FeaturePositive"` \| `"FeatureNegative"` | Which gating relation to establish. |
| `training_trials` | `Number` (optional) | Total number of training trials. |

## Example

```
OccasionSetting(
    feature = houselight,
    target  = tone,
    us      = shock,
    mode    = FeaturePositive,
    training_trials = 80
)
```

## Primary citation

- Holland, P. C. (1983). Occasion-setting in Pavlovian feature
  positive discriminations. In M. L. Commons, R. J. Herrnstein, & A. R.
  Wagner (Eds.), *Quantitative analyses of behavior: Discrimination
  processes* (Vol. 4, pp. 183–206). Ballinger.

## Related primitives

Related to but distinct from `ConditionedInhibition` (feature-negative
occasion setters survive summation tests differently than conditioned
inhibitors). Related to `Differential` in Tier A (differential
conditioning can be viewed as a degenerate case where the "feature" is
the CS identity itself).

