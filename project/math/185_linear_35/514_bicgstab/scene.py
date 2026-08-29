from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class BiCGSTAB(PacedScene):
    """#514 BiCGSTAB：非対称系の安定化双共役勾配（約45秒）"""

    def construct(self):
        self.show_heading("BiCGSTAB")
        self.draw_two()
        self.stabilize()
        self.show_formula()
        self.read(1.4)

    def draw_two(self):
        p = RoundedRectangle(width=2.3, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.4 + UP * 0.3)
        q = RoundedRectangle(width=2.3, height=1.3, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.4 + UP * 0.3)
        self.play(
            Create(p), FadeIn(MathTex(r"r", font_size=34).move_to(p)),
            Create(q), FadeIn(MathTex(r"\tilde r", font_size=34).move_to(q)),
            run_time=1.3,
        )
        note = self.ja_text("双方向残差", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def stabilize(self):
        cap = self.ja_text("安定化ステップ", font_size=24).move_to(self.note)
        zig = VMobject(color=ORANGE, stroke_width=4)
        zig.set_points_as_corners([LEFT * 1.2 + DOWN * 0.8, ORIGIN + DOWN * 0.3, RIGHT * 1.2 + DOWN * 0.9])
        self.play(Create(zig), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("非対称でも実用的", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"r_{k+1}=(I-\omega_k A)(I-\alpha_k A)r_k").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
