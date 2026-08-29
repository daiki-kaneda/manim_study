from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class StarsAndBars(PacedScene):
    """#317 星と棒：非負整数解の個数（約45秒）"""

    def construct(self):
        self.show_heading("星と棒")
        self.draw_stars()
        self.insert_bars()
        self.show_formula()
        self.read(1.4)

    def draw_stars(self):
        self.stars = VGroup(*[
            MathTex(r"\star", font_size=40, color=YELLOW).shift(LEFT * 2.8 + RIGHT * i * 0.7 + UP * 0.5)
            for i in range(7)
        ])
        # use dots instead of star latex for reliability
        self.stars = VGroup(*[
            Dot(LEFT * 2.8 + RIGHT * i * 0.7 + UP * 0.5, color=YELLOW, radius=0.12)
            for i in range(7)
        ])
        self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in self.stars], lag_ratio=0.08), run_time=1.3)
        note = self.ja_text("n 個の星", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def insert_bars(self):
        # place bars between some stars
        bars = VGroup(*[
            Line(UP * 1.0 + LEFT * 1.05 + RIGHT * j * 1.4, DOWN * 0.05 + LEFT * 1.05 + RIGHT * j * 1.4, color=ORANGE, stroke_width=6)
            for j in range(3)
        ])
        cap = self.ja_text("棒を入れる", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(b) for b in bars], lag_ratio=0.15), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("k グループ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\#\{x_i\ge 0:\sum x_i=n\}=\binom{n+k-1}{k-1}").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
