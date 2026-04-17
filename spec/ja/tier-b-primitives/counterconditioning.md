# 逆条件づけ

## DSL 綴り

`Counterconditioning(phase1=<RespondentExpr>, phase2=<RespondentExpr>,
                    phase1_trials?=<Number>, phase2_trials?=<Number>)`

## 操作的定義

二相の手続き。**相 1:** CS が一方の動機づけクラスの US（例: 嫌悪 US）と
対提示される。**相 2:** *同じ CS* が反対の動機づけクラスの US（例:
快楽 US）と対提示される。結果として生じる CR は相 1 の CR と異なる ——
単に弱くなるのではなく、符号が反転することが多い —— 行動的特徴は、
相 2 が相 1 の連合を消去するのではなく**置き換える**ことを示唆する。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `phase1` | `RespondentExpr` | 最初の CS–US1 対提示。 |
| `phase2` | `RespondentExpr` | 反対の価をもつ US による後続の CS–US2 対提示。 |
| `phase1_trials` | `Number`（任意） | 相 1 試行の数。 |
| `phase2_trials` | `Number`（任意） | 相 2 試行の数。 |

## 例

```
Counterconditioning(
    phase1 = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(tone, food,  isi=10-s, cs_duration=15-s),
    phase1_trials = 40,
    phase2_trials = 40
)
```

## 一次出典

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Dickinson, A., & Pearce, J. M. (1977). Inhibitory interactions
  between appetitive and aversive stimuli. *Psychological Bulletin*,
  84(4), 690–711. https://doi.org/10.1037/0033-2909.84.4.690

## 関連プリミティブ

逆条件づけは相 2 が CS を元の US と対提示しないという点で Tier A
`Extinction` と形式的に類似するが、反対価の US と対提示する点で異なる。
`ReconsolidationInterference` と関連する。後者は再活性化に続く新規学習の
配置を使用し、一部の研究者はこれを機構的に異なる逆条件づけの形式と
みなす。

