from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class GaussSeidelPre(PacedScene):
    """#575 ガウス・ザイデル前処理：三角部分で近似逆（約45秒）"""

    def construct(self):
        self.show_heading("ガウス・ザイデル前処理")
        self.draw_tri()
        self.forward()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_tri(self):
        cells = VGroup()
        for i in range(4):
            for j in range(4):
                op = 0.55 if j <= i else 0.08
                c = BLUE if j <= i else GREY
                sq = Square(0.55, color=c, fill_opacity=op, stroke_width=2)
                sq.shift(LEFT * 2.2 + RIGHT * j * 0.6 + UP * 1.1 + DOWN * i * 0.6)
                cells.add(sq)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.02), run_time=1.3)
        note = self.ja_text("下三角を取る", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def forward(self):
        cap = self.ja_text("前進代入が安い", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("緩和の一形態", font_size=24).move_to(self.note)
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
        eq = MathTex(r"M").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"M=D-L").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"M=D-L").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
