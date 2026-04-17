"""Unit tests for the 26 Tier B AST dataclasses.

Each class must:

- Be constructible with all required fields by keyword.
- Be frozen (mutation raises).
- Round-trip through `dataclasses.asdict`-equivalent access.
- Expose the names listed in `TIER_B_PRIMITIVES`.
"""

from __future__ import annotations

import pytest

from contingency_respondent_dsl import ast as tier_b_ast


EXPECTED_NAMES = {
    "HigherOrderConditioning",
    "SensoryPreconditioning",
    "Counterconditioning",
    "Blocking",
    "Overshadowing",
    "Overexpectation",
    "SuperConditioning",
    "RetrospectiveRevaluation",
    "ConditionedInhibition",
    "OccasionSetting",
    "InhibitionOfDelay",
    "SummationRetardationTest",
    "LatentInhibition",
    "USPreexposure",
    "Renewal",
    "Reinstatement",
    "SpontaneousRecovery",
    "LatentExtinction",
    "PavlovianPREE",
    "ContextualExtinction",
    "ReconsolidationInterference",
    "ConditionedTasteAversion",
    "StimulusGeneralization",
    "ContextualFearConditioning",
    "PeakProcedure",
    "MediatedConditioning",
}


def test_tier_b_primitives_tuple_has_26_entries():
    assert len(tier_b_ast.TIER_B_PRIMITIVES) == 26


def test_tier_b_primitives_identifier_set_matches_spec():
    names = {cls.__name__ for cls in tier_b_ast.TIER_B_PRIMITIVES}
    assert names == EXPECTED_NAMES


def test_duration_validates_positive_value_and_known_unit():
    d = tier_b_ast.Duration(value=15.0, unit="s")
    assert d.value == 15.0
    assert d.unit == "s"
    with pytest.raises(ValueError):
        tier_b_ast.Duration(value=0, unit="s")
    with pytest.raises(ValueError):
        tier_b_ast.Duration(value=15, unit="parsec")


def test_blocking_required_fields_and_optional_trials():
    b = tier_b_ast.Blocking(
        phase1="ph1", phase2="ph2", test="t",
        phase1_trials=40, phase2_trials=20, test_trials=10,
    )
    assert b.phase1 == "ph1"
    assert b.phase1_trials == 40
    # optional fields default to None
    b2 = tier_b_ast.Blocking(phase1="a", phase2="b", test="c")
    assert b2.phase1_trials is None


def test_blocking_is_frozen():
    b = tier_b_ast.Blocking(phase1="ph1", phase2="ph2", test="t")
    with pytest.raises(Exception):
        b.phase1 = "other"  # type: ignore[misc]


def test_renewal_requires_three_context_fields():
    r = tier_b_ast.Renewal(
        acquisition="acq", extinction="ext", test="tst",
        acquisition_context="ctx_a",
        extinction_context="ctx_b",
        test_context="ctx_a",
    )
    assert r.acquisition_context == "ctx_a"
    assert r.test_context == "ctx_a"


def test_occasion_setting_rejects_bad_mode():
    with pytest.raises(ValueError):
        tier_b_ast.OccasionSetting(
            feature="f", target="t", us="u", mode="Other",  # type: ignore[arg-type]
        )


def test_summation_retardation_rejects_bad_mode():
    with pytest.raises(ValueError):
        tier_b_ast.SummationRetardationTest(
            inhibitor="i", excitor="e", us="u", mode="Nope",  # type: ignore[arg-type]
        )


def test_stimulus_generalization_requires_at_least_two_gradient_entries():
    with pytest.raises(ValueError):
        tier_b_ast.StimulusGeneralization(
            training="train", test_gradient=("only_one",),
        )


def test_pavlovian_pree_probability_range():
    with pytest.raises(ValueError):
        tier_b_ast.PavlovianPREE(
            acquisition="a", extinction="e", test="t",
            reinforcement_probability=1.5,
        )


def test_duration_bearing_primitives_accept_duration_instances():
    d15s = tier_b_ast.Duration(value=15.0, unit="s")
    d10s = tier_b_ast.Duration(value=10.0, unit="s")
    iod = tier_b_ast.InhibitionOfDelay(
        cs="tone", us="shock", cs_duration=d15s, isi=d10s,
    )
    assert iod.cs_duration is d15s


def test_all_classes_are_frozen():
    """Spot-check: every dataclass in TIER_B_PRIMITIVES is frozen."""
    for cls in tier_b_ast.TIER_B_PRIMITIVES:
        params = getattr(cls, "__dataclass_params__", None)
        assert params is not None, f"{cls.__name__} is not a dataclass"
        assert params.frozen, f"{cls.__name__} is not frozen"

