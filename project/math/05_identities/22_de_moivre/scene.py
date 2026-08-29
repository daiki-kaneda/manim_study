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


class DeMoivre(JapaneseScene):
    """#22 ド・モアブルの定理（約90秒）"""

    def construct(self):
        self.R = 2.0
        self.origin = LEFT * 2.4 + DOWN * 0.05
        self.theta = 32 * DEGREES
        self.show_heading("ド・モアブルの定理")
        self.draw_plane()
        self.show_powers()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_plane(self):
        axes_x = Line(
            self.origin + LEFT * 0.3 * self.R,
            self.origin + RIGHT * 1.25 * self.R,
            color=GREY,
            stroke_width=2,
        )
        axes_y = Line(
            self.origin + DOWN * 1.15 * self.R,
            self.origin + UP * 1.2 * self.R,
            color=GREY,
            stroke_width=2,
        )
        circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        z0 = MathTex(r"z=\cos\theta+i\sin\theta", font_size=32)
        z0.to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(Create(axes_x), Create(axes_y), Create(circle), run_time=0.9)
        self.play(FadeIn(z0), run_time=0.45)
        self.hold(0.4)
        self.z0 = z0

    def show_powers(self):
        colors = [YELLOW, ORANGE, GREEN, TEAL]
        labels = [r"z", r"z^2", r"z^3", r"z^4"]
        dots = VGroup()
        rays = VGroup()
        labs = VGroup()
        for n in range(1, 5):
            ang = n * self.theta
            p = self._pt(ang)
            ray = Line(self.origin, p, color=colors[n - 1], stroke_width=3)
            dot = Dot(p, color=colors[n - 1], radius=0.07)
            lab = MathTex(labels[n - 1], color=colors[n - 1], font_size=30)
            offset = UR if ang < 80 * DEGREES else RIGHT
            lab.next_to(p, offset, buff=0.12)
            self.play(Create(ray), FadeIn(dot), FadeIn(lab), run_time=0.55)
            note = MathTex(rf"n={n}", font_size=28).next_to(self.z0, DOWN, aligned_edge=RIGHT, buff=0.25)
            if n == 1:
                self.n_lab = note
                self.play(FadeIn(self.n_lab), run_time=0.25)
            else:
                self.play(Transform(self.n_lab, note), run_time=0.3)
            self.hold(0.4)
            rays.add(ray)
            dots.add(dot)
            labs.add(lab)
        self.hold(0.5)

    def show_formula(self):
        formula = MathTex(
            r"(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta"
        ).scale(0.78)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.2)
        note = self.ja_text("偏角が n 倍、絶対値は 1 のまま", font_size=24)
        note.next_to(formula, UP, buff=0.22)
        self.play(FadeIn(note), run_time=0.45)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
