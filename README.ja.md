# contingency-respondent-dsl

:gb: [English README](README.md)

[`contingency-dsl`](../contingency-dsl/) 向けの Tier B Pavlov 型（レスポンデント）手続き拡張。本パッケージは、Core のレスポンデント層の文法を**変更することなく**、`ExtensionRespondentPrimitive` 拡張点を介して生成規則を登録することで、26 の古典的条件づけ手続きを定義する。

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
│   ├── auxiliary.md             設計チェックポイントログ
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
- 5 つのデモ用プリミティブ（blocking, renewal, latent inhibition, overshadowing, reinstatement）に対する具体的な `expected_ast` dict 付きの適合性フィクスチャ。残りの 21 件のフィクスチャには `input` 文字列は埋まっているが、引数スキーマがパーサ経由でエンドツーエンドに実行されるまで `expected_ast: null` のまま

## インストール（ローカル開発用）

本パッケージは上流の OperantKit ポリシーに従って `mise` + `venv` を使用する。`uv` は使用しない。

```sh
# contingency-respondent-dsl/ 内部から
mise exec -- python -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m pip install pytest
.venv/bin/pytest tests/ -q
```

Core のパーサ（`contingency-dsl-py`）は別の兄弟パッケージであり、本パッケージ自身のユニットテストを動かすためには不要：Tier B パーサは拡張境界において既に評価されたキーワード引数の上で動作し、ネストされた Tier A 式はその境界では不透明な dict として扱われる。

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
ext.parse_primitive("Renewal", None, { ... })
```

`register()` ヘルパは dict、`register_tier_b(ext)` メソッドを公開する任意のオブジェクト、または素の名前空間を受け付ける。

### カバレッジ状況

26 プリミティブ全ての識別子は登録済み（未知の識別子は `UnknownPrimitiveError` を送出）。エンドツーエンドのパース経路は 5 つのデモ用プリミティブで検証済み；残りの 21 件については AST クラスは定義・登録されているが、往復経路はフィクスチャが埋まっている限りにおいて適合性ランナー内の `from_dict` / `to_dict` 経由でのみ実行される。

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
