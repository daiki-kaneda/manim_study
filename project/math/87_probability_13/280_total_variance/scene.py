from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class TotalVariance(PacedScene):
    """#280 全分散：条件付き分散の期待＋平均の分散（約45秒）"""

    def construct(self):
        self.show_heading("全分散の法則")
        self.draw_clusters()
        self.split()
        self.show_formula()
        self.read(1.4)

    def draw_clusters(self):
        # two clusters with different means and spreads
        c1 = VGroup(*[
            Dot(LEFT * 2.2 + UP * 0.3 + RIGHT * dx + UP * dy, color=BLUE, radius=0.08)
            for dx, dy in [(-0.3, 0.2), (0.1, -0.15), (0.25, 0.25), (-0.15, -0.25), (0.0, 0.05)]
        ])
        c2 = VGroup(*[
            Dot(RIGHT * 1.8 + UP * 0.2 + RIGHT * dx + UP * dy, color=TEAL, radius=0.08)
            for dx, dy in [(-0.4, 0.15), (0.2, -0.2), (0.35, 0.3), (-0.2, -0.3), (0.05, 0.0), (0.15, 0.2)]
        ])
        self.play(FadeIn(c1), FadeIn(c2), run_time=1.3)
        note = self.ja_text("グループごと", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.c1, self.c2 = c1, c2

    def split(self):
        # within braces
        b1 = SurroundingRectangle(self.c1, color=ORANGE, buff=0.2)
        b2 = SurroundingRectangle(self.c2, color=ORANGE, buff=0.2)
        cap = self.ja_text("中のばらつき", font_size=24).move_to(self.note)
        self.play(Create(b1), Create(b2), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        # between: line connecting centers
        m1 = self.c1.get_center()
        m2 = self.c2.get_center()
        link = DoubleArrow(m1, m2, buff=0.35, color=YELLOW, stroke_width=4)
        cap2 = self.ja_text("平均の差", font_size=24).move_to(self.note)
        self.play(Create(link), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(
            r"\mathrm{Var}X=\mathbb{E}[\mathrm{Var}(X\mid Y)]+\mathrm{Var}(\mathbb{E}[X\mid Y])"
        ).scale(0.68)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
