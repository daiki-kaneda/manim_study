from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class QuasiNewton(PacedScene):
    """#431 準ニュートン：ヘッセを逐次近似（約45秒）"""

    def construct(self):
        self.show_heading("準ニュートン法")
        self.draw_updates()
        self.bfgs()
        self.show_formula()
        self.read(1.4)

    def draw_updates(self):
        mats = VGroup(*[
            Square(side_length=0.9, color=BLUE, stroke_width=2).shift(LEFT * 2.8 + RIGHT * i * 1.2 + UP * 0.5)
            for i in range(4)
        ])
        labs = VGroup(*[MathTex(rf"B_{k}", font_size=28).move_to(mats[i]) for i, k in enumerate([0, 1, 2, "k"])])
        self.play(LaggedStart(*[FadeIn(m) for m in mats], lag_ratio=0.1), FadeIn(labs), run_time=1.4)
        note = self.ja_text("近似ヘッセ", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bfgs(self):
        arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0.05, color=YELLOW, stroke_width=4).shift(DOWN * 0.5)
        cap = self.ja_text("勾配差で更新", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("BFGS など", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"B_{k+1}=B_k+\Delta(s_k,y_k)").scale(0.88)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
