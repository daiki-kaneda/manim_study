from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class VonNeumann(PacedScene):
    """#346 フォン・ノイマン：トレース内積 ⟨A,B⟩=tr(A*B)（約45秒）"""

    def construct(self):
        self.show_heading("フォン・ノイマンの内積")
        self.draw_matrices()
        self.pair()
        self.show_formula()
        self.read(1.4)

    def draw_matrices(self):
        a = Matrix([["a", "b"], ["c", "d"]], h_buff=0.85, v_buff=0.7).scale(0.85).shift(LEFT * 2.6 + UP * 0.3)
        b = Matrix([["e", "f"], ["g", "h"]], h_buff=0.85, v_buff=0.7).scale(0.85).shift(RIGHT * 1.8 + UP * 0.3)
        self.play(FadeIn(a), FadeIn(b), run_time=1.3)
        note = self.ja_text("2 つの行列", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def pair(self):
        mid = MathTex(r"\langle A,B\rangle", color=ORANGE, font_size=42).shift(DOWN * 0.5)
        cap = self.ja_text("内積にする", font_size=24).move_to(self.note)
        self.play(Write(mid), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("トレースで", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\langle A,B\rangle=\mathrm{tr}(A^{*}B)").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
