from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class JacobiIteration(PacedScene):
    """#250 ヤコビ反復は成分ごとの更新（約45秒）"""

    def construct(self):
        self.show_heading("ヤコビ反復")
        self.draw_guess()
        self.iterate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_guess(self):
        self.dots = VGroup()
        # guess point in plane
        self.origin = LEFT * 2.5 + DOWN * 1.2
        ax = Line(self.origin + LEFT * 0.2, self.origin + RIGHT * 5.2, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.2, self.origin + UP * 3.4, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.7)
        # true solution
        self.sol = self.origin + RIGHT * 3.2 + UP * 2.0
        self.play(FadeIn(Dot(self.sol, color=YELLOW, radius=0.1)), run_time=0.5)
        self.x = Dot(self.origin + RIGHT * 0.8 + UP * 0.6, color=BLUE, radius=0.1)
        self.play(FadeIn(self.x), run_time=0.5)
        note = self.ja_text("初期近似", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def iterate(self):
        path = [
            self.origin + RIGHT * 1.6 + UP * 1.5,
            self.origin + RIGHT * 2.5 + UP * 1.7,
            self.origin + RIGHT * 2.95 + UP * 1.9,
            self.sol,
        ]
        trail = VGroup()
        for i, p in enumerate(path):
            trail.add(Dot(p, radius=0.05, color=GREY_B))
            self.play(self.x.animate.move_to(p), FadeIn(trail[-1]), run_time=0.85)
            if i == 1:
                cap = self.ja_text("更新", font_size=24).move_to(self.note)
                self.play(Transform(self.note, cap), run_time=0.4)
        cap2 = self.ja_text("解へ収束", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
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
        eq = MathTex(r"x_i^{(k+1)}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x_i^{(k+1)}=\frac{1}{a_{ii}}\Big(b_i-\sum_{j\neq i}a_{ij}x_j^{(k)}\Big)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x_i^{(k+1)}=\frac{1}{a_{ii}}\Big(b_i-\sum_{j\neq i}a_{ij}x_j^{(k)}\Big)").scale(0.62)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.1)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
