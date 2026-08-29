from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class OpenMapping(PacedScene):
    """#296 開写像：全射有界線形は開集合を開へ（約45秒）"""

    def construct(self):
        self.show_heading("開写像定理")
        self.draw_sets()
        self.map_open()
        self.show_formula()
        self.read(1.4)

    def draw_sets(self):
        self.U = Circle(radius=1.3, color=BLUE, fill_opacity=0.35, stroke_width=3).shift(LEFT * 2.6 + UP * 0.2)
        self.play(FadeIn(self.U), run_time=1.0)
        note = self.ja_text("開集合 U", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def map_open(self):
        arrow = Arrow(LEFT * 0.9, RIGHT * 0.5, buff=0.1, color=YELLOW, stroke_width=4)
        T = MathTex(r"T", font_size=40).next_to(arrow, UP, buff=0.1)
        V = Ellipse(width=3.2, height=2.0, color=ORANGE, fill_opacity=0.35, stroke_width=3).shift(RIGHT * 2.5 + UP * 0.2)
        cap = self.ja_text("全射線形", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), FadeIn(T), Transform(self.note, cap), run_time=1.2)
        self.play(FadeIn(V), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("像も開", font_size=24).move_to(self.note)
        self.play(Indicate(V, color=YELLOW), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"U\text{ open}\Rightarrow T(U)\text{ open}").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
