from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FredholmAlternative(PacedScene):
    """#368 フレドホルムの択一：可解か核が非自明か（約45秒）"""

    def construct(self):
        self.show_heading("フレドホルムの択一")
        self.draw_two()
        self.choose()
        self.show_formula()
        self.read(1.4)

    def draw_two(self):
        left = RoundedRectangle(width=3.2, height=2.0, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.4 + UP * 0.2)
        right = RoundedRectangle(width=3.2, height=2.0, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.4 + UP * 0.2)
        l = self.ja_text("一意に解ける", font_size=26).move_to(left)
        r = self.ja_text("核が非自明", font_size=26).move_to(right)
        self.play(FadeIn(left), FadeIn(l), FadeIn(right), FadeIn(r), run_time=1.5)
        note = self.ja_text("二者択一", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.left, self.right = left, right

    def choose(self):
        or_txt = MathTex(r"\mathrm{or}", font_size=40).move_to(UP * 0.2)
        cap = self.ja_text("どちらか一方", font_size=24).move_to(self.note)
        self.play(FadeIn(or_txt), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("両立しない", font_size=24).move_to(self.note)
        self.play(Indicate(self.left, color=YELLOW), Indicate(self.right, color=YELLOW), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"Tx=y\ \text{solvable}\ \Leftrightarrow\ y\perp\ker T^{*}").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
