from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class JFunction(PacedScene):
    """#652 J関数：FとGの比で相互作用を見る（約45秒）"""

    def construct(self):
        self.show_heading("J関数")
        self.draw_j()
        self.interpret()
        self.show_formula()
        self.read(1.4)

    def draw_j(self):
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 2, 1], x_length=5.2, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.1)
        base = DashedLine(axes.c2p(0, 1), axes.c2p(3, 1), color=GREY, stroke_width=2)
        J = axes.plot(lambda r: 1 + 0.5 * (1.8 ** (-r)) - 0.2 * r * 0.1, x_range=[0.1, 2.8], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(base), Create(J), run_time=1.4)
        note = self.ja_text("J=1 が独立", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def interpret(self):
        cap = self.ja_text("J<1 は集中", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("J>1 は反発", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"J(r)=\frac{1-G(r)}{1-F(r)}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
