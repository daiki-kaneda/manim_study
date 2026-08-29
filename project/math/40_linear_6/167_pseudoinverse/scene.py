from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Pseudoinverse(PacedScene):
    """#167 擬似逆は伸びた向きを戻す（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.3 + DOWN * 0.1
        self.show_heading("擬似逆")
        self.draw_ellipse()
        self.invert_axes()
        self.show_formula()
        self.read(1.4)

    def draw_ellipse(self):
        ax = Line(self.origin + LEFT * 2.5, self.origin + RIGHT * 3.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.1, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        self.ell = Ellipse(width=3.5, height=1.4, color=YELLOW, stroke_width=5).move_to(self.origin)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.play(Create(self.ell), run_time=1.4)
        a = Arrow(self.origin, self.origin + RIGHT * 1.75, buff=0, color=ORANGE, stroke_width=4)
        b = Arrow(self.origin, self.origin + UP * 0.7, buff=0, color=GREEN, stroke_width=4)
        self.play(GrowArrow(a), GrowArrow(b), run_time=1.1)
        note = self.ja_text("伸びた向き", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note
        self.a = a
        self.b = b

    def invert_axes(self):
        circ = Circle(radius=1.2, color=BLUE, stroke_width=5).move_to(self.origin)
        na = Arrow(self.origin, self.origin + RIGHT * 1.2, buff=0, color=ORANGE, stroke_width=4)
        nb = Arrow(self.origin, self.origin + UP * 1.2, buff=0, color=GREEN, stroke_width=4)
        cap = self.ja_text("逆に縮める", font_size=24).move_to(self.note)
        self.play(
            Transform(self.ell, circ),
            Transform(self.a, na),
            Transform(self.b, nb),
            Transform(self.note, cap),
            run_time=2.0,
        )
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"A^{+}=V\Sigma^{+}U^{\mathsf T}").scale(0.95)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
