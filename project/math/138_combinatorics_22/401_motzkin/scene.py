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
        self.derive()
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

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"M_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"M_n=M_{n-1}+\sum_{k=0}^{n-2}M_k M_{n-2-k}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"M_n=M_{n-1}+\sum_{k=0}^{n-2}M_k M_{n-2-k}").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
