from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Birthday(JapaneseScene):
    """#121 誕生日のパラドックス（約90秒）"""

    def construct(self):
        self.show_heading("誕生日")
        self.draw_grid()
        self.place_people()
        self.show_formula()
        self.hold(1.2)

    def draw_grid(self):
        cells = VGroup()
        origin = LEFT * 5.0 + UP * 1.35
        self.n, self.m = 12, 5
        self.size = 0.42
        self.origin = origin
        for r in range(self.m):
            for c in range(self.n):
                sq = Square(side_length=self.size, color=GREY, stroke_width=1)
                sq.move_to(origin + RIGHT * (c * self.size) + DOWN * (r * self.size))
                cells.add(sq)
        self.play(FadeIn(cells), run_time=0.7)
        cap = self.ja_text("日のマス", font_size=24)
        cap.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(cap), run_time=0.3)
        self.hold(0.4)
        self.cells, self.cap = cells, cap

    def _cell(self, r, c):
        return self.origin + RIGHT * (c * self.size) + DOWN * (r * self.size)

    def place_people(self):
        # いくつか散らし、最後に同じマスへ 2 人
        slots = [(0, 1), (1, 4), (2, 8), (0, 9), (3, 2), (4, 10), (1, 1), (2, 5), (3, 7), (4, 3), (0, 6), (1, 11)]
        dots = VGroup()
        for i, (r, c) in enumerate(slots):
            d = Dot(self._cell(r, c), radius=0.08, color=BLUE)
            self.play(FadeIn(d, scale=0.6), run_time=0.12)
            dots.add(d)
        collide = Dot(self._cell(1, 4), radius=0.08, color=YELLOW).shift(RIGHT * 0.09)
        self.play(FadeIn(collide, scale=0.6), run_time=0.25)
        self.play(Indicate(dots[1], color=WHITE), Indicate(collide, color=WHITE), run_time=0.6)
        nxt = self.ja_text("23 人で半分", font_size=24).move_to(self.cap)
        self.play(Transform(self.cap, nxt), run_time=0.35)
        self.hold(0.6)

    def show_formula(self):
        formula = MathTex(r"n=23:\ P\approx 50\%").scale(1.0)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
