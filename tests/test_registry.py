"""Unit tests for the Tier B registry / extension dispatch."""

from __future__ import annotations

import pytest

from contingency_respondent_dsl import (
    ArityError,
    DEFAULT_REGISTRY,
    MissingFieldError,
    PRIMITIVE_REGISTRY,
    TierBExtension,
    TierBRegistry,
    UnknownFieldError,
    UnknownPrimitiveError,
    ast as tier_b_ast,
    register,
)


def test_primitive_registry_has_26_entries():
    assert len(PRIMITIVE_REGISTRY) == 26
    assert set(PRIMITIVE_REGISTRY) == {
        cls.__name__ for cls in tier_b_ast.TIER_B_PRIMITIVES
    }


def test_default_registry_keywords_match_primitive_registry():
    assert DEFAULT_REGISTRY.keywords == frozenset(PRIMITIVE_REGISTRY)


def test_unknown_primitive_raises():
    with pytest.raises(UnknownPrimitiveError):
        DEFAULT_REGISTRY.parse_primitive("NotARealThing", None, {})


def test_positional_arguments_rejected():
    with pytest.raises(ArityError):
        DEFAULT_REGISTRY.parse_primitive(
            "Blocking",
            positional_args=["oops"],
            keyword_args={"phase1": "a", "phase2": "b", "test": "c"},
        )


def test_missing_required_field_raises():
    with pytest.raises(MissingFieldError):
        DEFAULT_REGISTRY.parse_primitive(
            "Blocking", None, {"phase1": "a"},
        )


def test_unknown_keyword_raises():
    with pytest.raises(UnknownFieldError):
        DEFAULT_REGISTRY.parse_primitive(
            "Blocking",
            None,
            {
                "phase1": "a", "phase2": "b", "test": "c",
                "bogus_kwarg": 1,
            },
        )


def test_blocking_roundtrip_via_registry():
    node = DEFAULT_REGISTRY.parse_primitive(
        "Blocking",
        None,
        {
            "phase1": {"type": "Pair.ForwardDelay", "cs": "a", "us": "shock"},
            "phase2": {"type": "Pair.ForwardDelay", "cs": "a+x", "us": "shock"},
            "test": {"type": "Extinction", "cs": "x"},
            "phase1_trials": 40,
            "phase2_trials": 20,
            "test_trials": 10,
        },
    )
    assert isinstance(node, tier_b_ast.Blocking)
    assert node.phase1_trials == 40
    assert node.phase2["cs"] == "a+x"


def test_tier_b_extension_surface():
    ext = TierBExtension.build()
    assert ext.name == "respondent-tier-b"
    assert len(ext.primitive_keywords) == 26
    assert "Blocking" in ext.primitive_keywords

    node = ext.parse_primitive(
        "ConditionedInhibition", None,
        {"training": "trn", "test": "tst"},
    )
    assert isinstance(node, tier_b_ast.ConditionedInhibition)


def test_register_attaches_to_dict_like_registry():
    bag: dict = {}
    ext = register(bag)
    assert "respondent-tier-b" in bag
    assert bag["respondent-tier-b"] is ext


def test_register_falls_back_to_attribute_attachment():
    class Namespace: ...
    ns = Namespace()
    ext = register(ns)
    assert ns.tier_b is ext


def test_register_uses_register_tier_b_hook_when_present():
    captured: list = []

    class CoreLikeRegistry:
        def register_tier_b(self, ext):
            captured.append(ext)

    r = CoreLikeRegistry()
    ext = register(r)
    assert captured == [ext]


def test_duration_coercion_on_wire_shape():
    node = DEFAULT_REGISTRY.parse_primitive(
        "SpontaneousRecovery",
        None,
        {
            "acquisition": {"type": "Pair.ForwardDelay"},
            "extinction": {"type": "Extinction"},
            "retention_interval": {"value": 24, "unit": "h"},
            "test": {"type": "Extinction"},
        },
    )
    assert isinstance(node, tier_b_ast.SpontaneousRecovery)
    assert node.retention_interval == tier_b_ast.Duration(value=24, unit="h")


def test_registry_is_independent_of_tier_b_extension_instance():
    """Rebuilding an extension should not perturb the module-level registry."""
    r1 = TierBRegistry.default()
    r2 = TierBRegistry.default()
    assert r1.keywords == r2.keywords

