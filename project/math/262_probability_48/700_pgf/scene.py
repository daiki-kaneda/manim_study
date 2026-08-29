from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PGF(PacedScene):
    """#700 確率母関数：非負整数値確率の母関数（約45秒）"""

    def construct(self):
        self.show_heading("確率母関数")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 1.2, 0.5], y_range=[0, 1.2, 0.5], x_length=5.0, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT*0.3+UP*0.15)
        g = axes.plot(lambda s: 0.2 + 0.7 * s ** 2, x_range=[0.02, 1.05], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(g), run_time=1.3)

        note = self.ja_text("s のべき級数", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("畳み込みが積", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("階乗モーメント", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"G(s)=\mathbb{E}[s^X]").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
