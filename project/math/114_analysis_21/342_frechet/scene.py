from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FrechetDerivative(PacedScene):
    """#342 フレシェ微分：線形近似のノルム誤差（約45秒）"""

    def construct(self):
        self.show_heading("フレシェ微分")
        self.draw_map()
        self.linearize()
        self.show_formula()
        self.read(1.4)

    def draw_map(self):
        self.axes = Axes(x_range=[0, 4, 1], y_range=[0, 3.2, 1], x_length=5.8, y_length=3.0,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.5 + UP * 0.15)
        f = self.axes.plot(lambda x: 0.35 * x * x + 0.4, x_range=[0.3, 3.5], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(f), run_time=1.4)
        note = self.ja_text("写像 f", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def linearize(self):
        x0 = 1.6
        y0 = 0.35 * x0 * x0 + 0.4
        # tangent slope 0.7*x0
        m = 0.7 * x0
        tang = self.axes.plot(lambda x: y0 + m * (x - x0), x_range=[0.6, 2.8], color=ORANGE, stroke_width=4)
        pt = Dot(self.axes.c2p(x0, y0), color=YELLOW, radius=0.1)
        cap = self.ja_text("線形近似", font_size=24).move_to(self.note)
        self.play(FadeIn(pt), Create(tang), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("誤差 o(h)", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\lim_{h\to 0}\frac{\|f(x+h)-f(x)-Ah\|}{\|h\|}=0").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=2.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
