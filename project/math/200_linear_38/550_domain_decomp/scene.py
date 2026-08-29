from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class DomainDecomposition(PacedScene):
    """#550 領域分割：部分領域で並列に解く（約45秒）"""

    def construct(self):
        self.show_heading("領域分割")
        self.draw_domain()
        self.overlap()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_domain(self):
        big = RoundedRectangle(width=5.5, height=3.0, corner_radius=0.1, color=GREY, stroke_width=2).shift(UP * 0.15)
        left = RoundedRectangle(width=2.8, height=2.6, corner_radius=0.08, color=BLUE, stroke_width=3, fill_opacity=0.2).shift(LEFT * 1.2 + UP * 0.15)
        right = RoundedRectangle(width=2.8, height=2.6, corner_radius=0.08, color=ORANGE, stroke_width=3, fill_opacity=0.2).shift(RIGHT * 1.2 + UP * 0.15)
        self.play(Create(big), FadeIn(left), FadeIn(right), run_time=1.4)
        note = self.ja_text("部分領域", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def overlap(self):
        cap = self.ja_text("重なり／界面条件", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("並列計算向き", font_size=24).move_to(self.note)
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
        formula = self.ja_text("領域分割：部分問題を反復結合", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
