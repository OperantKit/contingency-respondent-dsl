# Sensory Preconditioning

## DSL spelling

`SensoryPreconditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                       test=<RespondentExpr>,
                       phase1_trials?=<Number>, phase2_trials?=<Number>)`

## Operational definition

A three-phase procedure. **Phase 1:** two neutral CSs (CS1, CS2) are
paired with each other in the absence of any US. **Phase 2:** CS1 is
paired with a US. **Test:** CS2 is presented alone. A CR to CS2 — despite
its never having been paired with the US directly — is attributed to the
Phase-1 CS1–CS2 association (which mediates retrieval of CS1, which is
now a CS).

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1` | `RespondentExpr` | CS–CS pairing in absence of US, e.g., `Pair.ForwardDelay(cs2, cs1, ...)`. |
| `phase2` | `RespondentExpr` | First-order conditioning of CS1, e.g., `Pair.ForwardDelay(cs1, us, ...)`. |
| `test` | `RespondentExpr` | Test of CS2 alone, typically `Extinction(cs2)` or `CSOnly(cs2, ...)`. |
| `phase1_trials` | `Number` (optional) | Number of CS–CS pairings. |
| `phase2_trials` | `Number` (optional) | Number of CS1–US pairings. |

## Example

```
SensoryPreconditioning(
    phase1 = Pair.ForwardDelay(light, tone, isi=5-s, cs_duration=10-s),
    phase2 = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    test   = CSOnly(light, trials=8),
    phase1_trials = 16,
    phase2_trials = 40
)
```

## Primary citation

- Brogden, W. J. (1939). Sensory pre-conditioning. *Journal of
  Experimental Psychology*, 25(4), 323–332.
  https://doi.org/10.1037/h0058944
- Rizley, R. C., & Rescorla, R. A. (1972). Associations in second-order
  conditioning and sensory preconditioning. *Journal of Comparative and
  Physiological Psychology*, 81(1), 1–11. https://doi.org/10.1037/h0033333

## Related primitives

Closely related to `HigherOrderConditioning` — both chain CS–CS
associations, but sensory preconditioning pairs the CSs *before* any US
exposure, which dissociates the two procedures under Rescorla–Wagner
(the underlying associative structure differs per Rizley & Rescorla,
1972).

