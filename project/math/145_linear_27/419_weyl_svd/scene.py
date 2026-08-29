from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class WeylSingular(PacedScene):
    """#419 特異値のワイル不等式（約45秒）"""

    def construct(self):
        self.show_heading("特異値のワイル")
        self.draw_sigmas()
        self.perturb()
        self.show_formula()
        self.read(1.4)

    def draw_sigmas(self):
        axes = Axes(x_range=[0, 5.2, 1], y_range=[0, 1.5, 1], x_length=6.0, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.5 + LEFT * 0.2)
        vals = [1.3, 0.9, 0.55, 0.3]
        bars = VGroup(*[
            Rectangle(width=0.7, height=v * 1.5, color=BLUE, fill_opacity=0.5, stroke_width=2)
            .move_to(axes.c2p(i + 1, v * 0.75))
            for i, v in enumerate(vals)
        ])
        self.play(Create(axes), LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.1), run_time=1.4)
        note = self.ja_text("特異値", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.bars = bars

    def perturb(self):
        shifts = [0.15, -0.1, 0.08, -0.05]
        anims = [b.animate.stretch_to_fit_height(max(0.2, b.height + s)) for b, s in zip(self.bars, shifts)]
        cap = self.ja_text("摂動しても", font_size=24).move_to(self.note)
        self.play(*anims, Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("差は抑えられる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"|\sigma_i(A)-\sigma_i(B)|\le\|A-B\|").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
