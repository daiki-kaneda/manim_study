from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LatusRectum(PacedScene):
    """#614 通径：焦点を通り軸に垂直な弦（約45秒）"""

    def construct(self):
        self.show_heading("通径")
        self.draw_chord()
        self.length()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_chord(self):
        axes = Axes(x_range=[-2.5, 2.5, 1], y_range=[-1.5, 1.5, 1], x_length=5.5, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 1, "include_ticks": False}).shift(UP * 0.15)
        ell = Ellipse(width=4.0, height=2.4, color=BLUE, stroke_width=3).move_to(axes.c2p(0, 0))
        focus = Dot(axes.c2p(1.2, 0), color=YELLOW, radius=0.09)
        lr = Line(axes.c2p(1.2, -0.9), axes.c2p(1.2, 0.9), color=ORANGE, stroke_width=4)
        self.play(Create(axes), Create(ell), FadeIn(focus), Create(lr), run_time=1.4)
        note = self.ja_text("焦点を通る弦", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def length(self):
        cap = self.ja_text("軸に垂直", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("長さ 2b²/a", font_size=24).move_to(self.note)
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
        eq = MathTex(r"L").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"L=\frac{2b^2}{a}=2a(1-e^2)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"L=\frac{2b^2}{a}=2a(1-e^2)").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
