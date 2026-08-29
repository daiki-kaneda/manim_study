from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ReflectionPrinciple(PacedScene):
    """#304 反射原理：壁を越えた道を折り返す（約45秒）"""

    def construct(self):
        self.show_heading("反射原理")
        self.draw_path()
        self.reflect()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        self.axes = Axes(
            x_range=[0, 6.2, 1],
            y_range=[-1.5, 3.2, 1],
            x_length=7.5,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.15 + LEFT * 0.15)
        wall = DashedLine(self.axes.c2p(0, 1.5), self.axes.c2p(6, 1.5), color=GREY, stroke_width=3)
        pts = [0, 0.4, 0.9, 1.6, 2.2, 1.8, 2.5]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([self.axes.c2p(i, y) for i, y in enumerate(pts)])
        self.play(Create(self.axes), Create(wall), run_time=1.0)
        self.play(Create(path), run_time=1.3)
        note = self.ja_text("壁 a", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.path = path
        self.pts = pts

    def reflect(self):
        # reflect prefix until first hit above 1.5
        a = 1.5
        refl = []
        hit = False
        for i, y in enumerate(self.pts):
            if not hit and y >= a:
                hit = True
            if not hit:
                refl.append(2 * a - y)
            else:
                refl.append(y)
        rpath = VMobject(color=ORANGE, stroke_width=4)
        rpath.set_points_as_corners([self.axes.c2p(i, y) for i, y in enumerate(refl)])
        cap = self.ja_text("折り返す", font_size=24).move_to(self.note)
        self.play(Create(rpath), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("数えに使う", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"P(\max S_k\ge a)=2P(S_n\ge a)").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
