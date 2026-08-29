from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SteinerEllipse(PacedScene):
    """#648 シュタイナー楕円：三角形の面積最大内接楕円（約45秒）"""

    def construct(self):
        self.show_heading("シュタイナー楕円")
        self.draw_tri()
        self.ellipse()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_tri(self):
        tri = Polygon(LEFT * 3 + DOWN * 1.2, RIGHT * 2.5 + DOWN * 1.2, UP * 1.8 + LEFT * 0.3,
                      color=BLUE, stroke_width=3)
        self.play(Create(tri), run_time=1.2)
        note = self.ja_text("三角形に内接", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.tri = tri

    def ellipse(self):
        ell = Ellipse(width=3.2, height=1.5, color=ORANGE, stroke_width=3).move_to(self.tri.get_center_of_mass() + DOWN * 0.15)
        cap = self.ja_text("面積最大", font_size=24).move_to(self.note)
        self.play(Create(ell), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("中点で接する", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\mathrm{area}(E)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathrm{area}(E)=\frac{\pi}{3\sqrt{3}}\,\mathrm{area}(\triangle)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathrm{area}(E)=\frac{\pi}{3\sqrt{3}}\,\mathrm{area}(\triangle)").scale(0.65)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
