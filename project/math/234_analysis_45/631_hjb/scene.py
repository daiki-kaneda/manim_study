from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HJB(PacedScene):
    """#631 ハミルトン・ヤコビ・ベルマン：価値関数のPDE（約45秒）"""

    def construct(self):
        self.show_heading("ハミルトン・ヤコビ")
        self.draw_value()
        self.pde()
        self.show_formula()
        self.read(1.4)

    def draw_value(self):
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.4 + UP * 0.15)
        V = axes.plot(lambda x: 1.5 * (2 ** (-x)) + 0.2, x_range=[0.05, 2.9], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(V), FadeIn(MathTex(r"V(x)", font_size=28).next_to(axes, UP, buff=0.08)), run_time=1.3)
        note = self.ja_text("価値関数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def pde(self):
        cap = self.ja_text("最適性のPDE", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("粘性解", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\min_u\{\nabla V\cdot f+L\}=0").scale(0.8)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
