# 感覚性前条件づけ

## DSL 綴り

`SensoryPreconditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                       test=<RespondentExpr>,
                       phase1_trials?=<Number>, phase2_trials?=<Number>)`

## 操作的定義

三相の手続き。**相 1:** 二つの中性 CS (CS1, CS2) が US 非存在下で
互いに対提示される。**相 2:** CS1 が US と対提示される。**テスト:**
CS2 が単独で提示される。CS2 が US と直接対提示されたことはないにも
かかわらず CR が生じる場合、この CR は相 1 の CS1–CS2 連合に帰属される
（この連合が CS1 — 現在は条件刺激 — の検索を媒介する）。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1` | `RespondentExpr` | US 非存在下の CS–CS 対提示。例: `Pair.ForwardDelay(cs2, cs1, ...)`。 |
| `phase2` | `RespondentExpr` | CS1 の一次条件づけ。例: `Pair.ForwardDelay(cs1, us, ...)`。 |
| `test` | `RespondentExpr` | CS2 単独のテスト。典型的には `Extinction(cs2)` または `CSOnly(cs2, ...)`。 |
| `phase1_trials` | `Number`（任意） | CS–CS 対提示の数。 |
| `phase2_trials` | `Number`（任意） | CS1–US 対提示の数。 |

## 例

```
SensoryPreconditioning(
    phase1 = Pair.ForwardDelay(light, tone, isi=5-s, cs_duration=10-s),
    phase2 = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    test   = CSOnly(light, trials=8),
    phase1_trials = 16,
    phase2_trials = 40
)
```

## 一次出典

- Brogden, W. J. (1939). Sensory pre-conditioning. *Journal of
  Experimental Psychology*, 25(4), 323–332.
  https://doi.org/10.1037/h0058944
- Rizley, R. C., & Rescorla, R. A. (1972). Associations in second-order
  conditioning and sensory preconditioning. *Journal of Comparative and
  Physiological Psychology*, 81(1), 1–11. https://doi.org/10.1037/h0033333

## 関連プリミティブ

`HigherOrderConditioning` と密接に関連する。両者とも CS–CS 連合を
連鎖させるが、感覚性前条件づけは US 曝露*前*に CS を対提示するため、
Rescorla–Wagner の下で両手続きが解離される（基礎となる連合構造が
異なる。Rizley & Rescorla, 1972）。

