"""Shared helpers for Japanese math videos built with Manim."""

from manim_math.japanese import (
    JapaneseScene,
    PacedScene,
    get_japanese_font,
    get_japanese_tex_template,
    ja_tex,
    ja_text,
)
from manim_math.path_setup import add_repo_root_to_syspath

__all__ = [
    "JapaneseScene",
    "PacedScene",
    "add_repo_root_to_syspath",
    "get_japanese_font",
    "get_japanese_tex_template",
    "ja_tex",
    "ja_text",
]
