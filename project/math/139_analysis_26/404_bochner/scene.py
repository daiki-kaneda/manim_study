from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class BochnerIntegral(PacedScene):
    """#404 ボホナー：Banach 値関数の積分（約45秒）"""

    def construct(self):
        self.show_heading("ボホナー積分")
        self.draw_steps()
        self.limit()
        self.show_formula()
        self.read(1.4)

    def draw_steps(self):
        axes = Axes(x_range=[0, 5.2, 1], y_range=[0, 2.2, 1], x_length=6.5, y_length=2.6,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.4)
        heights = [0.6, 1.4, 1.1, 1.8, 0.9]
        bars = VGroup(*[
            Rectangle(width=0.9, height=h * 1.1, color=BLUE, fill_opacity=0.45, stroke_width=2)
            .move_to(axes.c2p(i + 0.5, h / 2))
            for i, h in enumerate(heights)
        ])
        self.play(Create(axes), LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.1), run_time=1.5)
        note = self.ja_text("単関数", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.bars = bars

    def limit(self):
        curve = self.bars  # reuse visual as approximation
        cap = self.ja_text("近似を細かく", font_size=24).move_to(self.note)
        self.play(self.bars.animate.set_fill(opacity=0.7), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("Banach 値積分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\int f=\lim_n\int s_n").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
