# Latent Inhibition (CS Preexposure Effect)

## DSL spelling

`LatentInhibition(preexposure=<RespondentExpr>, training=<RespondentExpr>,
                 test=<RespondentExpr>,
                 preexposure_trials?=<Number>,
                 training_trials?=<Number>)`

## Operational definition

A three-phase procedure. **Phase 1 (preexposure):** the to-be-CS is
presented repeatedly without any US. **Phase 2 (training):** the
preexposed CS is paired with the US. **Test:** the CS is presented;
acquisition is slower (and asymptotic CR is lower) than in a
non-preexposed control. The preexposed CS is said to have acquired
*latent inhibition* — a loss of associability that is usually
attributed to attentional or associative-learning-rate mechanisms
(Lubow & Moore, 1959; Pearce & Hall, 1980).

## Parameters

| Name | Type | Description |
|---|---|---|
| `preexposure` | `RespondentExpr` | CS-alone preexposure, typically `CSOnly(cs, trials=N)`. |
| `training` | `RespondentExpr` | CS–US pairing. |
| `test` | `RespondentExpr` | Test of the preexposed CS. |
| `preexposure_trials` | `Number` (optional) | Number of preexposure presentations. |
| `training_trials` | `Number` (optional) | Number of training trials. |

## Example

```
LatentInhibition(
    preexposure = CSOnly(tone, trials=80),
    training    = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    test        = Extinction(tone),
    preexposure_trials = 80,
    training_trials    = 40
)
```

## Primary citation

- Lubow, R. E., & Moore, A. U. (1959). Latent inhibition: The effect
  of nonreinforced pre-exposure to the conditional stimulus. *Journal
  of Comparative and Physiological Psychology*, 52(4), 415–419.
  https://doi.org/10.1037/h0046700

## Related primitives

Closely related to `USPreexposure` — both preexposure-effect
preparations, but one preexposes the CS and the other the US. Pearce &
Hall (1980) is the canonical theoretical framework.

