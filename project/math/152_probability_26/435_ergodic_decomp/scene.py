from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class ErgodicDecomposition(PacedScene):
    """#435 エルゴード分解：不変測度をエルゴードの重ねに（約45秒）"""

    def construct(self):
        self.show_heading("エルゴード分解")
        self.draw_mixture()
        self.decompose()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_mixture(self):
        big = Circle(radius=1.8, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.1)
        self.play(Create(big), run_time=1.0)
        note = self.ja_text("不変測度", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.big = big

    def decompose(self):
        parts = VGroup(*[
            Circle(radius=0.55, color=c, fill_opacity=0.4, stroke_width=2).shift(RIGHT * 1.8 + UP * dy)
            for dy, c in [(-1.1, ORANGE), (0.0, TEAL), (1.1, YELLOW)]
        ])
        arrows = VGroup(*[Arrow(LEFT * 0.3, RIGHT * 0.7, buff=0.05, color=GREY, stroke_width=3).shift(UP * dy) for dy in [-1.1, 0, 1.1]])
        cap = self.ja_text("部品に分ける", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), FadeIn(parts), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("各々エルゴード", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("不変測度はエルゴードの重ね", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
