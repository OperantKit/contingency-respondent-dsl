# 媒介条件づけ

## DSL 綴り

`MediatedConditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                    test=<RespondentExpr>,
                    phase1_trials?=<Number>, phase2_trials?=<Number>)`

## 操作的定義

媒介する刺激表象を通じて連合を確立する二相の手続き。**相 1:** CS A が
動機づけ的に重要な刺激 S（しばしば風味や US）と対提示される。
**相 2:** CS A が新しい結果 O と共に提示されるが、S は物理的に存在
しない。**テスト:** S（または S に連合する刺激）に対する応答が、S が
直接 O と対提示されたかのように変化する。Wagner (1981) の SOP 枠組みの
下では、A は相 2 の間に S の A2 モード表象を検索し、この表象が A–O
連合を支持する。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1` | `RespondentExpr` | A–S 対提示。 |
| `phase2` | `RespondentExpr` | A が新しい結果 O と共に提示される。S は物理的に不在。 |
| `test` | `RespondentExpr` | S（または S 連合刺激）のテスト。 |
| `phase1_trials` | `Number`（任意） | A–S 対提示の数。 |
| `phase2_trials` | `Number`（任意） | A–O 試行の数。 |

## 例

```
MediatedConditioning(
    phase1 = Pair.ForwardDelay(tone, flavor, isi=5-s, cs_duration=10-s),
    phase2 = Pair.ForwardDelay(tone, lithium, isi=5-s, cs_duration=10-s),
    test   = CSOnly(flavor, trials=8),
    phase1_trials = 40,
    phase2_trials = 8
)
```

## 一次出典

- Holland, P. C. (1981). Acquisition of representation-mediated
  conditioned food aversions. *Learning and Motivation*, 12(1),
  1–18. https://doi.org/10.1016/0023-9690(81)90022-9

## 関連プリミティブ

`HigherOrderConditioning` および `SensoryPreconditioning` と密接に
関連する — 三者はいずれも中間表象を介した連鎖学習を含む。媒介条件
づけは、媒介する *CS* ではなく媒介する *表象* が相 2 の連合を担う点で
特徴的である — Wagner (1981) の SOP 的説明が典型的に援用される。

