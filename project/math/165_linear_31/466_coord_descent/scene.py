from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CoordinateDescent(PacedScene):
    """#466 座標降下：一座標ずつ最小化（約45秒）"""

    def construct(self):
        self.show_heading("座標降下")
        self.draw_grid()
        self.steps()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_grid(self):
        axes = Axes(x_range=[-0.5, 3.5, 1], y_range=[-0.5, 3.5, 1], x_length=4.8, y_length=4.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 1.2 + UP * 0.1)
        # level curves ellipses
        levels = VGroup(*[
            Ellipse(width=w, height=h, color=BLUE, stroke_width=2).move_to(axes.c2p(1.5, 1.5))
            for w, h in [(3.2, 2.0), (2.2, 1.4), (1.2, 0.8)]
        ])
        self.play(Create(axes), LaggedStart(*[Create(e) for e in levels], lag_ratio=0.1), run_time=1.4)
        note = self.ja_text("等高線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def steps(self):
        pts = [(0.4, 2.8), (2.4, 2.8), (2.4, 1.2), (1.6, 1.2), (1.6, 1.5)]
        path = VMobject(color=ORANGE, stroke_width=4)
        path.set_points_as_corners([self.axes.c2p(x, y) for x, y in pts])
        dots = VGroup(*[Dot(self.axes.c2p(x, y), color=YELLOW, radius=0.08) for x, y in pts])
        cap = self.ja_text("軸に平行に動く", font_size=24).move_to(self.note)
        self.play(Create(path), FadeIn(dots), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("座標ごと最適化", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x_i\leftarrow\arg\min_{t}f(x_1,\ldots,t,\ldots)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x_i\leftarrow\arg\min_{t}f(x_1,\ldots,t,\ldots)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x_i\leftarrow\arg\min_{t}f(x_1,\ldots,t,\ldots)").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
