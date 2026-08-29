from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MirrorDescent(PacedScene):
    """#490 鏡面降下：双対空間で勾配、ミラー写像で戻す（約45秒）"""

    def construct(self):
        self.show_heading("鏡面降下")
        self.draw_spaces()
        self.mirror_map()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_spaces(self):
        primal = RoundedRectangle(width=2.4, height=1.5, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.5 + UP * 0.2)
        dual = RoundedRectangle(width=2.4, height=1.5, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.5 + UP * 0.2)
        self.play(
            Create(primal), FadeIn(MathTex(r"X", font_size=34).move_to(primal)),
            Create(dual), FadeIn(MathTex(r"X^*", font_size=34).move_to(dual)),
            run_time=1.3,
        )
        note = self.ja_text("双対で進む", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mirror_map(self):
        a1 = Arrow(LEFT * 1.1 + UP * 0.5, RIGHT * 1.1 + UP * 0.5, buff=0.1, color=ORANGE, stroke_width=3)
        a2 = Arrow(RIGHT * 1.1 + DOWN * 0.4, LEFT * 1.1 + DOWN * 0.4, buff=0.1, color=YELLOW, stroke_width=3)
        cap = self.ja_text("ミラー写像", font_size=24).move_to(self.note)
        self.play(GrowArrow(a1), GrowArrow(a2), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("Bregman距離", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x_{k+1}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x_{k+1}=\nabla\Phi^*(\nabla\Phi(x_k)-\eta\nabla f(x_k))").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x_{k+1}=\nabla\Phi^*(\nabla\Phi(x_k)-\eta\nabla f(x_k))").scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
