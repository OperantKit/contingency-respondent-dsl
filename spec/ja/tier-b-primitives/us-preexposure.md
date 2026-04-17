# US 事前曝露効果

## DSL 綴り

`USPreexposure(preexposure=<RespondentExpr>, training=<RespondentExpr>,
              test=<RespondentExpr>,
              preexposure_trials?=<Number>,
              training_trials?=<Number>)`

## 操作的定義

`LatentInhibition` と並行する三相の手続きだが、CS ではなく US を
事前曝露する。**相 1（事前曝露）:** US 単独が反復提示される。
**相 2（訓練）:** CS が同じ US と対提示される。**テスト:** CS が
提示される。獲得が非事前曝露統制より遅く、漸近 CR が低い。連合的
（US 表象）および非連合的（馴化、動機づけ）な説明が提案されている
(Randich & LoLordo, 1979)。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `preexposure` | `RespondentExpr` | US 単独の事前曝露。典型的には `USOnly(us, trials=N)`。 |
| `training` | `RespondentExpr` | CS–US 対提示。 |
| `test` | `RespondentExpr` | CS のテスト。 |
| `preexposure_trials` | `Number`（任意） | US 事前曝露の数。 |
| `training_trials` | `Number`（任意） | CS–US 訓練試行の数。 |

## 例

```
USPreexposure(
    preexposure = USOnly(shock, trials=40),
    training    = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    test        = Extinction(tone),
    preexposure_trials = 40,
    training_trials    = 40
)
```

## 一次出典

- Randich, A., & LoLordo, V. M. (1979). Associative and nonassociative
  theories of the UCS preexposure phenomenon. *Psychological Bulletin*,
  86(3), 523–548. https://doi.org/10.1037/0033-2909.86.3.523

## 関連プリミティブ

`LatentInhibition` と密接に関連する — 構造的に対称な双対統制の
事前曝露準備である。両者は通常、事前曝露効果の CS-側対 US-側の説明を
解離するために併用される。

