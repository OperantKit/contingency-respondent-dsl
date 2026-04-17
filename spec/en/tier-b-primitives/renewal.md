# Renewal (ABA / ABC / AAB)

## DSL spelling

`Renewal(acquisition=<RespondentExpr>, extinction=<RespondentExpr>,
        test=<RespondentExpr>,
        acquisition_context=<ContextRef>,
        extinction_context=<ContextRef>,
        test_context=<ContextRef>)`

## Operational definition

A three-phase procedure with context manipulation. The CS is trained in
context A, extinguished in a different context (B, for ABA / ABC), and
tested in a third context. When the test context differs from the
extinction context, the CR to the CS is restored ("renewal"). The ABA
design renews in the acquisition context; ABC renews in a novel
context; AAB renews after a context shift following acquisition and
extinction in the same context. Bouton (2004) interprets renewal as
evidence that extinction is context-specific new learning, not erasure.

## Parameters

| Name | Type | Description |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US pairing. |
| `extinction` | `RespondentExpr` | CS-alone presentations after acquisition. |
| `test` | `RespondentExpr` | Test of the CS. |
| `acquisition_context` | `ContextRef` | Context during Phase 1. |
| `extinction_context` | `ContextRef` | Context during Phase 2. |
| `test_context` | `ContextRef` | Context during Phase 3 (the test). Determines ABA vs. ABC vs. AAB. |

## Example

```
# ABA renewal
Renewal(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    test        = Extinction(tone),
    acquisition_context = "ctx_a",
    extinction_context  = "ctx_b",
    test_context        = "ctx_a"
)
```

## Primary citation

- Bouton, M. E., & Bolles, R. C. (1979). Contextual control of the
  extinction of conditioned fear. *Learning and Motivation*, 10(4),
  445–466. https://doi.org/10.1016/0023-9690(79)90057-2
- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804

## Related primitives

Closely related to `Reinstatement`, `SpontaneousRecovery`, and
`ContextualExtinction` — all extinction-recovery phenomena under
Bouton's retrieval theory. Depends on `ContextRef` (Core
`foundations/context.md`).

