from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class IncompleteCholesky(PacedScene):
    """#561 不完全コレスキー：疎な近似分解（約45秒）"""

    def construct(self):
        self.show_heading("不完全コレスキー")
        self.draw_sparse()
        self.drop()
        self.show_formula()
        self.read(1.4)

    def draw_sparse(self):
        cells = VGroup()
        for i in range(5):
            for j in range(5):
                if abs(i - j) <= 1:
                    sq = Square(0.45, color=BLUE, fill_opacity=0.5, stroke_width=2)
                else:
                    sq = Square(0.45, color=GREY, fill_opacity=0.05, stroke_width=1)
                sq.shift(LEFT * 2.4 + RIGHT * j * 0.5 + UP * 1.2 + DOWN * i * 0.5)
                cells.add(sq)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.02), run_time=1.4)
        note = self.ja_text("疎パターン", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def drop(self):
        cap = self.ja_text("小さな入口を捨てる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("前処理に使う", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A\approx \tilde L\tilde L^\top").scale(0.95)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
