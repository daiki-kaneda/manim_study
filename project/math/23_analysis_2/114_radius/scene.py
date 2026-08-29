from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class RadiusOfConvergence(JapaneseScene):
    """#114 収束半径（約90秒）"""

    def construct(self):
        self.origin = LEFT * 1.9 + DOWN * 0.15
        self.show_heading("収束半径")
        self.draw_disk()
        self.show_formula()
        self.hold(1.2)

    def draw_disk(self):
        ax = Line(self.origin + LEFT * 2.5, self.origin + RIGHT * 2.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.1, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        disk = Circle(radius=1.7, color=BLUE, fill_opacity=0.35, stroke_width=3).move_to(self.origin)
        r = Line(self.origin, self.origin + RIGHT * 1.7, color=YELLOW, stroke_width=4)
        self.play(Create(ax), Create(ay), run_time=0.4)
        self.play(FadeIn(disk), Create(r), run_time=0.7)
        lab = MathTex("R", color=YELLOW, font_size=32).next_to(r, DOWN, buff=0.08)
        self.play(FadeIn(lab), run_time=0.3)
        note = self.ja_text("円内で収束", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\sum a_n z^n\quad(|z|<R)").scale(1.0)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
