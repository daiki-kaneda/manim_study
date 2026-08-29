from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class EulerCharacteristic(JapaneseScene):
    """#116 オイラーの多面体公式（約90秒）"""

    def construct(self):
        self.show_heading("多面体公式")
        self.draw_cube()
        self.count()
        self.show_formula()
        self.hold(1.2)

    def draw_cube(self):
        front = Square(side_length=2.2, color=WHITE, stroke_width=3)
        back = Square(side_length=2.2, color=GREY, stroke_width=2).shift(RIGHT * 0.85 + UP * 0.7)
        corners_f = [front.get_corner(d) for d in (DL, DR, UR, UL)]
        corners_b = [back.get_corner(d) for d in (DL, DR, UR, UL)]
        connectors = VGroup(*[Line(a, b, color=WHITE, stroke_width=2) for a, b in zip(corners_f, corners_b)])
        group = VGroup(back, connectors, front).shift(LEFT * 0.6 + DOWN * 0.15)
        self.play(Create(back), Create(connectors), Create(front), run_time=1.0)
        self.hold(0.35)
        self.cube = group

    def count(self):
        rows = VGroup(
            self.ja_text("頂点  8", font_size=26),
            self.ja_text("辺    12", font_size=26),
            self.ja_text("面    6", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        rows.to_edge(RIGHT, buff=0.45).shift(UP * 0.4)
        for r in rows:
            self.play(FadeIn(r), run_time=0.35)
            self.hold(0.18)
        self.hold(0.4)

    def show_formula(self):
        formula = MathTex(r"V-E+F=2").scale(1.2)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=0.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
