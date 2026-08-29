from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class StirlingFirstKind(PacedScene):
    """#257 スターリング第一種はサイクルへの分割（約45秒）"""

    def construct(self):
        self.show_heading("スターリング第一種")
        self.draw_elements()
        self.make_cycles()
        self.show_formula()
        self.read(1.4)

    def draw_elements(self):
        self.dots = VGroup()
        labs = VGroup()
        for i, name in enumerate("1234"):
            p = LEFT * 2.6 + RIGHT * i * 1.5 + UP * 1.6
            d = Dot(p, radius=0.13, color=WHITE)
            lab = MathTex(name, font_size=28).next_to(d, UP, buff=0.1)
            self.dots.add(d)
            labs.add(lab)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in self.dots], lag_ratio=0.12), run_time=1.4)
        self.play(FadeIn(labs), run_time=0.4)
        note = self.ja_text("4 個", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def make_cycles(self):
        # two cycles: (1 2) and (3 4)
        c1 = ArcBetweenPoints(self.dots[0].get_center(), self.dots[1].get_center(), angle=-PI * 0.8, color=BLUE, stroke_width=4)
        c1b = ArcBetweenPoints(self.dots[1].get_center(), self.dots[0].get_center(), angle=-PI * 0.8, color=BLUE, stroke_width=4)
        c2 = ArcBetweenPoints(self.dots[2].get_center(), self.dots[3].get_center(), angle=-PI * 0.8, color=ORANGE, stroke_width=4)
        c2b = ArcBetweenPoints(self.dots[3].get_center(), self.dots[2].get_center(), angle=-PI * 0.8, color=ORANGE, stroke_width=4)
        cap = self.ja_text("2 サイクル", font_size=24).move_to(self.note)
        self.play(Create(c1), Create(c1b), Create(c2), Create(c2b), Transform(self.note, cap), run_time=1.7)
        self.read(0.3)
        # one 4-cycle sketch
        ring = Ellipse(width=5.2, height=1.6, color=TEAL, stroke_width=3).move_to(ORIGIN + DOWN * 0.6)
        cap2 = self.ja_text("サイクル分割", font_size=24).move_to(self.note)
        self.play(Create(ring), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"c(n,k)=\begin{bmatrix}n\\k\end{bmatrix}").scale(1.0)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
