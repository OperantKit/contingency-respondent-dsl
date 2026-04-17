# Spontaneous Recovery

## DSL spelling

`SpontaneousRecovery(acquisition=<RespondentExpr>,
                    extinction=<RespondentExpr>,
                    retention_interval=<Duration>,
                    test=<RespondentExpr>)`

## Operational definition

A three-phase procedure plus a retention interval. **Phase 1
(acquisition):** CS–US pairing. **Phase 2 (extinction):** CS-alone
presentations until the CR extinguishes. **Phase 3 (retention):** no
training for a period (`retention_interval`). **Phase 4 (test):** the
CS is presented; the CR reappears, in proportion to the retention
interval. Bouton (2004) treats spontaneous recovery as a
time-as-context effect: passage of time shifts the context away from
the extinction context, restoring retrieval of the Phase-1
association.

## Parameters

| Name | Type | Description |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US pairing. |
| `extinction` | `RespondentExpr` | CS-alone presentations. |
| `retention_interval` | `Duration` | Time between end of extinction and test (e.g., `24-h` expressed as the Core-compatible duration). |
| `test` | `RespondentExpr` | Test of the CS. |

## Example

```
SpontaneousRecovery(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    retention_interval = 1440-min,
    test        = Extinction(tone)
)
```

## Primary citation

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Rescorla, R. A. (2004). Spontaneous recovery. *Learning & Memory*,
  11(5), 501–509. https://doi.org/10.1101/lm.77504

## Related primitives

Closely related to `Renewal` (both restore extinguished responding via
context shift; for spontaneous recovery the "context" is time) and to
`Reinstatement` (US-alone instead of time-alone).

