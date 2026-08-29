from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CSDecomposition(PacedScene):
    """#358 CS 分解：部分空間の角を余弦・正弦で（約45秒）"""

    def construct(self):
        self.show_heading("CS 分解")
        self.draw_planes()
        self.angles()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_planes(self):
        self.O = ORIGIN + DOWN * 0.1
        p1 = Line(self.O + LEFT * 2.8, self.O + RIGHT * 2.8, color=BLUE, stroke_width=4)
        p2 = Line(self.O + LEFT * 2.4 + DOWN * 1.0, self.O + RIGHT * 2.4 + UP * 1.0, color=TEAL, stroke_width=4)
        self.play(Create(p1), Create(p2), run_time=1.3)
        note = self.ja_text("2 部分空間", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def angles(self):
        ang = Angle(
            Line(self.O, self.O + RIGHT * 2),
            Line(self.O, self.O + RIGHT * 1.8 + UP * 0.75),
            radius=0.7,
            color=ORANGE,
        )
        cap = self.ja_text("主角度", font_size=24).move_to(self.note)
        self.play(Create(ang), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cs = MathTex(r"C,S", color=YELLOW, font_size=42).shift(DOWN * 0.6 + RIGHT * 2.2)
        cap2 = self.ja_text("cos / sin", font_size=24).move_to(self.note)
        self.play(FadeIn(cs), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"U^{*}PV").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"U^{*}PV=\mathrm{diag}(C,S),\ C^{2}+S^{2}=I").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"U^{*}PV=\mathrm{diag}(C,S),\ C^{2}+S^{2}=I").scale(0.75)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
