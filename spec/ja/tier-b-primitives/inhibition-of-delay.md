# 遅延抑制

## DSL 綴り

`InhibitionOfDelay(cs=<StimulusRef>, us=<StimulusRef>,
                  cs_duration=<Duration>, isi=<Duration>,
                  training_trials?=<Number>)`

## 操作的定義

拡張された前向き遅延訓練（長い CS-から-US 間隔）では、CR は CS 開始時に
即時発現せず、CS 間隔の後半、US に近い部分でのみ現れる。CS 間隔の
前半部分は「抑制されている」と言われる — これは前向き遅延条件づけとは
別個の準備ではなく、創発的な時間的パターンである。よく訓練された前向き
遅延準備において一般的に報告される実証的特徴であるため、明示的に
名付けられる。

## パラメータ

| 名前 | 型 | 説明 |
|---|---|---|
| `cs` | `StimulusRef` | 条件刺激。 |
| `us` | `StimulusRef` | 無条件刺激。 |
| `cs_duration` | `Duration` | CS の総持続時間。 |
| `isi` | `Duration` | CS 開始から US 開始までの間隔 (ISI)。 |
| `training_trials` | `Number`（任意） | 訓練試行の数。 |

## 例

```
InhibitionOfDelay(
    cs = tone,
    us = shock,
    cs_duration = 60-s,
    isi         = 45-s,
    training_trials = 200
)
```

## 一次出典

- Pavlov, I. P. (1927). *Conditioned reflexes: An investigation of the
  physiological activity of the cerebral cortex* (G. V. Anrep, Trans.).
  Oxford University Press.
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper
  control procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109

## 関連プリミティブ

長い ISI をもつ `Pair.ForwardDelay`（Tier A）に構造的に依存する。
`PeakProcedure` と関連する（両者とも時間弁別現象である）。分析は
タイミング理論 (Gibbon & Balsam, 1981) を通じて行われるのが典型的。

