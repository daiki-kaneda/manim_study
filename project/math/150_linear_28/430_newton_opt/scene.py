from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class NewtonOptimization(PacedScene):
    """#430 ニュートン法：ヘッセで曲率補正（約45秒）"""

    def construct(self):
        self.show_heading("ニュートン法")
        self.draw_curve()
        self.newton_step()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        axes = Axes(x_range=[-0.5, 3.2, 1], y_range=[-0.5, 2.5, 1], x_length=6.2, y_length=3.0,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.2 + UP * 0.1)
        curve = axes.plot(lambda x: 0.25 * (x - 1.5) ** 2 + 0.4, x_range=[0.2, 3.0], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(curve), run_time=1.3)
        note = self.ja_text("二次近似", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def newton_step(self):
        x0 = 2.6
        p0 = Dot(self.axes.c2p(x0, 0.25 * (x0 - 1.5) ** 2 + 0.4), color=ORANGE, radius=0.1)
        # tangent / quadratic hint toward min at 1.5
        p1 = Dot(self.axes.c2p(1.5, 0.4), color=RED, radius=0.1)
        arrow = Arrow(p0.get_center(), p1.get_center(), buff=0.08, color=YELLOW, stroke_width=3)
        cap = self.ja_text("ヘッセで補正", font_size=24).move_to(self.note)
        self.play(FadeIn(p0), GrowArrow(arrow), FadeIn(p1), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("速い収束", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x_{+}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x_{+}=x-H^{-1}\nabla f").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x_{+}=x-H^{-1}\nabla f").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
