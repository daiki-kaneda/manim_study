from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Jacobian(PacedScene):
    """#151 極座標のヤコビアンは r（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.2 + DOWN * 0.15
        self.show_heading("ヤコビアン")
        self.draw_polar()
        self.grow_cells()
        self.show_formula()
        self.read(1.4)

    def _pt(self, r, th):
        return self.origin + RIGHT * (r * np.cos(th)) + UP * (r * np.sin(th))

    def _cell(self, r0, r1, t0, t1, color=YELLOW, opacity=0.35):
        n = 8
        pts = [self._pt(r0, t0 + (t1 - t0) * i / n) for i in range(n + 1)]
        pts += [self._pt(r1, t1 - (t1 - t0) * i / n) for i in range(n + 1)]
        return Polygon(*pts, color=color, fill_opacity=opacity, stroke_width=3)

    def draw_polar(self):
        rays = VGroup()
        for k in range(8):
            th = k * PI / 4
            rays.add(Line(self.origin, self._pt(2.7, th), color=GREY, stroke_width=2))
        arcs = VGroup()
        for r in (0.9, 1.7, 2.55):
            arcs.add(Circle(radius=r, color=GREY_B, stroke_width=2).move_to(self.origin))
        self.play(LaggedStart(*[Create(r) for r in rays], lag_ratio=0.08), run_time=1.6)
        self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.18), run_time=1.5)
        self.read(0.35)

    def grow_cells(self):
        inner = self._cell(0.9, 1.7, 0.15, 0.15 + PI / 4, color=BLUE)
        note = self.ja_text("近いマス", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(inner), FadeIn(note), run_time=1.2)
        self.read(0.4)
        outer = self._cell(1.7, 2.55, 0.15, 0.15 + PI / 4, color=YELLOW)
        cap = self.ja_text("外ほど広い", font_size=24).move_to(note)
        self.play(FadeIn(outer), Transform(note, cap), run_time=1.5)
        self.read(0.5)

    def show_formula(self):
        formula = MathTex(r"dA=r\,dr\,d\theta").scale(1.05)
        formula.to_edge(DOWN, buff=0.3)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
