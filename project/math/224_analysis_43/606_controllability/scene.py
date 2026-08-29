from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Controllability(PacedScene):
    """#606 可制御性：入力で状態を目標へ運ぶ（約45秒）"""

    def construct(self):
        self.show_heading("可制御性")
        self.draw_system()
        self.reach()
        self.show_formula()
        self.read(1.4)

    def draw_system(self):
        box = RoundedRectangle(width=2.4, height=1.3, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 0.5 + UP * 0.3)
        u = Arrow(LEFT * 3.5 + UP * 0.3, box.get_left(), buff=0.05, color=ORANGE, stroke_width=4)
        y = Arrow(box.get_right(), RIGHT * 3.2 + UP * 0.3, buff=0.05, color=TEAL, stroke_width=4)
        self.play(Create(box), GrowArrow(u), GrowArrow(y),
                  FadeIn(MathTex(r"x", font_size=36).move_to(box)),
                  FadeIn(MathTex(r"u", font_size=28).next_to(u, UP, buff=0.08)),
                  run_time=1.4)
        note = self.ja_text("入力で駆動", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def reach(self):
        cap = self.ja_text("任意の状態へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("有限時間で到達", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathrm{rank}\,[B\ AB\ \cdots\ A^{n-1}B]=n").scale(0.78)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
