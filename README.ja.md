# contingency-respondent-dsl

:gb: [English README](README.md)

[`contingency-dsl`](https://github.com/OperantKit/contingency-dsl) 向けの Tier B Pavlov 型（レスポンデント）手続き拡張。本パッケージは、Core のレスポンデント層の文法を**変更することなく**、`ExtensionRespondentPrimitive` 拡張点を介して生成規則を登録することで、26 の古典的条件づけ手続きを定義する。

## `contingency-dsl` との関係

Core パッケージはレスポンデント層を意図的に最小限に保つ —— 基盤となる二項随伴性プリミティブ（R1–R14: `Pair.*`, `Extinction`, `CSOnly`, `USOnly`, `Contingency`, `TrulyRandom`, `ExplicitlyUnpaired`, `Compound`, `Serial`, `ITI`, `Differential`）のみ。Core のレスポンデント文法は拡張フックを 1 つだけ公開している：

```ebnf
ExtensionRespondentPrimitive ::= Identifier "(" ArgList? ")"
```

より深い Pavlov 型カバレッジを必要とするサードパーティのレスポンデント語彙は、この拡張点を介して識別子を登録する。`contingency-respondent-dsl` はその最初かつ正典的な利用者。

## スコープ — 26 の Tier B プリミティブ

概念的系統別に分類（[`spec/en/tier-b-primitives/_index.md`](spec/en/tier-b-primitives/_index.md) 参照）：

- **獲得と高次条件づけ** — 高次条件づけ (Pavlov, 1927; Rizley & Rescorla, 1972), 感覚前条件づけ (Brogden, 1939), 拮抗条件づけ (Dickinson & Pearce, 1977)
- **手掛かり競合** — 阻止 (Kamin, 1969), 隠蔽 (Mackintosh, 1976), overexpectation (Rescorla, 1970), 超条件づけ (Rescorla, 1971), 遡及的再評価 (Van Hamme & Wasserman, 1994)
- **制止学習** — 条件性制止 (Rescorla, 1969), 条件性弁別 (Holland, 1983), 遅延制止 (Pavlov, 1927), 加算/遅延検定 (Rescorla, 1969)
- **前曝露** — 潜在制止 (Lubow & Moore, 1959), US 前曝露 (Randich & LoLordo, 1979)
- **消去と回復** — 更新 (Bouton & Bolles, 1979), 再生 (Rescorla & Heth, 1975), 自発的回復 (Rescorla, 2004), 潜在消去, Pavlov 型部分強化消去効果, 文脈的消去 (Bouton, 2004), 再固定化干渉 (Monfils et al., 2009)
- **特殊手続き** — 条件性味覚嫌悪 (Garcia, Ervin, & Koelling, 1966), 刺激般化 (Hovland, 1937), 文脈的恐怖条件づけ (Fanselow, 1990), peak procedure (Roberts, 1981), 媒介条件づけ (Holland, 1981)

## リポジトリ構成

```
contingency-respondent-dsl/
├── spec/en/                      形式仕様（英語版正典）
│   ├── architecture.md           Core との結合方法
│   ├── design-philosophy.md      加法的拡張の規律
│   ├── integration-with-core.md  拡張点の契約
│   ├── grammar.md                26 の Tier B プリミティブ全ての EBNF
│   ├── theory.md                 Pavlov 型学習フレームワーク（指示レベル）
│   └── tier-b-primitives/        プリミティブごとのファイル + _index.md
├── spec/ja/                      spec/en/ の日本語ミラー
├── schema/
│   ├── grammar.ebnf              26 の Tier B 生成規則
│   ├── ast.schema.json           AST ノード用 JSON Schema 2020-12
│   └── extension-registry.md     プログラムがこのレジストリをロードする方法
├── conformance/
│   ├── README.md
│   └── tier-b/                   プリミティブごとに 1 つの .json フィクスチャ
└── docs/
    ├── en/README.md
    └── ja/README.md
```

## 状態

このパッケージが現在提供するもの：

- Core の `ExtensionRespondentPrimitive` を拡張する 26 の Pavlov 型手続きの EBNF 生成規則（[`spec/en/grammar.md`](spec/en/grammar.md) 参照）
- 生成される AST ノードの JSON Schema（[`schema/ast.schema.json`](schema/ast.schema.json) 参照）
- 主要 APA 引用付きの、プリミティブごとの操作的定義
- Python パーサのスケルトン（`src/contingency_respondent_dsl/`）：
  - 26 プリミティブ全てについて frozen dataclass（`ast.py`）
  - 識別子 + キーワード引数束を AST コンストラクタへディスパッチするレジストリ（`registry.py`）
  - AST スキーマ互換の dict シリアライザ（`serializer.py`）
  - 薄い `parse_primitive()` エントリポイント（`parser.py`）
- 26 プリミティブすべての適合性フィクスチャ（`conformance/tier-b/` 配下の 26 ファイル・28 ケース）。各ケースに `input` 文字列と具体的な `expected_ast` dict がある

## インストール

```bash
pip install git+https://github.com/OperantKit/contingency-respondent-dsl
```

ローカル開発では、上流の OperantKit ポリシーに従って `mise` + `venv` を使用する。`uv` は使用しない。

```sh
# contingency-respondent-dsl/ 内部から
mise exec -- python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/pytest tests/ -q
```

Core のパーサ（`contingency-dsl-py`）は別の兄弟パッケージであり、本パッケージ自身のユニットテストを動かすためには不要：Tier B パーサは拡張境界において既に評価されたキーワード引数の上で動作し、ネストされた Tier A 式はその境界では不透明な dict として扱われる。

## 30 秒で動く例

ABA 更新（renewal）の手続きをキーワード引数から組み立て、JSON にできる dict へ直列化して復元し、必須フィールドが欠けたときの挙動を見る:

```python
import json

from contingency_respondent_dsl import MissingFieldError, from_dict, parse_primitive, to_dict

# ABA 更新: 文脈 A で CS-US 対提示、文脈 B で消去、文脈 A でテスト。
arguments = {
    "acquisition": {"type": "Pair.ForwardDelay", "cs": "tone", "us": "shock"},
    "extinction": {"type": "Extinction", "cs": "tone"},
    "test": {"type": "Extinction", "cs": "tone"},
    "acquisition_context": "ctx_a",
    "extinction_context": "ctx_b",
    "test_context": "ctx_a",
}
node = parse_primitive("Renewal", keyword_args=arguments)
ast = to_dict(node)  # 素の dict。そのまま json.dumps できる
print(ast["type"], [ast[k] for k in ("acquisition_context", "extinction_context", "test_context")])
# Renewal ['ctx_a', 'ctx_b', 'ctx_a']
print(from_dict(json.loads(json.dumps(ast))) == node)  # True

incomplete = {k: v for k, v in arguments.items() if k != "test_context"}
try:
    parse_primitive("Renewal", keyword_args=incomplete)
except MissingFieldError as error:
    print(error)  # missing required keyword(s) for Renewal: ['test_context']
```

この例は本パッケージだけで動く。`Renewal(acquisition = ..., ...)` のような DSL のソース文字列を読むのは Core のパーサ [contingency-dsl-py](https://github.com/OperantKit/contingency-dsl-py)（`pip install contingency-dsl-py`）の役割で、本パッケージはそれに依存せず、評価済みの引数から始める。

## 自作の 50 行では足りない理由

実験ごとの dict や小さなクラスは手続きが 1 つなら足りるが、複数の Pavlov 型の実験計画を保存・比較・交換しはじめると破綻する:

- **名前の付いた 26 手続き.** 阻止、隠蔽、overexpectation、潜在制止、更新、再生、自発的回復、条件性制止、条件性弁別（occasion setting）、peak procedure など 26 手続きを、フィールド名の固定された frozen dataclass として登録している。2 つの研究室が「阻止」を書けば同じ構造になる。
- **適合性フィクスチャ.** `conformance/tier-b/` 配下の 26 ファイル・28 ケースが全プリミティブを網羅する。テストは各ケースを `parse_primitive` 経由と `from_dict` / `to_dict` 経由の両方で再生し、直列化した dict がフィクスチャと完全に一致することを求める。
- **引数を検証する.** 未知の識別子は `UnknownPrimitiveError`、位置引数は `ArityError`、必須キーワードの欠落は `MissingFieldError`、想定外のキーワードは `UnknownFieldError` を送出し、不完全な実験計画を黙って保存しない。
- **時間を検査する.** 時間フィールド（遅延制止の CS 持続時間と ISI など）は `{"value": 15, "unit": "s"}` か `(15, "s")` を受け付け、0 以下の値や `ms`・`s`・`min`・`h` 以外の単位は `ValueError` になる。
- **Core に対して加法的.** プリミティブは Core のレスポンデント層を `ExtensionRespondentPrimitive` フック 1 つだけで拡張するので、Core のレスポンデントプリミティブ（`Pair.*`、`Extinction`、`CSOnly` など）だけを使うプログラムは影響を受けない。

## 使い方

```python
from contingency_respondent_dsl import (
    parse_primitive,
    to_dict,
    from_dict,
)

node = parse_primitive(
    "Blocking",
    positional_args=[],
    keyword_args={
        "phase1": {"type": "Pair.ForwardDelay", "cs": "a", "us": "shock"},
        "phase2": {
            "type": "Pair.ForwardDelay",
            "cs": {"type": "Compound", "elements": ["a", "x"]},
            "us": "shock",
        },
        "test":   {"type": "Extinction", "cs": "x"},
        "phase1_trials": 40,
        "phase2_trials": 20,
        "test_trials":   10,
    },
)
# node は frozen な contingency_respondent_dsl.ast.Blocking インスタンス

serialized = to_dict(node)  # -> スキーマ形の dict
restored   = from_dict(serialized)
assert restored == node
```

Tier B 拡張をレジストリ様オブジェクトにアタッチするには：

```python
from contingency_respondent_dsl import register

bag: dict = {}
ext = register(bag)   # dict: "respondent-tier-b" キーに ext を格納
assert bag["respondent-tier-b"] is ext
node = ext.parse_primitive(
    "LatentInhibition",
    None,
    {
        "preexposure": {"type": "CSOnly", "cs": "tone"},
        "training": {"type": "Pair.ForwardDelay", "cs": "tone", "us": "shock"},
        "test": {"type": "Extinction", "cs": "tone"},
    },
)
print(type(node).__name__)  # LatentInhibition
```

`register()` ヘルパは dict、`register_tier_b(ext)` メソッドを公開する任意のオブジェクト、または素の名前空間を受け付ける。

### カバレッジ状況

26 プリミティブ全ての識別子は登録済み（未知の識別子は `UnknownPrimitiveError` を送出）。すべての適合性ケースを `parse_primitive` → `to_dict` と `from_dict` → `to_dict` の両経路で再生している。阻止・更新・潜在制止・隠蔽・再生の経路には、手書きのエンドツーエンドテストもある。

## ナビゲーション

- 形式仕様（英語）: [`spec/en/`](spec/en/)
- 形式仕様（日本語）: [`spec/ja/`](spec/ja/)
- EBNF 文法: [`schema/grammar.ebnf`](schema/grammar.ebnf)
- AST JSON Schema: [`schema/ast.schema.json`](schema/ast.schema.json)
- プリミティブ別索引: [`spec/en/tier-b-primitives/_index.md`](spec/en/tier-b-primitives/_index.md)
- 適合性フィクスチャ: [`conformance/tier-b/`](conformance/tier-b/)

## 参考文献（抜粋）

- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment and
  aversive behavior* (pp. 279–296). Appleton-Century-Crofts.
- Mackintosh, N. J. (1975). A theory of attention: Variations in the
  associability of stimuli with reinforcement. *Psychological Review*,
  82(4), 276–298. https://doi.org/10.1037/h0076778
- Pavlov, I. P. (1927). *Conditioned reflexes*. Oxford University Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning:
  Variations in the effectiveness of conditioned but not of unconditioned
  stimuli. *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper control
  procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
