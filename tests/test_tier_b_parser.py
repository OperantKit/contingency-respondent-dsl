"""End-to-end tests for the 5 demonstration Tier B primitives.

Each case exercises the full pipeline:

1. Dispatch ``(name, positional_args=[], keyword_args={...})`` through the
   registry → returns a Tier B AST node.
2. Serialize the AST to dict.
3. Deserialize the dict back to AST.
4. Assert AST equality (round-trip) and schema-shaped dict output.
"""

from __future__ import annotations

import json
import pathlib

import pytest

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


# ---------------------------------------------------------------------------
# Renewal — context kwargs (ABA)
# ---------------------------------------------------------------------------


def test_renewal_aba_full_roundtrip():
    import pytest

    node = parse_primitive(
        "Renewal",
        None,
        {
            "acquisition": TONE_SHOCK_PAIR,
            "extinction": EXTINCTION_TONE,
            "test": EXTINCTION_TONE,
            "acquisition_context": "ctx_a",
            "extinction_context": "ctx_b",
            "test_context": "ctx_a",
        },
    )
    assert isinstance(node, tier_b_ast.Renewal)
    # Three ContextRef fields discriminate ABA from ABC/AAB
    assert node.acquisition_context == "ctx_a"
    assert node.extinction_context == "ctx_b"
    assert node.test_context == "ctx_a"

    serialized = to_dict(node)
    assert serialized["type"] == "Renewal"
    assert serialized["acquisition_context"] == "ctx_a"
    assert serialized["extinction_context"] == "ctx_b"
    assert serialized["test_context"] == "ctx_a"
    _roundtrip_equal(node)

    with pytest.raises(Exception):
        parse_primitive(
            "Renewal",
            None,
            {
                "acquisition": TONE_SHOCK_PAIR,
                "extinction": EXTINCTION_TONE,
                "test": EXTINCTION_TONE,
                "acquisition_context": "ctx_a",
                "extinction_context": "ctx_b",
                # missing test_context
            },
        )


# ---------------------------------------------------------------------------
# LatentInhibition — two-phase preexposure+training+test
# ---------------------------------------------------------------------------


def test_latent_inhibition_full_roundtrip():
    cs_only = {"type": "CSOnly", "cs": "tone", "trials": 80}
    node = parse_primitive(
        "LatentInhibition",
        None,
        {
            "preexposure": cs_only,
            "training": TONE_SHOCK_PAIR,
            "test": EXTINCTION_TONE,
            "preexposure_trials": 80,
            "training_trials": 40,
        },
    )
    assert isinstance(node, tier_b_ast.LatentInhibition)
    assert node.preexposure_trials == 80
    assert node.training_trials == 40

    serialized = to_dict(node)
    assert serialized["type"] == "LatentInhibition"
    assert serialized["preexposure"]["type"] == "CSOnly"
    assert serialized["preexposure"]["trials"] == 80
    _roundtrip_equal(node)


def test_latent_inhibition_trials_optional():
    node = parse_primitive(
        "LatentInhibition",
        None,
        {
            "preexposure": {"type": "CSOnly", "cs": "tone"},
            "training": TONE_SHOCK_PAIR,
            "test": EXTINCTION_TONE,
        },
    )
    assert node.preexposure_trials is None
    assert node.training_trials is None
    serialized = to_dict(node)
    assert "preexposure_trials" not in serialized
    assert "training_trials" not in serialized


# ---------------------------------------------------------------------------
# Overshadowing — compound-stimulus training with symmetric element tests
# ---------------------------------------------------------------------------


def test_overshadowing_full_roundtrip():
    compound_training = {
        "type": "Pair.ForwardDelay",
        "cs": {
            "type": "Compound",
            "elements": ["loud_tone", "dim_light"],
        },
        "us": "shock",
        "isi": {"value": 10, "unit": "s"},
        "cs_duration": {"value": 15, "unit": "s"},
    }
    node = parse_primitive(
        "Overshadowing",
        None,
        {
            "training": compound_training,
            "test_a": {"type": "Extinction", "cs": "loud_tone"},
            "test_b": {"type": "Extinction", "cs": "dim_light"},
            "training_trials": 40,
        },
    )
    assert isinstance(node, tier_b_ast.Overshadowing)
    assert node.training_trials == 40
    assert node.test_a == {"type": "Extinction", "cs": "loud_tone"}
    assert node.test_b == {"type": "Extinction", "cs": "dim_light"}

    serialized = to_dict(node)
    assert serialized["type"] == "Overshadowing"
    # Compound-typed CS preserved inside the training expression
    assert serialized["training"]["cs"]["type"] == "Compound"
    assert serialized["training"]["cs"]["elements"] == ["loud_tone", "dim_light"]
    _roundtrip_equal(node)


# ---------------------------------------------------------------------------
# Reinstatement — four-phase acq/ext/US-alone/test
# ---------------------------------------------------------------------------


def test_reinstatement_full_roundtrip():
    import pytest

    us_only = {"type": "USOnly", "us": "shock", "trials": 4}
    node = parse_primitive(
        "Reinstatement",
        None,
        {
            "acquisition": TONE_SHOCK_PAIR,
            "extinction": EXTINCTION_TONE,
            "reinstatement_us": us_only,
            "test": EXTINCTION_TONE,
        },
    )
    assert isinstance(node, tier_b_ast.Reinstatement)
    assert node.acquisition == TONE_SHOCK_PAIR
    assert node.extinction == EXTINCTION_TONE
    assert node.reinstatement_us == us_only
    assert node.test == EXTINCTION_TONE

    serialized = to_dict(node)
    assert serialized["type"] == "Reinstatement"
    # All four phase fields are required in the serialized output
    for k in ("acquisition", "extinction", "reinstatement_us", "test"):
        assert k in serialized
    _roundtrip_equal(node)

    # Missing a required phase raises
    with pytest.raises(Exception):
        parse_primitive(
            "Reinstatement",
            None,
            {
                "acquisition": TONE_SHOCK_PAIR,
                "extinction": EXTINCTION_TONE,
                "test": EXTINCTION_TONE,
                # missing reinstatement_us
            },
        )


# ---------------------------------------------------------------------------
# Remaining 21 Tier B primitives — parametrized dispatch coverage
# ---------------------------------------------------------------------------
#
# Every fixture in `conformance/tier-b/*.json` supplies an ``expected_ast``
# whose ``type`` field names a Tier B primitive. For each fixture we:
#
#   1. Strip the ``type`` key from the expected_ast dict to obtain kwargs.
#   2. Dispatch ``parse_primitive(name, positional_args=None, keyword_args=kwargs)``.
#   3. Serialize the resulting AST and assert it equals the original fixture.
#
# This exercises the full registry dispatch path for every primitive,
# complementing the dict-based round-trip coverage in ``test_conformance.py``
# (which uses ``from_dict`` / ``to_dict`` but does not go through the
# registry's ``parse_primitive`` entry point).

_FIXTURES_DIR = pathlib.Path(__file__).resolve().parent.parent / "conformance" / "tier-b"


def _load_fixture_cases() -> list[tuple[str, dict]]:
    cases: list[tuple[str, dict]] = []
    for path in sorted(_FIXTURES_DIR.glob("*.json")):
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        for case in data:
            ea = case.get("expected_ast")
            if ea is None:
                continue
            cases.append((case.get("id", path.stem), ea))
    return cases


_FIXTURE_CASES = _load_fixture_cases()


@pytest.mark.parametrize(
    ("case_id", "expected_ast"),
    _FIXTURE_CASES,
    ids=[cid for (cid, _) in _FIXTURE_CASES],
)
def test_parse_primitive_dispatch_all_26(case_id: str, expected_ast: dict) -> None:
    name = expected_ast["type"]
    kwargs = {k: v for k, v in expected_ast.items() if k != "type"}

    node = parse_primitive(name, positional_args=None, keyword_args=kwargs)
    assert type(node).__name__ == name

    # Serialization must reproduce the fixture byte-for-byte (modulo dict
    # ordering). Empty-optional fields were already stripped from the
    # fixture's expected_ast so ``to_dict`` should produce an identical
    # dict without extra keys.
    serialized = to_dict(node)
    assert serialized == expected_ast, (
        f"{case_id}: parse_primitive -> to_dict drifted.\n"
        f"  expected: {expected_ast!r}\n"
        f"  got:      {serialized!r}"
    )


def test_all_26_tier_b_primitives_covered() -> None:
    """Sanity check: the parametrized sweep exercises every registered identifier."""
    covered = {ea["type"] for _, ea in _FIXTURE_CASES}
    assert covered == set(DEFAULT_REGISTRY.keywords), (
        f"parametrized coverage gap. "
        f"missing: {set(DEFAULT_REGISTRY.keywords) - covered}, "
        f"extra: {covered - set(DEFAULT_REGISTRY.keywords)}"
    )

