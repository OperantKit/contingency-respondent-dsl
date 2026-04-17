# パヴロフ型部分強化消去効果（PREE）

## DSL 綴り

`PavlovianPREE(acquisition=<RespondentExpr>, extinction=<RespondentExpr>,
              test=<RespondentExpr>,
              reinforcement_probability=<Probability>)`

## 操作的定義

獲得中の強化確率を操作する三相の手続き。**相 1（獲得）:** CS が
`reinforcement_probability` で与えられる割合の試行で US と対提示される。
残りの試行では CS 単独が提示される。**相 2（消去）:** すべての対提示が
除去される。**相 3（テスト）:** 消去中の CR の低下は、連続強化された
CS よりも部分強化された CS で *遅い* — 部分強化消去効果である。
Mackintosh (1974) は経験的パターンと競合する理論的説明をレビューする。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `acquisition` | `RespondentExpr` | 獲得相。意味論は周囲の Phase と `reinforcement_probability` によって決定される。 |
| `extinction` | `RespondentExpr` | 消去相。 |
| `test` | `RespondentExpr` | CS のテスト。 |
| `reinforcement_probability` | `Probability` | 獲得中に CS が US と対提示される確率。`0.0` は完全消去、`1.0` は連続強化。 |

## 例

```
PavlovianPREE(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    test        = Extinction(tone),
    reinforcement_probability = 0.5
)
```

**一次出典に関する注記。** 経験的効果は信頼性高く再現されるが、その
正統的パヴロフ一次出典は単一論文ではない。Mackintosh (1974) は正統的
教科書の扱いである。さらなる一次出典検証は
[`../auxiliary.md`](../auxiliary.md) でフラグ付きで明記される。

## 一次出典

- Mackintosh, N. J. (1974). *The psychology of animal learning*.
  Academic Press. *(教科書の扱い。一次経験的パヴロフ出典はさらなる
  検証を要する)*
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning.
  *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532 *(理論的説明)*

## 関連プリミティブ

Tier A `Contingency(p, q)` と関連する（部分強化は `Contingency(p, 0)` と
みなせる）。`Renewal`, `SpontaneousRecovery`, `ContextualExtinction` と
関連する。いずれも消去された CR の構造と回復可能性に関わる。

