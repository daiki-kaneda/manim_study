from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class DiskMethod(PacedScene):
    """#150 回転体の体積は円板の積み重ね（約50秒）"""

    def construct(self):
        self.show_heading("回転体")
        self.draw_curve()
        self.stack_disks()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _f(self, x):
        return 0.32 * x + 0.55

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=7.4,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.12 + LEFT * 0.4)
        self.curve = self.axes.plot(lambda x: 0.32 * x + 0.55, x_range=[0.25, 3.7], color=BLUE, stroke_width=5)
        axis_line = self.axes.plot(lambda x: 0, x_range=[0.2, 3.9], color=GREY, stroke_width=2)
        self.play(Create(self.axes), run_time=0.9)
        self.play(Create(self.curve), Create(axis_line), run_time=1.8)
        note = self.ja_text("軸のまわり", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note

    def _disk(self, x):
        r = self._f(x)
        c = self.axes.c2p(x, 0)
        return Ellipse(
            width=0.22,
            height=2 * abs(self.axes.c2p(x, r)[1] - c[1]),
            color=YELLOW,
            fill_opacity=0.22,
            stroke_width=3,
        ).move_to(c)

    def stack_disks(self):
        xs = [0.7, 1.35, 2.0, 2.65, 3.3]
        disks = VGroup(*[self._disk(x) for x in xs])
        cap = self.ja_text("円板を積む", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in disks], lag_ratio=0.18), Transform(self.note, cap), run_time=2.4)
        self.read(0.45)
        self.play(Indicate(disks[-1], color=WHITE), run_time=0.8)
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
        eq = MathTex(r"V").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"V=\pi\int_a^b [f(x)]^{2}\,dx").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"V=\pi\int_a^b [f(x)]^{2}\,dx").scale(0.92)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
