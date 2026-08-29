from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BellmanOpt(PacedScene):
    """#632 ベルマン最適性：部分問題の最適をつなぐ（約45秒）"""

    def construct(self):
        self.show_heading("ベルマン最適性")
        self.draw_chain()
        self.principle()
        self.show_formula()
        self.read(1.4)

    def draw_chain(self):
        nodes = VGroup(*[
            Circle(radius=0.35, color=c, stroke_width=3).shift(pos)
            for c, pos in [(BLUE, LEFT * 3 + UP * 0.3), (ORANGE, ORIGIN + UP * 0.3), (TEAL, RIGHT * 3 + UP * 0.3)]
        ])
        labs = VGroup(*[MathTex(s, font_size=26).move_to(n) for s, n in zip([r"x_0", r"x_k", r"x_N"], nodes)])
        arrows = VGroup(
            Arrow(nodes[0].get_right(), nodes[1].get_left(), buff=0.08, stroke_width=3),
            Arrow(nodes[1].get_right(), nodes[2].get_left(), buff=0.08, stroke_width=3),
        )
        self.play(LaggedStart(*[Create(n) for n in nodes], lag_ratio=0.1), FadeIn(labs),
                  GrowArrow(arrows[0]), GrowArrow(arrows[1]), run_time=1.4)
        note = self.ja_text("部分軌道も最適", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def principle(self):
        cap = self.ja_text("最適性の原理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("動的計画の核", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"V(x)=\min_u\{c(x,u)+V(f(x,u))\}").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
