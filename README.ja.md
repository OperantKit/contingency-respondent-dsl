# contingency-respondent-dsl

:gb: [English README](README.md)

contingency-respondent-dsl は、阻止・隠蔽・潜在制止・リニューアル・復位など 26 種類の Pavlov 型（レスポンデント）条件づけの手続きを、項目名の決まったレコードとして表し、JSON として保存・比較・交換できるようにします。レスポンデントのデザインを設定ファイル・分析の処理・テストで扱う研究者のためのものです。[OperantKit](https://github.com/OperantKit) の手続きの記法 [contingency-dsl](https://github.com/OperantKit/contingency-dsl) を拡張します。

**要点**

- 手続きごとに項目の組が 1 つに決まっているので、2 つの研究室が「阻止」を書き留めても同じレコードになります。
- 項目が足りない・綴りが違う・余計な項目がある場合はエラーになり、不完全なデザインが保存されることはありません。
- レコードは、`schema/` の JSON Schema に従う普通の辞書と相互に変換できます。

## インストール

Python 3.11 以上が必要です。パッケージはまだ PyPI に登録されていないので、GitHub から入れます。

```bash
pip install git+https://github.com/OperantKit/contingency-respondent-dsl
```

依存パッケージはありません。

## 例

ABA リニューアル（Bouton & Bolles, 1979）の手続きを項目から組み立て、JSON にできる辞書に変換して戻し、必須の項目が欠けたときの挙動を見ます。

```python
import json

from contingency_respondent_dsl import MissingFieldError, from_dict, parse_primitive, to_dict

# ABA リニューアル: 文脈 A で CS-US 対提示、文脈 B で消去、文脈 A でテスト。
arguments = {
    "acquisition": {"type": "Pair.ForwardDelay", "cs": "tone", "us": "shock"},
    "extinction": {"type": "Extinction", "cs": "tone"},
    "test": {"type": "Extinction", "cs": "tone"},
    "acquisition_context": "ctx_a",
    "extinction_context": "ctx_b",
    "test_context": "ctx_a",
}
node = parse_primitive("Renewal", keyword_args=arguments)
ast = to_dict(node)  # 普通の dict。そのまま json.dumps できる
print(ast["type"], [ast[k] for k in ("acquisition_context", "extinction_context", "test_context")])
# Renewal ['ctx_a', 'ctx_b', 'ctx_a']
print(from_dict(json.loads(json.dumps(ast))) == node)  # True

incomplete = {k: v for k, v in arguments.items() if k != "test_context"}
try:
    parse_primitive("Renewal", keyword_args=incomplete)
except MissingFieldError as error:
    print(error)  # missing required keyword(s) for Renewal: ['test_context']
```

`parse_primitive` は変更できないデータクラス（この例では `contingency_respondent_dsl.ast.Renewal`）を返します。未知の手続き名は `UnknownPrimitiveError`、位置引数は `ArityError`、想定外の項目は `UnknownFieldError` になります。時間は `{"value": 15, "unit": "s"}` か `(15, "s")` の形で書きます。値が正でない場合や、単位が `ms`・`s`・`min`・`h` 以外の場合は `ValueError` になります。

## 26 種類の手続き

| 系統 | 識別子 |
|---|---|
| 獲得と高次条件づけ | `HigherOrderConditioning`、`SensoryPreconditioning`、`Counterconditioning` |
| 手がかりの競合 | `Blocking`、`Overshadowing`、`Overexpectation`、`SuperConditioning`、`RetrospectiveRevaluation` |
| 制止の学習 | `ConditionedInhibition`、`OccasionSetting`、`InhibitionOfDelay`、`SummationRetardationTest` |
| 先行呈示 | `LatentInhibition`、`USPreexposure` |
| 消去と回復 | `Renewal`、`Reinstatement`、`SpontaneousRecovery`、`LatentExtinction`、`PavlovianPREE`、`ContextualExtinction`、`ReconsolidationInterference` |
| 特殊な手続き | `ConditionedTasteAversion`、`StimulusGeneralization`、`ContextualFearConditioning`、`PeakProcedure`、`MediatedConditioning` |

手続きごとに、操作的定義・項目・主要な出典を書いたページがあります。[一覧](spec/ja/tier-b-primitives/_index.md) から辿ってください。

## contingency-dsl との関係

contingency-dsl のレスポンデントのレイヤは小さく保たれていて、対提示（`Pair.*`）、`Extinction`、`CSOnly`、`USOnly`、`Contingency`、`TrulyRandom`、`ExplicitlyUnpaired`、`Compound`、`Serial`、`ITI`、`Differential`（「Tier A」のプリミティブ）だけを持ちます。これらを複数のフェーズにわたって組み合わせる手続き（上の 26 種類。「Tier B」のプリミティブ）は、Core のレスポンデント文法にある 1 つの拡張点を通じて追加され、その文法は変更しません。

```ebnf
ExtensionRespondentPrimitive ::= Identifier "(" ArgList? ")"
```

`contingency-respondent-dsl` は、この拡張点の最初の、かつ正規の利用者です。Core のレスポンデントのプリミティブだけを使うプログラムは影響を受けません。

## このリポジトリの中身

- `spec/en/`、`spec/ja/`: 仕様（アーキテクチャ、Core への差し込み方、文法、理論、手続きごとのページ）
- `schema/`: 26 種類の手続きの EBNF 文法（`grammar.ebnf`）、レコードの JSON Schema（`ast.schema.json`）、プログラムがこの拡張を読み込む方法（`extension-registry.md`）
- `conformance/tier-b/`: 26 個のファイル（手続きごとに 1 個）に 28 件のテストケース。各ケースに入力文字列と期待されるレコードがあります
- `src/contingency_respondent_dsl/`: Python のパッケージ（`parse_primitive`、`to_dict`、`from_dict`、`register`）

## 制限

- このパッケージは DSL のテキストを読みません。手続き名と、評価済みの項目から始めます。`Renewal(acquisition = ..., ...)` のようなテキストを読むのは Core のパーサ [contingency-dsl-py](https://github.com/OperantKit/contingency-dsl-py) の役目です。contingency-dsl-py はこれらの識別子を構文解析せず、`TierBExtension` はそのままでは contingency-dsl-py の `ExtensionRegistry` に渡せない（`annotation_keywords` を持たない）ため、2 つのパッケージを組み合わせてもテキストから最後まで読むことはできません。
- 手続きを記述するだけで、セッションを実行したり条件づけをシミュレーションしたりはしません。
- `LatentExtinction` と `PavlovianPREE` の主要な出典は、[一覧](spec/ja/tier-b-primitives/_index.md) で確認が必要と記されています。

## 開発に参加する人へ

```bash
git clone https://github.com/OperantKit/contingency-respondent-dsl
cd contingency-respondent-dsl
mise exec -- python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/python -m pytest -q
```

テストに contingency-dsl-py は要りません。この README と `README.md` の `python` ブロックは、すべて `tests/test_readme_examples.py` で実行されます。AI のコーディングエージェント向けの説明は [AGENTS.md](AGENTS.md) にあります。

## 参考文献

- Bouton, M. E., & Bolles, R. C. (1979). Contextual control of the extinction of conditioned fear. *Learning and Motivation*, 10(4), 445–466. https://doi.org/10.1016/0023-9690(79)90057-2

## 引用とライセンス

このパッケージを引用するときは [CITATION.cff](CITATION.cff) を使ってください。MIT License です。[LICENSE](LICENSE) を参照してください。
