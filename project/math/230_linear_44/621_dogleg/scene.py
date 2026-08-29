from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Dogleg(PacedScene):
    """#621 ドッグレッグ：信頼領域内の折れ線近似（約45秒）"""

    def construct(self):
        self.show_heading("ドッグレッグ")
        self.draw_path()
        self.steps()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        ball = Circle(radius=1.8, color=BLUE, stroke_width=3, fill_opacity=0.08).shift(LEFT * 0.2 + UP * 0.1)
        origin = Dot(ball.get_center(), color=YELLOW)
        cauchy = Dot(ball.get_center() + LEFT * 0.7 + DOWN * 0.3, color=ORANGE)
        newton = Dot(ball.get_center() + RIGHT * 1.5 + UP * 0.6, color=TEAL)
        path = VMobject(color=RED, stroke_width=4).set_points_as_corners(
            [origin.get_center(), cauchy.get_center(), newton.get_center()]
        )
        self.play(Create(ball), FadeIn(origin), FadeIn(cauchy), FadeIn(newton), Create(path), run_time=1.5)
        note = self.ja_text("折れ線経路", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def steps(self):
        cap = self.ja_text("コーシー→ニュートン", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("球との交点", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"s(\tau)=(1-\tau)s^{C}+\tau s^{N}").scale(0.78)
        formula.to_edge(DOWN, buff=0.18)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
