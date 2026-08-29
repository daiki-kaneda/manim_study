from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class ResolventIdentity(PacedScene):
    """#427 リゾルベント恒等式：差は積で表す（約45秒）"""

    def construct(self):
        self.show_heading("リゾルベント恒等式")
        self.draw_points()
        self.identity()
        self.show_formula()
        self.read(1.4)

    def draw_points(self):
        self.O = ORIGIN
        ax = Line(LEFT * 3, RIGHT * 3, color=GREY, stroke_width=2)
        ay = Line(DOWN * 1.8, UP * 1.8, color=GREY, stroke_width=2)
        z = Dot(RIGHT * 1.6 + UP * 1.0, color=BLUE, radius=0.1)
        w = Dot(RIGHT * 2.2 + DOWN * 0.6, color=ORANGE, radius=0.1)
        zl = MathTex("z", font_size=28).next_to(z, UR, buff=0.08)
        wl = MathTex("w", font_size=28).next_to(w, DR, buff=0.08)
        self.play(Create(ax), Create(ay), FadeIn(z), FadeIn(w), FadeIn(zl), FadeIn(wl), run_time=1.4)
        note = self.ja_text("2 点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def identity(self):
        cap = self.ja_text("差を展開", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("積で結ぶ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"R(z)-R(w)=(w-z)R(z)R(w)").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
