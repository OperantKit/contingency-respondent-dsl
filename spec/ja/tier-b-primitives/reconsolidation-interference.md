# 再固定化妨害

## DSL 綴り

`ReconsolidationInterference(acquisition=<RespondentExpr>,
                            reactivation=<RespondentExpr>,
                            interference_window=<Duration>,
                            extinction=<RespondentExpr>,
                            test=<RespondentExpr>)`

## 操作的定義

四相の手続き。**相 1（獲得）:** CS–US 対提示。**相 2（再活性化）:**
短い CS 単独提示。CS–US 記憶トレースを可塑的「再固定化」状態に戻すと
される。**妨害ウィンドウ:** 時間窓内（慣例的には再活性化後 10 分 – 6
時間）に記憶は妨害を受けやすい。**相 3（ウィンドウ内消去）:** ウィンドウ
内で CS 単独提示を行う。**相 4（テスト）:** CR が低減し、後の更新、
再発、自発的回復に抵抗する — 消去単独が生じさせるパターンより特徴的に
強い (Monfils et al., 2009)。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `acquisition` | `RespondentExpr` | CS–US 対提示。 |
| `reactivation` | `RespondentExpr` | 単一の CS 単独提示。典型的には `CSOnly(cs, trials=1)`。 |
| `interference_window` | `Duration` | 再活性化後に記憶が可塑的である時間窓。 |
| `extinction` | `RespondentExpr` | ウィンドウ内で配送される消去。 |
| `test` | `RespondentExpr` | CS のテスト。 |

## 例

```
ReconsolidationInterference(
    acquisition = Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s),
    reactivation = CSOnly(tone, trials=1),
    interference_window = 60-min,
    extinction = Extinction(tone),
    test = Extinction(tone)
)
```

## 一次出典

- Monfils, M.-H., Cowansage, K. K., Klann, E., & LeDoux, J. E. (2009).
  Extinction-reconsolidation boundaries: Key to persistent attenuation
  of fear memories. *Science*, 324(5929), 951–955.
  https://doi.org/10.1126/science.1167975

## 関連プリミティブ

消去調節クラスタの一員として `Counterconditioning`, `LatentExtinction`,
`ContextualExtinction` と関連する。本プリミティブを構造的に際立たせる
鍵となる特徴は `interference_window` タイミングパラメータである。

