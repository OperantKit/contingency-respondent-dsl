# Extension Registry — How a Program Loads Tier B

> Part of the `contingency-respondent-dsl` package. Describes how a
> program declares use of this extension registry, how the registry is
> structured, and how Core's parser discovers it.

---

## 1. What the registry is

The registry is a data structure that maps an identifier
(`<IdentUpper>`) to the argument schema, semantics anchor, and
provenance of a Tier B primitive. It is **not** a language construct
— the DSL grammar does not grow a "registry" keyword. The registry is
consumed at Phase 2 (post-parsing) by Core's respondent layer to
resolve any `ExtensionRespondentPrimitive` whose identifier is not a
Tier A reserved word.

Anchoring clause from Core:

> **Core `spec/en/respondent/grammar.md §4`:** "Extensions add
> production rules; they do not rewrite existing Tier A rules...
> Program-scoped closure: Each program maintains its own respondent
> registry."

This package supplies exactly one registry, named
`respondent_tier_b`, containing the 26 primitives enumerated in
[`../spec/en/tier-b-primitives/_index.md`](../spec/en/tier-b-primitives/_index.md).

---

## 2. Program-level activation (conceptual)

Pending Core's finalized registry-import syntax, the conceptual form
of program activation is:

```
# Program header
import respondent_tier_b
```

The activation directive (a) declares intent to use the registry's
identifiers, (b) gives the respondent parser a handle to resolve those
identifiers at Phase 2, and (c) is program-scoped: two co-executing
programs may import incompatible registries without interference.

If the program body uses `Blocking(...)` but omits
`import respondent_tier_b`, Core emits a Phase-2 error
`UNKNOWN_EXTENSION_PRIMITIVE`.

---

## 3. Registry entry shape

Each entry in `respondent_tier_b` has the following conceptual shape
(the concrete form is finalized by Core when registry APIs land):

```
RegistryEntry {
  identifier:        String,           # IdentUpper form
  arg_schema:        JsonSchemaRef,    # $ref into schema/ast.schema.json
  primary_citation:  ApaEntry,         # author, year, venue, DOI
  spec_file:         String,           # relative path into spec/en/tier-b-primitives/
  ja_spec_file:      String,           # relative path into spec/ja/tier-b-primitives/
}
```

For `Blocking`:

```
RegistryEntry {
  identifier:       "Blocking",
  arg_schema:       "schema/ast.schema.json#/$defs/Blocking",
  primary_citation: "Kamin, L. J. (1969). Predictability, surprise, attention,
                     and conditioning. In B. A. Campbell & R. M. Church (Eds.),
                     Punishment and aversive behavior (pp. 279-296).
                     Appleton-Century-Crofts.",
  spec_file:        "spec/en/tier-b-primitives/blocking.md",
  ja_spec_file:     "spec/ja/tier-b-primitives/blocking.md",
}
```

All 26 entries share this shape. The per-primitive pages under
[`../spec/en/tier-b-primitives/`](../spec/en/tier-b-primitives/) are the
source of truth for the registry content; an implementation is
expected to generate the registry automatically from those pages (or
from the JSON Schema, depending on which direction of truth is chosen
at implementation time).

---

## 4. What activation does *not* do

- It does not load code. This package has no executable code; the
  registry is purely declarative.
- It does not shadow Tier A identifiers. A program that writes
  `Extinction(tone)` always resolves through Core's Tier A rules,
  whether or not `respondent_tier_b` is imported.
- It does not alter parsing of the program prefix. The `import`
  directive (or its eventual syntactic equivalent) sits at the
  program header and has no effect on later token-level parsing.

---

## 5. Cross-reference

- Parent extension-point specification: `contingency-dsl/spec/en/
  respondent/grammar.md §4`.
- This package's grammar: [`grammar.ebnf`](grammar.ebnf).
- This package's AST JSON Schema: [`ast.schema.json`](ast.schema.json).
- Per-primitive pages: [`../spec/en/tier-b-primitives/`](../spec/en/tier-b-primitives/).

