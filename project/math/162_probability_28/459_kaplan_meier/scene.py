from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class KaplanMeier(PacedScene):
    """#459 カプランマイヤー：打ち切り付き生存曲線（約45秒）"""

    def construct(self):
        self.show_heading("カプランマイヤー")
        self.draw_steps()
        self.censor()
        self.show_formula()
        self.read(1.4)

    def draw_steps(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[0, 1.15, 1], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.3)
        pts = [(0, 1.0), (1.2, 1.0), (1.2, 0.85), (2.5, 0.85), (2.5, 0.65), (4.0, 0.65), (4.0, 0.45), (5.8, 0.45)]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([axes.c2p(x, y) for x, y in pts])
        self.play(Create(axes), Create(path), run_time=1.5)
        note = self.ja_text("階段の生存", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def censor(self):
        marks = VGroup(*[
            Line(self.axes.c2p(t, y - 0.08), self.axes.c2p(t, y + 0.08), color=ORANGE, stroke_width=3)
            for t, y in [(1.8, 0.85), (3.3, 0.65)]
        ])
        cap = self.ja_text("打ち切りも使う", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.15), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("積で推定", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\hat S(t)=\prod_{t_i\le t}\bigl(1-\frac{d_i}{n_i}\bigr)").scale(0.82)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
