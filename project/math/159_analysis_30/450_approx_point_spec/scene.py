from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class ApproxPointSpectrum(PacedScene):
    """#450 近似点スペクトル：ほぼ固有ベクトル（約45秒）"""

    def construct(self):
        self.show_heading("近似点スペクトル")
        self.draw_action()
        self.almost_eig()
        self.show_formula()
        self.read(1.4)

    def draw_action(self):
        self.O = LEFT * 2.2 + DOWN * 0.1
        x = Arrow(self.O, self.O + RIGHT * 1.6 + UP * 0.9, buff=0, color=BLUE, stroke_width=4)
        self.play(GrowArrow(x), run_time=1.0)
        note = self.ja_text("単位ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.x = x

    def almost_eig(self):
        tip = self.x.get_end()
        almost = Arrow(self.O, tip + RIGHT * 0.15 + DOWN * 0.1, buff=0, color=ORANGE, stroke_width=4)
        gap = DoubleArrow(tip, almost.get_end(), buff=0.05, color=YELLOW, stroke_width=3)
        cap = self.ja_text("(A-λ)x が小さい", font_size=24).move_to(self.note)
        self.play(GrowArrow(almost), Transform(self.note, cap), run_time=1.3)
        self.play(GrowArrow(gap), run_time=0.7)
        self.read(0.25)
        cap2 = self.ja_text("近似固有値", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\inf_{\|x\|=1}\|(A-\lambda)x\|=0").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
