from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class HyperbolaFoci(PacedScene):
    """#588 双曲線の焦点：差が一定の軌跡（約45秒）"""

    def construct(self):
        self.show_heading("双曲線の焦点")
        self.draw_hyp()
        self.foci()
        self.show_formula()
        self.read(1.4)

    def draw_hyp(self):
        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[-2.2, 2.2, 1], x_length=7.0, y_length=3.2, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.1)
        right = axes.plot(lambda x: (0.6 * ((x / 1.2) ** 2 - 1)) ** 0.5 if abs(x) >= 1.2 else 0, x_range=[1.2, 3.2], color=BLUE, stroke_width=4)
        right2 = axes.plot(lambda x: -(0.6 * ((x / 1.2) ** 2 - 1)) ** 0.5 if abs(x) >= 1.2 else 0, x_range=[1.2, 3.2], color=BLUE, stroke_width=4)
        left = axes.plot(lambda x: (0.6 * ((x / 1.2) ** 2 - 1)) ** 0.5 if abs(x) >= 1.2 else 0, x_range=[-3.2, -1.2], color=BLUE, stroke_width=4)
        left2 = axes.plot(lambda x: -(0.6 * ((x / 1.2) ** 2 - 1)) ** 0.5 if abs(x) >= 1.2 else 0, x_range=[-3.2, -1.2], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(right), Create(right2), Create(left), Create(left2), run_time=1.5)
        note = self.ja_text("双曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def foci(self):
        f1 = Dot(self.axes.c2p(1.5, 0), color=YELLOW, radius=0.1)
        f2 = Dot(self.axes.c2p(-1.5, 0), color=YELLOW, radius=0.1)
        cap = self.ja_text("2 焦点", font_size=24).move_to(self.note)
        self.play(FadeIn(f1), FadeIn(f2), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("距離の差が一定", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"||PF_1|-|PF_2||=2a").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
