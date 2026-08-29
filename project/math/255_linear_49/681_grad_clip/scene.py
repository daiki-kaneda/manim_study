from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GradientClipping(PacedScene):
    """#681 勾配クリッピング：大きすぎる勾配を制限（約45秒）"""

    def construct(self):
        self.show_heading("勾配クリッピング")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        long = Arrow(LEFT * 2.5 + DOWN * 0.2, RIGHT * 2.8 + UP * 1.0, buff=0.05, color=RED, stroke_width=5)
        clipped = Arrow(LEFT * 2.5 + DOWN * 0.2, RIGHT * 0.5 + UP * 0.25, buff=0.05, color=BLUE, stroke_width=5)
        self.play(GrowArrow(long), run_time=0.9)
        self.play(Transform(long, clipped), run_time=1.0)

        note = self.ja_text("爆発を防ぐ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("ノルムで切る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("安定化の定番", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"g\leftarrow g\cdot\min(1,\theta/\|g\|)").scale(0.78)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
