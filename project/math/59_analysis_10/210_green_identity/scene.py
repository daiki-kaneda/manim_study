from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class GreenIdentity(PacedScene):
    """#210 グリーン恒等式は発散の積分（約45秒）"""

    def construct(self):
        self.show_heading("グリーンの恒等式")
        self.draw_domain()
        self.show_flux()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_domain(self):
        self.domain = Ellipse(width=5.2, height=3.2, color=BLUE, stroke_width=4).shift(DOWN * 0.15)
        fill = self.domain.copy().set_fill(BLUE, opacity=0.2).set_stroke(width=0)
        self.play(Create(self.domain), FadeIn(fill), run_time=1.5)
        note = self.ja_text("領域", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def show_flux(self):
        # gradient arrows inside
        arrows = VGroup()
        for x in np.linspace(-1.6, 1.6, 4):
            for y in np.linspace(-0.8, 0.8, 3):
                p = np.array([x, y, 0]) + DOWN * 0.15
                v = 0.35 * np.array([0.6, 0.35, 0])
                arrows.add(Arrow(p, p + v, buff=0, color=YELLOW, stroke_width=3, max_tip_length_to_length_ratio=0.25))
        cap = self.ja_text("勾配", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.05), Transform(self.note, cap), run_time=1.6)
        self.read(0.3)
        # boundary normals
        normals = VGroup()
        for t in np.linspace(0, TAU, 10, endpoint=False):
            p = self.domain.point_at_angle(t)
            n = p - self.domain.get_center()
            n = 0.45 * n / np.linalg.norm(n)
            normals.add(Arrow(p, p + n, buff=0, color=ORANGE, stroke_width=3, max_tip_length_to_length_ratio=0.28))
        cap2 = self.ja_text("境界の流れ", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in normals], lag_ratio=0.06), Transform(self.note, cap2), run_time=1.6)
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
        eq = MathTex(r"\int_\Omega\nabla u\cdot\nabla v").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\int_\Omega\nabla u\cdot\nabla v=\oint_{\partial\Omega}u\partial_n v-\int_\Omega u\Delta v").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\int_\Omega\nabla u\cdot\nabla v=\oint_{\partial\Omega}u\partial_n v-\int_\Omega u\Delta v").scale(0.55)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.1)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
