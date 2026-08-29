from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LARS(PacedScene):
    """#753 LARS：最小角回帰でパスを追う（約45秒）"""

    def construct(self):
        self.show_heading("LARS")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        path = VMobject(color=BLUE, stroke_width=3).set_points_as_corners(
            [axes.c2p(0.2, 0.2), axes.c2p(1.2, 1.0), axes.c2p(2.2, 1.4), axes.c2p(3.4, 1.6)])
        self.play(Create(axes), Create(path), run_time=1.3)
        note = self.ja_text("相関が等しい方向", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("変数を順に追加", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("Lasso パスへ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\hat\beta(\lambda)=\arg\min\|y-X\beta\|_2^2+\lambda\|\beta\|_1").scale(0.55)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
