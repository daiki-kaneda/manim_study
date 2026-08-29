from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class DFP(PacedScene):
    """#610 DFP法：BFGSの双対的な準ニュートン更新（約45秒）"""

    def construct(self):
        self.show_heading("DFP法")
        self.draw_pair()
        self.dual()
        self.show_formula()
        self.read(1.4)

    def draw_pair(self):
        left = RoundedRectangle(width=2.6, height=1.4, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.2)
        right = RoundedRectangle(width=2.6, height=1.4, corner_radius=0.12, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        self.play(Create(left), Create(right),
                  FadeIn(MathTex(r"H_k\approx A^{-1}", font_size=28).move_to(left)),
                  FadeIn(MathTex(r"y=\nabla f_+-\nabla f", font_size=24).move_to(right)),
                  run_time=1.4)
        note = self.ja_text("逆ヘッセ近似", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def dual(self):
        cap = self.ja_text("BFGSの双対", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("セカント条件", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"H_{+}=H-\frac{Hyy^\top H}{y^\top Hy}+\frac{ss^\top}{y^\top s}").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
