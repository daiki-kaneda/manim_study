from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CalculusOfVariations(PacedScene):
    """#224 変分：長さ最小は直線（約45秒）"""

    def construct(self):
        self.show_heading("変分法")
        self.draw_endpoints()
        self.compare_paths()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_endpoints(self):
        self.A = LEFT * 3.2 + DOWN * 1.0
        self.B = RIGHT * 3.2 + UP * 1.1
        self.play(
            FadeIn(Dot(self.A, color=YELLOW, radius=0.1)),
            FadeIn(Dot(self.B, color=YELLOW, radius=0.1)),
            run_time=0.9,
        )
        al = MathTex("A", font_size=28).next_to(self.A, DOWN, buff=0.12)
        bl = MathTex("B", font_size=28).next_to(self.B, UP, buff=0.12)
        self.play(FadeIn(al), FadeIn(bl), run_time=0.4)
        note = self.ja_text("両端固定", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compare_paths(self):
        wiggly = CubicBezier(self.A, self.A + UR * 1.8 + RIGHT * 0.5, self.B + DL * 1.5 + LEFT * 0.8, self.B)
        wiggly.set_color(RED).set_stroke(width=4)
        mid = CubicBezier(self.A, self.A + UP * 1.2 + RIGHT * 1.5, self.B + DOWN * 0.8 + LEFT * 1.2, self.B)
        mid.set_color(ORANGE).set_stroke(width=4)
        straight = Line(self.A, self.B, color=TEAL, stroke_width=5)
        self.play(Create(wiggly), run_time=1.1)
        cap = self.ja_text("長い", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.read(0.2)
        self.play(Create(mid), run_time=1.0)
        self.play(Create(straight), run_time=1.1)
        cap2 = self.ja_text("最短は直線", font_size=24).move_to(self.note)
        self.play(Indicate(straight, color=YELLOW), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\delta\int L(x,\dot x)\,dt").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\delta\int L(x,\dot x)\,dt=0").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\delta\int L(x,\dot x)\,dt=0").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
