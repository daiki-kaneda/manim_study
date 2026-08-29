from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class TiltStability(PacedScene):
    """#750 傾き安定性：傾斜した心での安定性（約45秒）"""

    def construct(self):
        self.show_heading("傾き安定性")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[-1.5, 1.5, 1], y_range=[0, 2, 1], x_length=4.5, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.4 + UP * 0.15)
        line = Line(axes.c2p(-1.2, 0.3), axes.c2p(1.2, 1.7), color=ORANGE, stroke_width=4)
        self.play(Create(axes), Create(line), run_time=1.3)
        note = self.ja_text("心を傾ける", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("傾き関数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("壁越えの前段階", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mu_\beta(E)=\frac{\Im Z_\beta(E)}{\Re Z_\beta(E)}").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
