from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class LowRankApprox(PacedScene):
    """#226 低ランク近似は主方向だけ残す（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.5 + DOWN * 1.1
        self.show_heading("低ランク近似")
        self.draw_cloud()
        self.project()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_cloud(self):
        rng = np.random.default_rng(2)
        pts = []
        for _ in range(36):
            t = rng.normal(0, 1.1)
            n = rng.normal(0, 0.28)
            x, y = 1.1 * t + 0.15 * n, 0.55 * t + n
            pts.append(Dot(self._pt([x, y]), radius=0.045, color=BLUE))
        self.dots = VGroup(*pts)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in self.dots], lag_ratio=0.03), run_time=1.7)
        note = self.ja_text("データ", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def project(self):
        axis = Line(self._pt([-2.6, -1.3]), self._pt([2.6, 1.3]), color=ORANGE, stroke_width=4)
        cap = self.ja_text("主方向", font_size=24).move_to(self.note)
        self.play(Create(axis), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        # collapse dots toward axis
        new_dots = VGroup()
        for d in self.dots:
            p = d.get_center() - self.origin
            # project onto direction (2.6, 1.3)
            v = np.array([2.6, 1.3, 0])
            v = v / np.linalg.norm(v)
            proj = np.dot(p, v) * v
            new_dots.add(Dot(self.origin + proj, radius=0.045, color=TEAL))
        cap2 = self.ja_text("ランク 1 に", font_size=24).move_to(self.note)
        self.play(Transform(self.dots, new_dots), Transform(self.note, cap2), run_time=1.6)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"A_k=\sum_{i=1}^{k}\sigma_i u_i v_i^{\mathsf T}").scale(0.82)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
