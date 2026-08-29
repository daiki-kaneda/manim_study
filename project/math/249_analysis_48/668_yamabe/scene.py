from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class YamabeProblem(PacedScene):
    """#668 ヤマベ問題：共形変形でスカラー曲率を定数に（約45秒）"""

    def construct(self):
        self.show_heading("ヤマベ問題")
        self.draw()
        self.conform()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        box = RoundedRectangle(width=3.8, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 0.4 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"g\mapsto u^{4/(n-2)}g", font_size=30).move_to(box)), run_time=1.4)
        note = self.ja_text("共形変形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def conform(self):
        cap = self.ja_text("スカラー曲率一定", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("山辺定数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"L_g u = \lambda u^{(n+2)/(n-2)}").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
