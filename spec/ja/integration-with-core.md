# Core との統合 — レスポンデント拡張ポイント契約

> `contingency-respondent-dsl` パッケージの一部。本パッケージの
> 26 個の Tier B プリミティブが Core レスポンデント文法に **Core を変更せずに** 
> どのように接続されるかを正確に規定する。

---

## 1. 契約（一行で）

Core (`contingency-dsl/spec/en/respondent/grammar.md §4`) は以下を宣言する。

```ebnf
ExtensionRespondentPrimitive ::= IdentUpper "(" ArgList? ")"
IdentUpper                   ::= [A-Z][a-zA-Z0-9_]*
```

本パッケージは、この単一の抽象規則を特定の識別子と引数スキーマで
具体化する産出規則を供給する。これが統合契約の全てである。

---

## 2. 各 Tier B プリミティブに課される義務

本パッケージが定義するすべてのプリミティブ `P` について:

1. **識別子形式**。`P` は `Ident(...)` として綴られる。ここで `Ident`
   は `IdentUpper` に一致し、Core の Tier A 予約キーワード (`Pair`,
   `ForwardDelay`, `ForwardTrace`, `Simultaneous`, `Backward`,
   `Extinction`, `CSOnly`, `USOnly`, `Contingency`, `TrulyRandom`,
   `ExplicitlyUnpaired`, `Compound`, `Serial`, `ITI`, `Differential`,
   `trials`, `isi`, `cs_duration`, `trace_interval`, `mode`, `mean`,
   `min_separation`, `p`, `fixed`, `uniform`, `exponential`) の
   いずれでもない。
2. **引数リスト**。引数リストはコンマ区切りのキーワードまたは
   位置引数の列である。各引数は以下のいずれか:
   - 単位付き数値、確率、文字列ラベルなどのリテラル値
   - `StimulusRef`（let バインディングされた識別子、または文字列リテラル）
   - 入れ子のレスポンデント式（Tier A **または** Tier B） — これにより
     `Blocking(phase1=..., phase2=..., test=...)` が他のプリミティブを
     参照できる。
3. **Phase 2 レジストリエントリ**。`P` は宣言された引数スキーマと
   ともに Tier B レジストリに自己登録する。レジストリは
   `IdentUpper` → スキーマのマッピングであり、Phase 2 が引数の
   個数と型を検証するためにこれを使用する。
4. **非 TC**。`P` の操作的定義は有限の宣言的手続きであり、文法に
   反復、再帰、または状態依存の分岐を導入しない。

---

## 3. プログラムスコープでの有効化

Tier B を使用するプログラムは、ヘッダでレジストリを有効化する（概念的）。

```
# プログラムヘッダ（構文は Core が確定する。以下は概念的な形）
import respondent_tier_b
```

有効化後:

- すべての Tier B 識別子（`Blocking`, `LatentInhibition`, `Renewal`
  など）は本レジストリを通じて解決される。
- Tier A 識別子は Core の Tier A 規則を通じて解決され続ける
  （Tier B は Tier A を決してシャドウしない）。
- 未知の識別子は構文解析エラーのまま残る。「文字列」へのフォール
  バックは存在しない。

本レジストリを有効化*しない*プログラムは Tier B プリミティブを使用
できない。そのようなプログラムで `Blocking(...)` は Phase 1 の構文
エラーではなく、Phase 2 の構文解析エラーである。

---

## 4. サンプルプログラム

```
# プログラムヘッダ
import respondent_tier_b

# バインディング
let tone_a = "tone_a"
let tone_x = "tone_x"
let shock  = "shock"

# Blocking (Kamin 1969)
Blocking(
    phase1 = Pair.ForwardDelay(tone_a, shock, isi=10-s, cs_duration=15-s),
    phase2 = Pair.ForwardDelay(Compound([tone_a, tone_x]), shock,
                                isi=10-s, cs_duration=15-s),
    test   = Extinction(tone_x),
    phase1_trials = 40,
    phase2_trials = 20,
    test_trials   = 10
)
```

ここで:

- `Blocking` は本パッケージのレジストリを通じて解決される。
- `Pair.ForwardDelay`, `Compound`, `Extinction` は Tier A であり、
  Core を通じて解決される。
- 単位付き数値リテラル (`10-s`, `15-s`) と `trials` キーワードは
  Core の既存の慣例に従う。

---

## 5. 境界でのエラーハンドリング

| シナリオ | 報告側 | エラークラス |
|---|---|---|
| 構文的に不正な識別子 (`3Blocking(...)`) | Core パーサ (Phase 1) | `SYNTAX` |
| 整形された識別子だがレジストリ未有効化 | Core Phase 2 | `UNKNOWN_EXTENSION_PRIMITIVE` |
| レジストリ有効、識別子未登録 | Core Phase 2 （レジストリ問い合わせ付き） | `UNKNOWN_EXTENSION_PRIMITIVE` |
| 登録されたプリミティブ、引数個数の不一致 | Tier B スキーマバリデータ | `ARITY_MISMATCH` |
| 登録されたプリミティブ、引数型の不一致 | Tier B スキーマバリデータ | `TYPE_MISMATCH` |
| 登録されたプリミティブ、必須フィールドの欠落 | Tier B スキーマバリデータ | `MISSING_FIELD` |
| 登録されたプリミティブ、未知のキーワード | Tier B スキーマバリデータ | `UNKNOWN_FIELD` |

最初の二つのエラークラスは Core の責任、残り四つは本パッケージの
責任であり、[`../../conformance/README.md`](../../conformance/README.md)
に文書化される。

---

## 6. レジストリエントリの形（概念）

レジストリはデータ構造であり、言語機能ではない。概念的なエントリの例
（正確な形はパーサ実装時に確定）:

```
registry_entry {
  identifier: "Blocking",
  arg_schema: {
    phase1:         RespondentExpr,  // 必須
    phase2:         RespondentExpr,  // 必須
    test:           RespondentExpr,  // 必須
    phase1_trials:  Number,          // 任意、デフォルト未指定
    phase2_trials:  Number,          // 任意
    test_trials:    Number,          // 任意
  },
  primary_citation: "Kamin (1969)",
  spec_file: "spec/en/tier-b-primitives/blocking.md",
}
```

各エントリの正典は [`tier-b-primitives/`](tier-b-primitives/) の
プリミティブごとのページである。

---

## 7. Core に明示的に追加しないもの

本パッケージは以下を **行わない**。

- Tier A プリミティブを再定義する。
- Core にアノテーションを追加する。アノテーションは Core の
  `annotations/extensions/respondent-annotator.md` のドメインに留まる。
- Core に相順序付け意味論を追加する。相順序付けは Core の
  `experiment/phase-sequence.md` が引き続き統括する。本パッケージと
  互換性があるのは、多相手続きである各 Tier B プリミティブ（阻止、
  更新、再発）が内部相を入れ子のレスポンデント式として表現し、
  新しい相レベルの構成を導入しないためである。
- 新しいアノテーション層を導入する。新しいアノテーションファミリを
  必要とするプログラムスコープの挙動は Tier B のスコープ外であり、
  別パッケージとして提案されるべきである。

