from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Burnside(PacedScene):
    """#233 バーンサイド：軌道数は固定点の平均（約45秒）"""

    def construct(self):
        self.show_heading("バーンサイドの補題")
        self.draw_necklace()
        self.average_fixed()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_necklace(self):
        self.O = LEFT * 2.2 + UP * 0.2
        beads = VGroup()
        cols = [BLUE, RED, BLUE, YELLOW]
        for i, col in enumerate(cols):
            ang = i * TAU / 4 + PI / 4
            p = self.O + 1.15 * np.array([np.cos(ang), np.sin(ang), 0])
            beads.add(Dot(p, radius=0.22, color=col))
        ring = Circle(radius=1.15, color=GREY, stroke_width=2).move_to(self.O)
        self.play(Create(ring), LaggedStart(*[FadeIn(b, scale=0.5) for b in beads], lag_ratio=0.12), run_time=1.6)
        note = self.ja_text("色ぬり", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.beads = beads
        self.ring = ring

    def average_fixed(self):
        # rotate 90°
        cap = self.ja_text("回転でうつす", font_size=24).move_to(self.note)
        self.play(Rotate(self.beads, angle=PI / 2, about_point=self.O), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        # show fixed by identity vs only mono for 90°
        mono = VGroup(*[Dot(b.get_center(), radius=0.22, color=BLUE) for b in self.beads])
        cap2 = self.ja_text("固定点", font_size=24).move_to(self.note)
        self.play(Transform(self.beads, mono), Transform(self.note, cap2), run_time=1.3)
        self.read(0.35)
        avg = MathTex(r"\frac{1}{|G|}\sum_g \mathrm{Fix}(g)", color=YELLOW).scale(0.85)
        avg.to_edge(RIGHT, buff=0.35).shift(DOWN * 0.2)
        self.play(Write(avg), run_time=1.3)
        self.read(0.3)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\#\mathrm{orbits}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\#\mathrm{orbits}=\frac{1}{|G|}\sum_{g\in G}\mathrm{Fix}(g)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\#\mathrm{orbits}=\frac{1}{|G|}\sum_{g\in G}\mathrm{Fix}(g)").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
