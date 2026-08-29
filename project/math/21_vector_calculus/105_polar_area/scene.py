from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class PolarArea(JapaneseScene):
    """#105 極座標の面積（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.3 + DOWN * 0.85
        self.show_heading("極座標の面積")
        self.draw_sector()
        self.slice()
        self.show_formula()
        self.hold(1.2)

    def draw_sector(self):
        r = 2.4
        axes_x = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 3.6, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.1, color=GREY, stroke_width=2)
        self.play(Create(axes_x), Create(axes_y), run_time=0.4)
        self.arc = Sector(
            inner_radius=0,
            outer_radius=r,
            angle=70 * DEGREES,
            start_angle=15 * DEGREES,
            color=BLUE,
            fill_opacity=0.45,
            stroke_width=2,
            arc_center=self.origin,
        )
        self.play(FadeIn(self.arc), run_time=0.7)
        note = self.ja_text("扇形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.45)
        self.note = note
        self.r = r

    def slice(self):
        wedges = VGroup()
        start = 15 * DEGREES
        n = 6
        span = 70 * DEGREES / n
        colors = [BLUE, TEAL, GREEN, YELLOW, ORANGE, PINK]
        for i in range(n):
            wedges.add(
                Sector(
                    inner_radius=0,
                    outer_radius=self.r,
                    angle=span,
                    start_angle=start + i * span,
                    color=colors[i],
                    fill_opacity=0.55,
                    stroke_width=1,
                    arc_center=self.origin,
                )
            )
        self.play(FadeOut(self.arc), FadeIn(wedges), run_time=0.7)
        cap = self.ja_text("細い扇の和", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"A=\frac12\int r^{2}\,d\theta").scale(1.05)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
