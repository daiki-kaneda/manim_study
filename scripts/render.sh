#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="$ROOT${PYTHONPATH:+:$PYTHONPATH}"
cd "$ROOT"

if [[ $# -eq 0 ]]; then
  echo "Usage: $0 <scene-file> <SceneName> [manim args...]" >&2
  echo "Example: $0 project/math/01_proofs_without_words/02_triangle_area/scene.py TriangleArea -pql" >&2
  exit 1
fi

exec manim "$@"
