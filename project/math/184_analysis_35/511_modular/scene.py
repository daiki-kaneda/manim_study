from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ModularTheory(PacedScene):
    """#511 モジュラー理論：Δ と J が代数を記述（約45秒）"""

    def construct(self):
        self.show_heading("モジュラー理論")
        self.draw_ops()
        self.polar()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        d = RoundedRectangle(width=2.2, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.5 + UP * 0.3)
        j = RoundedRectangle(width=2.2, height=1.3, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.5 + UP * 0.3)
        self.play(
            Create(d), FadeIn(MathTex(r"\Delta", font_size=36).move_to(d)),
            Create(j), FadeIn(MathTex(r"J", font_size=36).move_to(j)),
            run_time=1.3,
        )
        note = self.ja_text("モジュラー作用素", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def polar(self):
        arrow = Arrow(LEFT * 1.1, RIGHT * 1.1, buff=0.1, color=ORANGE, stroke_width=4)
        cap = self.ja_text("極分解から", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("共役線形 J", font_size=24).move_to(self.note)
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
        eq = MathTex(r"S").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"S=J\Delta^{1/2},\quad JMJ=M'").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"S=J\Delta^{1/2},\quad JMJ=M'").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
