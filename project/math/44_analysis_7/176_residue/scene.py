from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Residue(PacedScene):
    """#176 留数は囲む点の係数（約45秒）"""

    def construct(self):
        self.origin = LEFT * 1.9 + DOWN * 0.1
        self.show_heading("留数")
        self.draw_plane()
        self.loop_around()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_plane(self):
        ax = Line(self.origin + LEFT * 2.6, self.origin + RIGHT * 3.5, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.2, self.origin + UP * 2.25, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.pole = Dot(self.origin + RIGHT * 0.85 + UP * 0.55, color=ORANGE, radius=0.1)
        lab = MathTex(r"z_0", color=ORANGE, font_size=30).next_to(self.pole, UR, buff=0.08)
        self.play(FadeIn(self.pole, scale=0.4), FadeIn(lab), run_time=0.9)
        note = self.ja_text("極", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def loop_around(self):
        c = self.pole.get_center()
        loop = Circle(radius=1.15, color=YELLOW, stroke_width=5).move_to(c)
        cap = self.ja_text("一周", font_size=24).move_to(self.note)
        self.play(Create(loop), Transform(self.note, cap), run_time=1.8)
        self.read(0.3)
        dot = Dot(c + RIGHT * 1.15, color=TEAL, radius=0.08)
        self.play(FadeIn(dot), run_time=0.35)
        self.play(MoveAlongPath(dot, loop), run_time=2.2)
        cap2 = self.ja_text("係数が残る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\oint f").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\oint f=\ 2\pi i\sum\mathrm{Res}(f;z_k)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\oint f=\ 2\pi i\sum\mathrm{Res}(f;z_k)").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
