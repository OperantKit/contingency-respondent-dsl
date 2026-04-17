"""Conformance runner.

Walks ``conformance/tier-b/*.json`` and, for every case that has both an
``input`` string and a concrete ``expected_ast`` dict, asserts that the
registry produces an AST whose serialized form equals the fixture's
expected AST.

Because this package does not lex the surface DSL (that is Core's job),
the fixture's ``input`` string is *not* re-parsed here; instead the
``expected_ast`` itself is used as the round-trip target:

1. ``from_dict(expected_ast)`` -> AST node
2. ``to_dict(node)`` -> serialized
3. ``serialized == expected_ast``

Cases with ``expected_ast: null`` are skipped with the fixture's own
``todo`` string as the skip reason.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from contingency_respondent_dsl import from_dict, to_dict


FIXTURES_DIR = (
    Path(__file__).resolve().parent.parent / "conformance" / "tier-b"
)


def _load_cases() -> list[tuple[str, str, dict]]:
    cases: list[tuple[str, str, dict]] = []
    for path in sorted(FIXTURES_DIR.glob("*.json")):
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, list):
            continue
        for case in data:
            cases.append((path.name, case.get("id", "<unknown>"), case))
    return cases


CASES = _load_cases()


@pytest.mark.parametrize(
    ("fixture", "case_id", "case"),
    CASES,
    ids=[f"{fname}::{cid}" for (fname, cid, _) in CASES],
)
def test_fixture_roundtrip(fixture: str, case_id: str, case: dict) -> None:
    expected = case.get("expected_ast")
    if expected is None:
        reason = case.get("todo") or "expected_ast not yet populated"
        pytest.skip(f"{fixture}::{case_id}: {reason}")

    # 1. dict -> AST
    node = from_dict(expected)
    assert node is not None, f"{fixture}::{case_id}: from_dict returned None"

    # 2. AST -> dict
    serialized = to_dict(node)

    # 3. Shape equivalence
    assert serialized == expected, (
        f"{fixture}::{case_id}: round-trip shape drifted.\n"
        f"  expected: {expected!r}\n"
        f"  got:      {serialized!r}"
    )


def test_fixture_directory_has_26_files() -> None:
    """Sanity check that the fixture set matches the 26 Tier B primitives."""
    json_files = sorted(FIXTURES_DIR.glob("*.json"))
    assert len(json_files) == 26, (
        f"expected 26 Tier B fixture files, found {len(json_files)}: "
        f"{[p.name for p in json_files]}"
    )


def test_all_fixtures_declare_required_fields() -> None:
    """Every case must have id / comment / input / expected_ast."""
    for path in sorted(FIXTURES_DIR.glob("*.json")):
        with path.open("r", encoding="utf-8") as fh:
            cases = json.load(fh)
        assert isinstance(cases, list), f"{path.name} is not a JSON array"
        for case in cases:
            for key in ("id", "comment", "input"):
                assert key in case, (
                    f"{path.name}: case missing '{key}': {case!r}"
                )
            # expected_ast is required but may be null
            assert "expected_ast" in case, (
                f"{path.name}: case missing 'expected_ast' key: {case!r}"
            )

