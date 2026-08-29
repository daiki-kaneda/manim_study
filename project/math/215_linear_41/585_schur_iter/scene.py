from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class SchurComplementIter(PacedScene):
    """#585 シューア補完反復：ブロック消去で解く（約45秒）"""

    def construct(self):
        self.show_heading("シューア補完反復")
        self.draw_blocks()
        self.reduce()
        self.show_formula()
        self.read(1.4)

    def draw_blocks(self):
        A = RoundedRectangle(width=1.6, height=1.2, corner_radius=0.08, color=BLUE, stroke_width=2).shift(LEFT * 2.4 + UP * 0.7)
        B = RoundedRectangle(width=1.6, height=1.2, corner_radius=0.08, color=TEAL, stroke_width=2).shift(LEFT * 0.5 + UP * 0.7)
        C = RoundedRectangle(width=1.6, height=1.2, corner_radius=0.08, color=ORANGE, stroke_width=2).shift(LEFT * 2.4 + DOWN * 0.7)
        D = RoundedRectangle(width=1.6, height=1.2, corner_radius=0.08, color=YELLOW, stroke_width=2).shift(LEFT * 0.5 + DOWN * 0.7)
        labs = VGroup(
            MathTex("A", font_size=28).move_to(A), MathTex("B", font_size=28).move_to(B),
            MathTex("C", font_size=28).move_to(C), MathTex("D", font_size=28).move_to(D),
        )
        self.play(Create(A), Create(B), Create(C), Create(D), FadeIn(labs), run_time=1.4)
        note = self.ja_text("2×2 ブロック", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def reduce(self):
        S = RoundedRectangle(width=2.4, height=1.3, corner_radius=0.1, color=RED, stroke_width=3).shift(RIGHT * 2.4 + UP * 0.1)
        cap = self.ja_text("シューア補元へ縮約", font_size=24).move_to(self.note)
        self.play(Create(S), FadeIn(MathTex(r"S", font_size=34).move_to(S)), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("小さい系を反復", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"S=D-CA^{-1}B").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
