from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class CircleArea(JapaneseScene):
    """#29 円の面積：扇形を並べる（約90秒）"""

    def construct(self):
        self.n = 8
        self.R = 1.6
        self.show_heading("円の面積")
        self.draw_circle()
        self.rearrange()
        self.show_formula()
        self.hold(1.2)

    def _wedge(self, color):
        # 二等分線が +x 方向。尖端は ORIGIN。
        return AnnularSector(
            inner_radius=0,
            outer_radius=self.R,
            angle=TAU / self.n,
            start_angle=-TAU / (2 * self.n),
            color=color,
            fill_opacity=0.85,
            stroke_width=1.2,
            stroke_color=WHITE,
        )

    def draw_circle(self):
        colors = [BLUE, TEAL]
        pieces = VGroup()
        for i in range(self.n):
            sec = self._wedge(colors[i % 2])
            sec.rotate(PI / 2 + i * TAU / self.n, about_point=ORIGIN)
            pieces.add(sec)
        pieces.shift(LEFT * 2.7 + UP * 0.2)
        r_line = Line(
            pieces.get_center(),
            pieces.get_center() + RIGHT * self.R,
            color=YELLOW,
            stroke_width=3,
        )
        r_lab = MathTex("r", color=YELLOW, font_size=32).next_to(r_line, DOWN, buff=0.08)
        self.play(FadeIn(pieces), run_time=0.8)
        self.play(Create(r_line), FadeIn(r_lab), run_time=0.5)
        self.hold(0.6)
        self.pieces = pieces
        self.r_line, self.r_lab = r_line, r_lab

    def rearrange(self):
        self.play(FadeOut(self.r_line), FadeOut(self.r_lab), run_time=0.3)
        n, R = self.n, self.R
        chord = 2 * R * np.sin(PI / n)
        h = R * np.cos(PI / n)
        origin = np.array([0.15, -1.45, 0.0])
        arranged = VGroup()
        for i in range(n):
            sec = self._wedge([BLUE, TEAL][i % 2])
            x = origin[0] + i * chord / 2
            if i % 2 == 0:
                sec.rotate(PI / 2, about_point=ORIGIN)
                sec.shift(np.array([x, origin[1], 0.0]))
            else:
                sec.rotate(-PI / 2, about_point=ORIGIN)
                sec.shift(np.array([x, origin[1] + h, 0.0]))
            arranged.add(sec)

        self.play(Transform(self.pieces, arranged), run_time=1.25)
        self.hold(0.55)
        height_bar = Line(
            origin + LEFT * 0.15,
            origin + LEFT * 0.15 + UP * h,
            color=YELLOW,
            stroke_width=3,
        )
        h_lab = MathTex(r"\approx r", color=YELLOW, font_size=28).next_to(height_bar, LEFT, buff=0.1)
        w_line = Line(
            origin + DOWN * 0.28,
            origin + DOWN * 0.28 + RIGHT * (n * chord / 2),
            color=ORANGE,
            stroke_width=3,
        )
        w_lab = MathTex(r"\approx\pi r", color=ORANGE, font_size=30).next_to(w_line, DOWN, buff=0.1)
        self.play(Create(height_bar), FadeIn(h_lab), run_time=0.5)
        self.play(Create(w_line), FadeIn(w_lab), run_time=0.55)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"(\pi r)\cdot r=\pi r^2").scale(1.15)
        formula.to_edge(UP, buff=1.15).to_edge(RIGHT, buff=0.45)
        self.play(Write(formula), run_time=1.0)
        note = self.ja_text("扇形を並べると長方形", font_size=24)
        note.next_to(formula, DOWN, buff=0.28)
        self.play(FadeIn(note), run_time=0.4)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
