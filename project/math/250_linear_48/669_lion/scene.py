from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LionOptimizer(PacedScene):
    """#669 Lion：符号だけで進むメモリ軽量最適化（約45秒）"""

    def construct(self):
        self.show_heading("Lion")
        self.draw()
        self.sign()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[-1, 2, 1], x_length=4.5, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.4 + UP * 0.1)
        path = VMobject(color=BLUE, stroke_width=3).set_points_as_corners(
            [axes.c2p(-1.5, 1.5), axes.c2p(-0.5, 0.8), axes.c2p(0.3, 0.5), axes.c2p(1.2, 0.2)])
        self.play(Create(axes), Create(path), run_time=1.3)
        note = self.ja_text("符号更新", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sign(self):
        cap = self.ja_text("sign(m) で進む", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("メモリが軽い", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\theta\leftarrow\theta-\eta\,\mathrm{sign}(m)").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
