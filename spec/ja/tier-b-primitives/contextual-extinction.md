# 文脈性消去

## DSL 綴り

`ContextualExtinction(acquisition=<RespondentExpr>,
                     extinction=<RespondentExpr>,
                     test=<RespondentExpr>,
                     context=<ContextRef>)`

## 操作的定義

消去文脈を明示する消去手続き。消去学習がその文脈に拘束されていることを
実証するために使用される。明示的な `context` パラメータを要求する点、
およびテスト時に文脈拘束の主張を実証的に検定可能にする点（典型的には
後に `Renewal` と比較する）で、Tier A `Extinction` と異なる。Bouton
(2004) は正統的な理論的枠組みである。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US 対提示。 |
| `extinction` | `RespondentExpr` | `context` における CS 単独提示。 |
| `test` | `RespondentExpr` | CS のテスト。 |
| `context` | `ContextRef` | 消去文脈。 |

## 例

```
ContextualExtinction(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    test        = Extinction(tone),
    context     = "ctx_b"
)
```

## 一次出典

- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804

## 関連プリミティブ

`Renewal` と密接に関連する（同じ文脈枠組み。更新は文脈性消去が要求
しないテスト文脈のシフトを追加する）。検索理論クラスタの一員として
`LatentExtinction` および `SpontaneousRecovery` と関連する。

