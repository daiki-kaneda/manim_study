from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class AASimilarity(JapaneseScene):
    """#7 AA 相似（約90秒）"""

    def construct(self):
        self.title = self.show_heading("AA 相似")
        self.draw_triangles()
        self.mark_equal_angles()
        self.show_conclusion()
        self.hold(1.2)

    def draw_triangles(self):
        self.A = LEFT * 3.6 + UP * 1.7
        self.B = LEFT * 4.8 + DOWN * 1.4
        self.C = LEFT * 1.7 + DOWN * 1.4
        t1 = Polygon(self.A, self.B, self.C, color=BLUE, fill_opacity=0.35, stroke_width=2)
        labs1 = VGroup(
            MathTex("A", font_size=28).next_to(self.A, UP, buff=0.12),
            MathTex("B", font_size=28).next_to(self.B, DL, buff=0.1),
            MathTex("C", font_size=28).next_to(self.C, DR, buff=0.1),
        )
        self.play(Create(t1), FadeIn(labs1), run_time=0.9)

        self.D = RIGHT * 1.6 + UP * 1.35
        self.E = RIGHT * 0.55 + DOWN * 1.5
        self.F = RIGHT * 3.55 + DOWN * 1.5
        t2 = Polygon(self.D, self.E, self.F, color=ORANGE, fill_opacity=0.35, stroke_width=2)
        labs2 = VGroup(
            MathTex("D", font_size=28).next_to(self.D, UP, buff=0.12),
            MathTex("E", font_size=28).next_to(self.E, DL, buff=0.1),
            MathTex("F", font_size=28).next_to(self.F, DR, buff=0.1),
        )
        self.play(Create(t2), FadeIn(labs2), run_time=0.9)
        self.hold(0.6)
        self.t1, self.t2 = t1, t2

    def _angle_mark(self, vertex, p1, p2, color, radius=0.32):
        return Angle(Line(vertex, p1), Line(vertex, p2), radius=radius, color=color, stroke_width=3)

    def mark_equal_angles(self):
        a1 = self._angle_mark(self.A, self.B, self.C, BLUE)
        a2 = self._angle_mark(self.D, self.E, self.F, BLUE)
        b1 = self._angle_mark(self.B, self.A, self.C, ORANGE, radius=0.38)
        b2 = self._angle_mark(self.E, self.D, self.F, ORANGE, radius=0.38)
        self.play(Create(a1), Create(a2), run_time=0.8)
        eq1 = MathTex(r"\angle A=\angle D", font_size=32).to_edge(RIGHT, buff=0.55).shift(UP * 1.3)
        self.play(FadeIn(eq1), run_time=0.5)
        self.hold(0.7)
        self.play(Create(b1), Create(b2), run_time=0.8)
        eq2 = MathTex(r"\angle B=\angle E", font_size=32).next_to(eq1, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(FadeIn(eq2), run_time=0.5)
        self.hold(0.9)
        self.eqs = VGroup(eq1, eq2)

    def show_conclusion(self):
        sim = MathTex(r"\triangle ABC \sim \triangle DEF").scale(1.15)
        sim.to_edge(DOWN, buff=0.85)
        self.play(Write(sim), run_time=1.0)
        ratio = MathTex(r"\frac{AB}{DE}=\frac{AC}{DF}=\frac{BC}{EF}", font_size=36)
        ratio.next_to(sim, UP, buff=0.28)
        self.play(FadeIn(ratio), run_time=0.7)
        note = self.ja_text("2角が等しければ相似", font_size=26)
        note.next_to(self.eqs, DOWN, aligned_edge=RIGHT, buff=0.45)
        self.play(FadeIn(note), run_time=0.5)
        self.play(Indicate(sim, color=BLUE), run_time=0.8)
        self.hold(1.3)
