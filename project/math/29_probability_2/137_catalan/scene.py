from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Catalan(PacedScene):
    """#137 カタラン数（約45秒）"""

    def construct(self):
        self.show_heading("カタラン数")
        self.draw_grid()
        self.draw_paths()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_grid(self):
        self.origin = LEFT * 3.6 + DOWN * 1.7
        self.step = 1.15
        n = 4
        lines = VGroup()
        for i in range(n + 1):
            lines.add(Line(
                self.origin + RIGHT * (i * self.step),
                self.origin + RIGHT * (i * self.step) + UP * (n * self.step),
                color=GREY, stroke_width=2,
            ))
            lines.add(Line(
                self.origin + UP * (i * self.step),
                self.origin + UP * (i * self.step) + RIGHT * (n * self.step),
                color=GREY, stroke_width=2,
            ))
        diag = DashedLine(
            self.origin,
            self.origin + RIGHT * (n * self.step) + UP * (n * self.step),
            color=ORANGE, stroke_width=3,
        )
        self.play(Create(lines), run_time=1.6)
        self.play(Create(diag), run_time=0.8)
        self.read(0.35)
        self.n = n

    def _pt(self, i, j):
        return self.origin + RIGHT * (i * self.step) + UP * (j * self.step)

    def draw_paths(self):
        good = [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4)]
        bad = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 4)]
        gline = VMobject(color=YELLOW, stroke_width=6)
        gline.set_points_as_corners([self._pt(*p) for p in good])
        self.play(Create(gline), run_time=2.0)
        note = self.ja_text("対角線の下", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.4)
        bline = VMobject(color=RED, stroke_width=4)
        bline.set_points_as_corners([self._pt(*p) for p in bad])
        cap = self.ja_text("超えるとダメ", font_size=24).move_to(note)
        self.play(Create(bline), Transform(note, cap), run_time=1.6)
        self.read(0.5)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"C_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"C_n=\frac{1}{n+1}\binom{2n}{n}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"C_n=\frac{1}{n+1}\binom{2n}{n}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.8)
