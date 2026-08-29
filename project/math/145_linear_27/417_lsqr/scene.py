from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class LSQR(PacedScene):
    """#417 LSQR：最小二乗の Krylov 解法（約45秒）"""

    def construct(self):
        self.show_heading("LSQR")
        self.draw_residual()
        self.krylov()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_residual(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[0, 1.4, 1], x_length=6.5, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.45)
        vals = [1.2, 0.7, 0.4, 0.22, 0.12, 0.07]
        dots = VGroup(*[Dot(axes.c2p(i + 1, v), color=ORANGE, radius=0.08) for i, v in enumerate(vals)])
        path = VMobject(color=ORANGE, stroke_width=3)
        path.set_points_as_corners([d.get_center() for d in dots])
        self.play(Create(axes), Create(path), FadeIn(dots), run_time=1.5)
        note = self.ja_text("残差", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def krylov(self):
        box = RoundedRectangle(width=3.0, height=1.2, corner_radius=0.12, color=BLUE, stroke_width=3).shift(DOWN * 0.85 + LEFT * 0.3)
        lab = MathTex(r"K_k(A^{*}A,A^{*}b)", font_size=30).move_to(box)
        cap = self.ja_text("Krylov で解く", font_size=24).move_to(self.note)
        self.play(Create(box), FadeIn(lab), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("最小二乗向き", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\min\|Ax-b\|_2").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\min\|Ax-b\|_2").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\min\|Ax-b\|_2").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
