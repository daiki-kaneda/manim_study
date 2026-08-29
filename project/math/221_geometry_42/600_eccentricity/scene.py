from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Eccentricity(PacedScene):
    """#600 離心率：円錐曲線を分類する比（約45秒）"""

    def construct(self):
        self.show_heading("離心率")
        self.draw_conics()
        self.values()
        self.show_formula()
        self.read(1.4)

    def draw_conics(self):
        ell = Ellipse(width=2.2, height=1.4, color=BLUE, stroke_width=3).shift(LEFT * 2.8 + UP * 0.3)
        para = axes_plot = None
        # parabola sketch
        axes = Axes(x_range=[0, 2, 1], y_range=[-1.2, 1.2, 1], x_length=2.0, y_length=2.0, tips=False,
                    axis_config={"stroke_width": 1, "include_ticks": False}).shift(UP * 0.3)
        para = axes.plot(lambda x: 0.8 * (x ** 0.5) if x > 0 else 0, x_range=[0.05, 1.8], color=TEAL, stroke_width=3)
        para2 = axes.plot(lambda x: -0.8 * (x ** 0.5) if x > 0 else 0, x_range=[0.05, 1.8], color=TEAL, stroke_width=3)
        hyp = Ellipse(width=1.0, height=1.6, color=ORANGE, stroke_width=3).shift(RIGHT * 2.8 + UP * 0.3)  # visual stand-in
        # better: two branches as arcs
        self.play(Create(ell), Create(axes), Create(para), Create(para2), run_time=1.4)
        note = self.ja_text("円錐曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def values(self):
        labs = VGroup(
            MathTex(r"e<1", font_size=28).shift(LEFT * 2.8 + DOWN * 1.2),
            MathTex(r"e=1", font_size=28).shift(DOWN * 1.2),
            MathTex(r"e>1", font_size=28).shift(RIGHT * 2.5 + DOWN * 1.2),
        )
        cap = self.ja_text("e で形が決まる", font_size=24).move_to(self.note)
        self.play(FadeIn(labs), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("焦点と準線の比", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"e=\frac{c}{a}").scale(0.95)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
