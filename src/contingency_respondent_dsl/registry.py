"""Registry: map Tier B identifiers to AST constructors.

Design
------

``spec/en/integration-with-core.md §1`` specifies the boundary contract:
Core hands off any call of the form ``IdentUpper "(" ArgList? ")"`` (where
``IdentUpper`` is not a Tier A reserved keyword) to this package. The
handoff signature in this Python reference implementation is::

    registry.parse_primitive(name, positional_args, keyword_args) -> AST node

Where ``name`` is the ``IdentUpper`` string, and ``keyword_args`` is a
``dict[str, Any]`` carrying already-evaluated argument values (nested
``RespondentExpr`` values, ``StimulusRef``/``ContextRef`` strings,
``Duration`` instances, ``int``/``float`` literals, and tuples of
stimulus refs where schemas require arrays).

Core's ``contingency_dsl.extensions.ExtensionRegistry`` targets the
``@``-prefixed annotation-extension mechanism (theory.md §4.7), not the
respondent ``ExtensionRespondentPrimitive`` point. The two extension points
share the same philosophy (orthogonal, additive, keyword-disjoint) but
have different interface shapes: annotations extend a schedule-expression
decorator layer, while respondent primitives extend a respondent-expression
head. This module therefore defines its own :class:`TierBRegistry`
data-carrying type alongside a :class:`TierBExtension` shim that preserves
interoperability with the Core naming conventions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Mapping

from . import ast as _ast
from .ast import (
    Blocking,
    ConditionedInhibition,
    ConditionedTasteAversion,
    ContextualExtinction,
    ContextualFearConditioning,
    Counterconditioning,
    HigherOrderConditioning,
    InhibitionOfDelay,
    LatentExtinction,
    LatentInhibition,
    MediatedConditioning,
    OccasionSetting,
    Overexpectation,
    Overshadowing,
    PavlovianPREE,
    PeakProcedure,
    ReconsolidationInterference,
    Reinstatement,
    Renewal,
    RetrospectiveRevaluation,
    SensoryPreconditioning,
    SpontaneousRecovery,
    StimulusGeneralization,
    SummationRetardationTest,
    SuperConditioning,
    USPreexposure,
    TIER_B_PRIMITIVES,
)


# ---------------------------------------------------------------------------
# Errors — mirror the error classes in spec/en/integration-with-core.md §5
# ---------------------------------------------------------------------------


class TierBError(Exception):
    """Base class for Tier B registry errors."""


class UnknownPrimitiveError(TierBError):
    """Identifier is not a registered Tier B primitive (``UNKNOWN_EXTENSION_PRIMITIVE``)."""


class ArityError(TierBError):
    """Positional arguments supplied where keywords are expected, or wrong count.

    Tier B primitives are keyword-only in every production in
    ``spec/en/grammar.md``. Any positional argument raises this error.
    """


class MissingFieldError(TierBError):
    """Required keyword argument was omitted (``MISSING_FIELD``)."""


class UnknownFieldError(TierBError):
    """Unknown keyword argument supplied (``UNKNOWN_FIELD``)."""


# ---------------------------------------------------------------------------
# PRIMITIVE_REGISTRY — the identifier → AST class map
# ---------------------------------------------------------------------------


PRIMITIVE_REGISTRY: Mapping[str, type] = {
    cls.__name__: cls for cls in TIER_B_PRIMITIVES
}
"""Identifier → AST class. Exactly the 26 Tier B primitives."""


# Per-primitive field promotion rules. Certain keyword arguments must be
# coerced from the wire-level shape (e.g. a ``dict`` or ``list`` arriving
# from JSON) into the dataclass field type. This is intentionally narrow:
# nested ``RespondentExpr`` fields are passed through unchanged.
_DURATION_FIELDS: dict[str, frozenset[str]] = {
    "InhibitionOfDelay": frozenset({"cs_duration", "isi"}),
    "SpontaneousRecovery": frozenset({"retention_interval"}),
    "ReconsolidationInterference": frozenset({"interference_window"}),
    "ConditionedTasteAversion": frozenset({"cs_duration", "delay_to_us"}),
    "ContextualFearConditioning": frozenset({"us_onset_from_entry"}),
    "PeakProcedure": frozenset({"fi_duration", "peak_probe_duration"}),
}

_TUPLE_FIELDS: dict[str, frozenset[str]] = {
    "StimulusGeneralization": frozenset({"test_gradient"}),
}


def _coerce_duration(value: Any) -> _ast.Duration:
    if isinstance(value, _ast.Duration):
        return value
    if isinstance(value, Mapping):
        return _ast.Duration(value=float(value["value"]), unit=str(value["unit"]))
    if isinstance(value, (tuple, list)) and len(value) == 2:
        return _ast.Duration(value=float(value[0]), unit=str(value[1]))
    raise TypeError(
        f"cannot coerce {type(value).__name__} to Duration: {value!r}"
    )


def _coerce_tuple(value: Any) -> tuple:
    if isinstance(value, tuple):
        return value
    if isinstance(value, list):
        return tuple(value)
    raise TypeError(
        f"cannot coerce {type(value).__name__} to tuple: {value!r}"
    )


def _prepare_kwargs(
    name: str, kwargs: Mapping[str, Any]
) -> dict[str, Any]:
    """Apply per-primitive wire-to-field coercions."""
    dur = _DURATION_FIELDS.get(name, frozenset())
    tup = _TUPLE_FIELDS.get(name, frozenset())
    out: dict[str, Any] = {}
    for key, val in kwargs.items():
        if key in dur:
            out[key] = _coerce_duration(val)
        elif key in tup:
            out[key] = _coerce_tuple(val)
        else:
            out[key] = val
    return out


# ---------------------------------------------------------------------------
# TierBRegistry — the public dispatcher
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TierBRegistry:
    """Dispatch table for Tier B primitives.

    Typically constructed via :func:`register` or the module-level
    :data:`DEFAULT_REGISTRY`. Immutable once built.
    """

    _dispatch: Mapping[str, Callable[..., Any]]

    @staticmethod
    def default() -> "TierBRegistry":
        """Registry pre-populated with all 26 Tier B primitives."""
        return TierBRegistry(_dispatch=dict(PRIMITIVE_REGISTRY))

    @property
    def keywords(self) -> frozenset[str]:
        """Identifier set advertised by this registry (26 Tier B names)."""
        return frozenset(self._dispatch.keys())

    def __contains__(self, name: str) -> bool:
        return name in self._dispatch

    def parse_primitive(
        self,
        name: str,
        positional_args: list[Any] | tuple[Any, ...] | None = None,
        keyword_args: Mapping[str, Any] | None = None,
    ) -> Any:
        """Dispatch a Core-handed call ``name(positional_args, **keyword_args)``.

        Raises:
            UnknownPrimitiveError: ``name`` is not a registered Tier B primitive.
            ArityError: any positional argument is supplied (Tier B is
                keyword-only in every production).
            MissingFieldError: a required keyword is absent.
            UnknownFieldError: an unexpected keyword is supplied.
        """
        if name not in self._dispatch:
            raise UnknownPrimitiveError(
                f"'{name}' is not a registered Tier B primitive. "
                f"Known: {sorted(self._dispatch)}"
            )

        positional = list(positional_args or ())
        if positional:
            raise ArityError(
                f"Tier B primitive '{name}' is keyword-only; received "
                f"{len(positional)} positional argument(s)."
            )

        kwargs = dict(keyword_args or {})
        cls = self._dispatch[name]

        coerced = _prepare_kwargs(name, kwargs)

        # Delegate field-existence/arity validation to the dataclass
        # constructor but rewrite the errors into the spec's error classes.
        field_names = {f for f in cls.__dataclass_fields__}  # type: ignore[attr-defined]
        unknown = set(coerced) - field_names
        if unknown:
            raise UnknownFieldError(
                f"unknown keyword(s) for {name}: {sorted(unknown)}"
            )
        required = {
            f
            for f, fd in cls.__dataclass_fields__.items()  # type: ignore[attr-defined]
            if fd.default is _MISSING and fd.default_factory is _MISSING  # type: ignore[misc]
        }
        missing = required - set(coerced)
        if missing:
            raise MissingFieldError(
                f"missing required keyword(s) for {name}: {sorted(missing)}"
            )

        return cls(**coerced)


# Sentinel for "no default" used with dataclass Field default detection
from dataclasses import MISSING as _MISSING  # noqa: E402


# ---------------------------------------------------------------------------
# TierBExtension — a small shim that mimics the Core ExtensionModule naming
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TierBExtension:
    """Extension handle surfacing the Tier B keyword set and dispatcher.

    The Core ``contingency_dsl.extensions.ExtensionRegistry`` is keyed on
    ``@``-prefixed annotation extensions and is not a parent class here.
    :class:`TierBExtension` mirrors the same surface (``name``, ``version``,
    keyword set advertisement, ``parse_primitive`` dispatch) so that a
    future respondent-aware Core registry can adopt it without rework.
    """

    name: str = "respondent-tier-b"
    version: str = "reference"
    _registry: TierBRegistry = None  # type: ignore[assignment]

    @staticmethod
    def build() -> "TierBExtension":
        return TierBExtension(_registry=TierBRegistry.default())

    @property
    def primitive_keywords(self) -> frozenset[str]:
        return self._registry.keywords

    def parse_primitive(
        self,
        name: str,
        positional_args: list[Any] | tuple[Any, ...] | None = None,
        keyword_args: Mapping[str, Any] | None = None,
    ) -> Any:
        return self._registry.parse_primitive(
            name, positional_args, keyword_args
        )


# ---------------------------------------------------------------------------
# register() — helper exposed to user code
# ---------------------------------------------------------------------------


def register(registry: Any) -> TierBExtension:
    """Attach a Tier B extension to *registry* and return the extension.

    *registry* is treated as a generic container object (attribute or
    dict-like). The function is intentionally permissive so it can front
    both a bare ``dict``, a Core ``ExtensionRegistry``-shaped object, or a
    plain namespace. Concrete behaviors:

    1. If *registry* exposes a ``register_tier_b(ext)`` method, call it.
    2. Else if *registry* is a mutable mapping, store the extension under
       the key ``"respondent-tier-b"``.
    3. Else set ``registry.tier_b`` to the new extension (fallback).

    In all cases the returned :class:`TierBExtension` is usable directly
    via ``ext.parse_primitive(...)``.
    """
    extension = TierBExtension.build()

    hook = getattr(registry, "register_tier_b", None)
    if callable(hook):
        hook(extension)
        return extension

    if isinstance(registry, dict):
        registry[extension.name] = extension
        return extension

    try:
        setattr(registry, "tier_b", extension)
    except (AttributeError, TypeError):
        # Fall through to simply returning the extension; callers that
        # want attachment can use ``ext = register(registry)``.
        pass
    return extension


DEFAULT_REGISTRY = TierBRegistry.default()
"""Convenience singleton holding all 26 Tier B primitive identifiers."""

