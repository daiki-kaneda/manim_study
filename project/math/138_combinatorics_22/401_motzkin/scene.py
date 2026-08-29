from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Motzkin(PacedScene):
    """#401 モツキン数：上がり・平坦・下がりで非負な道（約45秒）"""

    def construct(self):
        self.show_heading("モツキン数")
        self.draw_path()
        self.count()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[-0.3, 2.5, 1], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35)
        # Motzkin path: up, level, up, down, level, down
        pts = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 1), (5, 1), (6, 0)]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([axes.c2p(x, y) for x, y in pts])
        dots = VGroup(*[Dot(axes.c2p(x, y), color=ORANGE, radius=0.08) for x, y in pts])
        self.play(Create(axes), Create(path), FadeIn(dots), run_time=1.6)
        note = self.ja_text("モツキン道", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def count(self):
        steps = VGroup(
            MathTex(r"\nearrow", color=TEAL, font_size=36),
            MathTex(r"\rightarrow", color=YELLOW, font_size=36),
            MathTex(r"\searrow", color=ORANGE, font_size=36),
        ).arrange(RIGHT, buff=0.45).shift(DOWN * 0.85)
        cap = self.ja_text("3 種の歩み", font_size=24).move_to(self.note)
        self.play(FadeIn(steps), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("非負で数える", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"M_n=M_{n-1}+\sum_{k=0}^{n-2}M_k M_{n-2-k}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
