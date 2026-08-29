from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class IntegerPartitions(PacedScene):
    """#569 整数の分割：和の順序を無視（約45秒）"""

    def construct(self):
        self.show_heading("整数の分割")
        self.draw_parts()
        self.p_n()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_parts(self):
        parts = ["5", "4+1", "3+2", "3+1+1", "2+2+1", "2+1+1+1", "1+1+1+1+1"]
        cells = VGroup(*[MathTex(p, font_size=28).shift(UP * 1.3 + DOWN * i * 0.4 + LEFT * 0.5) for i, p in enumerate(parts)])
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.05), run_time=1.5)
        note = self.ja_text("n=5 の分割", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def p_n(self):
        cap = self.ja_text("順序は同一視", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("分割数 p(n)", font_size=24).move_to(self.note)
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
        formula = MathTex(r"p(5)=7").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
