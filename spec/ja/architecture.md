# アーキテクチャ — contingency-respondent-dsl

> `contingency-respondent-dsl` パッケージの一部。本ドキュメントは、
> 本パッケージの文法が Core `contingency-dsl` のレスポンデント層と
> `ExtensionRespondentPrimitive` 拡張ポイントを通じてどのように統合
> されるかを記述する。**Core に新たな層を追加しない。**

---

## 1. OperantKit レイヤースタックにおける位置

`contingency-dsl` (Core) はすでに六層 Ψ アーキテクチャ
(`foundations / operant / respondent / composed / experiment /
annotations`) を定義している。Core のレスポンデント層は意図的に
最小化されており、基礎的なパヴロフ型プリミティブ (R1–R14) のみを
カバーする (Pavlov, 1927; Rescorla, 1967; Mackintosh, 1974)。
より深いパヴロフ現象 — 阻止 (ブロッキング)、覆い隠し
(オーバーシャドウイング)、潜在抑制、更新 (リニューアル)、再発、
条件性抑制など — は **Tier B** に属し、本パッケージが扱う。

したがって `contingency-respondent-dsl` は **新たな層ではない**。
Core レスポンデント文法に既存する拡張ポイントの利用者である。

```
contingency-dsl (Core)
├── foundations/
├── operant/
├── respondent/
│   ├── grammar.md
│   │   ├── core_respondent_primitive   ← Tier A (R1–R14)
│   │   └── extension_respondent_primitive   ← 拡張ポイント; §2 参照
│   ├── theory.md
│   └── primitives.md
├── composed/
├── experiment/
└── annotations/

contingency-respondent-dsl (本パッケージ)
├── spec/en/grammar.md                  ← 26 個の Tier B 産出規則
└── schema/grammar.ebnf                 ← 26 個の EBNF
     (両者とも上記の拡張ポイント経由で登録される)
```

---

## 2. 拡張ポイント契約

Core の `spec/en/respondent/grammar.md §4` は拡張ポイントを次のように
定義する（言い換え）。

```ebnf
RespondentExpr ::=
      CoreRespondentPrimitive            (* Tier A: R1–R14 *)
    | ExtensionRespondentPrimitive       (* Tier B / サードパーティ *)

ExtensionRespondentPrimitive ::=
      IdentUpper "(" ArgList? ")"
    -- プログラムスコープの解決 (レスポンデントレジストリ)
```

本パッケージが定義する任意の Tier B プリミティブは、次の形式で綴られる。

```
<IdentUpper>(<arg_list>)
```

ここで `IdentUpper` は `[A-Z][a-zA-Z0-9_]*` に一致し、引数リストは
`spec/en/tier-b-primitives/<name>.md` で文書化された
プリミティブ固有のスキーマに従う。

Core のパーサは、このような識別子形式の式をすべて構文的に有効と
扱い（Core の `foundations/ll2-proof.md` に従い最初のトークンで
LL(1) 区別可能）、意味論的検証 — レジストリ参照と引数型チェックを
含む — を Phase 2 ポスト・パースに委ねる。本パッケージは自身の
26 プリミティブに関して Phase 2 の規則を供給する。

---

## 3. プログラムが拡張を有効化する方法

プログラムは Tier B レジストリを宣言的に有効化する。以下は想定される
概念的な形式である。正確な構文は、Core がレジストリインポート構文を
確定した時点で決まる。

```
# プログラムヘッダ（概念的）
import respondent_tier_b

# 本体（以下の識別子はすべて Tier B レジストリを通じて解決される）
phase acquisition:
    Pair.ForwardDelay(tone, shock, isi=10-s, cs_duration=15-s)

phase test:
    Blocking(
        phase1 = Pair.ForwardDelay(a, shock, isi=10-s, cs_duration=15-s),
        phase2 = Pair.ForwardDelay(Compound([a, x]), shock,
                                    isi=10-s, cs_duration=15-s),
        test   = Extinction(x)
    )
```

注意: `Blocking(...)` の識別子は Core の Tier A 予約セットに**含まれない**。
本パッケージのレジストリがロードされているときのみ解決される。
レジストリがロードされていない場合、Core は構文解析エラーを送出する
（未知の `ExtensionRespondentPrimitive` は静かに受理されない）。

---

## 4. 本パッケージが行わないこと

- **Tier A プリミティブの再定義は行わない**。`Pair.*`, `Extinction`,
  `CSOnly`, `USOnly`, `Contingency`, `TrulyRandom`,
  `ExplicitlyUnpaired`, `Compound`, `Serial`, `ITI`, `Differential`
  は Core が所有する。
- **レスポンデント文法の CFG クラスを変更しない**。新しい各産出は
  `IdentUpper "(" ArgList? ")"` の形式であり、Core の LL(2) 解析で
  すでにカバーされている。
- **チューリング完全性を導入しない**。すべての Tier B プリミティブは
  有限の宣言的手続きであり、そのパラメータは構文解析時に確定する
  リテラル値である。
- **パーサを書かない**。本チェックポイントは仕様のみ: 文法、AST
  スキーマ、適合性フィクスチャ、ドキュメント。Python パーサは
  別の後続作業である。

---

## 5. Tier B の科学的スコープ

26 個の Tier B プリミティブは、パヴロフ型学習文献から
**実験者が名前を付けたくなる手続き的に異なる準備** として選ばれている。
選定の根拠は以下のとおり。

- 古典的な EAB の扱い: Pavlov (1927); Rescorla (1967, 1968, 1969,
  1970, 1971, 1972); Mackintosh (1974); Bouton (2004)。
- 現代の学習理論レビュー: Mackintosh (1975); Pearce & Hall (1980);
  Wagner (1981); Bouton (2016); Pearce (2013)。
- 特定手続きの一次出典: 阻止は Kamin (1969)、機会設定は Holland
  (1983)、条件性味覚嫌悪は Garcia, Ervin, & Koelling (1966)、
  再固定化妨害は Monfils et al. (2009)、文脈性恐怖は Fanselow
  (1990)、ピーク手続きは Roberts (1981)。

26 個すべてのプリミティブとその一次出典をグループ化した表は
[`spec/en/tier-b-primitives/_index.md`](tier-b-primitives/_index.md)
を参照。

---

## 6. Core アノテーションとの関係

一部のパヴロフ現象は、原理的には新しい文法産出ではなく Tier A
プリミティブへのアノテーションとして表現できる。その境界は
Core の `annotations/boundary-decision.md` が定める。本パッケージの
26 プリミティブはすべて **拡張文法側** に配置された。理由は各
プリミティブが以下を満たすためである。

- 複数相の手続きの **構造** を導入または制約する（例: `Blocking` は
  Phase 1 / Phase 2 / Test の特定順序、および Phase 2 における
  複合 CS 提示を要求する）。単一の Tier A 手続きの性質を注釈するだけ
  ではない。
- 文献上、別手続きを修飾する形ではなく、自立した準備として名付けられる。

Tier A + アノテーションで綺麗に分解できる現象（CS モダリティ、
US 強度、ITI ジッタ）は、Core の
`annotations/extensions/respondent-annotator.md` に留まり、本パッケージ
では再仕様化しない。

---

## 7. 参考文献

- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Bouton, M. E. (2016). *Learning and behavior: A contemporary synthesis*
  (2nd ed.). Sinauer.
- Fanselow, M. S. (1990). Factors governing one-trial contextual
  conditioning. *Animal Learning & Behavior*, 18(3), 264–270.
  https://doi.org/10.3758/BF03205285
- Garcia, J., Ervin, F. R., & Koelling, R. A. (1966). Learning with
  prolonged delay of reinforcement. *Psychonomic Science*, 5(3),
  121–122. https://doi.org/10.3758/BF03328311
- Holland, P. C. (1983). Occasion-setting in Pavlovian feature positive
  discriminations. In M. L. Commons, R. J. Herrnstein, & A. R. Wagner
  (Eds.), *Quantitative analyses of behavior* (Vol. 4, pp. 183–206).
  Ballinger.
- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment
  and aversive behavior* (pp. 279–296). Appleton-Century-Crofts.
- Mackintosh, N. J. (1974). *The psychology of animal learning*.
  Academic Press.
- Mackintosh, N. J. (1975). A theory of attention: Variations in the
  associability of stimuli with reinforcement. *Psychological Review*,
  82(4), 276–298. https://doi.org/10.1037/h0076778
- Monfils, M.-H., Cowansage, K. K., Klann, E., & LeDoux, J. E. (2009).
  Extinction-reconsolidation boundaries: Key to persistent attenuation
  of fear memories. *Science*, 324(5929), 951–955.
  https://doi.org/10.1126/science.1167975
- Pavlov, I. P. (1927). *Conditioned reflexes*. Oxford University Press.
- Pearce, J. M. (2013). *Animal learning and cognition* (3rd ed.).
  Psychology Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning:
  Variations in the effectiveness of conditioned but not of
  unconditioned stimuli. *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper control
  procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109
- Rescorla, R. A. (1969). Pavlovian conditioned inhibition.
  *Psychological Bulletin*, 72(2), 77–94.
  https://doi.org/10.1037/h0027760
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
- Roberts, S. (1981). Isolation of an internal clock. *Journal of
  Experimental Psychology: Animal Behavior Processes*, 7(3), 242–268.
  https://doi.org/10.1037/0097-7403.7.3.242
- Wagner, A. R. (1981). SOP: A model of automatic memory processing in
  animal behavior. In N. E. Spear & R. R. Miller (Eds.), *Information
  processing in animals: Memory mechanisms* (pp. 5–47). Erlbaum.

