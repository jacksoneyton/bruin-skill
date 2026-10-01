#!/usr/bin/env bash
# Regenerate agents/skills/bruin-expert/references from the upstream Bruin docs and templates.
#
# Needs: git, python3. Does a shallow, sparse clone of docs/ and templates/ only (a few MB of text).
# To use an existing local clone instead of fetching: BRUIN_SRC=/path/to/bruin tools/sync.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/agents/skills/bruin-expert/references"
SRC="${BRUIN_SRC:-}"

PY=python3
command -v "$PY" >/dev/null 2>&1 || PY=python

if [ -z "$SRC" ]; then
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  git clone --depth 1 --filter=blob:none --sparse https://github.com/bruin-data/bruin.git "$TMP/bruin"
  git -C "$TMP/bruin" sparse-checkout set docs templates
  SRC="$TMP/bruin"
fi

"$PY" "$ROOT/tools/build_references.py" --src "$SRC" --out "$OUT"
echo "Done. See $OUT/SOURCE.md for the upstream commit."
