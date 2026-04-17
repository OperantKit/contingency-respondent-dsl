# US Preexposure Effect

## DSL spelling

`USPreexposure(preexposure=<RespondentExpr>, training=<RespondentExpr>,
              test=<RespondentExpr>,
              preexposure_trials?=<Number>,
              training_trials?=<Number>)`

## Operational definition

A three-phase procedure paralleling `LatentInhibition`, but preexposing
the US rather than the CS. **Phase 1 (preexposure):** the US is
presented alone repeatedly. **Phase 2 (training):** a CS is paired with
the same US. **Test:** the CS is presented; acquisition is slower
and/or asymptotic CR is lower than in a non-preexposed control. Both
associative (US representation) and nonassociative (habituation,
motivational) accounts have been proposed (Randich & LoLordo, 1979).

## Parameters

| Name | Type | Description |
|---|---|---|
| `preexposure` | `RespondentExpr` | US-alone preexposure, typically `USOnly(us, trials=N)`. |
| `training` | `RespondentExpr` | CS–US pairing. |
| `test` | `RespondentExpr` | Test of the CS. |
| `preexposure_trials` | `Number` (optional) | Number of US preexposures. |
| `training_trials` | `Number` (optional) | Number of CS–US training trials. |

## Example

```
USPreexposure(
    preexposure = USOnly(shock, trials=40),
    training    = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    test        = Extinction(tone),
    preexposure_trials = 40,
    training_trials    = 40
)
```

## Primary citation

- Randich, A., & LoLordo, V. M. (1979). Associative and nonassociative
  theories of the UCS preexposure phenomenon. *Psychological Bulletin*,
  86(3), 523–548. https://doi.org/10.1037/0033-2909.86.3.523

## Related primitives

Closely related to `LatentInhibition` — dual-control preexposure
preparation with symmetric structure. The two are typically used
together to dissociate CS- versus US-locus accounts of the preexposure
effect.

