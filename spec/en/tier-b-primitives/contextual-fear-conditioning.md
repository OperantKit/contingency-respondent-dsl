# Contextual Fear Conditioning (CFC)

## DSL spelling

`ContextualFearConditioning(context=<ContextRef>, us=<StimulusRef>,
                           us_onset_from_entry=<Duration>,
                           training_trials?=<Number>)`

## Operational definition

A specialized preparation in which the *context* itself serves as the
CS. The animal is placed in a novel context; after a delay
(`us_onset_from_entry`) the US is delivered. On later re-exposure to
the same context (no US), a CR is elicited — freezing (in rodents),
suppression of ongoing behavior, or an analog measure. CFC has become
the standard preparation for dissociating hippocampal (context) from
amygdalar (discrete-CS) fear-learning substrates (Fanselow, 1990), but
the specification here is paradigm-neutral with respect to that
dissociation.

## Parameters

| Name | Type | Description |
|---|---|---|
| `context` | `ContextRef` | The training context, serving as the CS. |
| `us` | `StimulusRef` | Unconditional stimulus (typically footshock). |
| `us_onset_from_entry` | `Duration` | Time from context entry to US onset. |
| `training_trials` | `Number` (optional) | Number of conditioning sessions; often 1. |

## Example

```
ContextualFearConditioning(
    context = "ctx_shock",
    us = footshock,
    us_onset_from_entry = 180-s,
    training_trials = 1
)
```

## Primary citation

- Fanselow, M. S. (1990). Factors governing one-trial contextual
  conditioning. *Animal Learning & Behavior*, 18(3), 264–270.
  https://doi.org/10.3758/BF03205285

## Related primitives

Related to `Renewal` and `ContextualExtinction` in that context itself
is a first-class experimental object. Related to `ConditionedTasteAversion`
in supporting reliable one-trial conditioning.

