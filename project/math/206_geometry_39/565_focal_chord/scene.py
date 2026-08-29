from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class FocalChord(PacedScene):
    """#565 焦点弦：焦点を通る弦（約45秒）"""

    def construct(self):
        self.show_heading("焦点弦")
        self.draw_parabola()
        self.chord()
        self.show_formula()
        self.read(1.4)

    def draw_parabola(self):
        axes = Axes(x_range=[-0.5, 3, 1], y_range=[-2, 2, 1], x_length=5.5, y_length=3.2, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.1)
        para = axes.plot(lambda x: 1.2 * (x ** 0.5) if x >= 0 else 0, x_range=[0.01, 2.8], color=BLUE, stroke_width=4)
        para2 = axes.plot(lambda x: -1.2 * (x ** 0.5) if x >= 0 else 0, x_range=[0.01, 2.8], color=BLUE, stroke_width=4)
        focus = Dot(axes.c2p(0.5, 0), color=YELLOW, radius=0.1)
        self.play(Create(axes), Create(para), Create(para2), FadeIn(focus), run_time=1.5)
        note = self.ja_text("焦点 F", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def chord(self):
        a = self.axes.c2p(2.2, 1.2 * (2.2 ** 0.5))
        b = self.axes.c2p(0.8, -1.2 * (0.8 ** 0.5))
        chord = Line(a, b, color=ORANGE, stroke_width=4)
        cap = self.ja_text("焦点を通る弦", font_size=24).move_to(self.note)
        self.play(Create(chord), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("パラメータで表す", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"y^2=4ax").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
