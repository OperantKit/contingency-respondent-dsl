# Conformance Fixtures — Tier B

> Part of the `contingency-respondent-dsl` package. This directory holds
> skeleton test fixtures, one JSON file per Tier B primitive.

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
| `expected_ast` | yes | Expected AST output. May be `null` with an associated `todo` field until a parser exists to validate against. |
| `todo` | no | If `expected_ast` is `null`, this string documents what the expected AST should contain. |

Future-extensible fields (`error`, `diagnostics`, `phase`) may be added
without breaking existing fixtures.

---

## 2. Current status — design checkpoint

At this checkpoint the conformance directory holds **skeleton
fixtures**: one representative valid input per primitive, with
`expected_ast: null` and a `todo` description. A parser is not yet
implemented; the skeletons exist to anchor the fixture format and to
give a later parser implementation a concrete target.

When a parser becomes available, each case's `expected_ast` should be
filled in to mirror the structure declared by
[`../schema/ast.schema.json`](../schema/ast.schema.json).

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

