"""AST ↔ dict serializer for Tier B primitives.

The dict shape matches ``schema/ast.schema.json``: every AST node becomes
``{"type": "<ClassName>", ...fields...}`` and ``None``-valued optional
fields are omitted from the output (keeps fixtures minimal and matches the
schema's ``required`` / ``additionalProperties: false`` contract).

Nested ``RespondentExpr`` fields are:

- Passed through as-is if they are already ``dict``/primitive.
- Serialized recursively if they are Tier B AST nodes.
- Wrapped in ``{"type": "External", "repr": repr(obj)}`` as a *last* resort
  for unknown objects (e.g. future Tier A nodes handed in by Core before a
  cross-package serializer exists). This keeps round-trip hygiene at the
  Tier B boundary without constraining what Core may pass.
"""

from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, Mapping

from . import ast as _ast
from .ast import Duration, TIER_B_PRIMITIVES


_PRIMITIVE_TYPES: dict[str, type] = {cls.__name__: cls for cls in TIER_B_PRIMITIVES}


def to_dict(node: Any) -> Any:
    """Serialize a Tier B AST node (or nested ``RespondentExpr``) to dict.

    Primitive Python values (``str``, ``int``, ``float``, ``bool``, ``None``)
    are returned unchanged so this function composes cleanly with itself
    when traversing nested respondent expressions.
    """
    if node is None or isinstance(node, (str, int, float, bool)):
        return node

    if isinstance(node, Duration):
        return {"value": node.value, "unit": node.unit}

    if isinstance(node, (tuple, list)):
        return [to_dict(x) for x in node]

    if isinstance(node, Mapping):
        return {k: to_dict(v) for k, v in node.items()}

    if type(node).__name__ in _PRIMITIVE_TYPES:
        out: dict[str, Any] = {"type": type(node).__name__}
        for f in fields(node):  # type: ignore[arg-type]
            val = getattr(node, f.name)
            if val is None:
                continue
            out[f.name] = to_dict(val)
        return out

    if is_dataclass(node):
        # Unknown dataclass — best-effort serialization with class name.
        out = {"type": type(node).__name__}
        for f in fields(node):
            val = getattr(node, f.name)
            if val is None:
                continue
            out[f.name] = to_dict(val)
        return out

    # Unknown object — wrap rather than raise, so round-tripping a mixed
    # Tier A / Tier B AST does not fail at the Tier B seam.
    return {"type": "External", "repr": repr(node)}


def from_dict(data: Any) -> Any:
    """Reverse of :func:`to_dict` for Tier B nodes.

    Non-Tier-B dicts (or dicts lacking a recognized ``type``) are returned
    unchanged; this matches the serializer's treatment of external /
    Tier A expressions as opaque.
    """
    if data is None or isinstance(data, (str, int, float, bool)):
        return data

    if isinstance(data, list):
        return [from_dict(x) for x in data]

    if isinstance(data, Mapping):
        t = data.get("type")
        if t in _PRIMITIVE_TYPES:
            cls = _PRIMITIVE_TYPES[t]
            kwargs: dict[str, Any] = {}
            declared = {f.name for f in fields(cls)}  # type: ignore[arg-type]
            for key, val in data.items():
                if key == "type":
                    continue
                if key not in declared:
                    continue
                # Per-field reconstruction
                if _is_duration_field(cls, key):
                    kwargs[key] = _duration_from_dict(val)
                elif _is_tuple_field(cls, key):
                    kwargs[key] = tuple(val)
                else:
                    kwargs[key] = from_dict(val)
            return cls(**kwargs)
        # Unknown dict — keep opaque (may be a Tier A expression that Core
        # will reconstruct elsewhere) but still recurse into values.
        return {k: from_dict(v) for k, v in data.items()}

    return data


def _is_duration_field(cls: type, field_name: str) -> bool:
    from .registry import _DURATION_FIELDS  # lazy to avoid cycle

    return field_name in _DURATION_FIELDS.get(cls.__name__, frozenset())


def _is_tuple_field(cls: type, field_name: str) -> bool:
    from .registry import _TUPLE_FIELDS  # lazy to avoid cycle

    return field_name in _TUPLE_FIELDS.get(cls.__name__, frozenset())


def _duration_from_dict(value: Any) -> Duration:
    if isinstance(value, Duration):
        return value
    if isinstance(value, Mapping):
        return Duration(value=float(value["value"]), unit=str(value["unit"]))
    raise TypeError(
        f"cannot reconstruct Duration from {type(value).__name__}: {value!r}"
    )

