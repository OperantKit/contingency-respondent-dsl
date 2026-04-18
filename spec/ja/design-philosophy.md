# 設計思想 — contingency-respondent-dsl

> `contingency-respondent-dsl` パッケージの一部。本パッケージが Core に
> 何を、どのように追加するかを制約する設計原則を記録する。

---

## 1. 加算のみの規律

本パッケージは拡張ポイント `ExtensionRespondentPrimitive` を**経由する場合に限り**
Core レスポンデント文法に産出を追加できる。以下は禁止される。

- 任意の Tier A プリミティブの再定義 (`Pair.*`, `Extinction`,
  `CSOnly`, `USOnly`, `Contingency`, `TrulyRandom`,
  `ExplicitlyUnpaired`, `Compound`, `Serial`, `ITI`, `Differential`)。
- 新たな LL(2) 判定点の導入。各 Tier B プリミティブは
  `IdentUpper "(" ArgList? ")"` として綴られ、Core の
  `spec/en/respondent/grammar.md §3` に記録された予約キーワード検査を
  通じて、最初のトークンで Tier A から区別可能である。
- チューリング完全な構成の追加。各 Tier B プリミティブは有限の
  宣言的手続きであり、そのパラメータは構文解析時に確定するリテラル
  値でなければならない。
- `foundations/`, `operant/`, `composed/`, `experiment/`, `annotations/`
  いずれに対しても変更を要求すること。

提案されたプリミティブが上記のいずれかを必要とするならば、本パッケージの
スコープ外であり、Core への別提案としてルーティングされるべきである。

---

## 2. なぜ Tier B は独立パッケージなのか

EAB 中心の Core レスポンデント層は、主としてオペラント準備を走らせる
実験者 — 自身の手続きのレスポンデント要素を記述するために最小限の
二項語彙（対提示、消去、随伴性空間）を必要とする利用者 — を想定する。
本パッケージが提供する Tier B プリミティブは別の利用者を想定する:
古典的条件づけを主たる準備とし、手がかり競合、抑制性学習、事前曝露、
消去と回復の諸現象、および条件性味覚嫌悪、ピーク手続き、文脈性恐怖
条件づけなどの特殊な準備に対する名前を必要とする研究者である。

両者を分離することには以下の三つの具体的利点がある。

1. **認知的スコープ**。`contingency-dsl` を読む JEAB 実験者は、注意
   モデル、固定化、再固定化に言及する 26 個のパヴロフ専用
   プリミティブを迂回する必要がない。
2. **バージョン独立性** (精神において; どちらのパッケージも
   バージョン宣言は行わない — §5 参照)。Tier B はパヴロフ型学習文献の
   成長にあわせてプリミティブを獲得できる。EAB Core を動揺させない。
3. **レジストリ実証**。本パッケージはサードパーティが Core レスポン
   デント文法を拡張する最初の実例である。二つ目、三つ目の拡張
   パッケージ（例: 社会的学習の拡張、薬物自己投与の拡張）は同じ
   パターンを Core からの許可なしに使用できる。

---

## 3. プログラムスコープのレジストリ

拡張プリミティブは**プログラムスコープ**で解決され、グローバルでは
ない。Tier B を使用したい各プログラム（インタープリタ／ランタイム
インスタンス）は、プログラムヘッダで宣言する（概念的:
`import respondent_tier_b`）。レジストリ解決はそのプログラムに局所
である。本レジストリをインポートしないプログラムは `Blocking(...)`,
`Renewal(...)` などを未知の識別子として扱い、構文解析エラーを受け取る
（Core `respondent/grammar.md §4`、性質 2）。

これはオペラント側のスケジュール拡張原則（Core
`design-philosophy §5`）を継承しており、以下を保証する。

- プリミティブがそれを要求しなかったプログラムに「漏れる」ことはない。
- 二つのプログラムが競合する Tier B バリアントを互いに干渉せず
  ロードできる。
- Core パーサはプログラム独立のままである。

---

## 4. 26 プリミティブ選定の科学的正当性

本選定は網羅的ではなく **手続き中心** である。現象が Tier B
プリミティブとして列挙されるのは、以下をすべて満たす場合に限る。

1. 一次パヴロフ文献で独立した準備として名付けられている。
2. Tier A プリミティブの単純な合成としてエンコードすると
   **手続き上の意図が失われる** — 手続き構造（例: 阻止の
   Phase 1 / Phase 2 / Test 配列）が重要であり、AST に可視である
   べきである。
3. 少なくとも 1 本のピアレビュー付き一次論文で手続きが
   操作的に定義されている。

(2) を満たさない現象 — 例: 「強度 X の US」 — は本パッケージではなく
Core の `respondent-annotator` が扱う。

26 プリミティブの主要な根拠:

- **基礎的対提示とその統制手続き** — Pavlov (1927); Rescorla
  (1967, 1968) — は Core の Tier A。
- **単純な対提示を超えた獲得のバリアント** — 高次条件づけ、
  感覚性前条件づけ、逆条件づけ — Pavlov (1927); Brogden (1939);
  Rizley & Rescorla (1972); Dickinson & Pearce (1977)。
- **Rescorla & Wagner (1972) の手がかり競合の予測** — 阻止、覆い隠し、
  過剰期待、スーパー条件づけ、遡及的再評価 — Kamin (1969);
  Mackintosh (1976); Rescorla (1970, 1971); Van Hamme & Wasserman
  (1994)。
- **抑制性学習** — 条件性抑制、機会設定、遅延抑制、加算／遅延
  学習テスト — Rescorla (1969); Holland (1983)。
- **事前曝露効果** — 潜在抑制、US 事前曝露 — Lubow & Moore (1959);
  Randich & LoLordo (1979)。
- **消去と回復** — 更新、再発、自発的回復、文脈性消去、再固定化
  妨害 — Rescorla & Heth (1975); Bouton & Bolles (1979); Bouton
  (2004); Rescorla (2004); Monfils et al. (2009)。
- **特殊な準備** — 条件性味覚嫌悪、刺激般化、文脈性恐怖条件づけ、
  ピーク手続き、媒介条件づけ — Garcia, Ervin, & Koelling (1966);
  Hovland (1937); Fanselow (1990); Roberts (1981); Holland (1981)。

---

## 5. ファイル内バージョンマーカーなし

本パッケージは tracked ファイルにバージョンマーキング表現を
埋め込まない（「v1」なし、「メジャーバンプ」なし、「Core 凍結」なし）。
履歴は `git tag` / `git log` が担い、ドキュメントには二重化しない。

---

## 6. 参考文献

- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Bouton, M. E., & Bolles, R. C. (1979). Contextual control of the
  extinction of conditioned fear. *Learning and Motivation*, 10(4),
  445–466. https://doi.org/10.1016/0023-9690(79)90057-2
- Brogden, W. J. (1939). Sensory pre-conditioning. *Journal of
  Experimental Psychology*, 25(4), 323–332. https://doi.org/10.1037/h0058944
- Dickinson, A., & Pearce, J. M. (1977). Inhibitory interactions between
  appetitive and aversive stimuli. *Psychological Bulletin*, 84(4),
  690–711. https://doi.org/10.1037/0033-2909.84.4.690
- Fanselow, M. S. (1990). Factors governing one-trial contextual
  conditioning. *Animal Learning & Behavior*, 18(3), 264–270.
  https://doi.org/10.3758/BF03205285
- Garcia, J., Ervin, F. R., & Koelling, R. A. (1966). Learning with
  prolonged delay of reinforcement. *Psychonomic Science*, 5(3),
  121–122. https://doi.org/10.3758/BF03328311
- Holland, P. C. (1981). Acquisition of representation-mediated
  conditioned food aversions. *Learning and Motivation*, 12(1), 1–18.
  https://doi.org/10.1016/0023-9690(81)90022-9
- Holland, P. C. (1983). Occasion-setting in Pavlovian feature positive
  discriminations. In M. L. Commons, R. J. Herrnstein, & A. R. Wagner
  (Eds.), *Quantitative analyses of behavior* (Vol. 4, pp. 183–206).
  Ballinger.
- Hovland, C. I. (1937). The generalization of conditioned responses: I.
  The sensory generalization of conditioned responses with varying
  frequencies of tone. *Journal of General Psychology*, 17(1), 125–148.
  https://doi.org/10.1080/00221309.1937.9917977
- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment
  and aversive behavior* (pp. 279–296). Appleton-Century-Crofts.
- Lubow, R. E., & Moore, A. U. (1959). Latent inhibition. *Journal of
  Comparative and Physiological Psychology*, 52(4), 415–419.
  https://doi.org/10.1037/h0046700
- Mackintosh, N. J. (1975). A theory of attention. *Psychological
  Review*, 82(4), 276–298. https://doi.org/10.1037/h0076778
- Mackintosh, N. J. (1976). Overshadowing and stimulus intensity.
  *Animal Learning & Behavior*, 4(2), 186–192.
  https://doi.org/10.3758/BF03214033
- Monfils, M.-H., Cowansage, K. K., Klann, E., & LeDoux, J. E. (2009).
  Extinction-reconsolidation boundaries. *Science*, 324(5929), 951–955.
  https://doi.org/10.1126/science.1167975
- Pavlov, I. P. (1927). *Conditioned reflexes*. Oxford University Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning.
  *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Randich, A., & LoLordo, V. M. (1979). Associative and nonassociative
  theories of the UCS preexposure phenomenon. *Psychological Bulletin*,
  86(3), 523–548. https://doi.org/10.1037/0033-2909.86.3.523
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper control
  procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109
- Rescorla, R. A. (1968). Probability of shock in the presence and
  absence of CS in fear conditioning. *Journal of Comparative and
  Physiological Psychology*, 66(1), 1–5. https://doi.org/10.1037/h0025984
- Rescorla, R. A. (1969). Pavlovian conditioned inhibition. *Psychological
  Bulletin*, 72(2), 77–94. https://doi.org/10.1037/h0027760
- Rescorla, R. A. (1970). Reduction in the effectiveness of reinforcement
  after prior excitatory conditioning. *Learning and Motivation*, 1(4),
  372–381. https://doi.org/10.1016/0023-9690(70)90101-3
- Rescorla, R. A. (1971). Variation in the effectiveness of reinforcement
  and nonreinforcement following prior inhibitory conditioning. *Learning
  and Motivation*, 2(2), 113–123.
  https://doi.org/10.1016/0023-9690(71)90002-6
- Rescorla, R. A. (2004). Spontaneous recovery. *Learning & Memory*,
  11(5), 501–509. https://doi.org/10.1101/lm.77504
- Rescorla, R. A., & Heth, C. D. (1975). Reinstatement of fear to an
  extinguished conditioned stimulus. *Journal of Experimental Psychology:
  Animal Behavior Processes*, 1(1), 88–96.
  https://doi.org/10.1037/0097-7403.1.1.88
- Rescorla, R. A., & Solomon, R. L. (1967). Two-process learning theory.
  *Psychological Review*, 74(3), 151–182.
  https://doi.org/10.1037/h0024475
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
- Rizley, R. C., & Rescorla, R. A. (1972). Associations in second-order
  conditioning and sensory preconditioning. *Journal of Comparative and
  Physiological Psychology*, 81(1), 1–11. https://doi.org/10.1037/h0033333
- Roberts, S. (1981). Isolation of an internal clock. *Journal of
  Experimental Psychology: Animal Behavior Processes*, 7(3), 242–268.
  https://doi.org/10.1037/0097-7403.7.3.242
- Van Hamme, L. J., & Wasserman, E. A. (1994). Cue competition in
  causality judgments: The role of nonpresentation of compound stimulus
  elements. *Learning and Motivation*, 25(2), 127–151.
  https://doi.org/10.1006/lmot.1994.1008

