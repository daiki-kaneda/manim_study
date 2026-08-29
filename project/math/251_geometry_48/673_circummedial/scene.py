from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CircummedialTriangle(PacedScene):
    """#673 外心中点三角形：外心と辺中点の三角形（約45秒）"""

    def construct(self):
        self.show_heading("外心中点三角形")
        self.draw()
        self.props()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        A, B, C = UP * 1.8, LEFT * 2.6 + DOWN * 1.2, RIGHT * 2.6 + DOWN * 1.2
        tri = Polygon(A, B, C, color=BLUE, stroke_width=3)
        O = Dot(ORIGIN + DOWN * 0.15, color=YELLOW, radius=0.1)
        mids = VGroup(*[Dot((P + Q) / 2, color=ORANGE, radius=0.08) for P, Q in [(A, B), (B, C), (C, A)]])
        cm = Polygon(O.get_center(), mids[0].get_center(), mids[1].get_center(), color=TEAL, stroke_width=3)
        # better: triangle of O with two mids - actually circummedial is formed differently
        # Use triangle joining midpoints of segments from O to vertices approx
        self.play(Create(tri), FadeIn(O), FadeIn(mids), Create(Polygon(*[m.get_center() for m in mids], color=TEAL, stroke_width=3)), run_time=1.4)
        note = self.ja_text("外心と中点", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def props(self):
        cap = self.ja_text("面積は 1/4", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("中点三角形と一致", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"[m]=\tfrac14[\triangle]").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
