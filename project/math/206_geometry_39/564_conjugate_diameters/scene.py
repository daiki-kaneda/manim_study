from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ConjugateDiameters(PacedScene):
    """#564 共役直径：楕円の共役な直径対（約45秒）"""

    def construct(self):
        self.show_heading("共役直径")
        self.draw_ellipse()
        self.pair()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ellipse(self):
        ell = Ellipse(width=5.0, height=2.8, color=BLUE, stroke_width=3).shift(UP * 0.15)
        self.play(Create(ell), run_time=1.2)
        note = self.ja_text("楕円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def pair(self):
        d1 = Line(LEFT * 2.5 + UP * 0.15, RIGHT * 2.5 + UP * 0.15, color=ORANGE, stroke_width=4)
        d2 = Line(UP * 1.4 + LEFT * 0.3, DOWN * 1.1 + RIGHT * 0.3, color=YELLOW, stroke_width=4)
        cap = self.ja_text("共役な直径", font_size=24).move_to(self.note)
        self.play(Create(d1), Create(d2), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("中点の軌跡", font_size=24).move_to(self.note)
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
        formula = self.ja_text("共役直径：一方の中点が他方に平行", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
