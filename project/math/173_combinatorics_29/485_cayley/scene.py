from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CayleyFormula(PacedScene):
    """#485 ケイリーの公式：ラベル木は n^{n-2}（約45秒）"""

    def construct(self):
        self.show_heading("ケイリーの公式")
        self.draw_tree()
        self.count()
        self.show_formula()
        self.read(1.4)

    def draw_tree(self):
        pts = [
            UP * 1.5,
            LEFT * 1.8 + UP * 0.2,
            RIGHT * 1.8 + UP * 0.2,
            LEFT * 2.4 + DOWN * 1.3,
            LEFT * 0.6 + DOWN * 1.3,
            RIGHT * 0.8 + DOWN * 1.3,
            RIGHT * 2.6 + DOWN * 1.3,
        ]
        dots = VGroup(*[Dot(p, color=BLUE, radius=0.12) for p in pts])
        edges = VGroup(
            Line(pts[0], pts[1], color=GREY, stroke_width=3),
            Line(pts[0], pts[2], color=GREY, stroke_width=3),
            Line(pts[1], pts[3], color=GREY, stroke_width=3),
            Line(pts[1], pts[4], color=GREY, stroke_width=3),
            Line(pts[2], pts[5], color=GREY, stroke_width=3),
            Line(pts[2], pts[6], color=GREY, stroke_width=3),
        )
        labs = VGroup(*[MathTex(str(i + 1), font_size=22).next_to(dots[i], UP, buff=0.08) for i in range(7)])
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.08), FadeIn(dots), FadeIn(labs), run_time=1.5)
        note = self.ja_text("ラベル付き木", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def count(self):
        cap = self.ja_text("何通り？", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("プリューファー符号", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\#\{\text{labeled trees}\}=n^{n-2}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
