# contingency-respondent-dsl — Docs (English)

User-facing overview of the Tier B Pavlovian extension for
[`contingency-dsl`](../../../contingency-dsl/). The formal specification
lives in [`../../spec/en/`](../../spec/en/); this page is a short
introduction and navigation index.

## What is this?

`contingency-respondent-dsl` extends the Core respondent layer with 26
Pavlovian conditioning procedures — blocking, overshadowing, latent
inhibition, renewal, reinstatement, conditioned inhibition, occasion
setting, conditioned taste aversion, the peak procedure, and others.

It plugs into Core via a single extension point
(`ExtensionRespondentPrimitive`) and adds no new layer to the Core
architecture. Programs activate Tier B by declaring the registry in
their header (conceptual: `import respondent_tier_b`); Tier A stays
untouched.

## Status — specification only

There is **no parser** for this package yet. Integration happens via
a future parser that consumes the Core parse tree and hands off Tier B
identifiers to this extension registry. At this design checkpoint
the package provides:

- Per-primitive operational specifications with primary APA citations
  in [`../../spec/en/tier-b-primitives/`](../../spec/en/tier-b-primitives/).
- An EBNF grammar for the 26 Tier B productions in
  [`../../schema/grammar.ebnf`](../../schema/grammar.ebnf).
- A JSON Schema (2020-12) for AST nodes in
  [`../../schema/ast.schema.json`](../../schema/ast.schema.json).
- Conformance fixture skeletons in
  [`../../conformance/tier-b/`](../../conformance/tier-b/).

No installation instructions are provided at this time.

## Where to start

- **Overview of what lives where:** [`../../README.md`](../../README.md).
- **Architecture and how this plugs into Core:**
  [`../../spec/en/architecture.md`](../../spec/en/architecture.md).
- **Extension-point contract:**
  [`../../spec/en/integration-with-core.md`](../../spec/en/integration-with-core.md).
- **Full primitive table:**
  [`../../spec/en/tier-b-primitives/_index.md`](../../spec/en/tier-b-primitives/_index.md).
- **EBNF grammar:** [`../../schema/grammar.ebnf`](../../schema/grammar.ebnf).
- **Theory framework (pointer-level):**
  [`../../spec/en/theory.md`](../../spec/en/theory.md).

## Scope boundary

Phenomena that are genuinely operant (instrumental), three-term, or
compositions of operant and respondent procedures are *not* handled
here. Those remain in Core's `operant/` and `composed/` layers.
Phenomena that are annotations on Tier A primitives (CS modality, US
intensity) are handled by Core's
`annotations/extensions/respondent-annotator.md`.

## Contributing

- Follow [`../../CLAUDE.md`](../../CLAUDE.md) for file-access,
  design-checkpoint, and privacy rules.
- Add new primitives by (a) adding a spec page under
  `spec/en/tier-b-primitives/` plus its JA mirror, (b) extending
  `schema/grammar.ebnf` and `schema/ast.schema.json`, (c) adding a
  fixture under `conformance/tier-b/`, and (d) adding an entry to
  `spec/en/tier-b-primitives/_index.md` and its JA mirror.
- Every primitive requires a peer-reviewed primary citation in APA
  format.
