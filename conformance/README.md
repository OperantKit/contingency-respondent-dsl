# Conformance Fixtures — Tier B

> Part of the `contingency-respondent-dsl` package. This directory holds
> test fixtures, one JSON file per Tier B primitive.

---

## 1. Structure

```
conformance/
├── README.md
└── tier-b/
    ├── blocking.json
    ├── higher-order-conditioning.json
    ├── ...
```

Each file in `tier-b/` contains a JSON array of test cases for one
primitive. Each test case is an object with:

| Field | Required | Description |
|---|---|---|
| `id` | yes | Unique case identifier, kebab-case (e.g. `"blocking-basic"`). |
| `comment` | yes | One-line description of what the case exercises. |
| `input` | yes | The DSL string that the parser should consume. |
| `expected_ast` | yes | Expected AST output, mirroring [`../schema/ast.schema.json`](../schema/ast.schema.json). May be `null` with an associated `todo` field for a case whose expected AST is not yet written. |
| `todo` | no | If `expected_ast` is `null`, this string documents what the expected AST should contain. |

Future-extensible fields (`error`, `diagnostics`, `phase`) may be added
without breaking existing fixtures.

---

## 2. Current status

All 26 primitives have a fixture file (28 cases in total), and every
case has an `input` string and a concrete `expected_ast`; no case is
`null`. The test suite (`tests/test_conformance.py`) round-trips each
`expected_ast` through `from_dict` / `to_dict`, and
`tests/test_tier_b_parser.py` dispatches each one through
`parse_primitive()`. The `input` string is not re-parsed here, because
this package does not read DSL source text; that is the Core parser's
job.

---

## 3. Fixture file scope

- Exactly 26 JSON files under [`tier-b/`](tier-b/), one per Tier B
  primitive, named with the same kebab-case stem used in
  `spec/en/tier-b-primitives/`.
- No cross-primitive compound cases in this checkpoint. Composite
  fixtures may be added later under a sibling directory
  (`conformance/compositions/` or similar) when the parser supports it.

---

## 4. Running (future)

Once a parser exists, a typical invocation will be:

```
# conceptual; exact form decided at parser-implementation time
python -m contingency_respondent_dsl.conformance run conformance/tier-b/
```

Until then, the fixtures are read-only specifications and each JSON
file must remain valid per `python -m json.tool`.

---

## 5. Error-class conventions (when populated)

Cases that demonstrate errors should use the error classes enumerated
in [`../spec/en/integration-with-core.md §5`](../spec/en/integration-with-core.md):
`SYNTAX`, `UNKNOWN_EXTENSION_PRIMITIVE`, `ARITY_MISMATCH`,
`TYPE_MISMATCH`, `MISSING_FIELD`, `UNKNOWN_FIELD`. The first two are
reported by Core; the latter four by this package's Tier B schema
validator.

