from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ConstrainedCG(PacedScene):
    """#597 拘束付きCG：アフィン拘束の下で最小化（約45秒）"""

    def construct(self):
        self.show_heading("拘束付きCG")
        self.draw_plane()
        self.project()
        self.show_formula()
        self.read(1.4)

    def draw_plane(self):
        plane = Polygon(LEFT * 3 + DOWN * 1.2, RIGHT * 2.5 + DOWN * 0.5, RIGHT * 2.0 + UP * 1.5, LEFT * 3.2 + UP * 0.8,
                        color=BLUE, stroke_width=3, fill_opacity=0.15)
        self.play(Create(plane), run_time=1.2)
        note = self.ja_text("アフィン部分空間", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def project(self):
        arrow = Arrow(DOWN * 1.5 + RIGHT * 0.5, UP * 0.3 + LEFT * 0.2, buff=0.05, color=ORANGE, stroke_width=4)
        cap = self.ja_text("射影して進む", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("拘束を保つ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\min_x\tfrac12 x^\top Ax-b^\top x\ \mathrm{s.t.}\ Cx=d").scale(0.68)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
