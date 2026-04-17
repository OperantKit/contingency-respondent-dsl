# 過剰期待

## DSL 綴り

`Overexpectation(phase1_a=<RespondentExpr>, phase1_b=<RespondentExpr>,
                phase2_compound=<RespondentExpr>, test=<RespondentExpr>,
                phase1_trials?=<Number>, phase2_trials?=<Number>)`

## 操作的定義

三相の手続き。**相 1:** 2 つの CS (A, B) が個別に*同じ* US と漸近値
まで対提示される。**相 2:** 複合 AB が同じ US と対提示される。A と B が
それぞれ個別に US を予測するため、複合は漸近値 λ を超えて開始する。
**テスト:** A（または B、または両方）がテストされる。その CR は相 1
終了時より小さい —「過剰期待」が V を下方に駆動したのである。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1_a` | `RespondentExpr` | A–US 対提示を漸近値まで。 |
| `phase1_b` | `RespondentExpr` | B–US 対提示を漸近値まで。 |
| `phase2_compound` | `RespondentExpr` | AB 複合を同じ US と対提示。 |
| `test` | `RespondentExpr` | A または B 単独のテスト。 |
| `phase1_trials` | `Number`（任意） | 要素ごとの相 1 試行の数。 |
| `phase2_trials` | `Number`（任意） | 相 2 複合試行の数。 |

## 例

```
Overexpectation(
    phase1_a = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
    phase1_b = Pair.ForwardDelay(b, shock, isi=10-s, cs_duration=15-s),
    phase2_compound = Pair.ForwardDelay(Compound([a, b]), shock,
                                          isi=10-s, cs_duration=15-s),
    test = Extinction(a),
    phase1_trials = 40,
    phase2_trials = 10
)
```

## 一次出典

- Rescorla, R. A. (1970). Reduction in the effectiveness of
  reinforcement after prior excitatory conditioning. *Learning and
  Motivation*, 1(4), 372–381.
  https://doi.org/10.1016/0023-9690(70)90101-3

## 関連プリミティブ

`Blocking` および `Overshadowing` と密接に関連する。三者はいずれも
Rescorla & Wagner (1972) の共有漸近値制約から生じる手がかり競合
現象である。過剰期待は阻止の「鏡像」である。阻止は X が λ に達する
ことを妨げる。過剰期待は、A と B の複合予測が λ を超えるとき、両者を
それぞれの個別漸近値より下に駆動する。

