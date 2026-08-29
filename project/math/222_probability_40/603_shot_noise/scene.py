from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ShotNoise(PacedScene):
    """#603 ショットノイズ：点に応答関数を畳み込み（約45秒）"""

    def construct(self):
        self.show_heading("ショットノイズ")
        self.draw_shots()
        self.kernel()
        self.show_formula()
        self.read(1.4)

    def draw_shots(self):
        line = NumberLine(x_range=[0, 6, 1], length=7, include_numbers=False).shift(UP * 0.5)
        xs = [0.8, 2.0, 3.3, 4.7]
        dots = VGroup(*[Dot(line.n2p(x), color=YELLOW, radius=0.1) for x in xs])
        self.play(Create(line), FadeIn(dots), run_time=1.2)
        note = self.ja_text("到着時刻", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.line = line
        self.xs = xs

    def kernel(self):
        import numpy as np
        waves = VGroup()
        for x in self.xs:
            start = self.line.n2p(x)
            path = VMobject(color=BLUE, stroke_width=3)
            pts = [start + RIGHT * t + UP * 0.9 * np.exp(-1.2 * t) for t in np.linspace(0, 1.5, 12)]
            path.set_points_as_corners(pts)
            waves.add(path)
        cap = self.ja_text("応答を重ねる", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(w) for w in waves], lag_ratio=0.1), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("線形フィルタ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"X(t)=\sum_i h(t-T_i)").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
