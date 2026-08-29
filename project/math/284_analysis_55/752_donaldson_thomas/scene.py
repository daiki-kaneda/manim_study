from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class DonaldsonThomas(PacedScene):
    """#752 ドナルドソン・トーマス：曲線・層の仮想数え上げ（約45秒）"""

    def construct(self):
        self.show_heading("ドナルドソン・トーマス")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        curve = axes.plot(lambda t: 0.4 + 0.3 * t + 0.2 * (t - 1.5) ** 2, x_range=[0.1, 2.8], color=TEAL, stroke_width=3)
        self.play(Create(axes), Create(curve), run_time=1.3)
        note = self.ja_text("仮想基本類", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("完全交叉など", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("GW と対になる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\int_{[M]^{\mathrm{vir}}}1").scale(0.8)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
