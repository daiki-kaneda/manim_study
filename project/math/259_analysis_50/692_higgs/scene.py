from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HiggsMechanism(PacedScene):
    """#692 ヒッグス機構：対称性の破れで質量を付与（約45秒）"""

    def construct(self):
        self.show_heading("ヒッグス機構")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        pot = Axes(x_range=[-2, 2, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.1)
        mexican = pot.plot(lambda x: 0.3 + (x ** 2 - 1) ** 2, x_range=[-1.7, 1.7], color=ORANGE, stroke_width=3)
        self.play(Create(pot), Create(mexican), run_time=1.4)

        note = self.ja_text("ポテンシャルの形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("真空期待値", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("質量の起源", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"V(\phi)=\lambda(|\phi|^2-v^2)^2").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
