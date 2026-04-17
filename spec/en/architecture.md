# Architecture — contingency-respondent-dsl

> Part of the `contingency-respondent-dsl` package. Describes how this
> package's grammar merges with the Core `contingency-dsl` respondent layer
> via the `ExtensionRespondentPrimitive` extension point. **No new Core
> layer is introduced.**

---

## 1. Position in the OperantKit layer stack

`contingency-dsl` (Core) already defines the six-layer Ψ architecture
(`foundations / operant / respondent / composed / experiment /
annotations`). The Core respondent layer is intentionally minimal: it
covers the foundational Pavlovian primitives (R1–R14) and nothing more
(Pavlov, 1927; Rescorla, 1967; Mackintosh, 1974). Deeper Pavlovian
phenomena — blocking, overshadowing, latent inhibition, renewal,
reinstatement, conditioned inhibition, etc. — are **Tier B** and live
here.

`contingency-respondent-dsl` is therefore **not a new layer**. It is a
consumer of an already-existing extension point in the Core respondent
grammar:

```
contingency-dsl (Core)
├── foundations/
├── operant/
├── respondent/
│   ├── grammar.md
│   │   ├── core_respondent_primitive   ← Tier A (R1–R14)
│   │   └── extension_respondent_primitive   ← hook; see §2
│   ├── theory.md
│   └── primitives.md
├── composed/
├── experiment/
└── annotations/

contingency-respondent-dsl (this package)
├── spec/en/grammar.md                  ← 26 Tier B productions
└── schema/grammar.ebnf                 ← EBNF for the 26 productions
     (both register through the extension-point hook above)
```

---

## 2. The extension-point contract

Core's `spec/en/respondent/grammar.md §4` defines the extension point
verbatim (paraphrased here):

```ebnf
RespondentExpr ::=
      CoreRespondentPrimitive            (* Tier A: R1–R14 *)
    | ExtensionRespondentPrimitive       (* Tier B / third party *)

ExtensionRespondentPrimitive ::=
      IdentUpper "(" ArgList? ")"
    -- program-scoped resolution via a respondent registry
```

Any Tier B primitive this package defines is spelled as

```
<IdentUpper>(<arg_list>)
```

where `IdentUpper` matches `[A-Z][a-zA-Z0-9_]*`, and the argument list
conforms to the per-primitive schema documented in
`spec/en/tier-b-primitives/<name>.md`.

Core's parser treats any such identifier-form expression as syntactically
valid (LL(1)-distinguishable at the first token; see `foundations/
ll2-proof.md` in Core) and defers semantic validation — including
registry lookup and argument-type checking — to Phase 2 post-parsing.
This package supplies the Phase 2 rules for its 26 primitives.

---

## 3. How a program activates this extension

A program activates the Tier B registry declaratively. The following is
the intended conceptual form; exact syntax is finalized by the Core DSL
once registry-import syntax lands in Core:

```
# program header (conceptual)
import respondent_tier_b

# body (all identifiers below resolve through the Tier B registry)
phase acquisition:
    Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s)

phase test:
    Blocking(
        phase1 = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
        phase2 = Pair.ForwardDelay(Compound([a, x]), shock,
                                    isi=10-s, cs_duration=15-s),
        test   = Extinction(x)
    )
```

Note that the `Blocking(...)` identifier is **not** in Core's Tier A
reserved set; it resolves only because this package's registry is
loaded. If the registry is not loaded, Core emits a parse error — an
unknown `ExtensionRespondentPrimitive` is not silently accepted.

---

## 4. What this package does *not* do

- It does **not** redefine any Tier A primitive. `Pair.*`, `Extinction`,
  `CSOnly`, `USOnly`, `Contingency`, `TrulyRandom`,
  `ExplicitlyUnpaired`, `Compound`, `Serial`, `ITI`, and `Differential`
  are owned by Core.
- It does **not** alter the CFG class of the respondent grammar. Each
  new production is of the form `IdentUpper "(" ArgList? ")"`, which is
  already covered by the Core LL(2) analysis.
- It does **not** introduce Turing completeness. Every Tier B primitive
  is a finite, declarative procedure whose parameters are literal values
  at parse time.
- It does **not** write a parser. This checkpoint is specification only:
  grammar, AST schema, conformance fixtures, and docs. A Python parser
  is a separate follow-on effort.

---

## 5. Scientific scope of Tier B

The 26 Tier B primitives are selected from the Pavlovian-learning
literature as **procedurally distinct preparations that a working
researcher would want to name**. The selection is grounded in:

- Classic experimental-analysis-of-behavior treatment: Pavlov (1927);
  Rescorla (1967, 1968, 1969, 1970, 1971, 1972); Mackintosh (1974);
  Bouton (2004).
- Contemporary learning-theory review: Mackintosh (1975); Pearce & Hall
  (1980); Wagner (1981); Bouton (2016); Pearce (2013).
- Specific-procedure primary sources: Kamin (1969) for blocking;
  Holland (1983) for occasion setting; Garcia, Ervin, & Koelling (1966)
  for conditioned taste aversion; Monfils et al. (2009) for
  reconsolidation interference; Fanselow (1990) for contextual fear;
  Roberts (1981) for the peak procedure.

See [`spec/en/tier-b-primitives/_index.md`](tier-b-primitives/_index.md)
for the grouped table of all 26 primitives and their primary citations.

---

## 6. Relationship to Core annotations

Some Pavlovian phenomena could in principle be expressed as annotations
on Tier A primitives rather than as new grammar productions. Core's
`annotations/boundary-decision.md` governs that choice. The 26 primitives
in this package were all placed on the **extension-grammar side** of the
boundary because each of them:

- Introduces or constrains the **structure** of a multi-phase procedure
  (e.g., `Blocking` requires a specific Phase 1 / Phase 2 / Test sequence
  with compound CS presentation in Phase 2), rather than annotating a
  property of a single Tier A procedure.
- Is commonly named in the literature as its own preparation rather than
  as a modifier of another preparation.

Phenomena that *do* decompose cleanly into Tier A + annotation (CS
modality, US intensity, ITI jitter) remain in Core's
`annotations/extensions/respondent-annotator.md` and are not re-specified
here.

---

## 7. References

- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Bouton, M. E. (2016). *Learning and behavior: A contemporary synthesis*
  (2nd ed.). Sinauer.
- Fanselow, M. S. (1990). Factors governing one-trial contextual
  conditioning. *Animal Learning & Behavior*, 18(3), 264–270.
  https://doi.org/10.3758/BF03205285
- Garcia, J., Ervin, F. R., & Koelling, R. A. (1966). Learning with
  prolonged delay of reinforcement. *Psychonomic Science*, 5(3),
  121–122. https://doi.org/10.3758/BF03328311
- Holland, P. C. (1983). Occasion-setting in Pavlovian feature positive
  discriminations. In M. L. Commons, R. J. Herrnstein, & A. R. Wagner
  (Eds.), *Quantitative analyses of behavior* (Vol. 4, pp. 183–206).
  Ballinger.
- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment
  and aversive behavior* (pp. 279–296). Appleton-Century-Crofts.
- Mackintosh, N. J. (1974). *The psychology of animal learning*.
  Academic Press.
- Mackintosh, N. J. (1975). A theory of attention: Variations in the
  associability of stimuli with reinforcement. *Psychological Review*,
  82(4), 276–298. https://doi.org/10.1037/h0076778
- Monfils, M.-H., Cowansage, K. K., Klann, E., & LeDoux, J. E. (2009).
  Extinction-reconsolidation boundaries: Key to persistent attenuation
  of fear memories. *Science*, 324(5929), 951–955.
  https://doi.org/10.1126/science.1167975
- Pavlov, I. P. (1927). *Conditioned reflexes*. Oxford University Press.
- Pearce, J. M. (2013). *Animal learning and cognition* (3rd ed.).
  Psychology Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning:
  Variations in the effectiveness of conditioned but not of
  unconditioned stimuli. *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper control
  procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109
- Rescorla, R. A. (1969). Pavlovian conditioned inhibition. *Psychological
  Bulletin*, 72(2), 77–94. https://doi.org/10.1037/h0027760
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
- Roberts, S. (1981). Isolation of an internal clock. *Journal of
  Experimental Psychology: Animal Behavior Processes*, 7(3), 242–268.
  https://doi.org/10.1037/0097-7403.7.3.242
- Wagner, A. R. (1981). SOP: A model of automatic memory processing in
  animal behavior. In N. E. Spear & R. R. Miller (Eds.), *Information
  processing in animals: Memory mechanisms* (pp. 5–47). Erlbaum.

