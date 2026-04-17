# 阻止（ブロッキング）

## DSL 綴り

`Blocking(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
         test=<RespondentExpr>,
         phase1_trials?=<Number>, phase2_trials?=<Number>,
         test_trials?=<Number>)`

## 操作的定義

三相の手続き。**相 1:** CS A が US と漸近値まで対提示される。
**相 2:** 複合 AX（A が新奇 CS X と同時提示）が同じ US と対提示される。
**テスト:** X が単独で提示される。その CR は、相 1 の A 予備訓練を
受けていない統制の X と比較して顕著に小さい。A の予備訓練が X への
獲得を「阻止する」。A が US を完全に予測するため、X が解決すべき
予測誤差が残らないからである (Rescorla & Wagner, 1972)。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1` | `RespondentExpr` | A–US 対提示を漸近値まで。典型的には `Pair.ForwardDelay(a, us, ...)`。 |
| `phase2` | `RespondentExpr` | AX 複合を US と対提示。典型的には `Pair.ForwardDelay(Compound([a, x]), us, ...)`。 |
| `test` | `RespondentExpr` | X 単独のテスト。典型的には `Extinction(x)` または `CSOnly(x, ...)`。 |
| `phase1_trials` | `Number`（任意） | 相 1 A–US 試行の数。 |
| `phase2_trials` | `Number`（任意） | 相 2 AX–US 試行の数。 |
| `test_trials` | `Number`（任意） | X テスト試行の数。 |

## 例

```
Blocking(
    phase1 = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(Compound([a, x]), shock,
                                isi=10-s, cs_duration=15-s),
    test   = Extinction(x),
    phase1_trials = 40,
    phase2_trials = 20,
    test_trials   = 10
)
```

## 一次出典

- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment
  and aversive behavior* (pp. 279–296). Appleton-Century-Crofts.

## 関連プリミティブ

`Overshadowing` と密接に関連する。両者とも手がかり競合現象である。
阻止は A の*先行*訓練に依存する。覆い隠しは複合訓練中の際立ちの
非対称性のみを必要とする。Rescorla & Wagner (1972) の下では両者は
単一の共有漸近値制約を反映する。相 2 後に A が消去または過剰訓練
されたときに X の連合強度が変化することを示す `RetrospectiveRevaluation`
は阻止を拡張したものである。

