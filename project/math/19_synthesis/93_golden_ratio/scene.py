from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class GoldenRatio(JapaneseScene):
    """#93 黄金比とフィボナッチ（約90秒）"""

    def construct(self):
        self.show_heading("黄金比")
        self.tile()
        self.show_formula()
        self.hold(1.2)

    def tile(self):
        s = 0.72
        # bottom-left of the growing rectangle
        origin = LEFT * 3.4 + DOWN * 1.55
        # Fibonacci squares placed around the rectangle
        # 1 at origin, 1 to the right, 2 on top of those, 3 to the right, 5 on top
        specs = [
            ((0, 0), 1, BLUE),
            ((1, 0), 1, TEAL),
            ((0, 1), 2, GREEN),
            ((2, 0), 3, ORANGE),
            ((0, 3), 5, YELLOW),
        ]
        squares = VGroup()
        labels = VGroup()
        for (cx, cy), n, color in specs:
            side = n * s
            sq = Square(side_length=side, color=color, fill_opacity=0.45, stroke_width=2)
            sq.move_to(origin + RIGHT * (cx * s + side / 2) + UP * (cy * s + side / 2))
            lab = MathTex(str(n), font_size=28, color=WHITE).move_to(sq.get_center())
            squares.add(sq)
            labels.add(lab)
            self.play(FadeIn(sq), FadeIn(lab), run_time=0.4)
            self.hold(0.12)
        note = self.ja_text("長方形が黄金へ", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.55)

    def show_formula(self):
        formula = MathTex(r"\varphi=\frac{1+\sqrt{5}}{2}").scale(1.15)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
