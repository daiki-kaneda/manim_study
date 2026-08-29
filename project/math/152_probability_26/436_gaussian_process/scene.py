from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class GaussianProcess(PacedScene):
    """#436 ガウス過程：有限次元がすべて正規（約45秒）"""

    def construct(self):
        self.show_heading("ガウス過程")
        self.draw_samples()
        self.finite_dim()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_samples(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[-1.8, 1.8, 1], x_length=7.0, y_length=3.0,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.2)
        import numpy as np
        rng = np.random.default_rng(3)
        paths = VGroup()
        for color in [BLUE, TEAL, ORANGE]:
            ys = np.cumsum(rng.normal(0, 0.22, size=30))
            ys = ys - ys.mean()
            xs = np.linspace(0, 6, len(ys))
            p = VMobject(color=color, stroke_width=2.5)
            p.set_points_as_corners([axes.c2p(x, y) for x, y in zip(xs, ys)])
            paths.add(p)
        self.play(Create(axes), LaggedStart(*[Create(p) for p in paths], lag_ratio=0.15), run_time=1.8)
        note = self.ja_text("見本経路", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def finite_dim(self):
        xs = [1.5, 3.0, 4.5]
        dots = VGroup(*[Dot(self.axes.c2p(x, 0.3), color=YELLOW, radius=0.1) for x in xs])
        cap = self.ja_text("有限個の値", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("いつも正規", font_size=24).move_to(self.note)
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
        eq = MathTex(r"(X_{t_1},\ldots,X_{t_n})\sim\mathcal{N}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"(X_{t_1},\ldots,X_{t_n})\sim\mathcal{N}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"(X_{t_1},\ldots,X_{t_n})\sim\mathcal{N}").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
