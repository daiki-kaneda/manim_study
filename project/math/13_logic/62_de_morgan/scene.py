from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class DeMorgan(JapaneseScene):
    """#62 ド・モルガンの法則（約90秒）"""

    def construct(self):
        self.show_heading("ド・モルガン")
        self.draw_sets()
        self.shade()
        self.show_formula()
        self.hold(1.2)

    def draw_sets(self):
        frame = RoundedRectangle(width=7.2, height=3.6, corner_radius=0.15, color=GREY, stroke_width=2)
        frame.shift(DOWN * 0.15)
        self.c1 = Circle(radius=1.35, color=BLUE, stroke_width=3).shift(LEFT * 0.85 + DOWN * 0.15)
        self.c2 = Circle(radius=1.35, color=ORANGE, stroke_width=3).shift(RIGHT * 0.85 + DOWN * 0.15)
        la = MathTex("A", color=BLUE, font_size=32).next_to(self.c1, UL, buff=0.05)
        lb = MathTex("B", color=ORANGE, font_size=32).next_to(self.c2, UR, buff=0.05)
        self.play(Create(frame), Create(self.c1), Create(self.c2), FadeIn(la), FadeIn(lb), run_time=0.85)
        self.hold(0.45)
        self.frame = frame

    def shade(self):
        # 外側（和集合の補集合）を黄で示す：frame から 2 円を除くのは Difference が必要
        outside = Difference(self.frame, Union(self.c1, self.c2), color=YELLOW, fill_opacity=0.55, stroke_width=0)
        self.play(FadeIn(outside), run_time=0.8)
        note = self.ja_text("和集合の外側", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.7)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)
        both = self.ja_text("どちらにも入らない", font_size=24).move_to(note)
        self.play(Transform(note, both), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\neg(A\cup B)=\neg A\cap\neg B").scale(1.05)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
