"""contingency-respondent-dsl — Tier B Pavlovian primitive extension.

Provides respondent (Pavlovian) conditioning primitives that plug into
the contingency-dsl Core via the ``ExtensionRespondentPrimitive``
extension point. See ``spec/en/integration-with-core.md`` for the
boundary contract and ``spec/en/grammar.md`` for the Tier B productions.
"""

from __future__ import annotations

from . import ast as ast

__all__ = ["ast"]

