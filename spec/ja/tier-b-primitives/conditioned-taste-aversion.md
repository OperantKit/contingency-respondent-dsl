# 条件性味覚嫌悪 (CTA)

## DSL 綴り

`ConditionedTasteAversion(taste_cs=<StimulusRef>, visceral_us=<StimulusRef>,
                         cs_duration=<Duration>, delay_to_us=<Duration>,
                         training_trials?=<Number>)`

## 操作的定義

特殊なパヴロフ型準備。味覚 CS（例: 新奇な風味）が摂取され、長い遅延を
経て内蔵 US（例: 塩化リチウム誘発性の倦怠感）が続く。テストでは、
動物は CS の摂取を回避または減少させる。CTA は以下の点で特徴的である:
(a) 一試行条件づけを容易に支持する、(b) 長い CS–US 遅延（数時間）を
許容する、(c) 味覚 CS と内蔵 US の間に強い選択的連合可能性を示す
(Garcia, Ervin, & Koelling, 1966)。準備は概念的には、非常に長い
トレース間隔をもつ `Pair.ForwardTrace` の特殊例であるが、その操作的
パラメータ（味覚モダリティ、長い遅延、内蔵 US）が手続き的に制約される
ため、別途名付けられる。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `taste_cs` | `StimulusRef` | 味覚 CS（典型的には風味付き溶液）。 |
| `visceral_us` | `StimulusRef` | 内蔵 US（例: LiCl、回転誘発性の倦怠感）。 |
| `cs_duration` | `Duration` | CS 摂取機会の持続時間。 |
| `delay_to_us` | `Duration` | CS 終了から US 開始までの時間。 |
| `training_trials` | `Number`（任意） | 訓練試行の数。しばしば 1。 |

## 例

```
ConditionedTasteAversion(
    taste_cs = saccharin_solution,
    visceral_us = licl_injection,
    cs_duration = 10-min,
    delay_to_us = 60-min,
    training_trials = 1
)
```

## 一次出典

- Garcia, J., Ervin, F. R., & Koelling, R. A. (1966). Learning with
  prolonged delay of reinforcement. *Psychonomic Science*, 5(3),
  121–122. https://doi.org/10.3758/BF03328311

## 関連プリミティブ

長いトレース間隔をもつ制約された `Pair.ForwardTrace`（Tier A）。
`LatentInhibition` と関連する（味覚 CS への事前曝露が CTA の潜在抑制を
生じる）。味覚モダリティにおける一般的な `StimulusGeneralization`
研究と関連する。

