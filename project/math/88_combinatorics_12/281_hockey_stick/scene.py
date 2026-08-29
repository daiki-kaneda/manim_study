from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HockeyStick(PacedScene):
    """#281 ホッケースティック：斜め和は次の段（約45秒）"""

    def construct(self):
        self.show_heading("ホッケースティック恒等式")
        self.draw_diagonal()
        self.sum_to_next()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_diagonal(self):
        # Pascal-like diagonal cells
        self.cells = VGroup()
        labels = [
            r"\binom{r}{r}",
            r"\binom{r+1}{r}",
            r"\binom{r+2}{r}",
            r"\binom{r+3}{r}",
        ]
        for i, lab in enumerate(labels):
            box = RoundedRectangle(width=1.35, height=0.75, corner_radius=0.08, color=BLUE, stroke_width=3)
            box.shift(LEFT * 2.4 + RIGHT * i * 1.15 + UP * (1.2 - i * 0.35))
            t = MathTex(lab, font_size=28).move_to(box)
            self.cells.add(VGroup(box, t))
        self.play(LaggedStart(*[FadeIn(c) for c in self.cells], lag_ratio=0.12), run_time=1.6)
        note = self.ja_text("斜めの項", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sum_to_next(self):
        result = RoundedRectangle(width=1.6, height=0.85, corner_radius=0.08, color=ORANGE, stroke_width=3)
        result.shift(RIGHT * 2.5 + DOWN * 0.6)
        lab = MathTex(r"\binom{r+4}{r+1}", font_size=30).move_to(result)
        arrows = VGroup(*[
            Arrow(c.get_right(), result.get_left() + UP * (0.4 - i * 0.2), buff=0.1, color=YELLOW, stroke_width=3)
            for i, c in enumerate(self.cells)
        ])
        cap = self.ja_text("全部足す", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08), Transform(self.note, cap), run_time=1.5)
        self.read(0.2)
        cap2 = self.ja_text("次の段", font_size=24).move_to(self.note)
        self.play(FadeIn(result), FadeIn(lab), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"\sum_{i").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sum_{i=r}^{n}\binom{i}{r}=\binom{n+1}{r+1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sum_{i=r}^{n}\binom{i}{r}=\binom{n+1}{r+1}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
