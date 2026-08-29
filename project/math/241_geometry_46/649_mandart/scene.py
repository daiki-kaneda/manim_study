from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MandartInellipse(PacedScene):
    """#649 マンダール楕円：傍接円の接点に接する内接楕円（約45秒）"""

    def construct(self):
        self.show_heading("マンダール楕円")
        self.draw_contacts()
        self.ine()
        self.show_formula()
        self.read(1.4)

    def draw_contacts(self):
        tri = Polygon(LEFT * 2.8 + DOWN * 1.1, RIGHT * 2.6 + DOWN * 1.1, UP * 1.7,
                      color=BLUE, stroke_width=3)
        contacts = VGroup(
            Dot(LEFT * 0.8 + DOWN * 1.1, color=YELLOW, radius=0.08),
            Dot(RIGHT * 1.5 + UP * 0.1, color=YELLOW, radius=0.08),
            Dot(LEFT * 1.6 + UP * 0.15, color=YELLOW, radius=0.08),
        )
        self.play(Create(tri), FadeIn(contacts), run_time=1.3)
        note = self.ja_text("傍接接点", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ine(self):
        ell = Ellipse(width=2.4, height=1.2, color=ORANGE, stroke_width=3).shift(DOWN * 0.15)
        cap = self.ja_text("接点内接楕円", font_size=24).move_to(self.note)
        self.play(Create(ell), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("ミトゥテン接点系", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"E=\mathrm{Mandart}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
