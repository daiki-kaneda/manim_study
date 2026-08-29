from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GaussianElim(PacedScene):
    """#154 消去法は交点を保ったまま整える（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.5 + DOWN * 0.2
        self.show_heading("消去法")
        self.draw_lines()
        self.eliminate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _line(self, p, q, color):
        return Line(p, q, color=color, stroke_width=5)

    def draw_lines(self):
        ax = Line(self.origin + LEFT * 0.4, self.origin + RIGHT * 6.2, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.4, self.origin + UP * 3.15, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.85)
        # intersection at (2.4, 1.55) in scene coords from origin
        hit = self.origin + RIGHT * 2.55 + UP * 1.55
        self.l1 = self._line(self.origin + RIGHT * 0.3 + UP * 0.35, self.origin + RIGHT * 5.4 + UP * 2.7, BLUE)
        self.l2 = self._line(self.origin + RIGHT * 0.4 + UP * 2.55, self.origin + RIGHT * 5.1 + UP * 0.45, YELLOW)
        self.play(Create(self.l1), run_time=1.15)
        self.play(Create(self.l2), run_time=1.15)
        self.dot = Dot(hit, color=ORANGE, radius=0.09)
        self.play(FadeIn(self.dot, scale=0.4), run_time=0.55)
        note = self.ja_text("交点は同じ", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note
        self.hit = hit

    def eliminate(self):
        flat = self._line(self.origin + RIGHT * 0.25 + UP * 1.55, self.origin + RIGHT * 5.5 + UP * 1.55, YELLOW)
        cap = self.ja_text("一方を水平に", font_size=24).move_to(self.note)
        self.play(Transform(self.l2, flat), Transform(self.note, cap), run_time=1.8)
        self.read(0.4)
        drop = self._line(self.hit + DOWN * 1.55, self.hit + UP * 0.15, GREEN)
        cap2 = self.ja_text("代入する", font_size=24).move_to(self.note)
        self.play(Create(drop), Transform(self.note, cap2), run_time=1.2)
        self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"Ax").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"Ax=b \;\longrightarrow\; Ux=c").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"Ax=b \;\longrightarrow\; Ux=c").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
