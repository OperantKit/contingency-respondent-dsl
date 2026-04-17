# 条件性抑制（特徴陰性）

## DSL 綴り

`ConditionedInhibition(training=<RespondentExpr>, test=<RespondentExpr>,
                      training_trials?=<Number>)`

## 操作的定義

二種類の複合試行をもつ二要素訓練。**訓練:** 二種類の試行が混在する
— (a) CS A を US と対提示 (A+) (b) 複合 AI を *US なし* で提示 (AI−)。
訓練後、A は CR を誘発するが、AI− 試行の I の存在はその CR を抑制する。
**テスト:** 条件性抑制テスト（加算性または遅延学習。`SummationRetardationTest`
を参照）が、I が負の連合強度を獲得したことを確認する。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `training` | `RespondentExpr` | A+ と AI− を混在させた訓練。完全なプログラムでは `Serial` や `Phase` 式が典型的だが、周囲の Phase 構造が解釈できるものであれば任意の `RespondentExpr` を受ける。 |
| `test` | `RespondentExpr` | 加算性または遅延学習テスト。加算性の場合は典型的に `Extinction(Compound([excitor, i]))` など。 |
| `training_trials` | `Number`（任意） | 訓練試行の総数（両試行種類を合算）。 |

## 例

```
ConditionedInhibition(
    training = Serial(
        [Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
         Pair.ForwardDelay(Compound([a, i]), nothing,
                            isi=10-s, cs_duration=15-s)],
        isi=30-s
    ),
    test = Extinction(i),
    training_trials = 80
)
```

注意: 完全な条件性抑制パラダイムは通常、周囲の Phase 構造が A+ 試行と
AI− 試行をランダム順序で配送することを要求する。上記の `Serial` 形式は
概略である。実運用プログラムは通常、試行の混在を Phase レベルで表現する。

## 一次出典

- Rescorla, R. A. (1969). Pavlovian conditioned inhibition.
  *Psychological Bulletin*, 72(2), 77–94. https://doi.org/10.1037/h0027760

## 関連プリミティブ

`SuperConditioning` の前提条件。`SummationRetardationTest` によって
検証される。`OccasionSetting` と関連する。特徴陰性の機会設定子は
標的が強化されないことを信号し、抑制のような行動を生むが、条件性抑制
とは形式的に異なる (Holland, 1983)。

