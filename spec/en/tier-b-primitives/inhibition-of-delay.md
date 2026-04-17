# Inhibition of Delay

## DSL spelling

`InhibitionOfDelay(cs=<StimulusRef>, us=<StimulusRef>,
                  cs_duration=<Duration>, isi=<Duration>,
                  training_trials?=<Number>)`

## Operational definition

With extended forward-delay training (long CS-to-US interval), the CR
fails to emerge immediately at CS onset and instead appears only late
in the CS interval, close to the US. The early portion of the CS
interval is said to be "inhibited" — an emergent temporal pattern
rather than a distinct preparation from forward-delay conditioning,
but named explicitly because it is a commonly reported empirical
signature of well-trained forward-delay preparations.

## Parameters

| Name | Type | Description |
|---|---|---|
| `cs` | `StimulusRef` | Conditional stimulus. |
| `us` | `StimulusRef` | Unconditional stimulus. |
| `cs_duration` | `Duration` | Total duration of the CS. |
| `isi` | `Duration` | CS-onset-to-US-onset interval (ISI). |
| `training_trials` | `Number` (optional) | Number of training trials. |

## Example

```
InhibitionOfDelay(
    cs = tone,
    us = shock,
    cs_duration = 60-s,
    isi         = 45-s,
    training_trials = 200
)
```

## Primary citation

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper
  control procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109

## Related primitives

Depends structurally on `Pair.ForwardDelay` (Tier A) with a long ISI.
Related to `PeakProcedure` in that both are temporal-discrimination
phenomena. Analysis is typically via timing theories (Gibbon & Balsam,
1981).

