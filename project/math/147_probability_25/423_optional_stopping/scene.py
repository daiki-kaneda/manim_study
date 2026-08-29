from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class OptionalStopping(PacedScene):
    """#423 任意停止：マルチンゲールを止めても平均は保つ（約45秒）"""

    def construct(self):
        self.show_heading("任意停止定理")
        self.draw_path()
        self.stop()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[-0.5, 2.2, 1], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.3)
        ys = [1.0, 1.3, 0.8, 1.5, 1.1, 1.4, 1.2]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([axes.c2p(i, y) for i, y in enumerate(ys)])
        self.play(Create(axes), Create(path), run_time=1.5)
        note = self.ja_text("マルチンゲール", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes
        self.stop_pt = axes.c2p(4, 1.1)

    def stop(self):
        tau = Dot(self.stop_pt, color=RED, radius=0.12)
        vline = DashedLine(self.axes.c2p(4, -0.4), self.axes.c2p(4, 2.0), color=ORANGE, stroke_width=2)
        cap = self.ja_text("停止時刻 τ", font_size=24).move_to(self.note)
        self.play(Create(vline), FadeIn(tau), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("期待値は同じ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathbb{E}[X_{\tau}]=\mathbb{E}[X_0]").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
