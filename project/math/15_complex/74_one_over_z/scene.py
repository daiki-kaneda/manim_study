from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import polar


class OneOverZ(JapaneseScene):
    """#74 1/z は反転（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 0.05
        self.show_heading("1/z")
        self.draw_points()
        self.invert()
        self.show_formula()
        self.hold(1.2)

    def draw_points(self):
        axes_x = Line(self.origin + LEFT * 0.4, self.origin + RIGHT * 4.2, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 2.0, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        unit = Circle(radius=1.5, color=GREY, stroke_width=1.5).move_to(self.origin)
        self.play(Create(axes_x), Create(axes_y), Create(unit), run_time=0.7)
        z = np.array(polar(2.4, 32 * DEGREES))
        self.az = Arrow(self.origin, self.origin + z, buff=0, color=BLUE, stroke_width=4)
        lz = MathTex("z", color=BLUE, font_size=30).next_to(self.az.get_end(), UR, buff=0.08)
        self.play(GrowArrow(self.az), FadeIn(lz), run_time=0.55)
        note = self.ja_text("単位円の外", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.5)
        self.z, self.note = z, note

    def invert(self):
        inv = np.array(polar(1.5 * 1.5 / 2.4, -32 * DEGREES))
        # 半径 1.5 の円を単位とみなす: 1/r' = 1.5^2 / r
        ai = Arrow(self.origin, self.origin + inv, buff=0, color=YELLOW, stroke_width=5)
        li = MathTex(r"1/z", color=YELLOW, font_size=30).next_to(ai.get_end(), DR, buff=0.08)
        self.play(GrowArrow(ai), FadeIn(li), run_time=0.7)
        cap = self.ja_text("中へ、向きは逆", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\frac{1}{re^{i\theta}}=\frac{1}{r}e^{-i\theta}").scale(1.0)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
