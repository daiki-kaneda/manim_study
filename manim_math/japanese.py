"""Japanese TeX template and Text helpers.

Font selection (first match wins):

1. Environment variable ``MANIM_JAPANESE_FONT``
2. Hannari Mincho (the font used in existing scenes)
3. Other CJK fonts available via fontconfig (Noto, IPA, WenQuanYi, ...)
"""

from __future__ import annotations

import os
import subprocess
from functools import lru_cache
from typing import Any

try:
    from manim import Scene, Tex, TexTemplate, Text
except ImportError:  # pragma: no cover - allows importing helpers without manim
    Scene = object  # type: ignore[misc, assignment]
    Tex = None  # type: ignore[assignment]
    TexTemplate = None  # type: ignore[assignment]
    Text = None  # type: ignore[assignment]

PREFERRED_FONTS = (
    "HannariMincho-Regular",
    "Hannari Mincho",
    "HannariMincho",
    "Hiragino Mincho ProN",
    "YuMincho",
    "Yu Mincho",
    "Noto Serif CJK JP",
    "Noto Sans CJK JP",
    "IPAexMincho",
    "IPAMincho",
    "WenQuanYi Micro Hei",
    "Droid Sans Fallback",
)


def _fontconfig_families() -> set[str]:
    try:
        out = subprocess.check_output(
            ["fc-list", ":lang=ja", "family"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, OSError):
        try:
            out = subprocess.check_output(
                ["fc-list", "family"],
                text=True,
                stderr=subprocess.DEVNULL,
            )
        except (FileNotFoundError, subprocess.CalledProcessError, OSError):
            return set()

    families: set[str] = set()
    for line in out.splitlines():
        for part in line.split(","):
            name = part.strip()
            if name:
                families.add(name)
    return families


@lru_cache(maxsize=1)
def get_japanese_font() -> str:
    env = os.environ.get("MANIM_JAPANESE_FONT")
    if env:
        return env

    families = _fontconfig_families()
    exact = {name.lower(): name for name in families}
    for preferred in PREFERRED_FONTS:
        if preferred in families:
            return preferred
        if preferred.lower() in exact:
            return exact[preferred.lower()]

    for preferred in PREFERRED_FONTS:
        needle = preferred.lower()
        for family in families:
            if needle in family.lower() or family.lower() in needle:
                return family

    if families:
        return sorted(families)[0]
    return "sans-serif"


@lru_cache(maxsize=1)
def get_japanese_tex_template():
    if TexTemplate is None:
        raise ImportError("manim is required to build the Japanese TeX template")

    font = get_japanese_font()
    return TexTemplate(
        tex_compiler="xelatex",
        output_format=".xdv",
        documentclass=r"\documentclass[preview]{standalone}",
        preamble=rf"""
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{fontspec}}
\setmainfont{{{font}}}
""",
    )


def ja_tex(*args: Any, **kwargs: Any):
    """``Tex`` with the shared Japanese xelatex template."""
    if Tex is None:
        raise ImportError("manim is required to create Tex mobjects")
    kwargs.setdefault("tex_template", get_japanese_tex_template())
    return Tex(*args, **kwargs)


def ja_text(text: str, **kwargs: Any):
    """``Text`` using the detected Japanese font (no TeX required)."""
    if Text is None:
        raise ImportError("manim is required to create Text mobjects")
    kwargs.setdefault("font", get_japanese_font())
    return Text(text, **kwargs)


class JapaneseScene(Scene):
    """Scene base with ``ja_tex`` / ``ja_text`` for Japanese titles and mixed math.

    ``beat`` is the default linger after a visual beat. Shorts in this repo
    target roughly 60–90 seconds. Subclasses can override ``beat``.
    """

    beat = 3.0

    def ja_tex(self, *args: Any, **kwargs: Any):
        return ja_tex(*args, **kwargs)

    def ja_text(self, text: str, **kwargs: Any):
        return ja_text(text, **kwargs)

    def hold(self, beats: float = 1.0) -> None:
        self.wait(max(0.0, self.beat * beats))

    def show_heading(self, text: str, font_size: int = 42):
        """Fade in a Japanese title, then park it at the top edge."""
        title = self.ja_text(text, font_size=font_size)
        self.play(FadeIn(title), run_time=0.8)
        self.hold(0.6)
        self.play(title.animate.scale(0.55).to_edge(UP), run_time=0.45)
        return title
