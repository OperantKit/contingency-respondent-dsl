# 加算性／遅延学習テスト

## DSL 綴り

`SummationRetardationTest(inhibitor=<StimulusRef>, excitor=<StimulusRef>,
                         us=<StimulusRef>,
                         mode=("Summation" | "Retardation"))`

## 操作的定義

**テストプリミティブ** — 獲得手続きではない。事前に訓練された
`inhibitor` I を受け取り、I が負の連合強度を獲得したかを検定する。
**加算性テスト:** I と、別途訓練された `excitor` E との複合が検定される。
IE への CR が E 単独より小さければ I は抑制的である。**遅延学習
テスト:** I が US と対提示される。I への獲得が新奇統制 CS より遅ければ、
I の負の開始値が獲得を遅らせており、I は抑制的である。Rescorla (1969)
は、条件性抑制を確立するためには *両方* のテストが成功しなければ
ならないと主張した。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `inhibitor` | `StimulusRef` | 候補抑制子（通常は `ConditionedInhibition` または `OccasionSetting` 経由で訓練）。 |
| `excitor` | `StimulusRef` | 別途訓練された興奮性 CS（加算性）、または遅延学習訓練に使用する US。 |
| `us` | `StimulusRef` | US。 |
| `mode` | `"Summation"` \| `"Retardation"` | 二つの正統的テストのうちどちらを実施するか。 |

## 例

```
SummationRetardationTest(
    inhibitor = i,
    excitor   = e,
    us        = shock,
    mode      = Summation
)

SummationRetardationTest(
    inhibitor = i,
    excitor   = e,
    us        = shock,
    mode      = Retardation
)
```

## 一次出典

- Rescorla, R. A. (1969). Pavlovian conditioned inhibition.
  *Psychological Bulletin*, 72(2), 77–94. https://doi.org/10.1037/h0027760

## 関連プリミティブ

`ConditionedInhibition` および（部分的に）`OccasionSetting` の検証
プリミティブ。自身ではいかなる CS も訓練しない。`inhibitor` が
周囲のプログラムの先行準備によって訓練済みであることを前提とする。

