from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ExtouchTriangle(PacedScene):
    """#650 傍接点三角形：傍接円の接点が作る三角形（約45秒）"""

    def construct(self):
        self.show_heading("傍接点三角形")
        self.draw()
        self.props()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.8 + DOWN * 1.2, RIGHT * 2.8 + DOWN * 1.2, UP * 1.8,
                      color=BLUE, stroke_width=3)
        inc = Circle(radius=0.7, color=ORANGE, stroke_width=3).shift(DOWN * 0.35)
        # contact approx
        X = Dot(DOWN * 1.05, color=YELLOW, radius=0.08)
        Y = Dot(RIGHT * 1.35 + UP * 0.25, color=YELLOW, radius=0.08)
        Z = Dot(LEFT * 1.35 + UP * 0.25, color=YELLOW, radius=0.08)
        contact_tri = Polygon(X.get_center(), Y.get_center(), Z.get_center(), color=TEAL, stroke_width=3)
        self.play(Create(tri), Create(inc), FadeIn(VGroup(X, Y, Z)), Create(contact_tri), run_time=1.5)
        note = self.ja_text("接点を結ぶ", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def props(self):
        cap = self.ja_text("接触三角形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ナーゲル点へ", font_size=24).move_to(self.note)
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
        eq = MathTex(r"XY").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"XY=s-c,\ YZ=s-a,\ ZX=s-b").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"XY=s-c,\ YZ=s-a,\ ZX=s-b").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
