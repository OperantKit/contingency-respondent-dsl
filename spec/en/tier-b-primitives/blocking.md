# Blocking

## DSL spelling

`Blocking(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
         test=<RespondentExpr>,
         phase1_trials?=<Number>, phase2_trials?=<Number>,
         test_trials?=<Number>)`

## Operational definition

A three-phase procedure. **Phase 1:** CS A is paired with a US to
asymptote. **Phase 2:** the compound AX (A co-presented with a novel
CS X) is paired with the same US. **Test:** X is presented alone; its
CR is markedly smaller than that of a control X that had no Phase-1
pretraining of A. The pretraining of A "blocks" acquisition to X
because A fully predicts the US, leaving no prediction error for X to
resolve (Rescorla & Wagner, 1972).

## Parameters

| Name | Type | Description |
|---|---|---|
| `phase1` | `RespondentExpr` | A–US pairing to asymptote, typically `Pair.ForwardDelay(a, us, ...)`. |
| `phase2` | `RespondentExpr` | AX compound paired with the US, typically `Pair.ForwardDelay(Compound([a, x]), us, ...)`. |
| `test` | `RespondentExpr` | Test of X alone, typically `Extinction(x)` or `CSOnly(x, ...)`. |
| `phase1_trials` | `Number` (optional) | Number of Phase 1 A–US trials. |
| `phase2_trials` | `Number` (optional) | Number of Phase 2 AX–US trials. |
| `test_trials` | `Number` (optional) | Number of test trials of X. |

## Example

```
Blocking(
    phase1 = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(Compound([a, x]), shock,
                                isi=10-s, cs_duration=15-s),
    test   = Extinction(x),
    phase1_trials = 40,
    phase2_trials = 20,
    test_trials   = 10
)
```

## Primary citation

- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment
  and aversive behavior* (pp. 279–296). Appleton-Century-Crofts.

## Related primitives

Closely related to `Overshadowing` — both are cue-competition
phenomena. Blocking depends on *prior* training of A; overshadowing
requires only a salience asymmetry during compound training. Under
Rescorla & Wagner (1972), both reflect a single shared-asymptote
constraint. Related to `RetrospectiveRevaluation`, which extends
blocking by showing that X's associative strength changes *after*
Phase 2 when A is extinguished or overtrained.

