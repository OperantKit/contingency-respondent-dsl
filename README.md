# contingency-respondent-dsl

:jp: [日本語版 README](README.ja.md)

Tier B Pavlovian (respondent) procedure extension for
[`contingency-dsl`](https://github.com/OperantKit/contingency-dsl). This package defines 26 classical
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

This package currently provides:

- The EBNF productions for 26 Pavlovian procedures that extend Core's
  `ExtensionRespondentPrimitive` (see [`spec/en/grammar.md`](spec/en/grammar.md)).
- A JSON Schema for the resulting AST nodes
  (see [`schema/ast.schema.json`](schema/ast.schema.json)).
- Per-primitive operational definitions with primary APA citations.
- A Python parser for all 26 primitives (`src/contingency_respondent_dsl/`) with:
  - Frozen dataclasses for all 26 primitives (`ast.py`).
  - A registry that dispatches identifier + keyword-args bags to AST
    constructors (`registry.py`).
  - A dict serializer compatible with the AST schema (`serializer.py`).
  - A thin `parse_primitive()` entrypoint (`parser.py`).
- Conformance fixtures for all 26 primitives (28 cases in 26 files under
  `conformance/tier-b/`), each with an `input` string and a concrete
  `expected_ast` dict.

## Installation

```bash
pip install git+https://github.com/OperantKit/contingency-respondent-dsl
```

For local development this package uses `mise` + `venv` per the upstream
OperantKit policy. `uv` is not used.

```sh
# From inside contingency-respondent-dsl/
mise exec -- python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/pytest tests/ -q
```

The Core parser (`contingency-dsl-py`) is a separate sibling package and
is not required to exercise this package's own unit tests: the Tier B
parser operates on already-evaluated keyword arguments at the extension
boundary, and nested Tier A expressions are treated as opaque dicts on
that boundary.

## 30-second example

Build an ABA renewal procedure from its keyword arguments, serialize it to a JSON-ready dict, restore it, and see what happens when a required field is missing:

```python
import json

from contingency_respondent_dsl import MissingFieldError, from_dict, parse_primitive, to_dict

# ABA renewal: CS-US pairing in context A, extinction in context B, test in context A.
arguments = {
    "acquisition": {"type": "Pair.ForwardDelay", "cs": "tone", "us": "shock"},
    "extinction": {"type": "Extinction", "cs": "tone"},
    "test": {"type": "Extinction", "cs": "tone"},
    "acquisition_context": "ctx_a",
    "extinction_context": "ctx_b",
    "test_context": "ctx_a",
}
node = parse_primitive("Renewal", keyword_args=arguments)
ast = to_dict(node)  # plain dict, ready for json.dumps
print(ast["type"], [ast[k] for k in ("acquisition_context", "extinction_context", "test_context")])
# Renewal ['ctx_a', 'ctx_b', 'ctx_a']
print(from_dict(json.loads(json.dumps(ast))) == node)  # True

incomplete = {k: v for k, v in arguments.items() if k != "test_context"}
try:
    parse_primitive("Renewal", keyword_args=incomplete)
except MissingFieldError as error:
    print(error)  # missing required keyword(s) for Renewal: ['test_context']
```

The example needs only this package. Reading DSL source text such as `Renewal(acquisition = ..., ...)` is the job of the Core parser [contingency-dsl-py](https://github.com/OperantKit/contingency-dsl-py) (`pip install contingency-dsl-py`); this package does not depend on it and starts from the already-evaluated arguments.

## Why not a 50-line hand-written procedure record?

A dict or a small class per experiment works for one procedure, but breaks once several Pavlovian designs have to be stored, compared, and exchanged:

- **26 named procedures.** Blocking, overshadowing, overexpectation, latent inhibition, renewal, reinstatement, spontaneous recovery, conditioned inhibition, occasion setting, the peak procedure, and 16 others are registered as frozen dataclasses with fixed field names, so two labs writing "blocking" produce the same structure.
- **Conformance fixtures.** 28 cases in 26 fixture files under `conformance/tier-b/` cover every primitive. The tests replay each case through `parse_primitive` and through `from_dict` / `to_dict` and require the serialized dict to match the fixture exactly.
- **Arguments are validated.** An unknown identifier raises `UnknownPrimitiveError`, a positional argument raises `ArityError`, an omitted required keyword raises `MissingFieldError`, and an unexpected keyword raises `UnknownFieldError`, instead of silently storing an incomplete design.
- **Durations are checked.** Duration fields (for example the CS duration and ISI in inhibition of delay) accept `{"value": 15, "unit": "s"}` or `(15, "s")`; a non-positive value or a unit other than `ms`, `s`, `min`, `h` raises `ValueError`.
- **Additive to Core.** The primitives extend the Core respondent layer through the single `ExtensionRespondentPrimitive` hook, so programs that use only Core respondent primitives (`Pair.*`, `Extinction`, `CSOnly`, ...) are unaffected.

## Usage

```python
from contingency_respondent_dsl import (
    parse_primitive,
    to_dict,
    from_dict,
)

node = parse_primitive(
    "Blocking",
    positional_args=[],
    keyword_args={
        "phase1": {"type": "Pair.ForwardDelay", "cs": "a", "us": "shock"},
        "phase2": {
            "type": "Pair.ForwardDelay",
            "cs": {"type": "Compound", "elements": ["a", "x"]},
            "us": "shock",
        },
        "test":   {"type": "Extinction", "cs": "x"},
        "phase1_trials": 40,
        "phase2_trials": 20,
        "test_trials":   10,
    },
)
# node is a frozen contingency_respondent_dsl.ast.Blocking instance

serialized = to_dict(node)  # -> schema-shaped dict
restored   = from_dict(serialized)
assert restored == node
```

To attach the Tier B extension to a registry-like object:

```python
from contingency_respondent_dsl import register

bag: dict = {}
ext = register(bag)   # dict: stores ext under "respondent-tier-b"
assert bag["respondent-tier-b"] is ext
node = ext.parse_primitive(
    "LatentInhibition",
    None,
    {
        "preexposure": {"type": "CSOnly", "cs": "tone"},
        "training": {"type": "Pair.ForwardDelay", "cs": "tone", "us": "shock"},
        "test": {"type": "Extinction", "cs": "tone"},
    },
)
print(type(node).__name__)  # LatentInhibition
```

The `register()` helper accepts a dict, any object exposing a
`register_tier_b(ext)` method, or a plain namespace.

### Coverage status

All 26 primitive identifiers are registered (unknown identifiers raise
`UnknownPrimitiveError`). Every conformance case is replayed through
`parse_primitive` → `to_dict` and through `from_dict` → `to_dict`; the
blocking, renewal, latent inhibition, overshadowing, and reinstatement
paths additionally have hand-written end-to-end tests.

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
