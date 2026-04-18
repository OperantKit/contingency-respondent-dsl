# Latent Extinction (Pavlovian)

## DSL spelling

`LatentExtinction(acquisition=<RespondentExpr>, preexposure=<RespondentExpr>,
                 test=<RespondentExpr>,
                 preexposure_trials?=<Number>)`

## Operational definition

A three-phase procedure. **Phase 1 (acquisition):** CS–US pairing.
**Phase 2 (preexposure / context exposure):** the animal is exposed to
the training context *without* the CS and without the US, for an
extended period. **Phase 3 (test):** the CS is presented; the CR is
reduced relative to a no-Phase-2 control. The classic literature
(Seward & Levy, 1949) reports the effect for instrumental responding;
the Pavlovian analog treats it as context-specific weakening of
retrieval, consistent with Bouton (2004)'s retrieval theory.

## Parameters

| Name | Type | Description |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US pairing. |
| `preexposure` | `RespondentExpr` | Context exposure without CS or US; typically represented as a context-only phase. |
| `test` | `RespondentExpr` | Test of the CS. |
| `preexposure_trials` | `Number` (optional) | Number or duration of preexposure sessions. |

## Example

```
LatentExtinction(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    preexposure = CSOnly(context_a, trials=0),  -- schematic: Phase represents context-only exposure
    test        = Extinction(tone),
    preexposure_trials = 30
)
```

**Primary-source note.** The most frequently cited reference is Seward
& Levy (1949) for the instrumental form. For the *Pavlovian* form
referenced here, the cleanest theoretical framing is Bouton (2004);
a dedicated primary Pavlovian source has not been pinned down and
Bouton (2004) is used conservatively as the theoretical anchor.

## Primary citation

- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804
- Seward, J. P., & Levy, N. (1949). Latent extinction: Sign learning
  as a factor in extinction. *Journal of Experimental Psychology*,
  39(5), 660–668. https://doi.org/10.1037/h0057426 *(instrumental
  prototype; the Pavlovian form is extrapolated from Bouton's
  retrieval framework)*

## Related primitives

Closely related to `ContextualExtinction`, `Renewal`, and
`SpontaneousRecovery` — all in the retrieval-theory cluster.

