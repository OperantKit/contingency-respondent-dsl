# 潜在消去（パヴロフ型）

## DSL 綴り

`LatentExtinction(acquisition=<RespondentExpr>, preexposure=<RespondentExpr>,
                 test=<RespondentExpr>,
                 preexposure_trials?=<Number>)`

## 操作的定義

三相の手続き。**相 1（獲得）:** CS–US 対提示。**相 2（事前曝露／
文脈曝露）:** 動物が訓練文脈に、CS も US もない状態で長時間曝露される。
**相 3（テスト）:** CS が提示される。CR は相 2 のない統制に比べて
低減する。古典的文献 (Seward & Levy, 1949) はこの効果を道具的応答に
ついて報告している。パヴロフ型の類似は、Bouton (2004) の検索理論と
整合的な、検索の文脈特異的弱化として扱われる。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US 対提示。 |
| `preexposure` | `RespondentExpr` | CS も US もない文脈曝露。典型的には文脈のみの相として表現される。 |
| `test` | `RespondentExpr` | CS のテスト。 |
| `preexposure_trials` | `Number`（任意） | 事前曝露セッションの数または持続時間。 |

## 例

```
LatentExtinction(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    preexposure = CSOnly(context_a, trials=0),  -- 概略: Phase が文脈のみの曝露を表現
    test        = Extinction(tone),
    preexposure_trials = 30
)
```

**一次出典に関する注記。** 最も頻繁に引用される文献は道具的形式に
ついての Seward & Levy (1949) である。ここで参照される *パヴロフ型*
形式については、最も明確な理論的フレーミングは Bouton (2004) である。
専用のパヴロフ型一次出典は特定されておらず、Bouton (2004) を理論的
アンカーとして保守的に採用している。

## 一次出典

- Bouton, M. E. (2004). Context and behavioral processes in
  extinction. *Learning & Memory*, 11(5), 485–494.
  https://doi.org/10.1101/lm.78804
- Seward, J. P., & Levy, N. (1949). Latent extinction: Sign learning
  as a factor in extinction. *Journal of Experimental Psychology*,
  39(5), 660–668. https://doi.org/10.1037/h0057426 *(道具的原型。
  パヴロフ型形式は Bouton の検索的枠組みから外挿)*

## 関連プリミティブ

`ContextualExtinction`, `Renewal`, `SpontaneousRecovery` と密接に
関連する — いずれも検索理論クラスタの一員。

