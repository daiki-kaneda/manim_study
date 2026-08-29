from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
import numpy as np
from manim_math import PacedScene


class Stabilizability(PacedScene):
    """#618 可安定化：フィードバックで漸近安定へ（約45秒）"""

    def construct(self):
        self.show_heading("可安定化")
        self.draw_poles()
        self.feedback()
        self.show_formula()
        self.read(1.4)

    def draw_poles(self):
        plane = ComplexPlane(x_range=[-2, 2, 1], y_range=[-1.5, 1.5, 1], x_length=5.0, y_length=3.0).shift(LEFT * 0.3 + UP * 0.05)
        poles = VGroup(
            Dot(plane.n2p(-0.6 + 0.8j), color=RED, radius=0.1),
            Dot(plane.n2p(-0.6 - 0.8j), color=RED, radius=0.1),
            Dot(plane.n2p(0.7), color=ORANGE, radius=0.1),
        )
        self.play(Create(plane), FadeIn(poles), run_time=1.4)
        note = self.ja_text("不安定極あり", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.plane = plane
        self.bad = poles[2]

    def feedback(self):
        moved = Dot(self.plane.n2p(-1.0), color=TEAL, radius=0.1)
        cap = self.ja_text("フィードバック", font_size=24).move_to(self.note)
        self.play(Transform(self.bad, moved), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("左半平面へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\exists K:\ \sigma(A-BK)\subset\mathbb{C}_-").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
