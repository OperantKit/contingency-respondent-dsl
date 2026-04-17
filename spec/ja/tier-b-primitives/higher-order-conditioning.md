# 高次条件づけ（二次条件づけ）

## DSL 綴り

`HigherOrderConditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                        phase1_trials?=<Number>, phase2_trials?=<Number>)`

## 操作的定義

二相の手続き。**相 1:** 一次 CS (CS1) が US と対提示され、CS1 が条件
刺激として確立される。**相 2:** 二つ目の CS (CS2) が CS1 と対提示される。
*US は与えられない*。テストで CS2 単独が CR を誘発するが、その大きさは
特徴的に CS1 のものより小さい。CS2 に対する CR は「二次」と呼ばれる。
CS1 の先行する一次条件づけに依存するためである。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1` | `RespondentExpr` | 一次条件づけ（典型的には `Pair.ForwardDelay(cs1, us, ...)`）。 |
| `phase2` | `RespondentExpr` | 二次対提示。例: `Pair.ForwardDelay(cs2, cs1, ...)`。US なし。 |
| `phase1_trials` | `Number`（任意） | 一次試行の数。 |
| `phase2_trials` | `Number`（任意） | 二次試行の数。 |

## 例

```
HigherOrderConditioning(
    phase1 = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(light, tone, isi=5-s, cs_duration=10-s),
    phase1_trials = 40,
    phase2_trials = 20
)
```

## 一次出典

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Rizley, R. C., & Rescorla, R. A. (1972). Associations in second-order
  conditioning and sensory preconditioning. *Journal of Comparative and
  Physiological Psychology*, 81(1), 1–11. https://doi.org/10.1037/h0033333

## 関連プリミティブ

`SensoryPreconditioning` と密接に関連する。両者とも共有される要素を
通じて 2 つの CS を連鎖させるが、US 相の順序が異なる（二次条件づけは
CS1 を先に US と条件づける。感覚性前条件づけは US 曝露の前に CS1 と
CS2 を対提示する）。SOP 流の A2 媒介を通じて `MediatedConditioning` と
関連する (Wagner, 1981)。

