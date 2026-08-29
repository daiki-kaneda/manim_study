from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PascalIdentity(PacedScene):
    """#269 パスカル：隣り合う二項係数の和（約45秒）"""

    def construct(self):
        self.show_heading("パスカルの恒等式")
        self.draw_cells()
        self.add_up()
        self.show_formula()
        self.read(1.4)

    def draw_cells(self):
        # three cells: C(n-1,k-1), C(n-1,k) on top, C(n,k) below
        self.top_l = RoundedRectangle(width=1.6, height=0.9, corner_radius=0.08, color=BLUE, stroke_width=3)
        self.top_r = RoundedRectangle(width=1.6, height=0.9, corner_radius=0.08, color=TEAL, stroke_width=3)
        self.bot = RoundedRectangle(width=1.6, height=0.9, corner_radius=0.08, color=ORANGE, stroke_width=3)
        self.top_l.shift(LEFT * 1.5 + UP * 1.0)
        self.top_r.shift(RIGHT * 1.5 + UP * 1.0)
        self.bot.shift(DOWN * 0.5)
        l1 = MathTex(r"\binom{n-1}{k-1}", font_size=32).move_to(self.top_l)
        l2 = MathTex(r"\binom{n-1}{k}", font_size=32).move_to(self.top_r)
        l3 = MathTex(r"\binom{n}{k}", font_size=34).move_to(self.bot)
        self.play(FadeIn(self.top_l), FadeIn(self.top_r), FadeIn(l1), FadeIn(l2), run_time=1.4)
        note = self.ja_text("上の段", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.l3 = l3

    def add_up(self):
        plus = MathTex("+").scale(1.2).move_to(UP * 1.0)
        self.play(FadeIn(plus), run_time=0.4)
        arrows = VGroup(
            Arrow(self.top_l.get_bottom(), self.bot.get_top() + LEFT * 0.3, buff=0.1, color=YELLOW, stroke_width=3),
            Arrow(self.top_r.get_bottom(), self.bot.get_top() + RIGHT * 0.3, buff=0.1, color=YELLOW, stroke_width=3),
        )
        cap = self.ja_text("足すと下段", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrows[0]), GrowArrow(arrows[1]), FadeIn(self.bot), FadeIn(self.l3), Transform(self.note, cap), run_time=1.7)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}").scale(0.85)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
