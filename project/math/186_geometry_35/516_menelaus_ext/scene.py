from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MenelausExtension(PacedScene):
    """#516 メネラウスの拡張：有向比・球面などへ（約45秒）"""

    def construct(self):
        self.show_heading("メネラウスの拡張")
        self.draw_transversal()
        self.signed()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_transversal(self):
        A, B, C = UP * 2.1, LEFT * 2.8 + DOWN * 1.4, RIGHT * 2.8 + DOWN * 1.3
        tri = Polygon(A, B, C, color=BLUE, stroke_width=3)
        line = Line(LEFT * 3.2 + UP * 0.6, RIGHT * 3.2 + DOWN * 0.9, color=ORANGE, stroke_width=3)
        self.play(Create(tri), Create(line), run_time=1.3)
        note = self.ja_text("横断線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def signed(self):
        cap = self.ja_text("有向比版", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("球面でも類似", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA}=-1").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA}=-1").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
