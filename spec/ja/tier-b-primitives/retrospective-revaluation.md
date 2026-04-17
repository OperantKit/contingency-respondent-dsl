# 遡及的再評価／逆行性阻止

## DSL 綴り

`RetrospectiveRevaluation(phase1_compound=<RespondentExpr>,
                         phase2_element=<RespondentExpr>,
                         test=<RespondentExpr>)`

## 操作的定義

前向き阻止とは順序が逆の二相の手続き。**相 1:** 複合 AX が US と対提示
される。**相 2:** A 単独が訓練される（US とさらに対提示されるか、または
消去される）。**テスト:** X が単独で提示される。相 2 が A をさらに訓練
する場合、X の CR は相 2 のない統制と比較して*減少*する — 「逆行性阻止」。
相 2 が A を*消去*する場合、X の CR は*増強*される — 「覆い隠しからの
回復」。いずれのパターンも、X の連合強度が遡及的に改訂されることを
示す。この予測は Rescorla & Wagner (1972) では行われないが、Van Hamme
& Wasserman (1994) は不在手がかりに負の α を取らせることで取得する。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1_compound` | `RespondentExpr` | AX 複合を US と対提示。 |
| `phase2_element` | `RespondentExpr` | A 単独の訓練または消去。 |
| `test` | `RespondentExpr` | X 単独のテスト。 |

## 例

```
# 逆行性阻止: 相 2 で A をさらに訓練
RetrospectiveRevaluation(
    phase1_compound = Pair.ForwardDelay(Compound([a, x]), shock,
                                          isi=10-s, cs_duration=15-s),
    phase2_element  = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
    test            = Extinction(x)
)

# 覆い隠しからの回復: 相 2 で A を消去
RetrospectiveRevaluation(
    phase1_compound = Pair.ForwardDelay(Compound([a, x]), shock,
                                          isi=10-s, cs_duration=15-s),
    phase2_element  = Extinction(a),
    test            = Extinction(x)
)
```

## 一次出典

- Shanks, D. R. (1985). Forward and backward blocking in human
  contingency judgement. *Quarterly Journal of Experimental Psychology
  Section B*, 37(1b), 1–21. https://doi.org/10.1080/14640748508402082
- Van Hamme, L. J., & Wasserman, E. A. (1994). Cue competition in
  causality judgments: The role of nonpresentation of compound
  stimulus elements. *Learning and Motivation*, 25(2), 127–151.
  https://doi.org/10.1006/lmot.1994.1008

## 関連プリミティブ

`Blocking` を反転したもの。X が学習を明らかにするテスト構造は
`Overshadowing` と共有する。Mackintosh (1975) および Pearce–Hall
(1980) の連合可能性理論は、同じ実証パターンに対して代替的（注意
ベース）な説明を提供する。

