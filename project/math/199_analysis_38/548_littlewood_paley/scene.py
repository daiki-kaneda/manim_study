from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class LittlewoodPaley(PacedScene):
    """#548 リトルウッド・ペイリー：周波数帯で分解（約45秒）"""

    def construct(self):
        self.show_heading("リトルウッド・ペイリー")
        self.draw_bands()
        self.square_func()
        self.show_formula()
        self.read(1.4)

    def draw_bands(self):
        bands = VGroup(*[
            Rectangle(width=0.7 + i * 0.35, height=1.8, color=c, stroke_width=2, fill_opacity=0.25)
            .shift(LEFT * 2.8 + RIGHT * i * 1.2 + UP * 0.2)
            for i, c in enumerate([BLUE, TEAL, ORANGE, YELLOW, GREEN])
        ])
        self.play(LaggedStart(*[FadeIn(b) for b in bands], lag_ratio=0.1), run_time=1.4)
        note = self.ja_text("周波数ダイアド", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def square_func(self):
        cap = self.ja_text("二乗関数で測る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("Lp 同値ノルム", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"S(f)=\Big(\sum_k|\Delta_k f|^2\Big)^{1/2}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
