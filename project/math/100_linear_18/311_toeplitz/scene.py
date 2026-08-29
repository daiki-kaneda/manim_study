from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Toeplitz(PacedScene):
    """#311 トープリッツ：斜めが定数の行列（約45秒）"""

    def construct(self):
        self.show_heading("トープリッツ行列")
        self.draw_matrix()
        self.diagonals()
        self.show_formula()
        self.read(1.4)

    def draw_matrix(self):
        entries = [
            ["a_0", "a_{-1}", "a_{-2}"],
            ["a_1", "a_0", "a_{-1}"],
            ["a_2", "a_1", "a_0"],
        ]
        self.mat = Matrix(entries, h_buff=1.2, v_buff=0.75).scale(0.9).shift(LEFT * 0.8 + UP * 0.2)
        self.play(FadeIn(self.mat), run_time=1.4)
        note = self.ja_text("成分", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def diagonals(self):
        # highlight main diagonal entries visually with surrounding rects on get_entries
        ents = self.mat.get_entries()
        # indices 0,4,8 are a0
        rects = VGroup(*[SurroundingRectangle(ents[i], color=ORANGE, buff=0.08) for i in (0, 4, 8)])
        cap = self.ja_text("斜めが同じ", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(r) for r in rects], lag_ratio=0.15), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("a_{i-j} のみ", font_size=24).move_to(self.note)
        # avoid latex in ja_text - use short Japanese
        cap2 = self.ja_text("差分だけ依存", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.9)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"T_{ij}=a_{i-j}").scale(1.1)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
