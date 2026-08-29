from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class CosineArea(PacedScene):
    """#444 余弦面積：ヘロン前の展開（約45秒）"""

    def construct(self):
        self.show_heading("余弦面積")
        self.draw_triangle()
        self.expand()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.6 + DOWN * 1.4
        self.C = RIGHT * 2.7 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("3 辺", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def expand(self):
        fill = Polygon(self.A, self.B, self.C, color=TEAL, fill_opacity=0.3, stroke_width=0)
        cap = self.ja_text("cos で展開", font_size=24).move_to(self.note)
        self.play(FadeIn(fill), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("面積の二乗", font_size=24).move_to(self.note)
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
        eq = MathTex(r"16S^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"16S^{2}=4a^{2}b^{2}-(a^{2}+b^{2}-c^{2})^{2}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"16S^{2}=4a^{2}b^{2}-(a^{2}+b^{2}-c^{2})^{2}").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
