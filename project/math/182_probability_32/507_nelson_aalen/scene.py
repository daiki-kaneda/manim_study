from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class NelsonAalen(PacedScene):
    """#507 ネルソン・アーレン：累積ハザードのノンパラ推定（約45秒）"""

    def construct(self):
        self.show_heading("ネルソン・アーレン")
        self.draw_steps()
        self.jumps()
        self.show_formula()
        self.read(1.4)

    def draw_steps(self):
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 1.5, 1],
            x_length=6.5, y_length=2.6, tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.4)
        pts = [axes.c2p(0, 0), axes.c2p(1, 0), axes.c2p(1, 0.25), axes.c2p(2.2, 0.25),
               axes.c2p(2.2, 0.55), axes.c2p(3.5, 0.55), axes.c2p(3.5, 0.95), axes.c2p(5, 0.95)]
        path = VMobject(color=BLUE, stroke_width=4).set_points_as_corners(pts)
        self.play(Create(axes), Create(path), run_time=1.4)
        note = self.ja_text("階段過程", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def jumps(self):
        cap = self.ja_text("死亡時刻で跳ねる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("リスク集合で割る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\hat\Lambda(t)=\sum_{t_i\le t}\frac{d_i}{n_i}").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
