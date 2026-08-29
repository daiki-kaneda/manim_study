from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LogRank(PacedScene):
    """#472 対数ランク検定：2 群の生存を比べる（約45秒）"""

    def construct(self):
        self.show_heading("対数ランク検定")
        self.draw_curves()
        self.compare()
        self.show_formula()
        self.read(1.4)

    def draw_curves(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[0, 1.15, 1], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.3)
        s1 = [(0, 1), (1, 1), (1, 0.85), (2.5, 0.85), (2.5, 0.7), (4, 0.7), (4, 0.55), (6, 0.55)]
        s2 = [(0, 1), (1.5, 1), (1.5, 0.75), (3, 0.75), (3, 0.5), (5, 0.5), (5, 0.35), (6, 0.35)]
        p1 = VMobject(color=BLUE, stroke_width=4)
        p1.set_points_as_corners([axes.c2p(x, y) for x, y in s1])
        p2 = VMobject(color=ORANGE, stroke_width=4)
        p2.set_points_as_corners([axes.c2p(x, y) for x, y in s2])
        self.play(Create(axes), Create(p1), Create(p2), run_time=1.6)
        note = self.ja_text("2 群の生存", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compare(self):
        cap = self.ja_text("イベントごとに比較", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("差があるか検定", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Z=\frac{\sum(O_i-E_i)}{\sqrt{\sum V_i}}").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
