#!/usr/bin/env bash
# Install this repo's skills into a project's .agents folder.
#
# Usage: tools/install.sh <project-path>
#
# Safe to run whether or not <project-path>/.agents already exists. Existing files with the
# same path are overwritten by the copies in this repo, other files are left alone.
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <project-path>" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT="$1"

if [ ! -d "$PROJECT" ]; then
  echo "error: project path '$PROJECT' is not a directory" >&2
  exit 1
fi

DEST="$PROJECT/.agents"
mkdir -p "$DEST"
# The trailing /. copies the contents of agents/ into .agents/ instead of nesting agents/ inside it.
cp -r "$ROOT/agents/." "$DEST/"

echo "Installed into $DEST"
ls "$DEST/skills"
