# Conditioned Taste Aversion (CTA)

## DSL spelling

`ConditionedTasteAversion(taste_cs=<StimulusRef>, visceral_us=<StimulusRef>,
                         cs_duration=<Duration>, delay_to_us=<Duration>,
                         training_trials?=<Number>)`

## Operational definition

A specialized Pavlovian preparation. A gustatory CS (e.g., a novel
flavor) is consumed, followed after a long delay by a visceral US
(e.g., lithium chloride-induced malaise). On test, the animal avoids or
reduces consumption of the CS. CTA is notable for (a) readily
supporting one-trial conditioning, (b) tolerating long CS–US delays
(hours), and (c) showing strong selective associability between
gustatory CSs and visceral USs (Garcia, Ervin, & Koelling, 1966). The
preparation is conceptually a special case of `Pair.ForwardTrace` with
unusually long trace intervals, but is named separately because its
operational parameters (taste modality, long delay, visceral US) are
procedurally constrained.

## Parameters

| Name | Type | Description |
|---|---|---|
| `taste_cs` | `StimulusRef` | Gustatory CS (typically a flavored solution). |
| `visceral_us` | `StimulusRef` | Visceral US (e.g., LiCl, rotation-induced malaise). |
| `cs_duration` | `Duration` | Duration of CS consumption opportunity. |
| `delay_to_us` | `Duration` | Time from CS offset to US onset. |
| `training_trials` | `Number` (optional) | Number of training trials; often just 1. |

## Example

```
ConditionedTasteAversion(
    taste_cs = saccharin_solution,
    visceral_us = licl_injection,
    cs_duration = 10-min,
    delay_to_us = 60-min,
    training_trials = 1
)
```

## Primary citation

- Garcia, J., Ervin, F. R., & Koelling, R. A. (1966). Learning with
  prolonged delay of reinforcement. *Psychonomic Science*, 5(3),
  121–122. https://doi.org/10.3758/BF03328311

## Related primitives

Structurally a constrained `Pair.ForwardTrace` (Tier A) with a long
trace interval. Related to `LatentInhibition` (preexposure to the taste
CS produces latent inhibition of CTA). Related to general
`StimulusGeneralization` work in the taste modality.

