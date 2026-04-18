# 理論フレームワーク — ポインタレベル

> `contingency-respondent-dsl` パッケージの一部。これは短いフレーム
> ワークスケッチであり、**導出ではない**。26 個の Tier B プリミティブの
> 命名とパラメータの選択を主要なパヴロフ型学習理論に接続し、完全な
> 取り扱いについては主要教科書へのポインタを提供することを目的とする。

---

## 1. なぜ理論セクションが必要か

[`tier-b-primitives/`](tier-b-primitives/) の 26 個のプリミティブページは
それぞれ自身の一次出典を引用する。しかし、そのうちのいくつか — 阻止、
覆い隠し、過剰期待、スーパー条件づけ、遡及的再評価 — はパヴロフ型
連合可能性の量的モデルに照らしてはじめて理解可能となる。本ページは
Core と本パッケージが読者に前提とするモデルを名付け、どのプリミティブの
どのパラメータの選択がどのモデルに基づくかを述べる。
**方程式の導出は行わない。**

---

## 2. Rescorla–Wagner（誤差修正型連合可能性）

Rescorla & Wagner (1972) は連合強度を誤差修正型デルタ則としてモデル化する。

- 各 US は対提示された CS の固定漸近値 λ を支える。
- 学習率は CS の際立ち (αᵢ) と US 固有の速度 (β) に比例する。
- 予測誤差は、その試行に提示された各 CS にわたる総和 `λ − ΣVⱼ`。

RW は以下を直接予測する。

- **阻止** (Kamin, 1969) — 十分に訓練された CS A が複合 AX の誤差を
  ゼロにするため、X は強度を獲得しない。
- **覆い隠し** (Mackintosh, 1976; Pavlov, 1927) — 二つの CS が単一の
  漸近値 λ を共有するため、各 CS は単独訓練時より小さな強度を獲得する。
- **過剰期待** (Rescorla, 1970) — 独立した A+ と B+ 訓練の後、複合
  AB+ は漸近値を上回って開始し、V を小さくする方向へ駆動する。
- **スーパー条件づけ** (Rescorla, 1971) — 条件性抑制子が新奇 CS との
  複合になると、負の予測が生じ、新 CS が λ を超える。

RW に基づくパラメータをもつ Tier B 産出:
`BlockingExpr`, `OvershadowingExpr`, `OverexpectationExpr`,
`SuperConditioningExpr`, `ConditionedInhibitionExpr`,
`SummationRetardationTestExpr`。

---

## 3. Mackintosh (1975) — 注意変動

Mackintosh (1975) は、αᵢ（CS 際立ち）が CS の US 予測度に応じて増大する
ことを許容して RW を修正する。相対的に優れた予測子は注意を獲得し、
劣った予測子は失う。

Mackintosh は以下を説明する。

- **連続する相を通じた際立ちの差** — 冗長 CS がなぜ単にそれ以上
  強度を得ないのではなく、連合可能性を失うのか。
- RW 単独では苦労する、阻止における個別手がかり効果。

Mackintosh の α 動力学が問題になる Tier B 産出:
`LatentInhibitionExpr`, `OvershadowingExpr`,
`RetrospectiveRevaluationExpr`。

---

## 4. Pearce–Hall (1980) — 驚きに駆動される連合可能性

Pearce & Hall (1980) は、連合可能性が予測精度ではなく *予測誤差* とともに
増大すると主張する。試行 `n` で驚きをもたらした CS は試行 `n+1` で
高い α をもつ。よく予測された CS は低い α をもつ。

Pearce–Hall は以下の主要な説明である。

- **潜在抑制** (Lubow & Moore, 1959) — US を伴わない反復事前曝露により
  α がほぼゼロに駆動される。
- **消去と部分強化における α の継続的変化**。

PH に影響された Tier B 産出:
`LatentInhibitionExpr`, `PavlovianPREEExpr`。

---

## 5. SOP / AESOP (Wagner, 1981; Brandon & Wagner, 1991)

Wagner の SOP は刺激を、不活性 (I)、活性一次 (A1)、活性二次 (A2) の
メモリノードをサイクルする素子として表現する。A2-A2 共活性化が学習の
基質である。A1-A2 は興奮を生み、A2-A1 は抑制を生む。

SOP は以下のもっとも明快な説明である。

- **媒介条件づけ** (Holland, 1981) — CS が A2 における US 表象を検索し、
  この表象が新しい結果と連合する。
- **二次条件づけと感覚性前条件づけ** — A2 表象を経由した連鎖学習。

SOP に基づく Tier B 産出: `HigherOrderConditioningExpr`,
`SensoryPreconditioningExpr`, `MediatedConditioningExpr`。

---

## 6. Bouton (1993, 2004) — 検索と文脈

Bouton (1993, 2004) は、消去は **新しい学習** であり、消去解除ではないと
主張する。元の興奮性記憶は消去文脈と異なる文脈で利用可能かつ検索可能
のまま残る。

Bouton の検索理論は以下の主要な説明である。

- **更新** (Bouton & Bolles, 1979) — ABA / ABC / AAB デザイン; テスト時の
  文脈変化が興奮性記憶を回復する。
- **再発** (Rescorla & Heth, 1975) — US 単独提示が消去遮断された検索文脈を
  回復することで応答が回復する。
- **自発的回復** (Rescorla, 2004) — 時間経過が文脈変化の役割を果たす。
- **文脈性消去** — 消去学習は文脈特異的。

Bouton に基づく Tier B 産出: `RenewalExpr`,
`ReinstatementExpr`, `SpontaneousRecoveryExpr`,
`ContextualExtinctionExpr`。

---

## 7. タイミングモデル (Gibbon & Balsam, 1981; Gallistel & Gibbon, 2000)

スカラ期待理論とその後継である率推定モデルは、試行持続時間と ITI を
構造変数（I/T 比）として扱う。これらのモデルはピーク手続き (Roberts,
1981) および他のいくつかの手続きのタイミング依存パラメータの主要な
説明である。

タイミング理論に基づく Tier B 産出: `PeakProcedureExpr`;
`InhibitionOfDelayExpr` のパラメータ。

---

## 8. 本パッケージが立場を取らないこと

- RW, Mackintosh, Pearce–Hall, SOP, 検索理論間の選択。各 Tier B
  プリミティブは **手続き** であってモデルではない。どのモデルが
  結果を説明するかは研究者次第である。
- 神経基盤 (Fanselow 1990 の文脈性恐怖は海馬-扁桃体回路に依存するが、
  ここでの手続き仕様はその点でパラダイム中立)。
- レスポンデントデータのモル分析対分子分析。

特定モデルにコミットする*アノテーション*は Core
(`annotations/extensions/learning-models.md`) に存在し、ここには存在しない。

---

## 9. 参考文献 — ポインタ、導出ではない

- Bouton, M. E. (1993). Context, time, and memory retrieval in the
  interference paradigms of Pavlovian learning. *Psychological Bulletin*,
  114(1), 80–99. https://doi.org/10.1037/0033-2909.114.1.80
- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Bouton, M. E. (2016). *Learning and behavior: A contemporary synthesis*
  (2nd ed.). Sinauer.
- Brandon, S. E., & Wagner, A. R. (1991). Modulation of a discrete
  Pavlovian conditioned reflex by a putative emotive Pavlovian
  conditioned stimulus. *Journal of Experimental Psychology: Animal
  Behavior Processes*, 17(3), 299–311.
  https://doi.org/10.1037/0097-7403.17.3.299
- Gallistel, C. R., & Gibbon, J. (2000). Time, rate, and conditioning.
  *Psychological Review*, 107(2), 289–344.
  https://doi.org/10.1037/0033-295X.107.2.289
- Gibbon, J., & Balsam, P. (1981). Spreading association in time. In
  C. M. Locurto, H. S. Terrace, & J. Gibbon (Eds.), *Autoshaping and
  conditioning theory* (pp. 219–253). Academic Press.
- Mackintosh, N. J. (1974). *The psychology of animal learning*.
  Academic Press.
- Mackintosh, N. J. (1975). A theory of attention. *Psychological
  Review*, 82(4), 276–298. https://doi.org/10.1037/h0076778
- Pearce, J. M. (2013). *Animal learning and cognition* (3rd ed.).
  Psychology Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning.
  *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
- Wagner, A. R. (1981). SOP: A model of automatic memory processing in
  animal behavior. In N. E. Spear & R. R. Miller (Eds.), *Information
  processing in animals: Memory mechanisms* (pp. 5–47). Erlbaum.

