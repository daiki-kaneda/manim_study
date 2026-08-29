from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class RadicalAxis(PacedScene):
    """#242 根軸は方べきが等しい点の軌跡（約45秒）"""

    def construct(self):
        self.show_heading("根軸")
        self.draw_circles()
        self.draw_axis()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circles(self):
        self.c1 = Circle(radius=1.7, color=BLUE, stroke_width=3).move_to(LEFT * 1.6 + DOWN * 0.1)
        self.c2 = Circle(radius=1.25, color=TEAL, stroke_width=3).move_to(RIGHT * 1.5 + DOWN * 0.1)
        self.play(Create(self.c1), Create(self.c2), run_time=1.5)
        note = self.ja_text("2 円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def draw_axis(self):
        # radical axis of two circles: vertical-ish between centers
        # for circles (x+1.6)^2+y^2=1.7^2 and (x-1.5)^2+y^2=1.25^2
        # expand and subtract: line
        O1, O2 = self.c1.get_center(), self.c2.get_center()
        r1, r2 = 1.7, 1.25
        # axis: 2(O2-O1)·x = |O2|^2-|O1|^2 -r2^2 +r1^2  (in local)
        d = O2 - O1
        # point on axis closest to midpoint adjusted
        # parametric: from formula x = ( |O1|^2 - |O2|^2 - r1^2 + r2^2 ) ... use geometric
        # distance from O1 along O1O2: (d^2 + r1^2 - r2^2)/(2d)
        dist = np.linalg.norm(d)
        t = (dist ** 2 + r1 ** 2 - r2 ** 2) / (2 * dist)
        mid = O1 + (t / dist) * d
        # direction perpendicular to d
        perp = np.array([-d[1], d[0], 0]) / dist
        axis = Line(mid - 2.4 * perp, mid + 2.4 * perp, color=ORANGE, stroke_width=4)
        cap = self.ja_text("方べきが等しい", font_size=24).move_to(self.note)
        self.play(Create(axis), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        # sample point on axis with equal power dashes to both circles? show one point
        p = mid + 1.2 * perp
        self.play(FadeIn(Dot(p, color=YELLOW, radius=0.1)), run_time=0.6)
        cap2 = self.ja_text("根軸", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("方べきが等しい点の直線", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
