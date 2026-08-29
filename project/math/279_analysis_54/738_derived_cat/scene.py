from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class DerivedCategory(PacedScene):
    """#738 導来圏：複体をホモトピーで同一視する圏（約45秒）"""

    def construct(self):
        self.show_heading("導来圏")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.5, height=1.0, corner_radius=0.08, color=c, stroke_width=3).shift(pos)
            for c, pos in [(BLUE, LEFT * 2.4 + UP * 0.3), (ORANGE, ORIGIN + UP * 0.3), (TEAL, RIGHT * 2.4 + UP * 0.3)]
        ])
        labs = VGroup(*[MathTex(s, font_size=26).move_to(b) for s, b in zip([r"E^{-1}", r"E^0", r"E^1"], boxes)])
        arrows = VGroup(
            Arrow(boxes[0].get_right(), boxes[1].get_left(), buff=0.08, stroke_width=3),
            Arrow(boxes[1].get_right(), boxes[2].get_left(), buff=0.08, stroke_width=3),
        )
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.1), FadeIn(labs),
                  GrowArrow(arrows[0]), GrowArrow(arrows[1]), run_time=1.4)
        note = self.ja_text("複体の圏", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("擬同型で局所化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("三角圏になる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"D(\mathcal{A})=K(\mathcal{A})[Q^{-1}]").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
