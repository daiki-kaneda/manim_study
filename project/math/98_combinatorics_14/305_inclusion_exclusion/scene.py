from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class InclusionExclusion(PacedScene):
    """#305 包除原理：和から交わりを調整（約45秒）"""

    def construct(self):
        self.show_heading("包除原理")
        self.draw_sets()
        self.include_exclude()
        self.show_formula()
        self.read(1.4)

    def draw_sets(self):
        self.A = Circle(radius=1.5, color=BLUE, fill_opacity=0.35, stroke_width=3).shift(LEFT * 1.1 + UP * 0.2)
        self.B = Circle(radius=1.5, color=TEAL, fill_opacity=0.35, stroke_width=3).shift(RIGHT * 1.1 + UP * 0.2)
        self.play(FadeIn(self.A), FadeIn(self.B), run_time=1.3)
        note = self.ja_text("2 つの集合", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def include_exclude(self):
        plus = MathTex(r"|A|+|B|", font_size=36).shift(DOWN * 0.9 + LEFT * 1.5)
        minus = MathTex(r"-|A\cap B|", font_size=36, color=ORANGE).shift(DOWN * 0.9 + RIGHT * 1.6)
        cap = self.ja_text("足して", font_size=24).move_to(self.note)
        self.play(Write(plus), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        # highlight intersection
        inter = Intersection(self.A, self.B, color=ORANGE, fill_opacity=0.55, stroke_width=2)
        cap2 = self.ja_text("交わりを引く", font_size=24).move_to(self.note)
        self.play(FadeIn(inter), Write(minus), Transform(self.note, cap2), run_time=1.4)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"|A\cup B|=|A|+|B|-|A\cap B|").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
