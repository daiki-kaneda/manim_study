from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class IntouchTriangle(PacedScene):
    """#650 接点三角形：内接円の接点が作る三角形（約45秒）"""

    def construct(self):
        self.show_heading("接点三角形")
        self.draw()
        self.props()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.8 + DOWN * 1.2, RIGHT * 2.8 + DOWN * 1.2, UP * 1.8,
                      color=BLUE, stroke_width=3)
        inc = Circle(radius=0.7, color=ORANGE, stroke_width=3).shift(DOWN * 0.35)
        # contact approx
        X = Dot(DOWN * 1.05, color=YELLOW, radius=0.08)
        Y = Dot(RIGHT * 1.35 + UP * 0.25, color=YELLOW, radius=0.08)
        Z = Dot(LEFT * 1.35 + UP * 0.25, color=YELLOW, radius=0.08)
        contact_tri = Polygon(X.get_center(), Y.get_center(), Z.get_center(), color=TEAL, stroke_width=3)
        self.play(Create(tri), Create(inc), FadeIn(VGroup(X, Y, Z)), Create(contact_tri), run_time=1.5)
        note = self.ja_text("接点を結ぶ", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def props(self):
        cap = self.ja_text("接触三角形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ジェルゴンヌ点へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"XY=s-c,\ YZ=s-a,\ ZX=s-b").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
