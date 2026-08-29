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


class HarmonicOscillator(JapaneseScene):
    """#68 単振動 y''=-y（約90秒）"""

    def construct(self):
        self.R = 1.55
        self.origin = LEFT * 3.0 + DOWN * 0.1
        self.show_heading("単振動")
        self.draw_circle()
        self.project()
        self.show_formula()
        self.hold(1.2)

    def draw_circle(self):
        circle = Circle(radius=self.R, color=GREY, stroke_width=2).move_to(self.origin)
        self.play(Create(circle), run_time=0.55)
        angles = [20 * DEGREES, 70 * DEGREES, 130 * DEGREES]
        dots = VGroup()
        for ang in angles:
            p = self.origin + np.array(polar(self.R, ang))
            dots.add(Dot(p, color=YELLOW, radius=0.07))
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.2), run_time=0.7)
        self.hold(0.4)
        self.dots = dots
        self.angles = angles

    def project(self):
        # 縦軸への射影 = cos ではなく sin（高さ）
        axis = Line(self.origin + RIGHT * 2.3 + DOWN * 1.8, self.origin + RIGHT * 2.3 + UP * 1.8, color=GREY, stroke_width=2)
        self.play(Create(axis), run_time=0.4)
        for d, ang in zip(self.dots, self.angles):
            p = d.get_center()
            foot = np.array([self.origin[0] + 2.3, p[1], 0])
            self.play(Create(DashedLine(p, foot, color=BLUE, stroke_width=2)), FadeIn(Dot(foot, color=BLUE, radius=0.07)), run_time=0.4)
        note = self.ja_text("円の高さが振動", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"y''=-y\quad\Rightarrow\quad y=\cos t").scale(0.95)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
