# contingency-respondent-dsl — ドキュメント（日本語）

[`contingency-dsl`](../../../contingency-dsl/) の Tier B パヴロフ拡張の
利用者向け概観。正規の仕様は [`../../spec/ja/`](../../spec/ja/) にある。
本ページは短い導入とナビゲーションの索引である。

## 本パッケージとは

`contingency-respondent-dsl` は Core のレスポンデント層を、26 個の
パヴロフ型条件づけ手続き — 阻止（ブロッキング）、覆い隠し
（オーバーシャドウイング）、潜在抑制、更新（リニューアル）、再発、
条件性抑制、機会設定、条件性味覚嫌悪、ピーク手続きなど — で拡張する。

これは単一の拡張ポイント (`ExtensionRespondentPrimitive`) を通じて
Core に接続され、Core アーキテクチャに新しい層を追加しない。プログラムは
ヘッダでレジストリを宣言することで Tier B を有効化する（概念的:
`import respondent_tier_b`）。Tier A には手を加えない。

## ステータス — 仕様のみ

このパッケージには**まだパーサが存在しない**。統合は将来のパーサを
通じて行われる。そのパーサは Core のパースツリーを消費し、Tier B
識別子をこの拡張レジストリに渡す。本設計チェックポイントで本
パッケージは以下を提供する:

- [`../../spec/ja/tier-b-primitives/`](../../spec/ja/tier-b-primitives/)
  におけるプリミティブ毎の操作的仕様と主要な APA 引用。
- [`../../schema/grammar.ebnf`](../../schema/grammar.ebnf) における
  26 個の Tier B 産出規則の EBNF 文法。
- [`../../schema/ast.schema.json`](../../schema/ast.schema.json) における
  AST ノードの JSON Schema (2020-12)。
- [`../../conformance/tier-b/`](../../conformance/tier-b/) における
  適合性フィクスチャのスケルトン。

インストール手順は現時点では提供されない。

## 最初に読むべき場所

- **どこに何があるかの概観:** [`../../README.md`](../../README.md)。
- **アーキテクチャと Core への接続方法:**
  [`../../spec/ja/architecture.md`](../../spec/ja/architecture.md)。
- **拡張ポイント契約:**
  [`../../spec/ja/integration-with-core.md`](../../spec/ja/integration-with-core.md)。
- **プリミティブ全表:**
  [`../../spec/ja/tier-b-primitives/_index.md`](../../spec/ja/tier-b-primitives/_index.md)。
- **EBNF 文法:** [`../../schema/grammar.ebnf`](../../schema/grammar.ebnf)。
- **理論フレームワーク（ポインタレベル）:**
  [`../../spec/ja/theory.md`](../../spec/ja/theory.md)。

## スコープ境界

真にオペラント（道具的）な現象、三項随伴性の現象、またはオペラントと
レスポンデント手続きの合成は、**ここでは扱わない**。これらは Core の
`operant/` および `composed/` 層に残る。Tier A プリミティブへの
アノテーション（CS モダリティ、US 強度）は Core の
`annotations/extensions/respondent-annotator.md` が扱う。

## 貢献方法

- ファイルアクセス、設計チェックポイント、プライバシー規則については
  [`../../CLAUDE.md`](../../CLAUDE.md) に従う。
- 新しいプリミティブは以下の手順で追加する。(a) `spec/en/tier-b-primitives/`
  に仕様ページを追加し、JA ミラーも追加する。(b) `schema/grammar.ebnf`
  と `schema/ast.schema.json` を拡張する。(c) `conformance/tier-b/` に
  フィクスチャを追加する。(d) `spec/en/tier-b-primitives/_index.md` と
  その JA ミラーにエントリを追加する。
- 各プリミティブは APA 形式のピアレビュー付き一次出典を必須とする。
