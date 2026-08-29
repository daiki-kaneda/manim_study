from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CompensatedMartingale(PacedScene):
    """#555 補償マルチンゲール：N−Λ がマルチンゲール（約45秒）"""

    def construct(self):
        self.show_heading("補償マルチンゲール")
        self.draw_N()
        self.compensate()
        self.show_formula()
        self.read(1.4)

    def draw_N(self):
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 4, 1], x_length=6.2, y_length=2.5, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.4)
        pts = [axes.c2p(0, 0), axes.c2p(1, 0), axes.c2p(1, 1), axes.c2p(2.5, 1), axes.c2p(2.5, 2), axes.c2p(4, 2), axes.c2p(4, 3), axes.c2p(5, 3)]
        N = VMobject(color=BLUE, stroke_width=4).set_points_as_corners(pts)
        Lam = axes.plot(lambda t: 0.55 * t, x_range=[0, 5], color=ORANGE, stroke_width=3)
        self.play(Create(axes), Create(N), Create(Lam), run_time=1.5)
        note = self.ja_text("計数と累積強度", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compensate(self):
        cap = self.ja_text("引き算で中心化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("マルチンゲールに", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"M(t)=N(t)-\Lambda(t)").scale(0.95)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
