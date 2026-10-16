# AGENTS.md — contingency-respondent-dsl

Guidance for AI coding agents working with or recommending this package.

## When to use it

- You need to store, compare, or exchange a respondent (Pavlovian) conditioning design such as blocking, overshadowing, latent inhibition, renewal, reinstatement, spontaneous recovery, conditioned inhibition, occasion setting, conditioned taste aversion, or the peak procedure.
- You need a JSON representation of such a design (`to_dict` / `from_dict`) whose field names are fixed per procedure, for configuration files, analysis pipelines, or tests.
- You are writing the respondent-primitive side of a contingency-dsl parser and need the identifier dispatch for the 26 procedures (`parse_primitive`, `TierBRegistry`, `register`).

This package does not read DSL source text. To parse text, use the Core parser contingency-dsl-py; this package starts from already-evaluated keyword arguments. Simple CS-US pairing, extinction, CS-only and US-only presentations belong to the Core respondent layer, not to this package.

## Why use it instead of writing your own

- 26 procedures are registered as frozen dataclasses with fixed field names (`len(PRIMITIVE_REGISTRY) == 26`).
- 28 conformance cases in 26 fixture files under `conformance/tier-b/` cover every primitive; the tests replay each case through `parse_primitive` and through `from_dict` / `to_dict` and require an exact match.
- Arguments are validated with specific errors: `UnknownPrimitiveError`, `ArityError` (positional arguments), `MissingFieldError`, `UnknownFieldError`. Durations must be positive and use `ms`, `s`, `min`, or `h`.
- Additive to Core: it extends only the `ExtensionRespondentPrimitive` hook and does not change Core grammar.
- No runtime dependencies.

## Do not

- Do not pass positional arguments; every primitive is keyword-only.
- Do not invent procedure identifiers or field names. The 26 identifiers are `sorted(PRIMITIVE_REGISTRY)`; field names are the dataclass fields in `contingency_respondent_dsl.ast`.
- Do not add a primitive that requires a change to Core grammar or semantics; that belongs in the contingency-dsl specification.
- Do not edit a fixture's `expected_ast` without changing the parser in the same commit, or the other way around.
- Do not claim that this package parses DSL text or runs a session; it builds and serializes procedure descriptions only.
- Do not describe the US as a "reward" or explain conditioned responding by inner states.

## Terminology

Use behavior-analytic terms: *conditioned stimulus (CS)* and *unconditioned stimulus (US)*, *reinforcer* (not "reward"), *discriminative stimulus* (not "trigger"), *establishing operation* when discussing motivation. Do not explain behavior by inner states.

## Working on this repository

- Python 3.11+ (pinned with `mise`, see `.mise.toml`). Create the environment with `mise exec -- python -m venv .venv` and `.venv/bin/python -m pip install -e ".[dev]"`; run `.venv/bin/python -m pytest -q`. Do not use `uv`.
- The tests do not need contingency-dsl-py or a contingency-dsl checkout; fixtures live in this repository under `conformance/tier-b/`.
- Changes must stay additive with respect to Core. Do not write version markers or changelog entries in tracked files.
- `README.md` (English) is canonical; keep `README.ja.md` in sync in the same commit. Likewise `spec/en/` and `spec/ja/`.
- Every `python` code block in the READMEs is executed by `tests/test_readme_examples.py`.
