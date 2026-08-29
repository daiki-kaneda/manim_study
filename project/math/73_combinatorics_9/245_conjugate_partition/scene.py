from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ConjugatePartition(PacedScene):
    """#245 共役分割は図形の転置（約45秒）"""

    def construct(self):
        self.show_heading("共役分割")
        self.draw_shape()
        self.transpose()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _ferrers(self, rows, color, origin):
        g = VGroup()
        for i, n in enumerate(rows):
            for j in range(n):
                sq = Square(side_length=0.42, color=color, fill_opacity=0.5, stroke_width=2)
                sq.move_to(origin + RIGHT * j * 0.46 + DOWN * i * 0.46)
                g.add(sq)
        return g

    def draw_shape(self):
        self.rows = [4, 2, 1]
        self.diag = self._ferrers(self.rows, BLUE, LEFT * 3.4 + UP * 1.3)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.5) for sq in self.diag], lag_ratio=0.06), run_time=1.5)
        lab = MathTex(r"4+2+1", font_size=30).next_to(self.diag, DOWN, buff=0.2)
        self.play(FadeIn(lab), run_time=0.45)
        note = self.ja_text("分割", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.lab = lab

    def transpose(self):
        # conjugate of (4,2,1) is (3,2,1,1)
        conj = [3, 2, 1, 1]
        new = self._ferrers(conj, ORANGE, RIGHT * 0.6 + UP * 1.3)
        arrow = Arrow(LEFT * 0.6 + UP * 0.4, RIGHT * 0.2 + UP * 0.4, buff=0.05, color=YELLOW, stroke_width=4)
        cap = self.ja_text("転置", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.5) for sq in new], lag_ratio=0.05), run_time=1.4)
        lab2 = MathTex(r"3+2+1+1", font_size=30).next_to(new, DOWN, buff=0.2)
        self.play(FadeIn(lab2), run_time=0.5)
        cap2 = self.ja_text("共役分割", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\lambda\mapsto\lambda'").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\lambda\mapsto\lambda'").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\lambda\mapsto\lambda'").scale(1.2)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.5)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
