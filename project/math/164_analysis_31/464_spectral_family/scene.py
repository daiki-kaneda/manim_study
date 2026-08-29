from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SpectralFamily(PacedScene):
    """#464 スペクトル族：射影の増加族 E(λ)（約45秒）"""

    def construct(self):
        self.show_heading("スペクトル族")
        self.draw_line()
        self.projections()
        self.show_formula()
        self.read(1.4)

    def draw_line(self):
        self.O = LEFT * 0.3
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        self.play(Create(ax), run_time=0.9)
        note = self.ja_text("実軸上の λ", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.O = self.O

    def projections(self):
        boxes = VGroup(*[
            Square(side_length=0.75 + 0.15 * i, color=BLUE, fill_opacity=0.25 + 0.1 * i, stroke_width=2)
            .shift(LEFT * 2.2 + RIGHT * i * 1.2 + UP * 1.1)
            for i in range(4)
        ])
        labs = VGroup(*[MathTex(rf"E_{{\lambda_{i}}}", font_size=24).move_to(boxes[i]) for i in range(4)])
        # simpler labels
        labs = VGroup(*[MathTex(r"E", font_size=28).move_to(b) for b in boxes])
        cap = self.ja_text("射影が増える", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.12), FadeIn(labs), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("分解の単位", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\lambda\le\mu\implies E(\lambda)\le E(\mu)").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
