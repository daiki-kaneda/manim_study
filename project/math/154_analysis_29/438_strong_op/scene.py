from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class StrongOperatorTopology(PacedScene):
    """#438 強作用素位相：各ベクトルで収束（約45秒）"""

    def construct(self):
        self.show_heading("強作用素位相")
        self.draw_vectors()
        self.apply()
        self.show_formula()
        self.read(1.4)

    def draw_vectors(self):
        self.O = LEFT * 2.5 + DOWN * 0.2
        v = Arrow(self.O, self.O + RIGHT * 1.8 + UP * 1.0, buff=0, color=BLUE, stroke_width=4)
        self.play(GrowArrow(v), run_time=1.0)
        note = self.ja_text("ベクトルごと", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def apply(self):
        tips = VGroup(*[
            Dot(self.O + RIGHT * (1.2 + 0.2 * i) + UP * (0.7 + 0.1 * i), color=c, radius=0.08)
            for i, c in enumerate([GREY, TEAL, ORANGE, RED])
        ])
        arrows = VGroup(*[
            Arrow(self.O, t.get_center(), buff=0.05, color=t.get_color(), stroke_width=2)
            for t in tips
        ])
        cap = self.ja_text("像が動く", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("点ごとに収束", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"T_n\xrightarrow{s}T\iff T_nx\to Tx\ \forall x").scale(0.78)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
