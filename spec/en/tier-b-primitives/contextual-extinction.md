# Contextual Extinction

## DSL spelling

`ContextualExtinction(acquisition=<RespondentExpr>,
                     extinction=<RespondentExpr>,
                     test=<RespondentExpr>,
                     context=<ContextRef>)`

## Operational definition

An extinction procedure explicit about the extinction context, used to
demonstrate that extinction learning is bound to the context in which
it occurs. Differs from Tier A `Extinction` in that it requires an
explicit `context` parameter and, at test, makes the context-binding
claim empirically testable (typically via later comparison with
`Renewal`). Bouton (2004) is the canonical theoretical framework.

## Parameters

| Name | Type | Description |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US pairing. |
| `extinction` | `RespondentExpr` | CS-alone presentations in `context`. |
| `test` | `RespondentExpr` | Test of the CS. |
| `context` | `ContextRef` | The extinction context. |

## Example

```
ContextualExtinction(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    test        = Extinction(tone),
    context     = "ctx_b"
)
```

## Primary citation

- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804

## Related primitives

Closely related to `Renewal` (same context framework; renewal adds a
test-context shift that contextual extinction does not require).
Related to `LatentExtinction` and `SpontaneousRecovery` as members of
the retrieval-theory cluster.

