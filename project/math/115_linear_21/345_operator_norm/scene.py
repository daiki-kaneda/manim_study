from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class OperatorNorm(PacedScene):
    """#345 作用素ノルム：単位円の像の最大伸び（約45秒）"""

    def construct(self):
        self.show_heading("作用素ノルム")
        self.draw_unit()
        self.stretch()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_unit(self):
        self.O = LEFT * 2.2 + DOWN * 0.1
        self.unit = Circle(radius=1.2, color=GREY, stroke_width=3).move_to(self.O)
        self.play(Create(self.unit), run_time=1.1)
        note = self.ja_text("単位円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def stretch(self):
        image = Ellipse(width=3.4, height=1.6, color=ORANGE, stroke_width=4).move_to(RIGHT * 2.0 + DOWN * 0.1)
        arrow = Arrow(self.O + RIGHT * 1.3, image.get_left(), buff=0.1, color=YELLOW, stroke_width=4)
        cap = self.ja_text("線形写像", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.1)
        self.play(Create(image), run_time=1.1)
        self.read(0.25)
        # max radius marker
        r = Line(image.get_center(), image.get_center() + RIGHT * 1.7, color=TEAL, stroke_width=5)
        cap2 = self.ja_text("最大の伸び", font_size=24).move_to(self.note)
        self.play(Create(r), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"\|A\|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\|A\|=\sup_{\|x\|=1}\|Ax\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\|A\|=\sup_{\|x\|=1}\|Ax\|").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
