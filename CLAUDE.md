# contingency-respondent-dsl — Agent Guide

This package is a Tier B extension to [`../contingency-dsl`](../contingency-dsl/).
It provides 26 Pavlovian (respondent) conditioning procedures that register
themselves through the Core `ExtensionRespondentPrimitive` extension point,
without modifying the Core grammar.

## File access discipline

- **Read/write restricted to this package root.** Do not modify files outside
  `contingency-respondent-dsl/`. The parent `contingency-dsl/` package is
  read-only from this context.
- When this package is worked on inside an upstream monorepo, any rules
  defined at the monorepo level apply in full. This package must remain
  self-contained when distributed standalone (no upward path references).

## Design discipline (no in-file version markers)

- Do **not** write "v1", "v2", "major bump", "Core freeze", or any similar
  version-marking language in tracked files. Rely on `git tag` / `git log`
  for history; do not maintain an in-file changelog.
- Changes to Tier B primitives are allowed at any time, but must remain
  **additive** with respect to Core: no change in this package may require a
  change to Core grammar or Core semantics.
- If a proposed Tier B primitive would require Core to change, it is
  out-of-scope for this package and should be routed to Core as a separate
  proposal there.

## Privacy / persona rules (from operantkit)

- Do **not** attribute statements, recommendations, or proposals to living
  (or recently deceased) researchers. Persona agents named after real
  scientists (Lattal, Kuroda, Mizutani, Sakagami, Sawa, Tanno, Samejima,
  Hata, Matsui, Nihei, Fukuda, 黒田, 坂上, 澤, 丹野, 鮫島, 畑, 松井, 二瓶,
  福田, etc.) are fictional; do not write "Lattal suggests", "per personal
  communication", or similar attributions in tracked files.
- **APA bibliography entries are the only exception.** Cite published works
  normally (author, year, title, venue, DOI/URL).
- Scientific arguments in tracked files must be sourced to published,
  citeable work, not to persona-agent outputs.

## Environment rules

- Use `mise` to pin Python 3.11 (`.mise.toml`).
- Create virtualenvs with `mise exec -- python -m venv .venv`.
- **Never use `uv`** (`uv venv`, `uv run`, `uv add`, `uv pip install`,
  `uv sync`, `uv lock` are all prohibited by upstream policy).
- Install deps with `.venv/bin/python -m pip` once dependencies are introduced.
- Do not use direnv's `layout python` or related language layouts.

## Tracked vs. gitignored

- Refer to this package's `.gitignore` for ignored patterns.
- **Do not reference gitignored paths from tracked files.** Any planning,
  persona-review, or LLM-draft content goes under the gitignored scratch
  tree, never inline-linked from spec/docs/schema.

## CJK integrity (after any Japanese write)

After writing to `spec/ja/` or `docs/ja/`, grep for U+FFFD (`\uFFFD`,
displayed as `�`) and repair any occurrences before completing the task.
Zero tolerance.

## What this package contains at this checkpoint

- Specification (`spec/en/` + `spec/ja/` mirror), schema (`schema/`),
  conformance fixture skeletons (`conformance/tier-b/`), minimal docs
  (`docs/en/`, `docs/ja/`).
- **No parser implementation.** A Python parser and runtime registry are
  separate follow-on efforts. Do not add source code or tests in this
  checkpoint unless the user explicitly requests it.

