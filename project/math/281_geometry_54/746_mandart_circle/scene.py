from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MandartCircle(PacedScene):
    """#746 マンダール円：傍接円接点に関する円（約45秒）"""

    def construct(self):
        self.show_heading("マンダール円")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.6 + DOWN * 1.1, RIGHT * 2.6 + DOWN * 1.1, UP * 1.7, color=BLUE, stroke_width=3)
        contacts = VGroup(
            Dot(DOWN * 1.1, color=YELLOW, radius=0.08),
            Dot(RIGHT * 1.4 + UP * 0.2, color=YELLOW, radius=0.08),
            Dot(LEFT * 1.4 + UP * 0.2, color=YELLOW, radius=0.08),
        )
        circ = Circle(radius=0.85, color=ORANGE, stroke_width=3).shift(DOWN * 0.15)
        self.play(Create(tri), FadeIn(contacts), Create(circ), run_time=1.4)
        note = self.ja_text("傍接接点", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("共円配置", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("マンダール楕円と対", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"C_M").scale(0.95)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
