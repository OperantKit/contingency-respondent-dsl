# 刺激般化（パヴロフ型）

## DSL 綴り

`StimulusGeneralization(training=<RespondentExpr>,
                       test_gradient=[<StimulusRef>, <StimulusRef>, ...],
                       training_trials?=<Number>,
                       test_trials?=<Number>)`

## 操作的定義

二相の手続き。**訓練:** CS が US と漸近値まで対提示される。
**テスト:** 感覚次元に沿って parametric に変化する検定刺激の集合
（典型的には訓練された CS と複数の訓練外値を含む）が消去条件下で
提示される。検定刺激値に対する CR の大きさをプロットすると般化勾配が
得られる。これは古典的には訓練値でピークを示し、検定値が訓練値から
離れるにつれ低下する (Hovland, 1937)。勾配そのものがデータである。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `training` | `RespondentExpr` | CS–US 対提示。 |
| `test_gradient` | `StimulusRef` のリスト | 検定刺激。通常、訓練された CS および次元に沿った複数の隣接値を含む。 |
| `training_trials` | `Number`（任意） | 訓練試行の数。 |
| `test_trials` | `Number`（任意） | 各勾配点あたりの検定試行の数。 |

## 例

```
StimulusGeneralization(
    training = Pair.ForwardDelay(tone_1000hz, shock,
                                  isi=10-s, cs_duration=15-s),
    test_gradient = [tone_500hz, tone_750hz, tone_1000hz,
                     tone_1250hz, tone_1500hz],
    training_trials = 40,
    test_trials     = 8
)
```

## 一次出典

- Hovland, C. I. (1937). The generalization of conditioned responses:
  I. The sensory generalization of conditioned responses with varying
  frequencies of tone. *Journal of General Psychology*, 17(1),
  125–148. https://doi.org/10.1080/00221309.1937.9917977

## 関連プリミティブ

Tier A `Differential` と関連する（差別条件づけと般化テストを組み合わ
せると弁別後勾配が得られる）。`OccasionSetting` と関連する — 機会設定
テストは標的を感覚次元に沿って parametric に変化させることが多い。

