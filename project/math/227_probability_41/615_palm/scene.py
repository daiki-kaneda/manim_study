from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PalmDistribution(PacedScene):
    """#615 パーム分布：典型点から見た条件付き法則（約45秒）"""

    def construct(self):
        self.show_heading("パーム分布")
        self.draw_points()
        self.typical()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_points(self):
        plane = NumberPlane(x_range=[-3, 3, 1], y_range=[-1.5, 1.5, 1], x_length=6.5, y_length=2.8,
                            background_line_style={"stroke_opacity": 0.25}).shift(UP * 0.1)
        import random
        random.seed(7)
        pts = VGroup(*[Dot([random.uniform(-2.8, 2.8), random.uniform(-1.1, 1.1), 0], radius=0.07, color=BLUE)
                       for _ in range(14)])
        typ = Dot(ORIGIN + UP * 0.1, radius=0.12, color=YELLOW)
        self.play(Create(plane), FadeIn(pts), FadeIn(typ), run_time=1.4)
        note = self.ja_text("典型点で見る", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def typical(self):
        ring = Circle(radius=0.9, color=ORANGE, stroke_width=3).shift(UP * 0.1)
        cap = self.ja_text("条件付き配置", font_size=24).move_to(self.note)
        self.play(Create(ring), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("スラヴィニャク", font_size=24).move_to(self.note)
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
        eq = MathTex(r"P^0(A)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"P^0(A)=\frac{1}{\lambda|B|}\mathbb{E}\sum_{x\in\Phi\cap B}1_A(\theta_x\Phi)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"P^0(A)=\frac{1}{\lambda|B|}\mathbb{E}\sum_{x\in\Phi\cap B}1_A(\theta_x\Phi)").scale(0.55)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
