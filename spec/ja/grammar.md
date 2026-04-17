# 文法 — Tier B レスポンデントプリミティブ

> `contingency-respondent-dsl` パッケージの一部。本パッケージが Core の
> `ExtensionRespondentPrimitive` 拡張ポイントを通じて登録する 26 個の
> Tier B パヴロフ手続きの EBNF を規定する。

---

## 1. スコープと表記慣習

以下の産出は Core の `ExtensionRespondentPrimitive` (Core:
`spec/en/respondent/grammar.md §4`) を拡張する。いずれも Tier A 規則を
再定義せず、新たな LL(2) 判定点を導入せず、チューリング完全な構成を
追加しない。各 Tier B プリミティブは `IdentUpper "(" ArgList? ")"` 
として綴られ、最初のトークンで他のすべてのプリミティブと区別可能である。

共有される終端および字句規則 (`StimulusRef`, `Number`, `Duration`,
`Probability`, `ContextRef`, `RespondentExpr`) は Core から継承する
(`contingency-dsl` の `schema/foundations/grammar.ebnf` および
`schema/respondent/grammar.ebnf`)。以下で使用される正式な綴り:

- `StimulusRef` = 識別子、または二重引用符付き文字列
- `ContextRef` = 識別子、または二重引用符付き文字列（実験文脈を表す;
  Core `foundations/context.md`）
- `RespondentExpr` = 任意の Tier A または Tier B レスポンデント式
- `Number` = 10 進数または整数
- `Duration` = `Number "-" TimeUnit` (`TimeUnit` は `ms`, `s`, `min`
  のいずれか)
- `Probability` = `[0, 1]` の範囲にある `Number`

キーワード対位置引数の方針は Core の慣例に従う。引数順序が一意に
定まる場合は位置形式が定義される。プリミティブが 3 個以上の引数、
またはオプション引数をもつ場合はキーワード形式が推奨される。

---

## 2. 産出 — 獲得と高次条件づけ族

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

## 3. 産出 — 手がかり競合族

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

## 4. 産出 — 抑制性学習族

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

## 5. 産出 — 事前曝露族

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

## 6. 産出 — 消去と回復族

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

## 7. 産出 — 特殊な手続き

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

## 8. 予約キーワードの素集合性チェック

上記で導入された識別子は以下のとおり。

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

これらのいずれも Core の `contingency-dsl/spec/en/respondent/grammar.md §3`
に列挙された Tier A 予約セットと衝突しない。

ここで導入された新しいキーワード引数名 (`phase1`, `phase2`,
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
`extinction_context`, `test_context`, `mode`) は個別の Tier B 産出
内に**ローカル**である。ホスト産出の丸括弧の外には現れないため、
Core の予約セットとは衝突しない。

---

## 9. LL(k) / LL(2) に関する注記

上記のすべての産出は異なる先頭トークン識別子をもつ。唯一の曖昧性候補は
`mode =` キーワードだが、これは既に選ばれた産出 (`OccasionSetting`,
`SummationRetardationTest`) 内で先行する `=` の後にしか現れず、
`mode` の合法値は両産出で異なるため、クロス産出の曖昧性は存在しない。
したがってレスポンデント文法は LL(2) 互換のまま維持される（Core
`foundations/ll2-proof.md`）。

---

## 10. 参考文献

各プリミティブの一次出典の APA エントリは、プリミティブ固有のページ
[`tier-b-primitives/`](tier-b-primitives/) に記載される。文法ドキュメント
自身は構造仕様であり、独立した出典をもたない。

