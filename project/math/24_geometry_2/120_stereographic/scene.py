from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Stereographic(JapaneseScene):
    """#120 立体射影（約90秒）"""

    def construct(self):
        self.show_heading("立体射影")
        self.draw()
        self.show_formula()
        self.hold(1.2)

    def draw(self):
        o = LEFT * 1.7 + DOWN * 0.85
        equator = Ellipse(width=4.4, height=1.15, color=GREY, stroke_width=2).move_to(o)
        sphere = Circle(radius=1.55, color=WHITE, stroke_width=2).move_to(o + UP * 0.05)
        n = o + UP * 1.6
        plane = Line(o + LEFT * 3.3 + DOWN * 0.02, o + RIGHT * 4.2 + DOWN * 0.02, color=BLUE, stroke_width=3)
        p_s = o + LEFT * 0.85 + UP * 0.55
        p_p = o + LEFT * 2.15 + DOWN * 0.02
        ray = Line(n, p_p, color=YELLOW, stroke_width=3)
        self.play(Create(plane), Create(equator), Create(sphere), run_time=0.85)
        self.play(FadeIn(Dot(n, color=ORANGE, radius=0.08)), run_time=0.3)
        nlab = MathTex("N", color=ORANGE, font_size=28).next_to(n, UP, buff=0.08)
        self.play(FadeIn(nlab), Create(ray), FadeIn(Dot(p_s, color=YELLOW, radius=0.07)), FadeIn(Dot(p_p, color=BLUE, radius=0.07)), run_time=0.7)
        note = self.ja_text("北極から射す", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = self.ja_text("一点を除くと平面", font_size=26)
        formula.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(formula), run_time=0.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
