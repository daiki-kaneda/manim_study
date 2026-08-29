from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class JacobiPreconditioner(PacedScene):
    """#562 ヤコビ前処理：対角だけで近似逆（約45秒）"""

    def construct(self):
        self.show_heading("ヤコビ前処理")
        self.draw_diag()
        self.invert()
        self.show_formula()
        self.read(1.4)

    def draw_diag(self):
        cells = VGroup()
        for i in range(4):
            for j in range(4):
                c = YELLOW if i == j else GREY
                op = 0.55 if i == j else 0.1
                sq = Square(0.55, color=c, fill_opacity=op, stroke_width=2)
                sq.shift(LEFT * 2.2 + RIGHT * j * 0.6 + UP * 1.1 + DOWN * i * 0.6)
                cells.add(sq)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.02), run_time=1.3)
        note = self.ja_text("対角だけ残す", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def invert(self):
        cap = self.ja_text("逆は成分ごと", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("安い前処理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"M=\mathrm{diag}(A),\quad M^{-1}a_{ii}=1/a_{ii}").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
