from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class ConfidenceInterval(JapaneseScene):
    """#89 信頼区間（約90秒）"""

    def construct(self):
        self.show_heading("信頼区間")
        self.draw_truth()
        self.draw_intervals()
        self.show_formula()
        self.hold(1.2)

    def draw_truth(self):
        self.truth = Line(LEFT * 0.4 + UP * 2.2, LEFT * 0.4 + DOWN * 1.85, color=YELLOW, stroke_width=4)
        lab = MathTex(r"\mu", color=YELLOW, font_size=32).next_to(self.truth, UP, buff=0.12)
        self.play(Create(self.truth), FadeIn(lab), run_time=0.6)
        note = self.ja_text("真の平均", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.4)
        self.note = note

    def draw_intervals(self):
        # center offsets; last one misses on purpose
        centers = [-0.35, 0.2, -0.15, 0.45, 0.05, -0.55, 0.25, 1.55]
        half = 1.15
        segs = VGroup()
        y0 = 1.85
        for i, c in enumerate(centers):
            y = y0 - i * 0.42
            color = RED if abs(c) > 1.15 else BLUE
            seg = Line(RIGHT * (c - half) + UP * y, RIGHT * (c + half) + UP * y, color=color, stroke_width=5)
            segs.add(seg)
        for i, seg in enumerate(segs):
            self.play(Create(seg), run_time=0.22)
        miss = self.ja_text("たまに外す", font_size=24).move_to(self.note)
        self.play(Transform(self.note, miss), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"P(\mu\in I)=1-\alpha").scale(1.05)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
