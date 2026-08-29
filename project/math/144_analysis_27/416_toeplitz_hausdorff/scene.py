from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class ToeplitzHausdorff(PacedScene):
    """#416 トーエプリッツ・ハウスドルフ：数値域は凸（約45秒）"""

    def construct(self):
        self.show_heading("トーエプリッツ・ハウスドルフ")
        self.draw_field()
        self.convex()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_field(self):
        self.O = ORIGIN + DOWN * 0.1
        ax = Line(self.O + LEFT * 2.8, self.O + RIGHT * 2.8, color=GREY, stroke_width=2)
        ay = Line(self.O + DOWN * 1.8, self.O + UP * 1.8, color=GREY, stroke_width=2)
        blob = Ellipse(width=3.2, height=2.0, color=BLUE, fill_opacity=0.35, stroke_width=3).move_to(self.O + RIGHT * 0.3)
        self.play(Create(ax), Create(ay), FadeIn(blob), run_time=1.4)
        note = self.ja_text("数値域", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.blob = blob

    def convex(self):
        p = Dot(self.blob.get_center() + LEFT * 0.9 + UP * 0.3, color=ORANGE, radius=0.09)
        q = Dot(self.blob.get_center() + RIGHT * 0.8 + DOWN * 0.4, color=ORANGE, radius=0.09)
        seg = Line(p.get_center(), q.get_center(), color=YELLOW, stroke_width=3)
        cap = self.ja_text("2 点を結ぶ", font_size=24).move_to(self.note)
        self.play(FadeIn(p), FadeIn(q), Create(seg), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("線分も中に", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("数値域は凸集合", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
