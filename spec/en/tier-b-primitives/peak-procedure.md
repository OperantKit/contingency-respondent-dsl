# Peak Procedure (Temporal Discrimination)

## DSL spelling

`PeakProcedure(cs=<StimulusRef>, us=<StimulusRef>, fi_duration=<Duration>,
              peak_probe_duration=<Duration>,
              peak_probe_probability?=<Probability>,
              training_trials?=<Number>)`

## Operational definition

A timing-discrimination preparation. On reinforced trials, the CS
signals that the US will occur at a fixed latency after CS onset
(`fi_duration`). Intermixed "peak probe" trials have the CS present
for an extended period (`peak_probe_duration`, longer than
`fi_duration`) without US delivery. The distribution of responding
across the probe reveals a peak near the trained `fi_duration`,
indexing the animal's estimate of the US time (Roberts, 1981). The
peak procedure is the canonical preparation for scalar timing
measurements (Gibbon & Balsam, 1981).

## Parameters

| Name | Type | Description |
|---|---|---|
| `cs` | `StimulusRef` | CS marking trial onset. |
| `us` | `StimulusRef` | US delivered at `fi_duration` on reinforced trials. |
| `fi_duration` | `Duration` | Fixed CS-onset-to-US-delivery interval on reinforced trials. |
| `peak_probe_duration` | `Duration` | Extended CS duration on probe trials (usually 2–3× `fi_duration`). |
| `peak_probe_probability` | `Probability` (optional) | Proportion of trials that are probe trials; default is unspecified. |
| `training_trials` | `Number` (optional) | Total number of trials. |

## Example

```
PeakProcedure(
    cs = tone,
    us = food,
    fi_duration = 30-s,
    peak_probe_duration = 90-s,
    peak_probe_probability = 0.25,
    training_trials = 400
)
```

## Primary citation

- Roberts, S. (1981). Isolation of an internal clock. *Journal of
  Experimental Psychology: Animal Behavior Processes*, 7(3), 242–268.
  https://doi.org/10.1037/0097-7403.7.3.242

## Related primitives

Related to `InhibitionOfDelay` (both are temporal-discrimination
phenomena). Uses Tier A `Pair.ForwardDelay` as its underlying
reinforced-trial structure (with the probe trials as a structural
addition). Related to timing-theory-grounded parameters elsewhere in
the Tier B set (see [`../theory.md`](../theory.md) §7).

