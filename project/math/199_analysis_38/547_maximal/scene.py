from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MaximalFunction(PacedScene):
    """#547 極大関数：局所平均の上限（約45秒）"""

    def construct(self):
        self.show_heading("極大関数")
        self.draw_f()
        self.balls()
        self.show_formula()
        self.read(1.4)

    def draw_f(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[0, 2, 1], x_length=6.5, y_length=2.4, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35)
        f = axes.plot(lambda x: 0.4 + 0.8 * abs(x) / (1 + x * x) + 0.3 * (1 if abs(x) < 0.5 else 0), x_range=[-3, 3], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(f), run_time=1.4)
        note = self.ja_text("関数 f", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def balls(self):
        brackets = VGroup(
            BraceBetweenPoints(self.axes.c2p(-1.2, 0), self.axes.c2p(0.4, 0), color=ORANGE),
            BraceBetweenPoints(self.axes.c2p(-0.5, 0), self.axes.c2p(1.5, 0), color=TEAL),
        )
        cap = self.ja_text("区間平均の上限", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowFromCenter(b) for b in brackets], lag_ratio=0.2), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("弱型評価", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Mf(x)=\sup_{r>0}\frac{1}{|B_r|}\int_{B_r(x)}|f|").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
