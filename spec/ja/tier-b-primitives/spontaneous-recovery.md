# 自発的回復

## DSL 綴り

`SpontaneousRecovery(acquisition=<RespondentExpr>,
                    extinction=<RespondentExpr>,
                    retention_interval=<Duration>,
                    test=<RespondentExpr>)`

## 操作的定義

三相の手続きに保持間隔が加わる。**相 1（獲得）:** CS–US 対提示。
**相 2（消去）:** CR が消去されるまで CS 単独提示。**相 3（保持）:**
一定時間（`retention_interval`）訓練なし。**相 4（テスト）:** CS が
提示される。CR は保持間隔に比例して再び現れる。Bouton (2004) は自発的
回復を時間-を-文脈とする効果として扱う。時間の経過が消去文脈から
文脈をずらし、相 1 の連合の検索を回復する。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US 対提示。 |
| `extinction` | `RespondentExpr` | CS 単独提示。 |
| `retention_interval` | `Duration` | 消去終了からテストまでの時間（例: `24-h` は Core 互換の Duration 表現として）。 |
| `test` | `RespondentExpr` | CS のテスト。 |

## 例

```
SpontaneousRecovery(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    extinction  = Extinction(tone),
    retention_interval = 1440-min,
    test        = Extinction(tone)
)
```

## 一次出典

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Rescorla, R. A. (2004). Spontaneous recovery. *Learning & Memory*,
  11(5), 501–509. https://doi.org/10.1101/lm.77504

## 関連プリミティブ

`Renewal` と密接に関連する（両者とも文脈シフトで消去された応答を
回復する。自発的回復では「文脈」は時間である）。`Reinstatement` にも
関連する（時間単独ではなく US 単独）。

