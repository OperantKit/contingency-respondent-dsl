# Integration with Core — The Respondent Extension Point Contract

> Part of the `contingency-respondent-dsl` package. Specifies exactly how
> this package's 26 Tier B primitives plug into the Core respondent
> grammar, with no modification to Core.

---

## 1. The contract, in one line

Core (`contingency-dsl/spec/en/respondent/grammar.md §4`) declares:

```ebnf
ExtensionRespondentPrimitive ::= IdentUpper "(" ArgList? ")"
IdentUpper                   ::= [A-Z][a-zA-Z0-9_]*
```

This package supplies concrete production rules that each instantiate
this single abstract rule with a specific identifier and argument
schema. That is the entire integration contract.

---

## 2. Obligations on each Tier B primitive

For every primitive `P` defined in this package:

1. **Identifier form.** `P` is spelled `Ident(...)`, where `Ident`
   matches `IdentUpper` and is **not** one of Core's Tier A reserved
   keywords (`Pair`, `ForwardDelay`, `ForwardTrace`, `Simultaneous`,
   `Backward`, `Extinction`, `CSOnly`, `USOnly`, `Contingency`,
   `TrulyRandom`, `ExplicitlyUnpaired`, `Compound`, `Serial`, `ITI`,
   `Differential`, `trials`, `isi`, `cs_duration`, `trace_interval`,
   `mode`, `mean`, `min_separation`, `p`, `fixed`, `uniform`,
   `exponential`).
2. **Argument list.** The argument list is a comma-separated sequence of
   keyword or positional arguments, each of which is:
   - a literal value (number with unit, probability, string label), or
   - a `StimulusRef` (let-bound identifier or string literal), or
   - a nested respondent expression (Tier A **or** Tier B) — this is what
     lets `Blocking(phase1=..., phase2=..., test=...)` reference other
     primitives.
3. **Phase 2 registry entry.** `P` registers itself in the Tier B
   registry with its declared argument schema. The registry maps
   `IdentUpper` → schema; Phase 2 uses this to validate argument arity
   and types.
4. **Non-TC.** `P`'s operational definition is a finite declarative
   procedure. It does not introduce iteration, recursion, or
   state-dependent branching into the grammar.

---

## 3. Program-scoped activation

A program that intends to use Tier B activates the registry in its
header (conceptual):

```
# Program header (syntax finalized by Core; conceptual shape below)
import respondent_tier_b
```

Once activated:

- Every Tier B identifier (`Blocking`, `LatentInhibition`, `Renewal`,
  etc.) resolves through this registry.
- Tier A identifiers continue to resolve through Core's Tier A rules
  (Tier B never shadows Tier A).
- Unknown identifiers remain parse errors; there is no fallback to
  "string".

A program that does *not* activate this registry cannot use Tier B
primitives: `Blocking(...)` in such a program is a parse error at Phase
2, not a syntax error at Phase 1.

---

## 4. Example program

```
# Program header
import respondent_tier_b

# Bindings
let tone_a = "tone_a"
let tone_x = "tone_x"
let shock  = "shock"

# Blocking (Kamin 1969)
Blocking(
    phase1 = Pair.ForwardDelay(tone_a, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(Compound([tone_a, tone_x]), shock,
                                isi=10-s, cs_duration=15-s),
    test   = Extinction(tone_x),
    phase1_trials = 40,
    phase2_trials = 20,
    test_trials   = 10
)
```

Here:

- `Blocking` is resolved through this package's registry.
- `Pair.ForwardDelay`, `Compound`, and `Extinction` are Tier A, resolved
  through Core.
- Numeric-with-unit literals (`10-s`, `15-s`) and the `trials` keyword
  follow Core's existing conventions.

---

## 5. Error handling at the boundary

| Scenario | Reported by | Error class |
|---|---|---|
| Syntactically malformed identifier (`3Blocking(...)`) | Core parser (Phase 1) | `SYNTAX` |
| Well-formed identifier but no registry activation | Core Phase 2 | `UNKNOWN_EXTENSION_PRIMITIVE` |
| Registry activated, identifier not registered | Core Phase 2 (with registry query) | `UNKNOWN_EXTENSION_PRIMITIVE` |
| Registered primitive, arity mismatch | Tier B schema validator | `ARITY_MISMATCH` |
| Registered primitive, argument type mismatch | Tier B schema validator | `TYPE_MISMATCH` |
| Registered primitive, required-field missing | Tier B schema validator | `MISSING_FIELD` |
| Registered primitive, unknown keyword | Tier B schema validator | `UNKNOWN_FIELD` |

The first two error classes are Core's responsibility; the remaining
four are this package's responsibility and are documented in
[`../../conformance/README.md`](../../conformance/README.md).

---

## 6. What the registry entry looks like (conceptual)

The registry is a data structure, not a language feature. A conceptual
entry (the concrete form is finalized when a parser is implemented):

```
registry_entry {
  identifier: "Blocking",
  arg_schema: {
    phase1:         RespondentExpr,  // required
    phase2:         RespondentExpr,  // required
    test:           RespondentExpr,  // required
    phase1_trials:  Number,          // optional, default unspecified
    phase2_trials:  Number,          // optional
    test_trials:    Number,          // optional
  },
  primary_citation: "Kamin (1969)",
  spec_file: "spec/en/tier-b-primitives/blocking.md",
}
```

The per-primitive pages in
[`tier-b-primitives/`](tier-b-primitives/) are the source of truth for
each entry.

---

## 7. What is explicitly *not* added to Core

This package does **not**:

- Redefine Tier A primitives.
- Add annotations to Core. Annotations remain the domain of
  `annotations/extensions/respondent-annotator.md` in Core.
- Add phase-sequencing semantics to Core. Phase sequencing continues to
  be governed by `experiment/phase-sequence.md` in Core, which is
  compatible with Tier B because each Tier B primitive that is itself a
  multi-phase procedure (blocking, renewal, reinstatement) expresses its
  internal phases through nested respondent expressions, not through new
  phase-level constructs.
- Introduce new annotation layers. Program-scoped behavior that would
  require new annotation families is out-of-scope for Tier B and should
  be proposed as a separate package.

