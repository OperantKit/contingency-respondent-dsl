# 機会設定（オケージョンセッター）

## DSL 綴り

`OccasionSetting(feature=<StimulusRef>, target=<StimulusRef>,
                us=<StimulusRef>,
                mode=("FeaturePositive" | "FeatureNegative"),
                training_trials?=<Number>)`

## 操作的定義

機会設定子は、それ自身は興奮または抑制の強度を獲得することなく、
標的 CS の予測的地位を調節する刺激である。**特徴陽性**訓練では、
試行が Feature→Target→US と Target 単独（US なし）を交互に行う。
特徴が強化を制御する。**特徴陰性**訓練では、試行が Target→US と
Feature+Target（US なし）を交互に行う。特徴が強化の不在を制御する。
機会設定子は加算テストでの振る舞いにおいて条件性抑制子と異なる。
機会設定子は、別途訓練された興奮子を抑制するのに失敗する (Holland,
1983)。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `feature` | `StimulusRef` | 機会設定 CS (F)。 |
| `target` | `StimulusRef` | 強化が調節される標的 CS (T)。 |
| `us` | `StimulusRef` | 無条件刺激。 |
| `mode` | `"FeaturePositive"` \| `"FeatureNegative"` | 確立する制御関係。 |
| `training_trials` | `Number`（任意） | 訓練試行の総数。 |

## 例

```
OccasionSetting(
    feature = houselight,
    target  = tone,
    us      = shock,
    mode    = FeaturePositive,
    training_trials = 80
)
```

## 一次出典

- Holland, P. C. (1983). Occasion-setting in Pavlovian feature
  positive discriminations. In M. L. Commons, R. J. Herrnstein, & A. R.
  Wagner (Eds.), *Quantitative analyses of behavior: Discrimination
  processes* (Vol. 4, pp. 183–206). Ballinger.

## 関連プリミティブ

`ConditionedInhibition` と関連するが区別される（特徴陰性機会設定子は
加算テストにおいて条件性抑制子と異なる振る舞いをする）。Tier A の
`Differential` と関連する（差別条件づけは「特徴」が CS 同一性そのもの
である退化したケースとみなせる）。

