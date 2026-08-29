from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BaireCategory(PacedScene):
    """#331 ベール：完備なら可算個の疎集合で尽くせない（約45秒）"""

    def construct(self):
        self.show_heading("ベールの範疇定理")
        self.draw_space()
        self.holes()
        self.show_formula()
        self.read(1.4)

    def draw_space(self):
        self.box = RoundedRectangle(width=6.5, height=3.4, corner_radius=0.1, color=BLUE, stroke_width=3).shift(UP * 0.15)
        self.play(Create(self.box), run_time=1.1)
        note = self.ja_text("完備空間", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def holes(self):
        holes = VGroup(*[
            Circle(radius=r, color=ORANGE, fill_opacity=0.35, stroke_width=2).move_to(pos)
            for r, pos in [
                (0.35, LEFT * 2.0 + UP * 0.6),
                (0.45, RIGHT * 0.3 + DOWN * 0.4),
                (0.3, RIGHT * 2.0 + UP * 0.5),
                (0.25, LEFT * 0.5 + UP * 0.9),
            ]
        ])
        cap = self.ja_text("疎な穴", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(h) for h in holes], lag_ratio=0.12), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        leftover = Dot(RIGHT * 1.2 + DOWN * 0.9, color=YELLOW, radius=0.12)
        cap2 = self.ja_text("残りがある", font_size=24).move_to(self.note)
        self.play(FadeIn(leftover, scale=0.5), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("疎集合では尽くせない", font_size=28)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
