from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Pigeonhole(JapaneseScene):
    """#49 鳩の巣原理（約90秒）"""

    def construct(self):
        self.show_heading("鳩の巣原理")
        self.draw_holes()
        self.place_pigeons()
        self.show_formula()
        self.hold(1.2)

    def draw_holes(self):
        self.holes = VGroup()
        origin = LEFT * 3.6 + DOWN * 0.4
        for i in range(4):
            box = RoundedRectangle(width=1.5, height=1.7, corner_radius=0.12, color=GREY, stroke_width=2)
            box.move_to(origin + RIGHT * (i * 1.85))
            lab = MathTex(str(i + 1), font_size=22, color=GREY).next_to(box, DOWN, buff=0.12)
            self.holes.add(VGroup(box, lab))
        self.play(LaggedStart(*[FadeIn(h) for h in self.holes], lag_ratio=0.12), run_time=0.9)
        cap = self.ja_text("巣が 4 つ", font_size=26)
        cap.to_edge(RIGHT, buff=0.45).shift(UP * 1.7)
        self.play(FadeIn(cap), run_time=0.35)
        self.hold(0.5)
        self.cap = cap

    def place_pigeons(self):
        colors = [BLUE, GREEN, ORANGE, TEAL, YELLOW]
        pigeons = VGroup()
        # 4 羽を 1 つずつ、5 羽目を最初の巣へ
        slots = [0, 1, 2, 3, 0]
        for i, hole_i in enumerate(slots):
            bird = Dot(radius=0.16, color=colors[i])
            box = self.holes[hole_i][0]
            # 同じ巣の 2 羽目は少しずらす
            offset = UP * (0.35 if i < 4 else -0.35)
            bird.move_to(box.get_center() + offset)
            self.play(FadeIn(bird, scale=0.5), run_time=0.35)
            pigeons.add(bird)
            if i == 3:
                self.play(Transform(self.cap, self.ja_text("5 羽目", font_size=26).move_to(self.cap)), run_time=0.3)
        self.play(Indicate(pigeons[0], color=WHITE), Indicate(pigeons[4], color=WHITE), run_time=0.7)
        crowded = self.ja_text("どれか 1 つに 2 羽", font_size=24).move_to(self.cap)
        self.play(Transform(self.cap, crowded), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        row = VGroup(
            self.ja_text("n 個の入れ物に n+1 個あれば", font_size=26),
        )
        formula = self.ja_text("どれかに 2 個以上", font_size=32)
        formula.to_edge(DOWN, buff=0.35)
        row.next_to(formula, UP, buff=0.18)
        self.play(FadeIn(row), FadeIn(formula), run_time=0.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
