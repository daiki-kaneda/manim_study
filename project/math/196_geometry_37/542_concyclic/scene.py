from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ConcyclicCondition(PacedScene):
    """#542 共円条件：四点が同一円上（約45秒）"""

    def construct(self):
        self.show_heading("共円条件")
        self.draw_quad()
        self.angles()
        self.show_formula()
        self.read(1.4)

    def draw_quad(self):
        circ = Circle(radius=1.8, color=BLUE, stroke_width=3).shift(UP * 0.1)
        pts = [circ.point_from_proportion(t) for t in [0.05, 0.28, 0.55, 0.8]]
        quad = Polygon(*pts, color=ORANGE, stroke_width=3)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.09) for p in pts])
        self.play(Create(circ), Create(quad), FadeIn(dots), run_time=1.4)
        note = self.ja_text("四点共円", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def angles(self):
        cap = self.ja_text("対角の和が180°", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("同じ弧の円周角", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\angle ABC+\angle ADC=180^\circ").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
