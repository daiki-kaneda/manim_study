from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PairCorrelation(PacedScene):
    """#628 ペア相関：二点距離の相対密度（約45秒）"""

    def construct(self):
        self.show_heading("ペア相関")
        self.draw_g()
        self.interpret()
        self.show_formula()
        self.read(1.4)

    def draw_g(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2.2, 1], x_length=5.5, y_length=2.5,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.2 + UP * 0.1)
        g = axes.plot(lambda r: 1 + 0.9 * (2.5 ** (-r)) * (1 if r > 0.15 else 0), x_range=[0.15, 3.8], color=BLUE, stroke_width=3)
        base = DashedLine(axes.c2p(0, 1), axes.c2p(4, 1), color=GREY, stroke_width=2)
        self.play(Create(axes), Create(g), Create(base), run_time=1.4)
        note = self.ja_text("g(r) の形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def interpret(self):
        cap = self.ja_text("g>1 は集中", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("K の微分形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"g(r)=\frac{K'(r)}{d\,\omega_d r^{d-1}}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
