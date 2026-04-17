# スーパー条件づけ

## DSL 綴り

`SuperConditioning(phase1_inhibitor=<RespondentExpr>,
                   phase2_target=<RespondentExpr>,
                   test=<RespondentExpr>)`

## 操作的定義

二相の手続き。**相 1:** CS I が条件性抑制子として訓練される（例:
`ConditionedInhibition` を介して）。**相 2:** 複合 IX（I が新奇 CS X と
同時提示）が US と対提示される。**テスト:** X は、事前抑制子なしで
訓練された統制の X よりも*大きな* CR を誘発する。複合が 0 未満で開始
するため（I は負の連合強度をもつ）、US における予測誤差が新奇複合
よりも大きくなり、X に追加の漸近強度を与える。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1_inhibitor` | `RespondentExpr` | I の条件性抑制訓練。典型的には入れ子の `ConditionedInhibition(...)`。 |
| `phase2_target` | `RespondentExpr` | IX 複合を US と対提示。典型的には `Pair.ForwardDelay(Compound([i, x]), us, ...)`。 |
| `test` | `RespondentExpr` | X 単独のテスト。 |

## 例

```
SuperConditioning(
    phase1_inhibitor = ConditionedInhibition(
        training = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
        test     = Extinction(i),
        training_trials = 40
    ),
    phase2_target = Pair.ForwardDelay(Compound([i, x]), shock,
                                        isi=10-s, cs_duration=15-s),
    test = Extinction(x)
)
```

## 一次出典

- Rescorla, R. A. (1971). Variation in the effectiveness of
  reinforcement and nonreinforcement following prior inhibitory
  conditioning. *Learning and Motivation*, 2(2), 113–123.
  https://doi.org/10.1016/0023-9690(71)90002-6

## 関連プリミティブ

`Blocking` の鏡像である。阻止は複合が λ で開始するため X への学習が
*少なく*なる。スーパー条件づけは複合が 0 未満で開始するため X への
学習が*多く*なる。相 1 抑制子のために `ConditionedInhibition` に
依存する。三者はいずれも Rescorla & Wagner (1972) の共有漸近値規則
から導かれる。

