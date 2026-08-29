from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SingularValueThresholding(PacedScene):
    """#467 特異値縮小：ソフト閾値を σ に（約45秒）"""

    def construct(self):
        self.show_heading("特異値縮小")
        self.draw_sigmas()
        self.threshold()
        self.show_formula()
        self.read(1.4)

    def draw_sigmas(self):
        axes = Axes(x_range=[0, 5.2, 1], y_range=[0, 1.5, 1], x_length=6.0, y_length=2.5,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.45)
        vals = [1.3, 0.95, 0.55, 0.25, 0.1]
        self.bars = VGroup(*[
            Rectangle(width=0.7, height=v * 1.5, color=BLUE, fill_opacity=0.5, stroke_width=2)
            .move_to(axes.c2p(i + 1, v * 0.75))
            for i, v in enumerate(vals)
        ])
        self.play(Create(axes), LaggedStart(*[FadeIn(b) for b in self.bars], lag_ratio=0.1), run_time=1.4)
        note = self.ja_text("特異値", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.vals = vals
        self.axes = axes

    def threshold(self):
        # shrink bars
        new_h = [max(0.05, (v - 0.3) * 1.5) for v in self.vals]
        anims = [b.animate.stretch_to_fit_height(h).move_to(self.axes.c2p(i + 1, h / 2)) for i, (b, h) in enumerate(zip(self.bars, new_h))]
        cap = self.ja_text("一斉に縮める", font_size=24).move_to(self.note)
        self.play(*anims, Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("低ランクへ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathcal{D}_\lambda(A)=U\,S_\lambda(\Sigma)\,V^{*}").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
