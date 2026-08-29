from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Isoperimetric(JapaneseScene):
    """#78 同じ周なら正方形が最大面積（約90秒）"""

    def construct(self):
        self.show_heading("同じ周なら正方形")
        self.draw_rectangles()
        self.highlight_square()
        self.show_formula()
        self.hold(1.2)

    def _rect(self, w, h, color):
        r = Rectangle(width=w, height=h, color=color, fill_opacity=0.45, stroke_width=2)
        area = MathTex(rf"{w:.1f}\\times{h:.1f}", font_size=22, color=color)
        area.next_to(r, DOWN, buff=0.12)
        return VGroup(r, area)

    def draw_rectangles(self):
        # 周長 8（幅+高さ=4）
        specs = [(0.9, 3.1, BLUE), (1.5, 2.5, TEAL), (2.0, 2.0, YELLOW), (3.1, 0.9, GREEN)]
        group = VGroup()
        for w, h, color in specs:
            group.add(self._rect(w, h, color))
        group.arrange(RIGHT, buff=0.45, aligned_edge=DOWN)
        group.shift(DOWN * 0.15)
        for item in group:
            self.play(FadeIn(item, shift=UP * 0.1), run_time=0.35)
        note = self.ja_text("周はどれも同じ", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.55)
        self.group, self.note = group, note

    def highlight_square(self):
        sq = self.group[2]
        self.play(Indicate(sq[0], color=WHITE), run_time=0.7)
        cap = self.ja_text("正方形が最大", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"A=x(s-x),\quad x=\dfrac{s}{2}").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
