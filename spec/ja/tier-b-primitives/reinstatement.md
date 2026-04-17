# 再発

## DSL 綴り

`Reinstatement(acquisition=<RespondentExpr>, extinction=<RespondentExpr>,
              reinstatement_us=<RespondentExpr>,
              test=<RespondentExpr>)`

## 操作的定義

四相の手続き。**相 1（獲得）:** CS–US 対提示。**相 2（消去）:** CR が
消去されるまで CS を単独提示。**相 3（再発誘導）:** 消去文脈において
US 単独提示（CS なし）。**相 4（テスト）:** CS が提示される。CR が
部分的に回復する。再発は、消去された応答が回復可能であること、および
US 単独がそれを回復できることの古典的な実証であり、消去を消去解除では
なく検索 (Bouton, 2004) として解釈することと整合する。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US 対提示。 |
| `extinction` | `RespondentExpr` | CS 単独提示。 |
| `reinstatement_us` | `RespondentExpr` | US 単独提示。典型的には `USOnly(us, trials=N)`。 |
| `test` | `RespondentExpr` | CS のテスト。 |

## 例

```
Reinstatement(
    acquisition      = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction       = Extinction(tone),
    reinstatement_us = USOnly(shock, trials=4),
    test             = Extinction(tone)
)
```

## 一次出典

- Rescorla, R. A., & Heth, C. D. (1975). Reinstatement of fear to an
  extinguished conditioned stimulus. *Journal of Experimental
  Psychology: Animal Behavior Processes*, 1(1), 88–96.
  https://doi.org/10.1037/0097-7403.1.1.88
- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804

## 関連プリミティブ

`Renewal`, `SpontaneousRecovery`, `ContextualExtinction` と密接に
関連する。Tier A `USOnly` と関連する（再発の機構は通常、消去とテストの
間の `USOnly(...)` 相として文法的に実装される）。

