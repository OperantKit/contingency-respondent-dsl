# Counterconditioning

## DSL spelling

`Counterconditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                    phase1_trials?=<Number>, phase2_trials?=<Number>)`

## Operational definition

A two-phase procedure. **Phase 1:** a CS is paired with a US of one
motivational class (e.g., aversive US). **Phase 2:** the *same CS* is
paired with a US of the opposite motivational class (e.g., appetitive
US). The resulting CR differs from the Phase-1 CR — often switching
sign rather than merely weakening — and is the signature behavioral
outcome of Phase 2 replacing, rather than erasing, the Phase-1
association.

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1` | `RespondentExpr` | Initial CS–US1 pairing. |
| `phase2` | `RespondentExpr` | Subsequent CS–US2 pairing with a US of opposite valence. |
| `phase1_trials` | `Number` (optional) | Number of Phase 1 trials. |
| `phase2_trials` | `Number` (optional) | Number of Phase 2 trials. |

## Example

```
Counterconditioning(
    phase1 = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(tone, food,  isi=10-s, cs_duration=15-s),
    phase1_trials = 40,
    phase2_trials = 40
)
```

## Primary citation

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Dickinson, A., & Pearce, J. M. (1977). Inhibitory interactions
  between appetitive and aversive stimuli. *Psychological Bulletin*,
  84(4), 690–711. https://doi.org/10.1037/0033-2909.84.4.690

## Related primitives

Counterconditioning is formally similar to `Extinction` (Tier A) in
that Phase 2 does not pair the CS with the original US, but differs in
pairing it with an opposite-valence US. Related to
`ReconsolidationInterference`, which uses a reactivation-plus-new-
learning arrangement that some researchers treat as a mechanistically
distinct form of counterconditioning.

