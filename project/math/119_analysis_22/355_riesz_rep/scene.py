from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class RieszRepresentation(PacedScene):
    """#355 リース表現：連続線形汎関数は内積（約45秒）"""

    def construct(self):
        self.show_heading("リースの表現定理")
        self.draw_functional()
        self.represent()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_functional(self):
        self.O = LEFT * 0.6 + DOWN * 0.2
        # hyperplane
        plane = Line(self.O + LEFT * 2.5 + UP * 1.2, self.O + RIGHT * 2.8 + DOWN * 0.8, color=BLUE, stroke_width=4)
        self.play(Create(plane), run_time=1.2)
        note = self.ja_text("連続汎関数", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def represent(self):
        v = Arrow(self.O, self.O + RIGHT * 0.9 + UP * 1.5, buff=0, color=ORANGE, stroke_width=5)
        cap = self.ja_text("あるベクトルで", font_size=24).move_to(self.note)
        self.play(GrowArrow(v), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("内積に書ける", font_size=24).move_to(self.note)
        form = MathTex(r"f(x)=\langle x,v\rangle", color=YELLOW, font_size=36).shift(DOWN * 0.3 + RIGHT * 1.5)
        self.play(Write(form), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"f(x)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"f(x)=\langle x,v_f\rangle").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"f(x)=\langle x,v_f\rangle").scale(1.0)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
