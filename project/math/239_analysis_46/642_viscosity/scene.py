from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ViscositySolution(PacedScene):
    """#642 粘性解：非古典的なPDE解の概念（約45秒）"""

    def construct(self):
        self.show_heading("粘性解")
        self.draw_touch()
        self.test()
        self.show_formula()
        self.read(1.4)

    def draw_touch(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[-0.5, 2, 1], x_length=5.0, y_length=2.5,
                    tips=False, axis_config={"stroke_width": 1, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.1)
        u = axes.plot(lambda x: 0.4 * abs(x) + 0.3, x_range=[-1.8, 1.8], color=BLUE, stroke_width=3)
        phi = axes.plot(lambda x: 0.15 * x ** 2 + 0.55, x_range=[-1.2, 1.2], color=ORANGE, stroke_width=2)
        self.play(Create(axes), Create(u), Create(phi), run_time=1.4)
        note = self.ja_text("テスト関数で触る", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def test(self):
        cap = self.ja_text("劣解・優解", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("滑らかでなくても", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"F(x,u,Du,D^2u)=0").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
