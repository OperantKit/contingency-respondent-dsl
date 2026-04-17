# Retrospective Revaluation / Backward Blocking

## DSL spelling

`RetrospectiveRevaluation(phase1_compound=<RespondentExpr>,
                         phase2_element=<RespondentExpr>,
                         test=<RespondentExpr>)`

## Operational definition

A two-phase procedure whose order inverts forward blocking's. **Phase
1:** the compound AX is paired with a US. **Phase 2:** A alone is
trained (either further paired with the US or extinguished). **Test:**
X is presented alone. When Phase 2 further trains A, X's CR is
*reduced* relative to a no-Phase-2 control — "backward blocking." When
Phase 2 *extinguishes* A, X's CR is *enhanced* — "recovery from
overshadowing." Either pattern shows that X's associative strength is
revised retrospectively, a prediction that Rescorla & Wagner (1972) does
not make but that Van Hamme & Wasserman (1994) obtain by allowing
absent cues to take on negative α.

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1_compound` | `RespondentExpr` | AX compound paired with US. |
| `phase2_element` | `RespondentExpr` | A-alone training or extinction. |
| `test` | `RespondentExpr` | Test of X alone. |

## Example

```
# Backward blocking: Phase 2 further trains A
RetrospectiveRevaluation(
    phase1_compound = Pair.ForwardDelay(Compound([a, x]), shock,
                                          isi=10-s, cs_duration=15-s),
    phase2_element  = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
    test            = Extinction(x)
)

# Recovery from overshadowing: Phase 2 extinguishes A
RetrospectiveRevaluation(
    phase1_compound = Pair.ForwardDelay(Compound([a, x]), shock,
                                          isi=10-s, cs_duration=15-s),
    phase2_element  = Extinction(a),
    test            = Extinction(x)
)
```

## Primary citation

- Shanks, D. R. (1985). Forward and backward blocking in human
  contingency judgement. *Quarterly Journal of Experimental Psychology
  Section B*, 37(1b), 1–21. https://doi.org/10.1080/14640748508402082
- Van Hamme, L. J., & Wasserman, E. A. (1994). Cue competition in
  causality judgments: The role of nonpresentation of compound
  stimulus elements. *Learning and Motivation*, 25(2), 127–151.
  https://doi.org/10.1006/lmot.1994.1008

## Related primitives

Inverts `Blocking`. Shares the X-reveals-learning test with
`Overshadowing`. Mackintosh (1975)'s and Pearce–Hall (1980)'s
associability theories offer alternative (attention-based)
explanations of the same empirical pattern.

