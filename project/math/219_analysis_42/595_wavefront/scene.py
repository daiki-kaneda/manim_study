from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class WavefrontSet(PacedScene):
    """#595 波動前線：特異性が向く方向（約45秒）"""

    def construct(self):
        self.show_heading("波動前線")
        self.draw_sing()
        self.direction()
        self.show_formula()
        self.read(1.4)

    def draw_sing(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[-1.5, 1.5, 1], x_length=5.5, y_length=2.6, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.5 + UP * 0.2)
        # jump discontinuity visual
        left = Line(axes.c2p(-2, -0.5), axes.c2p(0, -0.5), color=BLUE, stroke_width=4)
        right = Line(axes.c2p(0, 0.8), axes.c2p(2, 0.8), color=BLUE, stroke_width=4)
        jump = DashedLine(axes.c2p(0, -0.5), axes.c2p(0, 0.8), color=ORANGE, stroke_width=3)
        self.play(Create(axes), Create(left), Create(right), Create(jump), run_time=1.4)
        note = self.ja_text("特異性の位置", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def direction(self):
        arrow = Arrow(ORIGIN, RIGHT * 1.5 + UP * 0.8, buff=0, color=YELLOW, stroke_width=4).shift(RIGHT * 1.5 + DOWN * 0.5)
        cap = self.ja_text("余接方向も記録", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("WF(u) ⊂ T*X", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathrm{WF}(u)\subset T^*X\setminus0").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
