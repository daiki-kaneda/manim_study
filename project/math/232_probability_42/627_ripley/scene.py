from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class RipleyK(PacedScene):
    """#627 リプリーのK：点過程の空間集中を測る（約45秒）"""

    def construct(self):
        self.show_heading("リプリーのK")
        self.draw_points()
        self.count()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_points(self):
        import random
        random.seed(3)
        plane = NumberPlane(x_range=[-3, 3, 1], y_range=[-1.5, 1.5, 1], x_length=6.5, y_length=2.8,
                            background_line_style={"stroke_opacity": 0.2}).shift(UP * 0.1)
        pts = VGroup(*[Dot([random.uniform(-2.7, 2.7), random.uniform(-1.1, 1.1), 0], radius=0.07, color=BLUE)
                       for _ in range(18)])
        center = Dot(ORIGIN + UP * 0.1, color=YELLOW, radius=0.11)
        ring = Circle(radius=1.0, color=ORANGE, stroke_width=3).move_to(center)
        self.play(Create(plane), FadeIn(pts), FadeIn(center), Create(ring), run_time=1.4)
        note = self.ja_text("半径 r の円", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def count(self):
        cap = self.ja_text("近傍点を数える", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("CSR なら πr²", font_size=24).move_to(self.note)
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
        eq = MathTex(r"K(r)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"K(r)=\lambda^{-1}\mathbb{E}^0 N(B(0,r)\setminus\{0\})").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"K(r)=\lambda^{-1}\mathbb{E}^0 N(B(0,r)\setminus\{0\})").scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
