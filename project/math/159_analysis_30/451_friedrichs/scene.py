from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class FriedrichsExtension(PacedScene):
    """#451 フリードリヒス：半有界作用素の自己共役拡張（約45秒）"""

    def construct(self):
        self.show_heading("フリードリヒス拡張")
        self.draw_form()
        self.extend()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_form(self):
        axes = Axes(x_range=[-0.5, 3.5, 1], y_range=[0, 2.2, 1], x_length=5.5, y_length=2.6,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.6 + UP * 0.3)
        curve = axes.plot(lambda x: 0.25 * x * x + 0.4, x_range=[0.1, 3.2], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(curve), run_time=1.3)
        note = self.ja_text("半有界", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def extend(self):
        box = RoundedRectangle(width=3.2, height=1.3, corner_radius=0.12, color=ORANGE, stroke_width=3).shift(DOWN * 0.9 + RIGHT * 0.5)
        lab = MathTex(r"A_F", font_size=36).move_to(box)
        cap = self.ja_text("二次形式から", font_size=24).move_to(self.note)
        self.play(Create(box), FadeIn(lab), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("自己共役拡張", font_size=24).move_to(self.note)
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
        formula = self.ja_text("半有界なら正の自己共役拡張", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
