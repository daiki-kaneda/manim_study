"""Make `import manim_math` work when Manim is launched from a scene file."""

from __future__ import annotations

import sys
from pathlib import Path


def add_repo_root_to_syspath(start: Path | None = None) -> Path:
    """Insert the repository root (the directory that contains `manim_math/`) onto sys.path."""
    current = (start or Path(__file__)).resolve()
    if current.is_file():
        current = current.parent
    for parent in [current, *current.parents]:
        if (parent / "manim_math" / "__init__.py").is_file():
            root = str(parent)
            if root not in sys.path:
                sys.path.insert(0, root)
            return parent
    raise RuntimeError("Could not locate the repository root containing manim_math/")
