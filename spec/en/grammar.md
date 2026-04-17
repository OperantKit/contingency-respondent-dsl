# Grammar — Tier B Respondent Primitives

> Part of the `contingency-respondent-dsl` package. Specifies the EBNF
> for the 26 Tier B Pavlovian procedures this package registers through
> Core's `ExtensionRespondentPrimitive` extension point.

---

## 1. Scope and conventions

The productions below extend Core's `ExtensionRespondentPrimitive`
(Core: `spec/en/respondent/grammar.md §4`). None of them redefine any
Tier A rule; none introduce new LL(2) decision points; none add
Turing-complete constructs. Every Tier B primitive is spelled
`IdentUpper "(" ArgList? ")"` and is distinguishable from any other
primitive at its first token.

Shared terminal and lexical rules (`StimulusRef`, `Number`, `Duration`,
`Probability`, `ContextRef`, `RespondentExpr`) are inherited from Core
(`schema/foundations/grammar.ebnf` and `schema/respondent/grammar.ebnf`
in `contingency-dsl`). The canonical spellings used below are:

- `StimulusRef` = identifier or double-quoted string
- `ContextRef` = identifier or double-quoted string, denoting an
  experimental context (Core `foundations/context.md`)
- `RespondentExpr` = any Tier A or Tier B respondent expression
- `Number` = decimal or integer
- `Duration` = `Number "-" TimeUnit` (`TimeUnit` one of `ms`, `s`, `min`)
- `Probability` = `Number` in `[0, 1]`

Keyword-vs-positional policy follows Core conventions: positional forms
are defined where argument order is unambiguous; keyword forms are
preferred when a primitive has three or more arguments or any optional
argument.

---

## 2. Productions — Acquisition and higher-order family

```ebnf
HigherOrderConditioningExpr ::=
    "HigherOrderConditioning" "(" "phase1" "=" RespondentExpr
                                ","  "phase2" "=" RespondentExpr
                                ("," "phase1_trials" "=" Number)?
                                ("," "phase2_trials" "=" Number)? ")"

SensoryPreconditioningExpr ::=
    "SensoryPreconditioning" "(" "phase1" "=" RespondentExpr
                                "," "phase2" "=" RespondentExpr
                                "," "test"   "=" RespondentExpr
                                ("," "phase1_trials" "=" Number)?
                                ("," "phase2_trials" "=" Number)? ")"

CounterconditioningExpr ::=
    "Counterconditioning" "(" "phase1" "=" RespondentExpr
                             "," "phase2" "=" RespondentExpr
                             ("," "phase1_trials" "=" Number)?
                             ("," "phase2_trials" "=" Number)? ")"
```

---

## 3. Productions — Cue-competition family

```ebnf
BlockingExpr ::=
    "Blocking" "(" "phase1" "=" RespondentExpr
                  "," "phase2" "=" RespondentExpr
                  "," "test"   "=" RespondentExpr
                  ("," "phase1_trials" "=" Number)?
                  ("," "phase2_trials" "=" Number)?
                  ("," "test_trials"   "=" Number)? ")"

OvershadowingExpr ::=
    "Overshadowing" "(" "training" "=" RespondentExpr
                       "," "test_a" "=" RespondentExpr
                       "," "test_b" "=" RespondentExpr
                       ("," "training_trials" "=" Number)? ")"

OverexpectationExpr ::=
    "Overexpectation" "(" "phase1_a" "=" RespondentExpr
                         "," "phase1_b" "=" RespondentExpr
                         "," "phase2_compound" "=" RespondentExpr
                         "," "test" "=" RespondentExpr
                         ("," "phase1_trials" "=" Number)?
                         ("," "phase2_trials" "=" Number)? ")"

SuperConditioningExpr ::=
    "SuperConditioning" "(" "phase1_inhibitor" "=" RespondentExpr
                           "," "phase2_target"  "=" RespondentExpr
                           "," "test" "=" RespondentExpr ")"

RetrospectiveRevaluationExpr ::=
    "RetrospectiveRevaluation" "(" "phase1_compound" "=" RespondentExpr
                                  "," "phase2_element" "=" RespondentExpr
                                  "," "test" "=" RespondentExpr ")"
```

---

## 4. Productions — Inhibitory-learning family

```ebnf
ConditionedInhibitionExpr ::=
    "ConditionedInhibition" "(" "training" "=" RespondentExpr
                               "," "test" "=" RespondentExpr
                               ("," "training_trials" "=" Number)? ")"

OccasionSettingExpr ::=
    "OccasionSetting" "(" "feature" "=" StimulusRef
                         "," "target"  "=" StimulusRef
                         "," "us"      "=" StimulusRef
                         "," "mode"    "=" ("FeaturePositive" | "FeatureNegative")
                         ("," "training_trials" "=" Number)? ")"

InhibitionOfDelayExpr ::=
    "InhibitionOfDelay" "(" "cs" "=" StimulusRef
                           "," "us" "=" StimulusRef
                           "," "cs_duration" "=" Duration
                           "," "isi" "=" Duration
                           ("," "training_trials" "=" Number)? ")"

SummationRetardationTestExpr ::=
    "SummationRetardationTest" "(" "inhibitor" "=" StimulusRef
                                  "," "excitor"   "=" StimulusRef
                                  "," "us"        "=" StimulusRef
                                  "," "mode"      "=" ("Summation" | "Retardation") ")"
```

---

## 5. Productions — Preexposure family

```ebnf
LatentInhibitionExpr ::=
    "LatentInhibition" "(" "preexposure" "=" RespondentExpr
                          "," "training"   "=" RespondentExpr
                          "," "test"       "=" RespondentExpr
                          ("," "preexposure_trials" "=" Number)?
                          ("," "training_trials"    "=" Number)? ")"

USPreexposureExpr ::=
    "USPreexposure" "(" "preexposure" "=" RespondentExpr
                       "," "training"   "=" RespondentExpr
                       "," "test"       "=" RespondentExpr
                       ("," "preexposure_trials" "=" Number)?
                       ("," "training_trials"    "=" Number)? ")"
```

---

## 6. Productions — Extinction-and-recovery family

```ebnf
RenewalExpr ::=
    "Renewal" "(" "acquisition"  "=" RespondentExpr
                 "," "extinction"   "=" RespondentExpr
                 "," "test"         "=" RespondentExpr
                 "," "acquisition_context" "=" ContextRef
                 "," "extinction_context"  "=" ContextRef
                 "," "test_context"        "=" ContextRef ")"

ReinstatementExpr ::=
    "Reinstatement" "(" "acquisition" "=" RespondentExpr
                       "," "extinction"  "=" RespondentExpr
                       "," "reinstatement_us" "=" RespondentExpr
                       "," "test"        "=" RespondentExpr ")"

SpontaneousRecoveryExpr ::=
    "SpontaneousRecovery" "(" "acquisition" "=" RespondentExpr
                             "," "extinction"  "=" RespondentExpr
                             "," "retention_interval" "=" Duration
                             "," "test"        "=" RespondentExpr ")"

LatentExtinctionExpr ::=
    "LatentExtinction" "(" "acquisition" "=" RespondentExpr
                          "," "preexposure" "=" RespondentExpr
                          "," "test" "=" RespondentExpr
                          ("," "preexposure_trials" "=" Number)? ")"

PavlovianPREEExpr ::=
    "PavlovianPREE" "(" "acquisition" "=" RespondentExpr
                       "," "extinction" "=" RespondentExpr
                       "," "test" "=" RespondentExpr
                       "," "reinforcement_probability" "=" Probability ")"

ContextualExtinctionExpr ::=
    "ContextualExtinction" "(" "acquisition" "=" RespondentExpr
                              "," "extinction" "=" RespondentExpr
                              "," "test" "=" RespondentExpr
                              "," "context" "=" ContextRef ")"

ReconsolidationInterferenceExpr ::=
    "ReconsolidationInterference" "(" "acquisition" "=" RespondentExpr
                                     "," "reactivation" "=" RespondentExpr
                                     "," "interference_window" "=" Duration
                                     "," "extinction" "=" RespondentExpr
                                     "," "test" "=" RespondentExpr ")"
```

---

## 7. Productions — Specialized procedures

```ebnf
ConditionedTasteAversionExpr ::=
    "ConditionedTasteAversion" "(" "taste_cs" "=" StimulusRef
                                  "," "visceral_us" "=" StimulusRef
                                  "," "cs_duration" "=" Duration
                                  "," "delay_to_us"  "=" Duration
                                  ("," "training_trials" "=" Number)? ")"

StimulusGeneralizationExpr ::=
    "StimulusGeneralization" "(" "training" "=" RespondentExpr
                                "," "test_gradient" "=" "[" StimulusRef ("," StimulusRef)+ "]"
                                ("," "training_trials" "=" Number)?
                                ("," "test_trials" "=" Number)? ")"

ContextualFearConditioningExpr ::=
    "ContextualFearConditioning" "(" "context" "=" ContextRef
                                    "," "us" "=" StimulusRef
                                    "," "us_onset_from_entry" "=" Duration
                                    ("," "training_trials" "=" Number)? ")"

PeakProcedureExpr ::=
    "PeakProcedure" "(" "cs" "=" StimulusRef
                       "," "us" "=" StimulusRef
                       "," "fi_duration" "=" Duration
                       "," "peak_probe_duration" "=" Duration
                       ("," "peak_probe_probability" "=" Probability)?
                       ("," "training_trials" "=" Number)? ")"

MediatedConditioningExpr ::=
    "MediatedConditioning" "(" "phase1" "=" RespondentExpr
                              "," "phase2" "=" RespondentExpr
                              "," "test" "=" RespondentExpr
                              ("," "phase1_trials" "=" Number)?
                              ("," "phase2_trials" "=" Number)? ")"
```

---

## 8. Reserved-keyword disjointness check

The identifiers introduced above are:

```
HigherOrderConditioning, SensoryPreconditioning, Counterconditioning,
Blocking, Overshadowing, Overexpectation, SuperConditioning,
RetrospectiveRevaluation,
ConditionedInhibition, OccasionSetting, InhibitionOfDelay,
SummationRetardationTest,
LatentInhibition, USPreexposure,
Renewal, Reinstatement, SpontaneousRecovery, LatentExtinction,
PavlovianPREE, ContextualExtinction, ReconsolidationInterference,
ConditionedTasteAversion, StimulusGeneralization,
ContextualFearConditioning, PeakProcedure, MediatedConditioning
```

None of these collides with Core's Tier A reserved set listed in
`contingency-dsl/spec/en/respondent/grammar.md §3`.

New keyword-argument names introduced here (`phase1`, `phase2`,
`training`, `test`, `preexposure`, `acquisition`, `extinction`,
`retention_interval`, `feature`, `target`, `us`, `cs`, `taste_cs`,
`visceral_us`, `delay_to_us`, `inhibitor`, `excitor`,
`reinstatement_us`, `reactivation`, `interference_window`,
`reinforcement_probability`, `us_onset_from_entry`, `fi_duration`,
`peak_probe_duration`, `peak_probe_probability`, `test_gradient`,
`training_trials`, `phase1_trials`, `phase2_trials`, `test_trials`,
`preexposure_trials`, `phase1_a`, `phase1_b`, `phase2_compound`,
`phase2_target`, `phase1_inhibitor`, `phase1_compound`,
`phase2_element`, `test_a`, `test_b`, `acquisition_context`,
`extinction_context`, `test_context`, `mode`) are **local** to
individual Tier B productions; they do not appear outside the parens of
their host productions and so do not conflict with Core's reserved set.

---

## 9. LL(k) / LL(2) note

Every production above has a distinct first-token identifier. The only
ambiguity candidate, the `mode =` keyword, appears only after a
preceding `=` inside an already-selected production (`OccasionSetting`,
`SummationRetardationTest`), and the legal values of `mode` differ
between those two productions, so no cross-production ambiguity exists.
The respondent grammar thus remains LL(2)-compatible (Core
`foundations/ll2-proof.md`).

---

## 10. References

APA entries for each primitive's primary source appear in that
primitive's dedicated page under
[`tier-b-primitives/`](tier-b-primitives/). The grammar document itself
is a structural specification and is not independently cited.

