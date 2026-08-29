from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class HardySpace(PacedScene):
    """#570 ハードスペース：正則関数の境界値空間（約45秒）"""

    def construct(self):
        self.show_heading("ハードスペース")
        self.draw_disk()
        self.boundary()
        self.show_formula()
        self.read(1.4)

    def draw_disk(self):
        import numpy as np
        disk = Circle(radius=1.8, color=BLUE, stroke_width=3).shift(LEFT * 1.5 + UP * 0.1)
        center = LEFT * 1.5 + UP * 0.1
        rays = VGroup(*[
            Line(center, center + RIGHT * 1.6 * np.cos(a) + UP * 1.6 * np.sin(a), color=GREY, stroke_width=2)
            for a in [0.3, 1.0, 2.0, 3.5, 4.8]
        ])
        self.play(Create(disk), LaggedStart(*[Create(r) for r in rays], lag_ratio=0.08), run_time=1.4)
        note = self.ja_text("円板上の正則", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def boundary(self):
        arc = Arc(radius=1.8, start_angle=-0.4, angle=2.2, color=ORANGE, stroke_width=5).shift(LEFT * 1.5 + UP * 0.1)
        cap = self.ja_text("境界値が Lp", font_size=24).move_to(self.note)
        self.play(Create(arc), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("内側の平均で制御", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\|f\|_{H^p}=\sup_{r<1}\|f(re^{i\theta})\|_{L^p}").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
