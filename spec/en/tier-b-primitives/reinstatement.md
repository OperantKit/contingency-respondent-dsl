# Reinstatement

## DSL spelling

`Reinstatement(acquisition=<RespondentExpr>, extinction=<RespondentExpr>,
              reinstatement_us=<RespondentExpr>,
              test=<RespondentExpr>)`

## Operational definition

A four-phase procedure. **Phase 1 (acquisition):** CS–US pairing.
**Phase 2 (extinction):** CS-alone presentations until the CR
extinguishes. **Phase 3 (reinstatement):** US-alone presentations in
the extinction context (no CS). **Phase 4 (test):** the CS is
presented; the CR is partially restored. Reinstatement is a classical
demonstration that extinguished responding is recoverable and that the
US alone can restore it, consistent with a retrieval (Bouton, 2004)
rather than an erasure interpretation of extinction.

## Parameters

| Name | Type | Description |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US pairing. |
| `extinction` | `RespondentExpr` | CS-alone presentations. |
| `reinstatement_us` | `RespondentExpr` | US-alone presentations, typically `USOnly(us, trials=N)`. |
| `test` | `RespondentExpr` | Test of the CS. |

## Example

```
Reinstatement(
    acquisition      = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction       = Extinction(tone),
    reinstatement_us = USOnly(shock, trials=4),
    test             = Extinction(tone)
)
```

## Primary citation

- Rescorla, R. A., & Heth, C. D. (1975). Reinstatement of fear to an
  extinguished conditioned stimulus. *Journal of Experimental
  Psychology: Animal Behavior Processes*, 1(1), 88–96.
  https://doi.org/10.1037/0097-7403.1.1.88
- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804

## Related primitives

Closely related to `Renewal`, `SpontaneousRecovery`, and
`ContextualExtinction`. Related to Tier A `USOnly` (the mechanism of
reinstatement is typically implemented in the grammar as a
`USOnly(...)` phase between extinction and test).

