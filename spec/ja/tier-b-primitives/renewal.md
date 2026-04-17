# 更新（リニューアル、ABA / ABC / AAB）

## DSL 綴り

`Renewal(acquisition=<RespondentExpr>, extinction=<RespondentExpr>,
        test=<RespondentExpr>,
        acquisition_context=<ContextRef>,
        extinction_context=<ContextRef>,
        test_context=<ContextRef>)`

## 操作的定義

文脈操作を伴う三相手続き。CS が文脈 A で訓練され、異なる文脈（ABA /
ABC の場合 B）で消去され、三つ目の文脈でテストされる。テスト文脈が
消去文脈と異なるとき、CS への CR が回復する（「更新」）。ABA デザインは
獲得文脈で更新する。ABC は新奇文脈で更新する。AAB は獲得と消去を同一
文脈で行った後に文脈を変えることで更新する。Bouton (2004) は更新を、
消去が消去解除ではなく文脈特異的な新しい学習であることの証拠として
解釈する。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US 対提示。 |
| `extinction` | `RespondentExpr` | 獲得後の CS 単独提示。 |
| `test` | `RespondentExpr` | CS のテスト。 |
| `acquisition_context` | `ContextRef` | 相 1 の文脈。 |
| `extinction_context` | `ContextRef` | 相 2 の文脈。 |
| `test_context` | `ContextRef` | 相 3（テスト）の文脈。ABA, ABC, AAB を決定する。 |

## 例

```
# ABA 更新
Renewal(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    test        = Extinction(tone),
    acquisition_context = "ctx_a",
    extinction_context  = "ctx_b",
    test_context        = "ctx_a"
)
```

## 一次出典

- Bouton, M. E., & Bolles, R. C. (1979). Contextual control of the
  extinction of conditioned fear. *Learning and Motivation*, 10(4),
  445–466. https://doi.org/10.1016/0023-9690(79)90057-2
- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804

## 関連プリミティブ

`Reinstatement`, `SpontaneousRecovery`, `ContextualExtinction` と
密接に関連する — Bouton の検索理論下の消去と回復現象のすべてである。
`ContextRef` に依存する（Core `foundations/context.md`）。

