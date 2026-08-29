from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Hessenberg(PacedScene):
    """#333 ヘッセンベルグ形：ほぼ三角の相似形（約45秒）"""

    def construct(self):
        self.show_heading("ヘッセンベルグ形")
        self.draw_matrix()
        self.zeros()
        self.show_formula()
        self.read(1.4)

    def draw_matrix(self):
        entries = [
            ["*", "*", "*", "*"],
            ["*", "*", "*", "*"],
            ["0", "*", "*", "*"],
            ["0", "0", "*", "*"],
        ]
        self.mat = Matrix(entries, h_buff=0.85, v_buff=0.65).scale(0.95).shift(LEFT * 0.6 + UP * 0.15)
        self.play(FadeIn(self.mat), run_time=1.4)
        note = self.ja_text("行列", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def zeros(self):
        ents = self.mat.get_entries()
        # highlight lower zeros: indices for 4x4 matrix: row2 col0=8, row3 col0=12, row3 col1=13
        zeros = VGroup(ents[8], ents[12], ents[13])
        rects = VGroup(*[SurroundingRectangle(z, color=ORANGE, buff=0.06) for z in zeros])
        cap = self.ja_text("下はほぼ 0", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(r) for r in rects], lag_ratio=0.12), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("相似で到達", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"H=Q^{*}AQ,\ h_{ij}=0\ (i>j+1)").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
