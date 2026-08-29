from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class GivensRotation(PacedScene):
    """#405 ギブンス：平面回転で成分を消す（約45秒）"""

    def construct(self):
        self.show_heading("ギブンス回転")
        self.draw_plane()
        self.zero_entry()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_plane(self):
        axes = Axes(x_range=[-0.5, 2.5, 1], y_range=[-0.5, 2.5, 1], x_length=4.5, y_length=4.5,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 1.5 + UP * 0.1)
        v = Arrow(axes.c2p(0, 0), axes.c2p(1.6, 1.2), buff=0, color=BLUE, stroke_width=4)
        self.play(Create(axes), GrowArrow(v), run_time=1.3)
        note = self.ja_text("平面回転", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes
        self.v = v

    def zero_entry(self):
        v2 = Arrow(self.axes.c2p(0, 0), self.axes.c2p(2.0, 0), buff=0, color=ORANGE, stroke_width=4)
        arc = Arc(radius=1.2, start_angle=0.65, angle=-0.65, color=YELLOW).move_to(self.axes.c2p(0.6, 0.35))
        # better arc at origin
        arc = Arc(radius=1.0, start_angle=np.arctan2(1.2, 1.6), angle=-np.arctan2(1.2, 1.6),
                  arc_center=self.axes.c2p(0, 0), color=YELLOW, stroke_width=3)
        cap = self.ja_text("軸に合わせる", font_size=24).move_to(self.note)
        self.play(Create(arc), Transform(self.note, cap), run_time=1.1)
        self.play(Transform(self.v, v2), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("成分を 0 に", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"G").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"G=\begin{pmatrix}c & s \\ -s & c\end{pmatrix}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"G=\begin{pmatrix}c & s \\ -s & c\end{pmatrix}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
