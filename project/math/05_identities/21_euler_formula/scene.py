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


class EulerFormula(JapaneseScene):
    """#21 オイラーの公式（約90秒）"""

    def construct(self):
        self.R = 2.05
        self.origin = LEFT * 2.35 + DOWN * 0.1
        self.show_heading("オイラーの公式")
        self.draw_plane()
        self.move_on_circle()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_plane(self):
        axes_x = Line(
            self.origin + LEFT * 0.35 * self.R,
            self.origin + RIGHT * 1.3 * self.R,
            color=GREY,
            stroke_width=2,
        )
        axes_y = Line(
            self.origin + DOWN * 1.15 * self.R,
            self.origin + UP * 1.2 * self.R,
            color=GREY,
            stroke_width=2,
        )
        re = MathTex(r"\mathrm{Re}", font_size=26).next_to(axes_x.get_end(), DOWN, buff=0.12)
        im = MathTex(r"\mathrm{Im}", font_size=26).next_to(axes_y.get_end(), LEFT, buff=0.12)
        circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        self.play(Create(axes_x), Create(axes_y), FadeIn(re), FadeIn(im), run_time=0.7)
        self.play(Create(circle), run_time=0.8)
        self.hold(0.4)

    def _arms(self, ang, color=YELLOW):
        p = self._pt(ang)
        ray = Line(self.origin, p, color=color, stroke_width=3)
        dot = Dot(p, color=color, radius=0.07)
        px = np.array([p[0], self.origin[1], 0.0])
        py = np.array([self.origin[0], p[1], 0.0])
        to_x = DashedLine(p, px, color=BLUE, stroke_width=2)
        to_y = DashedLine(p, py, color=GREEN, stroke_width=2)
        return VGroup(ray, dot, to_x, to_y)

    def move_on_circle(self):
        angles = [38 * DEGREES, 90 * DEGREES, 128 * DEGREES]
        group = self._arms(angles[0])
        lab = MathTex(r"e^{i\theta}", color=YELLOW, font_size=34)
        lab.next_to(self._pt(angles[0]), UR, buff=0.12)
        cos_lab = MathTex(r"\cos\theta", color=BLUE, font_size=28)
        cos_lab.next_to(np.array([self._pt(angles[0])[0], self.origin[1], 0]), DOWN, buff=0.18)
        sin_lab = MathTex(r"i\sin\theta", color=GREEN, font_size=28)
        sin_lab.next_to(np.array([self.origin[0], self._pt(angles[0])[1], 0]), LEFT, buff=0.18)
        self.play(Create(group[0]), FadeIn(group[1]), run_time=0.6)
        self.play(Create(group[2]), Create(group[3]), FadeIn(lab), FadeIn(cos_lab), FadeIn(sin_lab), run_time=0.8)
        self.hold(0.7)
        for ang in angles[1:]:
            nxt = self._arms(ang)
            nxt_lab = MathTex(r"e^{i\theta}", color=YELLOW, font_size=34)
            nxt_lab.next_to(self._pt(ang), UR, buff=0.12)
            nxt_cos = MathTex(r"\cos\theta", color=BLUE, font_size=28)
            nxt_cos.next_to(np.array([self._pt(ang)[0], self.origin[1], 0]), DOWN, buff=0.18)
            nxt_sin = MathTex(r"i\sin\theta", color=GREEN, font_size=28)
            nxt_sin.next_to(np.array([self.origin[0], self._pt(ang)[1], 0]), LEFT, buff=0.18)
            self.play(
                Transform(group, nxt),
                Transform(lab, nxt_lab),
                Transform(cos_lab, nxt_cos),
                Transform(sin_lab, nxt_sin),
                run_time=0.75,
            )
            self.hold(0.45)
        self.hold(0.5)

    def show_formula(self):
        formula = MathTex(r"e^{i\theta}=\cos\theta+i\sin\theta").scale(1.05)
        formula.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.15)
        self.play(Write(formula), run_time=1.1)
        note = self.ja_text("単位円上の点", font_size=26)
        note.next_to(formula, DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.45)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
