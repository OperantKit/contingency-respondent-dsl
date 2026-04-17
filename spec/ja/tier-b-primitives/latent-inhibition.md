# 潜在抑制（CS 事前曝露効果）

## DSL 綴り

`LatentInhibition(preexposure=<RespondentExpr>, training=<RespondentExpr>,
                 test=<RespondentExpr>,
                 preexposure_trials?=<Number>,
                 training_trials?=<Number>)`

## 操作的定義

三相の手続き。**相 1（事前曝露）:** 将来の CS が US なしで反復提示
される。**相 2（訓練）:** 事前曝露された CS が US と対提示される。
**テスト:** CS が提示される。獲得が非事前曝露統制より遅く（漸近 CR
が低く）なる。事前曝露された CS は *潜在抑制* を獲得したと言われる。
これは通常、注意または連合学習率機構に帰属される (Lubow & Moore, 1959;
Pearce & Hall, 1980)。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `preexposure` | `RespondentExpr` | CS 単独の事前曝露。典型的には `CSOnly(cs, trials=N)`。 |
| `training` | `RespondentExpr` | CS–US 対提示。 |
| `test` | `RespondentExpr` | 事前曝露された CS のテスト。 |
| `preexposure_trials` | `Number`（任意） | 事前曝露提示の数。 |
| `training_trials` | `Number`（任意） | 訓練試行の数。 |

## 例

```
LatentInhibition(
    preexposure = CSOnly(tone, trials=80),
    training    = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    test        = Extinction(tone),
    preexposure_trials = 80,
    training_trials    = 40
)
```

## 一次出典

- Lubow, R. E., & Moore, A. U. (1959). Latent inhibition: The effect
  of nonreinforced pre-exposure to the conditional stimulus. *Journal
  of Comparative and Physiological Psychology*, 52(4), 415–419.
  https://doi.org/10.1037/h0046700

## 関連プリミティブ

`USPreexposure` と密接に関連する — 両者とも事前曝露効果の準備であるが、
一方は CS を、もう一方は US を事前曝露する。Pearce & Hall (1980) は
正統的な理論的枠組みである。

