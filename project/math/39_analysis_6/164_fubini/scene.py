from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Fubini(PacedScene):
    """#164 フビニは縦割り横割り（約45秒）"""

    def construct(self):
        self.origin = LEFT * 3.2 + DOWN * 1.55
        self.show_heading("フビニの定理")
        self.draw_region()
        self.slice_both_ways()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_region(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 5.8, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.5, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.region = Polygon(
            self.origin + RIGHT * 0.5 + UP * 0.4,
            self.origin + RIGHT * 4.2 + UP * 0.55,
            self.origin + RIGHT * 3.6 + UP * 2.85,
            self.origin + RIGHT * 0.9 + UP * 2.4,
            color=BLUE,
            fill_opacity=0.35,
            stroke_width=3,
        )
        self.play(FadeIn(self.region), run_time=1.2)
        note = self.ja_text("領域", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def slice_both_ways(self):
        verts = VGroup()
        for i in range(6):
            x = 0.85 + i * 0.55
            verts.add(Line(
                self.origin + RIGHT * x + UP * 0.5,
                self.origin + RIGHT * x + UP * (2.2 + 0.08 * i),
                color=YELLOW,
                stroke_width=4,
            ))
        cap = self.ja_text("縦に切る", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(v) for v in verts], lag_ratio=0.12), Transform(self.note, cap), run_time=1.8)
        self.read(0.35)
        hors = VGroup()
        for i in range(5):
            y = 0.7 + i * 0.4
            hors.add(Line(
                self.origin + RIGHT * 0.7 + UP * y,
                self.origin + RIGHT * (3.7 - 0.1 * i) + UP * y,
                color=ORANGE,
                stroke_width=4,
            ))
        cap2 = self.ja_text("横に切る", font_size=24).move_to(self.note)
        self.play(FadeOut(verts), LaggedStart(*[Create(h) for h in hors], lag_ratio=0.12), Transform(self.note, cap2), run_time=1.8)
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
        eq = MathTex(r"\iint_D f").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\iint_D f=\int\!\int f\,dx\,dy=\int\!\int f\,dy\,dx").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\iint_D f=\int\!\int f\,dx\,dy=\int\!\int f\,dy\,dx").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
