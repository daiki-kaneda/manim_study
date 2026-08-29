from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CalderonZygmund(PacedScene):
    """#535 カルデロン・ジグムント：特異核の分解（約45秒）"""

    def construct(self):
        self.show_heading("カルデロン・ジグムント")
        self.draw_kernel()
        self.decompose()
        self.show_formula()
        self.read(1.4)

    def draw_kernel(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-2, 2, 1], x_length=6.5, y_length=2.8, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.2)
        # 1/x style
        left = axes.plot(lambda x: 1.2 / x, x_range=[-3, -0.35], color=BLUE, stroke_width=4)
        right = axes.plot(lambda x: 1.2 / x, x_range=[0.35, 3], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(left), Create(right), run_time=1.4)
        note = self.ja_text("特異核", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def decompose(self):
        cap = self.ja_text("良い部分と悪い部分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("Lp 有界性", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Tf(x)=\mathrm{p.v.}\int K(x-y)f(y)\,dy").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
