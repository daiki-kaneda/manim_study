from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SurfaceOfRevolution(PacedScene):
    """#162 回転面の面積は帯の積み重ね（約45秒）"""

    def construct(self):
        self.show_heading("回転面")
        self.draw_curve()
        self.stack_bands()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[-2.0, 2.0, 1],
            x_length=7.4,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.12 + LEFT * 0.4)
        self.curve = self.axes.plot(
            lambda x: 0.55 + 0.55 * (x / 3.5) ** 0.7,
            x_range=[0.3, 3.6],
            color=BLUE,
            stroke_width=5,
        )
        axis = self.axes.plot(lambda x: 0, x_range=[0.2, 3.9], color=GREY, stroke_width=2)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.curve), Create(axis), run_time=1.7)
        note = self.ja_text("軸のまわり", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def _band(self, x, color=YELLOW):
        y = 0.55 + 0.55 * (x / 3.5) ** 0.7
        c = self.axes.c2p(x, 0)
        h = abs(self.axes.c2p(x, y)[1] - c[1])
        return Ellipse(width=0.28, height=2 * h, color=color, fill_opacity=0.18, stroke_width=3).move_to(c)

    def stack_bands(self):
        xs = [0.7, 1.35, 2.0, 2.65, 3.25]
        bands = VGroup(*[self._band(x) for x in xs])
        cap = self.ja_text("帯を積む", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(b, scale=0.5) for b in bands], lag_ratio=0.16), Transform(self.note, cap), run_time=2.2)
        self.read(0.4)
        slant = Line(self.axes.c2p(1.9, 0.55 + 0.55 * (1.9 / 3.5) ** 0.7), self.axes.c2p(2.55, 0.55 + 0.55 * (2.55 / 3.5) ** 0.7), color=ORANGE, stroke_width=6)
        cap2 = self.ja_text("斜めの長さ", font_size=24).move_to(self.note)
        self.play(Create(slant), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"S").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"S=2\pi\int_a^b y\sqrt{1+(y')^{2}}\,dx").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"S=2\pi\int_a^b y\sqrt{1+(y')^{2}}\,dx").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
