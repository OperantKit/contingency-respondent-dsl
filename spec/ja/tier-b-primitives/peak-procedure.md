# ピーク手続き（時間弁別）

## DSL 綴り

`PeakProcedure(cs=<StimulusRef>, us=<StimulusRef>, fi_duration=<Duration>,
              peak_probe_duration=<Duration>,
              peak_probe_probability?=<Probability>,
              training_trials?=<Number>)`

## 操作的定義

時間弁別の準備。強化試行では、CS は CS 開始から固定潜時
(`fi_duration`) 後に US が生じることを信号する。混在する「ピーク
プローブ」試行では CS が延長された期間 (`peak_probe_duration`、
`fi_duration` より長い) 提示され、US は配送されない。プローブにわたる
応答分布は、訓練された `fi_duration` 近傍にピークを現し、動物の US
時刻推定を指標する (Roberts, 1981)。ピーク手続きは、スカラタイミング
測定のための正統的準備である (Gibbon & Balsam, 1981)。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `cs` | `StimulusRef` | 試行開始を示す CS。 |
| `us` | `StimulusRef` | 強化試行で `fi_duration` に配送される US。 |
| `fi_duration` | `Duration` | 強化試行における CS 開始から US 配送までの固定間隔。 |
| `peak_probe_duration` | `Duration` | プローブ試行での延長 CS 持続時間（通常 `fi_duration` の 2–3 倍）。 |
| `peak_probe_probability` | `Probability`（任意） | プローブ試行の比率。デフォルト未指定。 |
| `training_trials` | `Number`（任意） | 試行総数。 |

## 例

```
PeakProcedure(
    cs = tone,
    us = food,
    fi_duration = 30-s,
    peak_probe_duration = 90-s,
    peak_probe_probability = 0.25,
    training_trials = 400
)
```

## 一次出典

- Roberts, S. (1981). Isolation of an internal clock. *Journal of
  Experimental Psychology: Animal Behavior Processes*, 7(3), 242–268.
  https://doi.org/10.1037/0097-7403.7.3.242

## 関連プリミティブ

`InhibitionOfDelay` と関連する（両者とも時間弁別現象である）。基礎と
なる強化試行構造として Tier A `Pair.ForwardDelay` を使用する
（プローブ試行は構造的追加）。Tier B 集合内のタイミング理論に根拠を
もつパラメータと関連する（[`../theory.md`](../theory.md) §7 参照）。

