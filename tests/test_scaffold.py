"""Scaffold-level smoke test.

Verifies the package imports cleanly.
"""

from __future__ import annotations


def test_package_imports():
    import contingency_respondent_dsl

    assert contingency_respondent_dsl is not None

