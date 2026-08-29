from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BridgelandStability(PacedScene):
    """#739 ブリッジランド安定性：導来圏の安定性条件（約45秒）"""

    def construct(self):
        self.show_heading("ブリッジランド安定性")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        ray = Arrow(axes.c2p(0, 0), axes.c2p(1.5, 1.5), buff=0.05, color=ORANGE, stroke_width=4)
        self.play(Create(axes), GrowArrow(ray), run_time=1.3)
        note = self.ja_text("中心電荷 Z", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("位相で傾き", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("壁越え", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Z:K(D)\to\mathbb{C}").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
