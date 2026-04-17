"""AST node classes for Tier B Pavlovian primitives.

One frozen dataclass per primitive, mirroring the schema declared in
``schema/ast.schema.json`` and the EBNF in ``spec/en/grammar.md``.

Shared reference types
----------------------

``StimulusRef`` and ``ContextRef`` are modelled as plain ``str`` (identifier
or string label). ``RespondentExpr`` is any Tier A or Tier B expression and
is modelled as ``Any`` at this boundary; Core is responsible for shaping
Tier A expressions and this package is responsible for shaping Tier B
expressions. Both surface through the same ``RespondentExpr`` slot.

``Duration`` is a small immutable record of ``(value, unit)``.
``Probability`` is a plain ``float`` in ``[0, 1]``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


StimulusRef = str
ContextRef = str
RespondentExpr = Any
Probability = float


_TIME_UNITS = frozenset({"ms", "s", "min", "h"})


@dataclass(frozen=True)
class Duration:
    """A duration literal, e.g. ``15-s`` or ``500-ms``."""

    value: float
    unit: str

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError(
                f"Duration.value must be > 0 (got {self.value})"
            )
        if self.unit not in _TIME_UNITS:
            raise ValueError(
                f"Duration.unit must be one of {sorted(_TIME_UNITS)} "
                f"(got {self.unit!r})"
            )


# ---------------------------------------------------------------------------
# §2  Acquisition and higher-order family
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class HigherOrderConditioning:
    phase1: RespondentExpr
    phase2: RespondentExpr
    phase1_trials: int | None = None
    phase2_trials: int | None = None


@dataclass(frozen=True)
class SensoryPreconditioning:
    phase1: RespondentExpr
    phase2: RespondentExpr
    test: RespondentExpr
    phase1_trials: int | None = None
    phase2_trials: int | None = None


@dataclass(frozen=True)
class Counterconditioning:
    phase1: RespondentExpr
    phase2: RespondentExpr
    phase1_trials: int | None = None
    phase2_trials: int | None = None


# ---------------------------------------------------------------------------
# §3  Cue-competition family
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Blocking:
    phase1: RespondentExpr
    phase2: RespondentExpr
    test: RespondentExpr
    phase1_trials: int | None = None
    phase2_trials: int | None = None
    test_trials: int | None = None


@dataclass(frozen=True)
class Overshadowing:
    training: RespondentExpr
    test_a: RespondentExpr
    test_b: RespondentExpr
    training_trials: int | None = None


@dataclass(frozen=True)
class Overexpectation:
    phase1_a: RespondentExpr
    phase1_b: RespondentExpr
    phase2_compound: RespondentExpr
    test: RespondentExpr
    phase1_trials: int | None = None
    phase2_trials: int | None = None


@dataclass(frozen=True)
class SuperConditioning:
    phase1_inhibitor: RespondentExpr
    phase2_target: RespondentExpr
    test: RespondentExpr


@dataclass(frozen=True)
class RetrospectiveRevaluation:
    phase1_compound: RespondentExpr
    phase2_element: RespondentExpr
    test: RespondentExpr


# ---------------------------------------------------------------------------
# §4  Inhibitory-learning family
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ConditionedInhibition:
    training: RespondentExpr
    test: RespondentExpr
    training_trials: int | None = None


OccasionSettingMode = Literal["FeaturePositive", "FeatureNegative"]


@dataclass(frozen=True)
class OccasionSetting:
    feature: StimulusRef
    target: StimulusRef
    us: StimulusRef
    mode: OccasionSettingMode
    training_trials: int | None = None

    def __post_init__(self) -> None:
        if self.mode not in ("FeaturePositive", "FeatureNegative"):
            raise ValueError(
                f"OccasionSetting.mode must be 'FeaturePositive' or "
                f"'FeatureNegative' (got {self.mode!r})"
            )


@dataclass(frozen=True)
class InhibitionOfDelay:
    cs: StimulusRef
    us: StimulusRef
    cs_duration: Duration
    isi: Duration
    training_trials: int | None = None


SummationRetardationMode = Literal["Summation", "Retardation"]


@dataclass(frozen=True)
class SummationRetardationTest:
    inhibitor: StimulusRef
    excitor: StimulusRef
    us: StimulusRef
    mode: SummationRetardationMode

    def __post_init__(self) -> None:
        if self.mode not in ("Summation", "Retardation"):
            raise ValueError(
                f"SummationRetardationTest.mode must be 'Summation' or "
                f"'Retardation' (got {self.mode!r})"
            )


# ---------------------------------------------------------------------------
# §5  Preexposure family
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class LatentInhibition:
    preexposure: RespondentExpr
    training: RespondentExpr
    test: RespondentExpr
    preexposure_trials: int | None = None
    training_trials: int | None = None


@dataclass(frozen=True)
class USPreexposure:
    preexposure: RespondentExpr
    training: RespondentExpr
    test: RespondentExpr
    preexposure_trials: int | None = None
    training_trials: int | None = None


# ---------------------------------------------------------------------------
# §6  Extinction-and-recovery family
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Renewal:
    acquisition: RespondentExpr
    extinction: RespondentExpr
    test: RespondentExpr
    acquisition_context: ContextRef
    extinction_context: ContextRef
    test_context: ContextRef


@dataclass(frozen=True)
class Reinstatement:
    acquisition: RespondentExpr
    extinction: RespondentExpr
    reinstatement_us: RespondentExpr
    test: RespondentExpr


@dataclass(frozen=True)
class SpontaneousRecovery:
    acquisition: RespondentExpr
    extinction: RespondentExpr
    retention_interval: Duration
    test: RespondentExpr


@dataclass(frozen=True)
class LatentExtinction:
    acquisition: RespondentExpr
    preexposure: RespondentExpr
    test: RespondentExpr
    preexposure_trials: int | None = None


@dataclass(frozen=True)
class PavlovianPREE:
    acquisition: RespondentExpr
    extinction: RespondentExpr
    test: RespondentExpr
    reinforcement_probability: Probability

    def __post_init__(self) -> None:
        if not (0.0 <= float(self.reinforcement_probability) <= 1.0):
            raise ValueError(
                "PavlovianPREE.reinforcement_probability must be in [0, 1] "
                f"(got {self.reinforcement_probability!r})"
            )


@dataclass(frozen=True)
class ContextualExtinction:
    acquisition: RespondentExpr
    extinction: RespondentExpr
    test: RespondentExpr
    context: ContextRef


@dataclass(frozen=True)
class ReconsolidationInterference:
    acquisition: RespondentExpr
    reactivation: RespondentExpr
    interference_window: Duration
    extinction: RespondentExpr
    test: RespondentExpr


# ---------------------------------------------------------------------------
# §7  Specialized procedures
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ConditionedTasteAversion:
    taste_cs: StimulusRef
    visceral_us: StimulusRef
    cs_duration: Duration
    delay_to_us: Duration
    training_trials: int | None = None


@dataclass(frozen=True)
class StimulusGeneralization:
    training: RespondentExpr
    test_gradient: tuple[StimulusRef, ...]
    training_trials: int | None = None
    test_trials: int | None = None

    def __post_init__(self) -> None:
        if len(self.test_gradient) < 2:
            raise ValueError(
                "StimulusGeneralization.test_gradient must have at least "
                f"2 entries (got {len(self.test_gradient)})"
            )


@dataclass(frozen=True)
class ContextualFearConditioning:
    context: ContextRef
    us: StimulusRef
    us_onset_from_entry: Duration
    training_trials: int | None = None


@dataclass(frozen=True)
class PeakProcedure:
    cs: StimulusRef
    us: StimulusRef
    fi_duration: Duration
    peak_probe_duration: Duration
    peak_probe_probability: Probability | None = None
    training_trials: int | None = None


@dataclass(frozen=True)
class MediatedConditioning:
    phase1: RespondentExpr
    phase2: RespondentExpr
    test: RespondentExpr
    phase1_trials: int | None = None
    phase2_trials: int | None = None


# ---------------------------------------------------------------------------
# Identifier set — the 26 Tier B primitives
# ---------------------------------------------------------------------------


TIER_B_PRIMITIVES: tuple[type, ...] = (
    HigherOrderConditioning,
    SensoryPreconditioning,
    Counterconditioning,
    Blocking,
    Overshadowing,
    Overexpectation,
    SuperConditioning,
    RetrospectiveRevaluation,
    ConditionedInhibition,
    OccasionSetting,
    InhibitionOfDelay,
    SummationRetardationTest,
    LatentInhibition,
    USPreexposure,
    Renewal,
    Reinstatement,
    SpontaneousRecovery,
    LatentExtinction,
    PavlovianPREE,
    ContextualExtinction,
    ReconsolidationInterference,
    ConditionedTasteAversion,
    StimulusGeneralization,
    ContextualFearConditioning,
    PeakProcedure,
    MediatedConditioning,
)
"""Tuple of the 26 Tier B AST classes in spec order (spec/en/grammar.md §2-§7)."""

