from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class OuterNapoleon(PacedScene):
    """#720 外側ナポレオン：外側の正三角形の中心（約45秒）"""

    def construct(self):
        self.show_heading("外側ナポレオン")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.3 + DOWN * 0.8, RIGHT * 2.3 + DOWN * 0.8, UP * 1.4, color=BLUE, stroke_width=3)
        tips = VGroup(
            Dot(DOWN * 2.0, color=ORANGE, radius=0.08),
            Dot(RIGHT * 3.2 + UP * 0.9, color=ORANGE, radius=0.08),
            Dot(LEFT * 3.2 + UP * 0.9, color=ORANGE, radius=0.08),
        )
        nap = Polygon(*[t.get_center() for t in tips], color=TEAL, stroke_width=3)
        self.play(Create(tri), FadeIn(tips), Create(nap), run_time=1.4)

        note = self.ja_text("外側に正三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("中心が正三角形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("内側版と対", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\triangle_N\ \mathrm{equil.}").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
