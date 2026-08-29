from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class OrderedBell(PacedScene):
    """#617 順序ベル数：集合の順序付き分割の総数（約45秒）"""

    def construct(self):
        self.show_heading("順序ベル数")
        self.draw_ordered()
        self.fubini()
        self.show_formula()
        self.read(1.4)

    def draw_ordered(self):
        blocks = VGroup(*[
            RoundedRectangle(width=1.5, height=0.9, corner_radius=0.1, color=c, stroke_width=3).shift(pos)
            for c, pos in [
                (BLUE, LEFT * 2.6 + UP * 0.5),
                (ORANGE, ORIGIN + UP * 0.5),
                (TEAL, RIGHT * 2.6 + UP * 0.5),
            ]
        ])
        arrows = VGroup(
            Arrow(blocks[0].get_right(), blocks[1].get_left(), buff=0.1, stroke_width=3),
            Arrow(blocks[1].get_right(), blocks[2].get_left(), buff=0.1, stroke_width=3),
        )
        labs = VGroup(
            MathTex(r"1", font_size=28).move_to(blocks[0]),
            MathTex(r"2", font_size=28).move_to(blocks[1]),
            MathTex(r"3", font_size=28).move_to(blocks[2]),
        )
        self.play(LaggedStart(*[Create(b) for b in blocks], lag_ratio=0.1), FadeIn(labs),
                  GrowArrow(arrows[0]), GrowArrow(arrows[1]), run_time=1.4)
        note = self.ja_text("ブロックに順序", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def fubini(self):
        cap = self.ja_text("フビニ数とも", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("選好配置の総数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"a_n=\sum_{k=0}^n k!\,S(n,k)").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
