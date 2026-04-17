# 文脈性恐怖条件づけ (CFC)

## DSL 綴り

`ContextualFearConditioning(context=<ContextRef>, us=<StimulusRef>,
                           us_onset_from_entry=<Duration>,
                           training_trials?=<Number>)`

## 操作的定義

*文脈*自体が CS として機能する特殊な準備。動物が新奇な文脈に配置
される。遅延（`us_onset_from_entry`）の後、US が配送される。同一文脈
への後の再曝露（US なし）で CR が誘発される — 凍結（ネズミ目の場合）、
進行中の行動の抑制、または類似の測度。CFC は、海馬（文脈）と扁桃体
（個別 CS）の恐怖学習基質を解離するための標準準備となった (Fanselow,
1990)。ここでの仕様はその解離に関してパラダイム中立である。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `context` | `ContextRef` | CS として機能する訓練文脈。 |
| `us` | `StimulusRef` | 無条件刺激（典型的には足底ショック）。 |
| `us_onset_from_entry` | `Duration` | 文脈進入から US 開始までの時間。 |
| `training_trials` | `Number`（任意） | 条件づけセッションの数。しばしば 1。 |

## 例

```
ContextualFearConditioning(
    context = "ctx_shock",
    us = footshock,
    us_onset_from_entry = 180-s,
    training_trials = 1
)
```

## 一次出典

- Fanselow, M. S. (1990). Factors governing one-trial contextual
  conditioning. *Animal Learning & Behavior*, 18(3), 264–270.
  https://doi.org/10.3758/BF03205285

## 関連プリミティブ

`Renewal` および `ContextualExtinction` と関連する（文脈自体が第一級の
実験対象である）。一試行条件づけを信頼性高く支持する点で
`ConditionedTasteAversion` と関連する。

