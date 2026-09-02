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

    Target length is about 30–60 seconds. Fill that with motion (longer
    ``run_time``, extra visual beats). Do not pad with long idle waits.
    ``beat`` remains for older scenes that call ``hold``.
    """

    beat = 3.0
    motion_scale = 1.0

    def ja_tex(self, *args: Any, **kwargs: Any):
        return ja_tex(*args, **kwargs)

    def ja_text(self, text: str, **kwargs: Any):
        return ja_text(text, **kwargs)

    def play(self, *args, **kwargs):
        scale = self.motion_scale
        if scale != 1.0:
            kwargs["run_time"] = kwargs.get("run_time", 1.0) * scale
        return super().play(*args, **kwargs)

    def hold(self, beats: float = 1.0) -> None:
        self.wait(max(0.0, self.beat * beats))

    def read(self, seconds: float = 0.55) -> None:
        """Brief look at the current frame, in seconds (not beats)."""
        self.wait(max(0.0, seconds))

    def show_heading(self, text: str, font_size: int = 42):
        """Fade in a Japanese title, then park it at the top edge."""
        from manim import FadeIn, UP

        title = self.ja_text(text, font_size=font_size)
        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.5)
        self.play(title.animate.scale(0.55).to_edge(UP), run_time=0.6)
        return title


class PacedScene(JapaneseScene):
    """30–60 second shorts: animations are stretched, idle waits are not."""

    motion_scale = 2.5


class LessonScene(JapaneseScene):
    """5–10 minute curriculum lesson. ``play()`` stays at 1x.

    Use this for ``curriculum_math_200`` / ``curriculum_algorithm_200``.
    Do not subclass ``PacedScene`` (that stretches motion for 30–60s shorts).
    """

    motion_scale = 1.0
    beat = 0.8

    def wipe(self, *keep):
        """Fade out every top-level mobject except ``keep``."""
        from manim import FadeOut

        keep_set = set(keep)
        victims = [m for m in list(self.mobjects) if m not in keep_set]
        if not victims:
            return
        self.play(*[FadeOut(m) for m in victims], run_time=0.45)
        for m in victims:
            self.remove(m)

    def linger(self, text: str = "", extra: float = 0.0) -> None:
        """Give time to read ``text``. Scales with length; not idle padding."""
        seconds = 1.15 + 0.08 * len(text)
        self.read(min(3.2, max(1.15, seconds)) + extra)

    def step_label(self, text: str, font_size: int = 24):
        """Park a short STEP chip at the top-left."""
        from manim import LEFT, UP, YELLOW

        label = self.ja_text(text, font_size=font_size, color=YELLOW)
        label.to_edge(UP, buff=1.02).to_edge(LEFT, buff=0.4)
        return label

    @staticmethod
    def below_chip(mob, chip, buff: float = 0.35):
        """Place ``mob`` under a left-edge chip without clipping the left side.

        ``next_to(chip, DOWN)`` centers on ``chip``. A short chip parked at the
        left edge then pushes a longer line past the left of the frame.
        Always left-align to the chip instead.
        """
        from manim import DOWN, LEFT

        mob.next_to(chip, DOWN, buff=buff)
        mob.align_to(chip, LEFT)
        return mob
