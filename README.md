# contingency-respondent-dsl

Tier B Pavlovian (respondent) procedure extension for
[`contingency-dsl`](../contingency-dsl/). This package defines 26 classical
conditioning procedures that extend the Core respondent layer **without
modifying** its grammar, by registering production rules through the
`ExtensionRespondentPrimitive` extension point.

## Relationship to `contingency-dsl`

The Core package keeps the respondent layer deliberately minimal — only the
foundational two-term contingency primitives (R1–R14: `Pair.*`, `Extinction`,
`CSOnly`, `USOnly`, `Contingency`, `TrulyRandom`, `ExplicitlyUnpaired`,
`Compound`, `Serial`, `ITI`, `Differential`). The Core respondent grammar
exposes a single extension hook:

```ebnf
ExtensionRespondentPrimitive ::= Identifier "(" ArgList? ")"
```

Any third-party respondent vocabulary that needs deeper Pavlovian coverage
registers its identifiers through this point. `contingency-respondent-dsl` is
the first and canonical consumer.

## Scope — 26 Tier B primitives

Grouped by conceptual family (see [`spec/en/tier-b-primitives/_index.md`](spec/en/tier-b-primitives/_index.md)):

- **Acquisition & higher-order** — higher-order conditioning (Pavlov, 1927;
  Rizley & Rescorla, 1972), sensory preconditioning (Brogden, 1939),
  counterconditioning (Dickinson & Pearce, 1977).
- **Cue competition** — blocking (Kamin, 1969), overshadowing (Mackintosh,
  1976), overexpectation (Rescorla, 1970), super-conditioning (Rescorla,
  1971), retrospective revaluation (Van Hamme & Wasserman, 1994).
- **Inhibitory learning** — conditioned inhibition (Rescorla, 1969),
  occasion setting (Holland, 1983), inhibition of delay (Pavlov, 1927),
  summation / retardation test (Rescorla, 1969).
- **Preexposure** — latent inhibition (Lubow & Moore, 1959), US preexposure
  (Randich & LoLordo, 1979).
- **Extinction & recovery** — renewal (Bouton & Bolles, 1979), reinstatement
  (Rescorla & Heth, 1975), spontaneous recovery (Rescorla, 2004), latent
  extinction, Pavlovian partial-reinforcement extinction effect, contextual
  extinction (Bouton, 2004), reconsolidation interference (Monfils et al.,
  2009).
- **Specialized procedures** — conditioned taste aversion (Garcia, Ervin, &
  Koelling, 1966), stimulus generalization (Hovland, 1937), contextual fear
  conditioning (Fanselow, 1990), peak procedure (Roberts, 1981), mediated
  conditioning (Holland, 1981).

## Repository layout

```
contingency-respondent-dsl/
├── spec/en/                      formal specification (English canon)
│   ├── architecture.md           how this package plugs into Core
│   ├── design-philosophy.md      additive-only extension discipline
│   ├── integration-with-core.md  extension-point contract
│   ├── grammar.md                EBNF for all 26 Tier B primitives
│   ├── theory.md                 Pavlovian learning framework (pointer-level)
│   ├── auxiliary.md             design-checkpoint log
│   └── tier-b-primitives/        one file per primitive + _index.md
├── spec/ja/                      Japanese mirror of spec/en/
├── schema/
│   ├── grammar.ebnf              the 26 Tier B productions
│   ├── ast.schema.json           JSON Schema 2020-12 for AST nodes
│   └── extension-registry.md     how a program loads this registry
├── conformance/
│   ├── README.md
│   └── tier-b/                   one .json fixture file per primitive
└── docs/
    ├── en/README.md
    └── ja/README.md
```

## Status

This package is a **specification-only design checkpoint**. It provides:

- The EBNF productions for 26 Pavlovian procedures that extend Core's
  `ExtensionRespondentPrimitive`.
- A JSON Schema (2020-12) for the resulting AST nodes.
- Per-primitive operational definitions with primary APA citations.
- Conformance fixture skeletons suitable for use once a parser exists.

A Python parser implementation, a runtime registry, and a conformance
validator are **not** part of this checkpoint; they are separate follow-on
efforts. No installation instructions are provided at this time.

## Navigation

- Formal specification (English): [`spec/en/`](spec/en/)
- Formal specification (Japanese): [`spec/ja/`](spec/ja/)
- EBNF grammar: [`schema/grammar.ebnf`](schema/grammar.ebnf)
- AST JSON Schema: [`schema/ast.schema.json`](schema/ast.schema.json)
- Per-primitive index: [`spec/en/tier-b-primitives/_index.md`](spec/en/tier-b-primitives/_index.md)
- Conformance fixtures: [`conformance/tier-b/`](conformance/tier-b/)

## References (selected)

- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment and
  aversive behavior* (pp. 279–296). Appleton-Century-Crofts.
- Mackintosh, N. J. (1975). A theory of attention: Variations in the
  associability of stimuli with reinforcement. *Psychological Review*,
  82(4), 276–298. https://doi.org/10.1037/h0076778
- Pavlov, I. P. (1927). *Conditioned reflexes*. Oxford University Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning:
  Variations in the effectiveness of conditioned but not of unconditioned
  stimuli. *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper control
  procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
