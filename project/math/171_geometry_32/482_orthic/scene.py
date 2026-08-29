from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class OrthicTriangle(PacedScene):
    """#482 垂心三角形：垂線の足を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("垂心三角形")
        self.draw_triangle()
        self.feet()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.2
        self.B = LEFT * 2.6 + DOWN * 1.4
        self.C = RIGHT * 2.9 + DOWN * 1.5
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("鋭角三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def feet(self):
        # approximate feet for visual
        Ha = self.B * 0.48 + self.C * 0.52
        Hb = self.A * 0.35 + self.C * 0.65
        Hc = self.A * 0.42 + self.B * 0.58
        altitudes = VGroup(
            Line(self.A, Ha, color=GREY, stroke_width=2),
            Line(self.B, Hb, color=GREY, stroke_width=2),
            Line(self.C, Hc, color=GREY, stroke_width=2),
        )
        orthic = Polygon(Ha, Hb, Hc, color=ORANGE, stroke_width=3)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.09) for p in [Ha, Hb, Hc]])
        cap = self.ja_text("3 垂線の足", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(a) for a in altitudes], lag_ratio=0.1), run_time=1.1)
        self.play(FadeIn(dots), Create(orthic), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("垂心が内心", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("垂心三角形：垂線の足を頂点に", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
