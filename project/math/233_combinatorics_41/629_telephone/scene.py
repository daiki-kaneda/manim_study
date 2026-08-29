from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class TelephoneNumbers(PacedScene):
    """#629 電話番号：完全マッチングを含む対合の数（約45秒）"""

    def construct(self):
        self.show_heading("電話番号")
        self.draw_involution()
        self.recurrence()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_involution(self):
        dots = VGroup(*[Dot(LEFT * 3 + RIGHT * i * 1.2 + UP * 0.4, color=BLUE, radius=0.12) for i in range(6)])
        # fixed points and a 2-cycle
        arcs = VGroup(
            ArcBetweenPoints(dots[0].get_center() + UP * 0.05, dots[1].get_center() + UP * 0.05, angle=-PI / 2, color=ORANGE, stroke_width=3),
            ArcBetweenPoints(dots[3].get_center() + UP * 0.05, dots[5].get_center() + UP * 0.05, angle=-PI / 2.5, color=ORANGE, stroke_width=3),
        )
        fixes = VGroup(*[Line(d.get_center() + DOWN * 0.15, d.get_center() + DOWN * 0.55, color=TEAL, stroke_width=3) for d in [dots[2], dots[4]]])
        self.play(FadeIn(dots), Create(arcs), Create(fixes), run_time=1.4)
        note = self.ja_text("対合の図", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def recurrence(self):
        cap = self.ja_text("固定点か2-cycle", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("インボリューション", font_size=22).move_to(self.note)
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
        eq = MathTex(r"T_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"T_n=T_{n-1}+(n-1)T_{n-2}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"T_n=T_{n-1}+(n-1)T_{n-2}").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
