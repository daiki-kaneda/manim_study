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
        self.derive()
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

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\langle A,B\rangle").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\langle A,B\rangle=\mathrm{tr}(A^{*}B)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\langle A,B\rangle=\mathrm{tr}(A^{*}B)").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
