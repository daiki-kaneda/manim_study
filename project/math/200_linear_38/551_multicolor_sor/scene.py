from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MulticolorSOR(PacedScene):
    """#551 多色SOR：色分けで並列緩和（約45秒）"""

    def construct(self):
        self.show_heading("多色SOR")
        self.draw_grid()
        self.colors()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_grid(self):
        cells = VGroup(*[
            Square(side_length=0.55, stroke_width=2, color=GREY).shift(LEFT * 2.2 + RIGHT * j * 0.6 + UP * 1.2 + DOWN * i * 0.6)
            for i in range(4) for j in range(4)
        ])
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.02), run_time=1.3)
        note = self.ja_text("格子点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.cells = cells

    def colors(self):
        reds = VGroup(*[self.cells[i * 4 + j].copy().set_fill(RED, 0.5).set_stroke(RED, 2) for i in range(4) for j in range(4) if (i + j) % 2 == 0])
        blacks = VGroup(*[self.cells[i * 4 + j].copy().set_fill(BLUE, 0.5).set_stroke(BLUE, 2) for i in range(4) for j in range(4) if (i + j) % 2 == 1])
        cap = self.ja_text("赤黒で分割", font_size=24).move_to(self.note)
        self.play(FadeIn(reds), FadeIn(blacks), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("同じ色は並列更新", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x^{(k+1)}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x^{(k+1)}=(1-\omega)x^{(k)}+\omega D^{-1}(b-Rx^{(k)})").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x^{(k+1)}=(1-\omega)x^{(k)}+\omega D^{-1}(b-Rx^{(k)})").scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
