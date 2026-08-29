from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np

class WienerMeasure(PacedScene):
    """#447 ウィーナー測度：経路空間のガウス測度（約45秒）"""

    def construct(self):
        self.show_heading("ウィーナー測度")
        self.draw_paths()
        self.measure()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_paths(self):
        import numpy as np
        axes = Axes(x_range=[0, 5.2, 1], y_range=[-1.6, 1.6, 1], x_length=6.5, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.25)
        rng = np.random.default_rng(5)
        paths = VGroup()
        for color in [BLUE, TEAL, ORANGE]:
            ys = np.cumsum(rng.normal(0, 0.25, size=35))
            ys -= ys[0]
            xs = np.linspace(0, 5, len(ys))
            p = VMobject(color=color, stroke_width=2.5)
            p.set_points_as_corners([axes.c2p(x, y) for x, y in zip(xs, ys)])
            paths.add(p)
        self.play(Create(axes), LaggedStart(*[Create(p) for p in paths], lag_ratio=0.12), run_time=1.7)
        note = self.ja_text("経路の束", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def measure(self):
        cap = self.ja_text("測度を載せる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ブラウンの法則", font_size=24).move_to(self.note)
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
        formula = self.ja_text("経路空間上のガウス測度", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
