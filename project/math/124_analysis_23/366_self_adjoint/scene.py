from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SelfAdjoint(PacedScene):
    """#366 自己共役：A*=A なら実スペクトル（約45秒）"""

    def construct(self):
        self.show_heading("自己共役作用素")
        self.draw_spectrum()
        self.real_line()
        self.show_formula()
        self.read(1.4)

    def draw_spectrum(self):
        self.O = LEFT * 0.4 + DOWN * 0.1
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        ay = Line(self.O + DOWN * 2.0, self.O + UP * 2.0, color=GREY, stroke_width=2)
        # complex plane with points on real axis
        self.play(Create(ax), Create(ay), run_time=0.9)
        pts = VGroup(*[Dot(self.O + RIGHT * x, color=ORANGE, radius=0.1) for x in [-1.8, -0.4, 1.2, 2.3]])
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in pts], lag_ratio=0.1), run_time=1.3)
        note = self.ja_text("固有値", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.pts = pts

    def real_line(self):
        brace = BraceBetweenPoints(self.pts[0].get_center(), self.pts[-1].get_center(), direction=DOWN, color=YELLOW)
        cap = self.ja_text("実軸の上", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("虚部は 0", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"A^{*}=A\ \Rightarrow\ \sigma(A)\subset\mathbb{R}").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
