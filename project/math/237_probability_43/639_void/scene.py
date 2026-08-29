from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class VoidProbability(PacedScene):
    """#639 ボイド確率：領域が空である確率（約45秒）"""

    def construct(self):
        self.show_heading("ボイド確率")
        self.draw_region()
        self.empty()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_region(self):
        import random
        random.seed(11)
        plane = NumberPlane(x_range=[-3, 3, 1], y_range=[-1.5, 1.5, 1], x_length=6.5, y_length=2.8,
                            background_line_style={"stroke_opacity": 0.2}).shift(UP * 0.1)
        pts = VGroup(*[Dot([random.uniform(-2.8, 2.8), random.uniform(-1.2, 1.2), 0], radius=0.07, color=BLUE)
                       for _ in range(16)])
        region = RoundedRectangle(width=2.2, height=1.4, corner_radius=0.1, color=ORANGE, stroke_width=3,
                                  fill_opacity=0.15).shift(LEFT * 0.3 + UP * 0.1)
        self.play(Create(plane), FadeIn(pts), Create(region), run_time=1.4)
        note = self.ja_text("領域 B", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def empty(self):
        cap = self.ja_text("点が入らない", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("生成汎関数へ", font_size=24).move_to(self.note)
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
        eq = MathTex(r"v(B)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"v(B)=P(\Phi\cap B=\emptyset)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"v(B)=P(\Phi\cap B=\emptyset)").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
