from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class RankOneUpdate(PacedScene):
    """#213 ランク1更新は一方向の外積（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.8 + DOWN * 1.2
        self.show_heading("ランク 1 更新")
        self.draw_grid()
        self.apply_update()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_grid(self):
        # unit square grid
        lines = VGroup()
        for i in range(5):
            lines.add(Line(self._pt([0, i * 0.55]), self._pt([2.2, i * 0.55]), color=GREY, stroke_width=2))
            lines.add(Line(self._pt([i * 0.55, 0]), self._pt([i * 0.55, 2.2]), color=GREY, stroke_width=2))
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.04), run_time=1.4)
        note = self.ja_text("格子", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.lines = lines

    def apply_update(self):
        # shear/stretch in direction u
        u = np.array([1.0, 0.55])
        u = u / np.linalg.norm(u)
        arr = Arrow(self.origin, self._pt(2.4 * u), buff=0, color=ORANGE, stroke_width=5)
        cap = self.ja_text("方向 u", font_size=24).move_to(self.note)
        self.play(GrowArrow(arr), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        # new grid sheared
        new = VGroup()
        for i in range(5):
            # horizontal lines get shifted along u proportional to y
            y = i * 0.55
            shift = 0.85 * y * u
            new.add(Line(self._pt(shift), self._pt(np.array([2.2, 0]) + shift), color=BLUE, stroke_width=2))
            x = i * 0.55
            p0 = np.array([x, 0.0])
            p1 = np.array([x, 2.2]) + 0.85 * 2.2 * u * 0  # verticals: x fixed then add uv^T
            # A = I + u v^T with v = (0.85, 0) roughly → stretch x
            p0s = p0 + 0.9 * p0[0] * u
            p1s = p1 + 0.9 * p1[0] * u
            new.add(Line(self._pt(p0s), self._pt(p1s), color=BLUE, stroke_width=2))
        cap2 = self.ja_text("一方向だけ", font_size=24).move_to(self.note)
        self.play(Transform(self.lines, new), Transform(self.note, cap2), run_time=1.7)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"A+uv^{\mathsf T}").scale(1.15)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
