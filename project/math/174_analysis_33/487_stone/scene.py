from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class StonesTheorem(PacedScene):
    """#487 ストーンの定理：ユニタリ群は自己共役生成（約45秒）"""

    def construct(self):
        self.show_heading("ストーンの定理")
        self.draw_group()
        self.generator()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_group(self):
        circle = Circle(radius=1.4, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.1)
        arrow = Arc(radius=1.4, start_angle=0.2, angle=2.0, color=ORANGE, stroke_width=4).shift(LEFT * 2.2 + UP * 0.1)
        tip = Arrow(ORIGIN, RIGHT * 0.01, color=ORANGE).move_to(arrow.get_end())
        self.play(Create(circle), Create(arrow), run_time=1.4)
        note = self.ja_text("1径数ユニタリ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def generator(self):
        box = RoundedRectangle(width=2.6, height=1.4, corner_radius=0.12, color=TEAL, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.1)
        lab = MathTex(r"A=A^*", font_size=34).move_to(box)
        cap = self.ja_text("自己共役生成元", font_size=24).move_to(self.note)
        self.play(Create(box), FadeIn(lab), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("量子力学の時間発展", font_size=24).move_to(self.note)
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
        eq = MathTex(r"U(t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"U(t)=e^{-itA},\quad A=A^*").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"U(t)=e^{-itA},\quad A=A^*").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
