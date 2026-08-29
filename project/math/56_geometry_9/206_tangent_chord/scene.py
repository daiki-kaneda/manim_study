from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class TangentChord(PacedScene):
    """#206 接弦定理：接線と弦の角は円周角（約45秒）"""

    def construct(self):
        self.show_heading("接弦定理")
        self.draw_circle()
        self.mark_angles()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        self.O = LEFT * 0.6 + DOWN * 0.15
        self.R = 2.0
        self.circ = Circle(radius=self.R, color=GREY, stroke_width=3).move_to(self.O)
        # point of tangency T at rightish
        ang_t = -0.35
        self.T = self.O + self.R * np.array([np.cos(ang_t), np.sin(ang_t), 0])
        # chord from T to B
        ang_b = 2.1
        self.B = self.O + self.R * np.array([np.cos(ang_b), np.sin(ang_b), 0])
        # another point C on major arc for inscribed angle
        ang_c = 3.5
        self.C = self.O + self.R * np.array([np.cos(ang_c), np.sin(ang_c), 0])
        # tangent direction perpendicular to radius OT
        rad = self.T - self.O
        tang_dir = np.array([-rad[1], rad[0], 0])
        tang_dir = tang_dir / np.linalg.norm(tang_dir)
        self.tang = Line(self.T - 2.2 * tang_dir, self.T + 1.6 * tang_dir, color=YELLOW, stroke_width=4)
        self.chord = Line(self.T, self.B, color=BLUE, stroke_width=4)
        self.play(Create(self.circ), run_time=1.1)
        self.play(Create(self.tang), run_time=1.0)
        self.play(Create(self.chord), FadeIn(Dot(self.T, color=YELLOW, radius=0.08)), run_time=1.1)
        note = self.ja_text("接線と弦", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def mark_angles(self):
        from manim.mobject.geometry.arc import Angle

        ang1 = Angle(self.tang, self.chord, radius=0.45, color=ORANGE)
        # inscribed angle at C subtended by arc TB: angle BCT? angle TCB between CT and CB
        ct = Line(self.C, self.T, color=TEAL, stroke_width=3)
        cb = Line(self.C, self.B, color=TEAL, stroke_width=3)
        self.play(Create(ct), Create(cb), FadeIn(Dot(self.C, color=TEAL, radius=0.08)), run_time=1.3)
        ang2 = Angle(ct, cb, radius=0.4, color=ORANGE)
        cap = self.ja_text("同じ角", font_size=24).move_to(self.note)
        self.play(Create(ang1), Create(ang2), Transform(self.note, cap), run_time=1.5)
        self.read(0.45)

    def show_formula(self):
        formula = self.ja_text("接線・弦の角＝円周角", font_size=28)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
