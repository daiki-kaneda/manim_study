from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EpsilonDelta(PacedScene):
    """#127 ε–δ：縦の幅に横の幅を合わせる（約45秒）"""

    def construct(self):
        self.show_heading("連続")
        self.draw_curve()
        self.fit_window()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 3.6, 1],
            x_length=7.2,
            y_length=3.5,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.18 + LEFT * 0.5)
        self.curve = self.axes.plot(lambda x: 0.22 * x * x + 0.55, x_range=[0.2, 3.7], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.curve), run_time=1.8)
        self.a = 2.1
        self.fa = 0.22 * self.a * self.a + 0.55
        dot = Dot(self.axes.c2p(self.a, self.fa), color=YELLOW, radius=0.08)
        self.play(FadeIn(dot), run_time=0.45)
        self.read(0.4)

    def _band(self, eps, color=ORANGE):
        y0 = self.fa - eps
        y1 = self.fa + eps
        p0 = self.axes.c2p(0.15, y0)
        p1 = self.axes.c2p(3.85, y1)
        rect = Rectangle(
            width=abs(p1[0] - p0[0]),
            height=abs(p1[1] - p0[1]),
            color=color,
            fill_opacity=0.18,
            stroke_width=2,
        )
        rect.move_to([(p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2, 0])
        return rect

    def _xwin(self, delta, color=YELLOW):
        x0, x1 = self.a - delta, self.a + delta
        p0 = self.axes.c2p(x0, 0.08)
        p1 = self.axes.c2p(x1, 0.08)
        return BraceBetweenPoints(p0, p1, direction=DOWN, color=color)

    def fit_window(self):
        band = self._band(0.55)
        note = self.ja_text("縦の幅", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(band), FadeIn(note), run_time=1.1)
        self.read(0.45)
        brace = self._xwin(0.85)
        cap = self.ja_text("横を合わせる", font_size=24).move_to(note)
        self.play(GrowFromCenter(brace), Transform(note, cap), run_time=1.2)
        self.read(0.4)
        band2 = self._band(0.28, color=YELLOW)
        brace2 = self._xwin(0.42)
        cap2 = self.ja_text("もっと狭く", font_size=24).move_to(note)
        self.play(Transform(band, band2), Transform(brace, brace2), Transform(note, cap2), run_time=1.5)
        self.read(0.5)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"|x-a|<\delta\ \Rightarrow\ |f(x)-L|<\varepsilon").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|x-a|<\delta\ \Rightarrow\ |f(x)-L|<\varepsilon").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"|x-a|<\delta\ \Rightarrow\ |f(x)-L|<\varepsilon").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.8)
