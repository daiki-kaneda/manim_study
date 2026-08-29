from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Marcinkiewicz(PacedScene):
    """#524 マルチンケヴィッチ：弱型端点から強型へ（約45秒）"""

    def construct(self):
        self.show_heading("マルチンケヴィッチ")
        self.draw_weak()
        self.interp()
        self.show_formula()
        self.read(1.4)

    def draw_weak(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.5, y_length=2.4, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.5 + UP * 0.3)
        decay = axes.plot(lambda t: 1.2 / (t + 0.4), x_range=[0.2, 3.8], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(decay), run_time=1.3)
        note = self.ja_text("弱型評価", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def interp(self):
        cap = self.ja_text("実補間", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("強型を得る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"T:L^{p_i}\to L^{q_i,\infty}\ \Rightarrow\ T:L^{p_\theta}\to L^{q_\theta}").scale(0.62)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
