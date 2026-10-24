# contingency-respondent-dsl

:jp: [日本語版 README](README.ja.md)

contingency-respondent-dsl describes 26 Pavlovian (respondent) conditioning procedures, such as blocking, overshadowing, latent inhibition, renewal, and reinstatement, as records with fixed field names that can be stored, compared, and exchanged as JSON. It is for researchers who keep respondent designs in configuration files, analysis pipelines, or tests. It extends [contingency-dsl](https://github.com/OperantKit/contingency-dsl), the procedure notation of [OperantKit](https://github.com/OperantKit).

**In short**

- Each procedure has one fixed set of fields, so two labs that write down "blocking" produce the same record.
- A missing, misspelled, or extra field raises an error instead of storing an incomplete design.
- Records convert to and from plain dictionaries that follow the JSON Schema in `schema/`.

## Installation

Python 3.11 or newer. The package is not on PyPI yet; install it from GitHub:

```bash
pip install git+https://github.com/OperantKit/contingency-respondent-dsl
```

It has no dependencies.

## Example

Build an ABA renewal procedure (Bouton & Bolles, 1979) from its fields, convert it to a JSON-ready dictionary and back, and see what happens when a required field is missing:

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

`parse_primitive` returns a frozen dataclass (`contingency_respondent_dsl.ast.Renewal` here). An unknown procedure name raises `UnknownPrimitiveError`, a positional argument raises `ArityError`, and an unexpected field raises `UnknownFieldError`. Durations are written as `{"value": 15, "unit": "s"}` or `(15, "s")`; a value that is not positive, or a unit other than `ms`, `s`, `min`, `h`, raises `ValueError`.

## The 26 procedures

| Family | Identifiers |
|---|---|
| Acquisition and higher-order | `HigherOrderConditioning`, `SensoryPreconditioning`, `Counterconditioning` |
| Cue competition | `Blocking`, `Overshadowing`, `Overexpectation`, `SuperConditioning`, `RetrospectiveRevaluation` |
| Inhibitory learning | `ConditionedInhibition`, `OccasionSetting`, `InhibitionOfDelay`, `SummationRetardationTest` |
| Preexposure | `LatentInhibition`, `USPreexposure` |
| Extinction and recovery | `Renewal`, `Reinstatement`, `SpontaneousRecovery`, `LatentExtinction`, `PavlovianPREE`, `ContextualExtinction`, `ReconsolidationInterference` |
| Specialized procedures | `ConditionedTasteAversion`, `StimulusGeneralization`, `ContextualFearConditioning`, `PeakProcedure`, `MediatedConditioning` |

Each procedure has its own page with an operational definition, its fields, and its primary citations; start from the [index](spec/en/tier-b-primitives/_index.md).

## Relationship to contingency-dsl

contingency-dsl keeps its respondent layer small: pairing (`Pair.*`), `Extinction`, `CSOnly`, `USOnly`, `Contingency`, `TrulyRandom`, `ExplicitlyUnpaired`, `Compound`, `Serial`, `ITI`, and `Differential` (the "Tier A" primitives). Procedures that combine several of these over phases, such as the 26 above (the "Tier B" primitives), are added through a single extension point in the Core respondent grammar, without changing that grammar:

```ebnf
ExtensionRespondentPrimitive ::= Identifier "(" ArgList? ")"
```

`contingency-respondent-dsl` is the first and canonical consumer of this extension point. Programs that use only the Core respondent primitives are unaffected by it.

## What is in this repository

- `spec/en/`, `spec/ja/`: the specification (architecture, how it plugs into Core, grammar, theory, one page per procedure)
- `schema/`: the EBNF grammar of the 26 procedures (`grammar.ebnf`), the JSON Schema of the records (`ast.schema.json`), and how a program loads the extension (`extension-registry.md`)
- `conformance/tier-b/`: 28 test cases in 26 files, one file per procedure, each with an input string and the expected record
- `src/contingency_respondent_dsl/`: the Python package (`parse_primitive`, `to_dict`, `from_dict`, `register`)

## Limitations

- This package does not read DSL text. It starts from the procedure name and its already-evaluated fields; reading text such as `Renewal(acquisition = ..., ...)` is the job of the Core parser [contingency-dsl-py](https://github.com/OperantKit/contingency-dsl-py). contingency-dsl-py does not parse these identifiers, and `TierBExtension` cannot be passed to its `ExtensionRegistry` as it is (it has no `annotation_keywords`), so text cannot be read end to end with the two packages.
- It describes procedures; it does not run sessions or simulate conditioning.
- The primary sources for `LatentExtinction` and `PavlovianPREE` are marked in the [index](spec/en/tier-b-primitives/_index.md) as requiring verification.

## For contributors

```bash
git clone https://github.com/OperantKit/contingency-respondent-dsl
cd contingency-respondent-dsl
mise exec -- python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/python -m pytest -q
```

The tests do not need contingency-dsl-py. Every `python` block in this README and in `README.ja.md` is run by `tests/test_readme_examples.py`. Notes for AI coding agents are in [AGENTS.md](AGENTS.md).

## References

- Bouton, M. E., & Bolles, R. C. (1979). Contextual control of the extinction of conditioned fear. *Learning and Motivation*, 10(4), 445–466. https://doi.org/10.1016/0023-9690(79)90057-2

## Citation and license

Cite this package with [CITATION.cff](CITATION.cff). MIT License; see [LICENSE](LICENSE).
