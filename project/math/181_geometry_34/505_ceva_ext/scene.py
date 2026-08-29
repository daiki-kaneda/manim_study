from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CevaExtension(PacedScene):
    """#505 チェバの拡張：三角以外や有向比へ（約45秒）"""

    def construct(self):
        self.show_heading("チェバの拡張")
        self.draw_triangle()
        self.signed()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.15
        self.B = LEFT * 2.7 + DOWN * 1.45
        self.C = RIGHT * 2.7 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        D = self.B * 0.4 + self.C * 0.6
        E = self.A * 0.35 + self.C * 0.65
        F = self.A * 0.55 + self.B * 0.45
        lines = VGroup(Line(self.A, D, color=ORANGE), Line(self.B, E, color=ORANGE), Line(self.C, F, color=ORANGE))
        self.play(Create(self.tri), LaggedStart(*[Create(l) for l in lines], lag_ratio=0.1), run_time=1.4)
        note = self.ja_text("共点チェバ", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def signed(self):
        cap = self.ja_text("有向比でも成立", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("三角関数形も", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\frac{\sin\angle BAP}{\sin\angle PAC}\cdot\frac{\sin\angle CBP}{\sin\angle PBA}\cdot\frac{\sin\angle ACP}{\sin\angle PCB}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\frac{\sin\angle BAP}{\sin\angle PAC}\cdot\frac{\sin\angle CBP}{\sin\angle PBA}\cdot\frac{\sin\angle ACP}{\sin\angle PCB}=1").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\frac{\sin\angle BAP}{\sin\angle PAC}\cdot\frac{\sin\angle CBP}{\sin\angle PBA}\cdot\frac{\sin\angle ACP}{\sin\angle PCB}=1").scale(0.55)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
