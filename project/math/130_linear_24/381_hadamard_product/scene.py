from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HadamardProduct(PacedScene):
    """#381 アダマール積：成分ごとの積（約45秒）"""

    def construct(self):
        self.show_heading("アダマール積")
        self.draw_mats()
        self.entrywise()
        self.show_formula()
        self.read(1.4)

    def draw_mats(self):
        a = Matrix([["1", "2"], ["3", "4"]], h_buff=0.8, v_buff=0.65).scale(0.85).shift(LEFT * 3.0 + UP * 0.3)
        b = Matrix([["5", "6"], ["7", "8"]], h_buff=0.8, v_buff=0.65).scale(0.85).shift(LEFT * 0.2 + UP * 0.3)
        circ = MathTex(r"\circ", font_size=40).move_to(LEFT * 1.6 + UP * 0.3)
        self.play(FadeIn(a), FadeIn(circ), FadeIn(b), run_time=1.4)
        note = self.ja_text("2 つの行列", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def entrywise(self):
        c = Matrix([["5", "12"], ["21", "32"]], h_buff=0.9, v_buff=0.65).scale(0.85).shift(RIGHT * 2.6 + UP * 0.3)
        arrow = Arrow(RIGHT * 0.9, RIGHT * 1.6, buff=0.05, color=YELLOW, stroke_width=4)
        cap = self.ja_text("成分ごと", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), FadeIn(c), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("積", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"(A\circ B)_{ij}=a_{ij}b_{ij}").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
