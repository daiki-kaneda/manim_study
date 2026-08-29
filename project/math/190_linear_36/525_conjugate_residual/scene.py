from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ConjugateResidual(PacedScene):
    """#525 共役残差：A-共役で残差を直交化（約45秒）"""

    def construct(self):
        self.show_heading("共役残差")
        self.draw_dirs()
        self.residual()
        self.show_formula()
        self.read(1.4)

    def draw_dirs(self):
        arrows = VGroup(*[
            Arrow(ORIGIN, RIGHT * 1.5 + UP * (0.9 - i * 0.7), buff=0, color=c, stroke_width=4).shift(LEFT * 2.0)
            for i, c in enumerate([BLUE, TEAL, ORANGE])
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), run_time=1.4)
        note = self.ja_text("探索方向", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def residual(self):
        cap = self.ja_text("残差がA直交", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("対称系向け", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"r_i^\top A r_j=0\ (i\neq j)").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
