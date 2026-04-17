"""Identifier-dispatched parser for Tier B primitives.

This module does **not** lex or parse the surface DSL text; that job
belongs to the Core ``contingency-dsl-py`` parser. When Core encounters
a call of the form ``IdentUpper "(" ArgList? ")"`` and the identifier is
not a Tier A keyword, Core hands the already-evaluated argument bag to
Tier B via :func:`parse_primitive` below. The result is a frozen AST
dataclass instance.

See ``spec/en/integration-with-core.md`` for the full contract.
"""

from __future__ import annotations

from typing import Any, Mapping

from .registry import DEFAULT_REGISTRY, TierBRegistry


def parse_primitive(
    name: str,
    positional_args: list[Any] | tuple[Any, ...] | None = None,
    keyword_args: Mapping[str, Any] | None = None,
    *,
    registry: TierBRegistry | None = None,
) -> Any:
    """Dispatch a Tier B call to its AST constructor.

    Thin convenience wrapper over
    :meth:`TierBRegistry.parse_primitive`.  If *registry* is ``None`` the
    module-level :data:`~contingency_respondent_dsl.registry.DEFAULT_REGISTRY`
    (all 26 primitives) is used.
    """
    reg = registry or DEFAULT_REGISTRY
    return reg.parse_primitive(name, positional_args, keyword_args)

