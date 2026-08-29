from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PolarDecomposition(PacedScene):
    """#357 極分解：A=U|A|（約45秒）"""

    def construct(self):
        self.show_heading("極分解")
        self.draw_stretch()
        self.rotate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_stretch(self):
        self.O = LEFT * 2.0 + DOWN * 0.1
        unit = Circle(radius=1.0, color=GREY, stroke_width=2).move_to(self.O)
        stretch = Ellipse(width=3.0, height=1.4, color=BLUE, stroke_width=3).move_to(self.O)
        self.play(Create(unit), run_time=0.9)
        self.play(TransformFromCopy(unit, stretch), run_time=1.2)
        note = self.ja_text("伸び |A|", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.stretch = stretch

    def rotate(self):
        arrow = Arrow(self.O + RIGHT * 1.6, RIGHT * 1.2 + DOWN * 0.1, buff=0.1, color=YELLOW, stroke_width=4)
        rot = Ellipse(width=3.0, height=1.4, color=ORANGE, stroke_width=3).move_to(RIGHT * 2.2 + DOWN * 0.1).rotate(0.6)
        cap = self.ja_text("回転 U", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.1)
        self.play(Create(rot), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("伸びてから回転", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"A").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"A=U|A|,\ |A|=\sqrt{A^{*}A}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A=U|A|,\ |A|=\sqrt{A^{*}A}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
