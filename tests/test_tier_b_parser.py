"""End-to-end tests for the 5 demonstration Tier B primitives.

Each case exercises the full pipeline:

1. Dispatch ``(name, positional_args=[], keyword_args={...})`` through the
   registry → returns a Tier B AST node.
2. Serialize the AST to dict.
3. Deserialize the dict back to AST.
4. Assert AST equality (round-trip) and schema-shaped dict output.
"""

from __future__ import annotations

from contingency_respondent_dsl import (
    DEFAULT_REGISTRY,
    ast as tier_b_ast,
    from_dict,
    parse_primitive,
    to_dict,
)


def _roundtrip_equal(node: object) -> None:
    serialized = to_dict(node)
    restored = from_dict(serialized)
    assert restored == node, (
        f"round-trip failed: {type(node).__name__} → "
        f"dict={serialized!r} → restored={restored!r}"
    )
    assert isinstance(serialized, dict)
    assert serialized.get("type") == type(node).__name__


# Representative Tier A expressions are passed as dicts at the boundary;
# Core normally supplies already-evaluated objects. Using dicts keeps the
# test isolated from Core's Tier A AST schema while still validating
# the Tier B seam.
TONE_SHOCK_PAIR = {
    "type": "Pair.ForwardDelay",
    "cs": "tone", "us": "shock",
    "isi": {"value": 10, "unit": "s"},
    "cs_duration": {"value": 15, "unit": "s"},
}

EXTINCTION_TONE = {"type": "Extinction", "cs": "tone"}


# ---------------------------------------------------------------------------
# Blocking — phase-structured kwargs
# ---------------------------------------------------------------------------

COMPOUND_AX_SHOCK_PAIR = {
    "type": "Pair.ForwardDelay",
    "cs": {"type": "Compound", "elements": ["tone_a", "tone_x"]},
    "us": "shock",
    "isi": {"value": 10, "unit": "s"},
    "cs_duration": {"value": 15, "unit": "s"},
}

EXTINCTION_X = {"type": "Extinction", "cs": "tone_x"}


def test_blocking_full_roundtrip():
    node = parse_primitive(
        "Blocking",
        positional_args=[],
        keyword_args={
            "phase1": TONE_SHOCK_PAIR,
            "phase2": COMPOUND_AX_SHOCK_PAIR,
            "test": EXTINCTION_X,
            "phase1_trials": 40,
            "phase2_trials": 20,
            "test_trials": 10,
        },
    )
    assert isinstance(node, tier_b_ast.Blocking)
    assert node.phase1 == TONE_SHOCK_PAIR
    assert node.phase2 == COMPOUND_AX_SHOCK_PAIR
    assert node.test == EXTINCTION_X
    assert node.phase1_trials == 40

    serialized = to_dict(node)
    assert serialized["type"] == "Blocking"
    assert serialized["phase1"]["cs"] == "tone"
    _roundtrip_equal(node)


def test_blocking_omits_none_trials_from_serialization():
    node = parse_primitive(
        "Blocking",
        None,
        {
            "phase1": TONE_SHOCK_PAIR,
            "phase2": TONE_SHOCK_PAIR,
            "test": EXTINCTION_TONE,
        },
    )
    serialized = to_dict(node)
    assert "phase1_trials" not in serialized
    assert "phase2_trials" not in serialized
    assert "test_trials" not in serialized


def test_blocking_is_in_default_registry():
    assert "Blocking" in DEFAULT_REGISTRY

