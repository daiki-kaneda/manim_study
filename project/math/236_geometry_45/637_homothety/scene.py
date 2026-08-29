from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Homothety(PacedScene):
    """#637 ホモセティ：定点を中心に相似拡大（約45秒）"""

    def construct(self):
        self.show_heading("ホモセティ")
        self.draw_shapes()
        self.scale()
        self.show_formula()
        self.read(1.4)

    def draw_shapes(self):
        O = Dot(LEFT * 2.5 + DOWN * 0.3, color=YELLOW, radius=0.1)
        tri1 = Polygon(LEFT * 1.2 + DOWN * 0.8, LEFT * 0.2 + DOWN * 0.8, LEFT * 0.7 + UP * 0.3,
                       color=BLUE, stroke_width=3)
        tri2 = Polygon(RIGHT * 0.5 + DOWN * 1.3, RIGHT * 2.5 + DOWN * 1.3, RIGHT * 1.5 + UP * 1.0,
                       color=ORANGE, stroke_width=3)
        rays = VGroup(*[
            DashedLine(O.get_center(), p, color=GREY, stroke_width=2)
            for p in [tri2.get_vertices()[0], tri2.get_vertices()[1], tri2.get_vertices()[2]]
        ])
        self.play(FadeIn(O), Create(tri1), Create(tri2), LaggedStart(*[Create(r) for r in rays], lag_ratio=0.08), run_time=1.5)
        note = self.ja_text("相似の中心", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def scale(self):
        cap = self.ja_text("比 k で拡大", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("向きを保つ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\overrightarrow{OP'}=k\,\overrightarrow{OP}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
