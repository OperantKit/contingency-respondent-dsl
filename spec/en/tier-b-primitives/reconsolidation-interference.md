# Reconsolidation Interference

## DSL spelling

`ReconsolidationInterference(acquisition=<RespondentExpr>,
                            reactivation=<RespondentExpr>,
                            interference_window=<Duration>,
                            extinction=<RespondentExpr>,
                            test=<RespondentExpr>)`

## Operational definition

A four-phase procedure. **Phase 1 (acquisition):** CS–US pairing.
**Phase 2 (reactivation):** brief CS-alone presentation, theorized to
return the CS–US memory trace to a labile "reconsolidation" state.
**Interference window:** within a time window (conventionally 10 min –
6 h after reactivation) the memory is susceptible to interference.
**Phase 3 (extinction within window):** CS-alone presentations
delivered inside the window. **Phase 4 (test):** the CR is reduced and
resists later renewal, reinstatement, and spontaneous recovery — a
pattern characteristically stronger than extinction alone produces
(Monfils et al., 2009).

## Parameters

| Name | Type | Description |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US pairing. |
| `reactivation` | `RespondentExpr` | Single CS-alone presentation, typically `CSOnly(cs, trials=1)`. |
| `interference_window` | `Duration` | Time window post-reactivation during which the memory is labile. |
| `extinction` | `RespondentExpr` | Extinction delivered within the window. |
| `test` | `RespondentExpr` | Test of the CS. |

## Example

```
ReconsolidationInterference(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    reactivation = CSOnly(tone, trials=1),
    interference_window = 60-min,
    extinction = Extinction(tone),
    test = Extinction(tone)
)
```

## Primary citation

- Monfils, M.-H., Cowansage, K. K., Klann, E., & LeDoux, J. E. (2009).
  Extinction-reconsolidation boundaries: Key to persistent attenuation
  of fear memories. *Science*, 324(5929), 951–955.
  https://doi.org/10.1126/science.1167975

## Related primitives

Related to `Counterconditioning`, `LatentExtinction`, and
`ContextualExtinction` as members of the extinction-modulation cluster.
The key structural feature distinguishing this primitive is the
`interference_window` timing parameter.

