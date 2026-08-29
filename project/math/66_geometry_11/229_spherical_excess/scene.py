from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class SphericalExcess(PacedScene):
    """#229 球面過剰は面積そのもの（約45秒）"""

    def construct(self):
        self.show_heading("球面過剰")
        self.draw_sphere_tri()
        self.show_excess()
        self.show_formula()
        self.read(1.4)

    def draw_sphere_tri(self):
        self.O = ORIGIN + DOWN * 0.1
        self.R = 2.15
        circ = Circle(radius=self.R, color=GREY, stroke_width=2).move_to(self.O)
        # three points on circle as "sphere triangle" silhouette
        angs = [0.3, 2.2, 4.3]
        self.pts = [self.O + self.R * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        arcs = VGroup()
        for i in range(3):
            a0, a1 = angs[i], angs[(i + 1) % 3]
            if a1 < a0:
                a1 += TAU
            arc = Arc(radius=self.R, start_angle=a0, angle=a1 - a0, arc_center=self.O, color=BLUE, stroke_width=4)
            arcs.add(arc)
        self.play(Create(circ), run_time=1.0)
        self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.15), run_time=1.5)
        self.play(LaggedStart(*[FadeIn(Dot(p, color=YELLOW, radius=0.09)) for p in self.pts], lag_ratio=0.1), run_time=0.9)
        note = self.ja_text("球面三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.3).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note
        self.arcs = arcs

    def show_excess(self):
        # fill region
        poly = Polygon(*self.pts, color=TEAL, fill_opacity=0.35, stroke_width=0)
        # Better: use the pie of arcs - approximate with polygon fan
        cap = self.ja_text("内角の和 > π", font_size=24).move_to(self.note)
        self.play(FadeIn(poly), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        # mark one large angle at a vertex with Angle
        ang = Angle(Line(self.pts[0], self.pts[2]), Line(self.pts[0], self.pts[1]), radius=0.45, color=ORANGE)
        cap2 = self.ja_text("過剰＝面積", font_size=24).move_to(self.note)
        self.play(Create(ang), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"A=(\alpha+\beta+\gamma)-\pi").scale(0.95)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
