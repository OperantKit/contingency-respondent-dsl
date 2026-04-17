"""contingency-respondent-dsl — Tier B Pavlovian primitive extension.

Provides respondent (Pavlovian) conditioning primitives that plug into
the contingency-dsl Core via the ``ExtensionRespondentPrimitive``
extension point. See ``spec/en/integration-with-core.md`` for the
boundary contract and ``spec/en/grammar.md`` for the Tier B productions.

The expected call shape from a Core-integrated parser is::

    registry.parse_primitive(
        name="Blocking",
        positional_args=[],
        keyword_args={"phase1": <expr>, "phase2": <expr>, "test": <expr>},
    )

which returns a :class:`~contingency_respondent_dsl.ast.Blocking` node.
"""

from __future__ import annotations

from . import ast as ast
from .parser import parse_primitive
from .registry import (
    ArityError,
    DEFAULT_REGISTRY,
    MissingFieldError,
    PRIMITIVE_REGISTRY,
    TierBExtension,
    TierBRegistry,
    UnknownFieldError,
    UnknownPrimitiveError,
    register,
)
from .serializer import from_dict, to_dict

__all__ = [
    "ast",
    "parse_primitive",
    "ArityError",
    "DEFAULT_REGISTRY",
    "MissingFieldError",
    "PRIMITIVE_REGISTRY",
    "TierBExtension",
    "TierBRegistry",
    "UnknownFieldError",
    "UnknownPrimitiveError",
    "register",
    "from_dict",
    "to_dict",
]

