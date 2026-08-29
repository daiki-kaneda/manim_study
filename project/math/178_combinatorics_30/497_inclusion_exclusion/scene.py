from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class InclusionExclusion(PacedScene):
    """#497 包含排除原理：和集合を足して引いて（約45秒）"""

    def construct(self):
        self.show_heading("包含排除原理")
        self.draw_venn()
        self.signs()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_venn(self):
        a = Circle(radius=1.3, color=BLUE, stroke_width=3, fill_opacity=0.25).shift(LEFT * 1.0 + UP * 0.3)
        b = Circle(radius=1.3, color=ORANGE, stroke_width=3, fill_opacity=0.25).shift(RIGHT * 1.0 + UP * 0.3)
        c = Circle(radius=1.3, color=TEAL, stroke_width=3, fill_opacity=0.2).shift(DOWN * 0.9)
        self.play(FadeIn(a), FadeIn(b), FadeIn(c), run_time=1.4)
        note = self.ja_text("3 集合", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def signs(self):
        plus = MathTex(r"+", font_size=48, color=GREEN).shift(RIGHT * 3.0 + UP * 0.8)
        minus = MathTex(r"-", font_size=48, color=RED).shift(RIGHT * 3.0 + DOWN * 0.2)
        cap = self.ja_text("足して引く", font_size=24).move_to(self.note)
        self.play(FadeIn(plus), FadeIn(minus), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("交差を補正", font_size=24).move_to(self.note)
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
        eq = MathTex(r"|A\cup B\cup C|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|B\cap C|-|C\cap A|+|A\cap B\cap C|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(
            r"|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|B\cap C|-|C\cap A|+|A\cap B\cap C|"
        ).scale(0.52)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
