from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class IsaacsEquation(PacedScene):
    """#655 アイザック方程式：微分ゲームのHJB系（約45秒）"""

    def construct(self):
        self.show_heading("アイザック方程式")
        self.draw_game()
        self.minmax()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_game(self):
        a = RoundedRectangle(width=2.2, height=1.2, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.3 + UP * 0.3)
        b = RoundedRectangle(width=2.2, height=1.2, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.3 + UP * 0.3)
        self.play(Create(a), Create(b),
                  FadeIn(MathTex(r"\alpha", font_size=34).move_to(a)),
                  FadeIn(MathTex(r"\beta", font_size=34).move_to(b)), run_time=1.3)
        note = self.ja_text("二人零和", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def minmax(self):
        cap = self.ja_text("min max ハミルトン", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("粘性解で扱う", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\sup_\alpha\inf_\beta H").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sup_\alpha\inf_\beta H=0").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sup_\alpha\inf_\beta H=0").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
