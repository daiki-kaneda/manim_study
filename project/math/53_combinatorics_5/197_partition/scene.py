from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PartitionNumbers(PacedScene):
    """#197 分割数は整数の分け方の数（約45秒）"""

    def construct(self):
        self.show_heading("分割数")
        self.draw_ferrers()
        self.count_more()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _ferrers(self, rows, color=BLUE, origin=ORIGIN):
        g = VGroup()
        for i, n in enumerate(rows):
            for j in range(n):
                sq = Square(side_length=0.38, color=color, fill_opacity=0.55, stroke_width=2)
                sq.move_to(origin + RIGHT * j * 0.42 + DOWN * i * 0.42)
                g.add(sq)
        return g

    def draw_ferrers(self):
        # partition of 5: 3+1+1
        self.diag = self._ferrers([3, 1, 1], BLUE, LEFT * 3.2 + UP * 1.2)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.5) for sq in self.diag], lag_ratio=0.06), run_time=1.6)
        lab = MathTex(r"3+1+1", font_size=32).next_to(self.diag, DOWN, buff=0.25)
        self.play(FadeIn(lab), run_time=0.5)
        note = self.ja_text("5 の分割", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note
        self.lab = lab

    def count_more(self):
        others = [
            ([5], TEAL, r"5"),
            ([4, 1], GREEN, r"4+1"),
            ([3, 2], ORANGE, r"3+2"),
            ([2, 2, 1], YELLOW, r"2+2+1"),
        ]
        shown = VGroup(self.diag, self.lab)
        for rows, col, tex in others:
            d = self._ferrers(rows, col, LEFT * 3.2 + UP * 1.2)
            lab = MathTex(tex, font_size=32).next_to(d, DOWN, buff=0.25)
            self.play(FadeOut(shown), FadeIn(d), FadeIn(lab), run_time=1.1)
            shown = VGroup(d, lab)
            self.read(0.2)
        cap = self.ja_text("全部で 7", font_size=24).move_to(self.note)
        # p(5)=7
        self.play(Transform(self.note, cap), run_time=0.7)
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
        eq = MathTex(r"p(5)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"p(5)=7").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"p(5)=7").scale(1.2)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.5)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
