# Higher-Order Conditioning

## DSL spelling

`HigherOrderConditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                        phase1_trials?=<Number>, phase2_trials?=<Number>)`

## Operational definition

A two-phase procedure. **Phase 1:** a first-order CS (CS1) is paired with
a US, establishing CS1 as a conditioned stimulus. **Phase 2:** a second
CS (CS2) is paired with CS1, *in the absence of the US*. At test, CS2
alone elicits a CR whose magnitude is characteristically smaller than
CS1's. The CR to CS2 is said to be "second-order" because it depends on
CS1's prior first-order conditioning.

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1` | `RespondentExpr` | First-order conditioning (typically `Pair.ForwardDelay(cs1, us, ...)`). |
| `phase2` | `RespondentExpr` | Second-order pairing, e.g., `Pair.ForwardDelay(cs2, cs1, ...)` with no US. |
| `phase1_trials` | `Number` (optional) | Number of first-order trials. |
| `phase2_trials` | `Number` (optional) | Number of second-order trials. |

## Example

```
HigherOrderConditioning(
    phase1 = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(light, tone, isi=5-s, cs_duration=10-s),
    phase1_trials = 40,
    phase2_trials = 20
)
```

## Primary citation

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Rizley, R. C., & Rescorla, R. A. (1972). Associations in second-order
  conditioning and sensory preconditioning. *Journal of Comparative and
  Physiological Psychology*, 81(1), 1–11. https://doi.org/10.1037/h0033333

## Related primitives

Closely related to `SensoryPreconditioning` — both chain two CSs via a
shared element, but the order of the US phase differs (second-order
conditions CS1 with US first; sensory preconditioning pairs CS1 and CS2
before any US exposure). Related to `MediatedConditioning` via SOP-style
A2 mediation (Wagner, 1981).

