# Pavlovian Partial-Reinforcement Extinction Effect (PREE)

## DSL spelling

`PavlovianPREE(acquisition=<RespondentExpr>, extinction=<RespondentExpr>,
              test=<RespondentExpr>,
              reinforcement_probability=<Probability>)`

## Operational definition

A three-phase procedure that manipulates reinforcement probability
during acquisition. **Phase 1 (acquisition):** the CS is paired with
the US on a proportion of trials given by
`reinforcement_probability`; on the remaining trials the CS is
presented alone. **Phase 2 (extinction):** all pairings are removed.
**Phase 3 (test):** the CR decline during extinction is *slower* for
a partially reinforced CS than for a continuously reinforced CS —
the partial-reinforcement extinction effect. Mackintosh (1974)
reviews the empirical pattern and the competing theoretical accounts.

## Parameters

| Name | Type | Description |
|---|---|---|
| `acquisition` | `RespondentExpr` | Acquisition phase; semantics determined by the enclosing Phase + by `reinforcement_probability`. |
| `extinction` | `RespondentExpr` | Extinction phase. |
| `test` | `RespondentExpr` | Test of the CS. |
| `reinforcement_probability` | `Probability` | Probability of US given CS during acquisition; `0.0` is full extinction, `1.0` is continuous reinforcement. |

## Example

```
PavlovianPREE(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    test        = Extinction(tone),
    reinforcement_probability = 0.5
)
```

**Primary-source note.** The empirical effect is reliably replicated
but its canonical Pavlovian primary-source is not a single paper.
Mackintosh (1974) is the canonical textbook treatment and is used
conservatively here as the primary anchor; further primary-source
verification remains open.

## Primary citation

- Mackintosh, N. J. (1974). *The psychology of animal learning*.
  Academic Press. *(textbook treatment; primary empirical Pavlovian
  source requires further verification)*
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning.
  *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532 *(theoretical account)*

## Related primitives

Related to Tier A `Contingency(p, q)` (partial reinforcement can be
viewed as `Contingency(p, 0)`). Related to `Renewal`,
`SpontaneousRecovery`, and `ContextualExtinction` in that all bear on
the structure and recoverability of the extinguished CR.

