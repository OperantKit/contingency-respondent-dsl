# 覆い隠し（オーバーシャドウイング）

## DSL 綴り

`Overshadowing(training=<RespondentExpr>, test_a=<RespondentExpr>,
              test_b=<RespondentExpr>,
              training_trials?=<Number>)`

## 操作的定義

単一相の訓練と、それに続く 2 つの要素テスト。際立ちの異なる 2 つの
CS (A, B) が複合として US と対提示される。テストでは各要素が単独で
提示される。際立ちが高いほうの要素は強い CR を誘発する。低いほうの
要素は、単独で訓練されていれば達成したはずの CR より弱い CR を誘発する。
際立ちの低い要素は、高い要素によって「覆い隠される」。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `training` | `RespondentExpr` | 複合 AB と US の対提示。例: `Pair.ForwardDelay(Compound([a, b]), us, ...)`。 |
| `test_a` | `RespondentExpr` | A 単独のテスト。典型的には `Extinction(a)` または `CSOnly(a, ...)`。 |
| `test_b` | `RespondentExpr` | B 単独のテスト。 |
| `training_trials` | `Number`（任意） | 複合訓練試行の数。 |

## 例

```
Overshadowing(
    training = Pair.ForwardDelay(Compound([loud_tone, dim_light]), shock,
                                  isi=10-s, cs_duration=15-s),
    test_a = Extinction(loud_tone),
    test_b = Extinction(dim_light),
    training_trials = 40
)
```

## 一次出典

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Mackintosh, N. J. (1976). Overshadowing and stimulus intensity.
  *Animal Learning & Behavior*, 4(2), 186–192.
  https://doi.org/10.3758/BF03214033

## 関連プリミティブ

`Blocking` と密接に関連する。両者とも Rescorla & Wagner (1972) の
共有漸近値規則によって予測される手がかり競合現象である。覆い隠しは
単一の訓練相における際立ちの非対称性のもとで典型的に報告される。
阻止は一方の要素の先行訓練を要求する (Kamin, 1969)。Mackintosh (1975)
の注意的説明を通じて `OccasionSetting` と関連する。

