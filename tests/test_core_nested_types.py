"""Nested Core respondent expressions use Core's AST type names and fields.

Tier B primitives carry Core (Tier A) respondent expressions as opaque
dicts. Those dicts must be shaped as Core serializes them, otherwise a
consumer that reads the Tier B AST together with Core's cannot dispatch on
``type``. Core's type names are written here, not loaded from Core, so the
package stays self-contained.
"""

from __future__ import annotations

import ast as pyast
import json
import re
from pathlib import Path
from typing import Any, Iterator

import pytest

from contingency_respondent_dsl import TierBExtension

ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = ROOT / "conformance" / "tier-b"
READMES = ("README.md", "README.ja.md")

# Core respondent AST: ``type`` discriminator -> required fields
# (``type`` itself omitted).
CORE_REQUIRED: dict[str, tuple[str, ...]] = {
    "PairForwardDelay": ("cs", "us", "isi", "cs_duration"),
    "PairForwardTrace": ("cs", "us", "trace_interval"),
    "PairSimultaneous": ("cs", "us"),
    "PairBackward": ("us", "cs", "isi"),
    "Extinction": ("cs",),
    "CSOnly": ("cs", "trials"),
    "USOnly": ("us", "trials"),
    "Contingency": ("p_us_given_cs", "p_us_given_no_cs"),
    "TrulyRandom": ("cs", "us"),
    "ExplicitlyUnpaired": ("cs", "us"),
    "Compound": ("cs_list",),
    "Serial": ("cs_list", "isi"),
    "ITI": ("distribution", "mean"),
    "Differential": ("cs_positive", "cs_negative"),
}

TIER_B_NAMES = frozenset(TierBExtension.build().primitive_keywords)

# One-line dict literals with a ``type`` key, as written in the README examples.
_DICT_LITERAL = re.compile(r"\{\"type\": \"[^\"]*\"[^{}]*\}")


def _typed_nodes(obj: Any, where: str) -> Iterator[tuple[str, dict[str, Any]]]:
    if isinstance(obj, dict):
        if "type" in obj:
            yield where, obj
        for key, value in obj.items():
            yield from _typed_nodes(value, f"{where}.{key}")
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            yield from _typed_nodes(value, f"{where}[{i}]")


def _fixture_nodes() -> list[tuple[str, dict[str, Any]]]:
    out: list[tuple[str, dict[str, Any]]] = []
    for path in sorted(FIXTURES_DIR.glob("*.json")):
        for case in json.loads(path.read_text(encoding="utf-8")):
            expected = case.get("expected_ast")
            if expected is None:
                continue
            out.extend(_typed_nodes(expected, f"{path.name}::{case['id']}"))
    return out


def _readme_nodes() -> list[tuple[str, dict[str, Any]]]:
    out: list[tuple[str, dict[str, Any]]] = []
    for name in READMES:
        text = (ROOT / name).read_text(encoding="utf-8")
        for match in _DICT_LITERAL.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            out.append((f"{name}:{line}", pyast.literal_eval(match.group(0))))
    return out


# conditioned-inhibition puts Pair expressions in a Serial, which Core's
# Serial (a list of stimulus references) cannot hold; that fixture needs a
# different Core expression, decided separately.
_KNOWN_SHAPE_GAPS = {"conditioned-inhibition.json::conditioned-inhibition-basic.training"}

NODES = _fixture_nodes() + _readme_nodes()


def test_nodes_were_collected() -> None:
    assert any(where.startswith("README.md") for where, _ in NODES)
    assert any(where.startswith("README.ja.md") for where, _ in NODES)
    assert any(node["type"] == "PairForwardDelay" for _, node in NODES)


@pytest.mark.parametrize(("where", "node"), NODES, ids=[w for w, _ in NODES])
def test_type_is_core_or_tier_b(where: str, node: dict[str, Any]) -> None:
    assert node["type"] in CORE_REQUIRED or node["type"] in TIER_B_NAMES, (
        f"{where}: type {node['type']!r} is neither a Core respondent type "
        f"nor a Tier B primitive"
    )


@pytest.mark.parametrize(
    ("where", "node"),
    [
        pytest.param(
            w, n,
            marks=pytest.mark.xfail(strict=True, reason="Serial holding Pair expressions"),
        ) if w in _KNOWN_SHAPE_GAPS else (w, n)
        for w, n in NODES
        if n["type"] in CORE_REQUIRED
    ],
    ids=[w for w, n in NODES if n["type"] in CORE_REQUIRED],
)
def test_core_node_has_core_required_fields(where: str, node: dict[str, Any]) -> None:
    missing = [f for f in CORE_REQUIRED[node["type"]] if f not in node]
    assert not missing, f"{where}: {node['type']} lacks Core's required {missing}"
