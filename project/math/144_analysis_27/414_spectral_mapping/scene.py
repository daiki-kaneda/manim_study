from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class SpectralMapping(PacedScene):
    """#414 スペクトル写像：σ(f(A))=f(σ(A))（約45秒）"""

    def construct(self):
        self.show_heading("スペクトル写像")
        self.draw_spec()
        self.map_f()
        self.show_formula()
        self.read(1.4)

    def draw_spec(self):
        self.O = LEFT * 0.3 + DOWN * 0.1
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        self.eigs = VGroup(*[Dot(self.O + RIGHT * x, color=BLUE, radius=0.1) for x in [-1.8, 0.2, 1.5]])
        self.play(Create(ax), FadeIn(self.eigs), run_time=1.3)
        note = self.ja_text("σ(A)", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def map_f(self):
        imgs = VGroup(*[Dot(self.O + RIGHT * (x * x * 0.45) + UP * 1.3, color=ORANGE, radius=0.1) for x in [-1.8, 0.2, 1.5]])
        arrows = VGroup(*[Arrow(e.get_center(), i.get_center(), buff=0.08, color=YELLOW, stroke_width=3) for e, i in zip(self.eigs, imgs)])
        cap = self.ja_text("f を当てる", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), Transform(self.note, cap), run_time=1.4)
        self.play(FadeIn(imgs), run_time=0.8)
        self.read(0.25)
        cap2 = self.ja_text("像がスペクトル", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\sigma(f(A))=f(\sigma(A))").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
