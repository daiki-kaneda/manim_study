from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Discriminant(JapaneseScene):
    """#15 判別式 D=0 の意味（約90秒）"""

    def construct(self):
        self.show_heading("判別式")
        self.show_definition()
        self.show_three_cases()
        self.hold(1.2)

    def show_definition(self):
        quad = MathTex(r"ax^2+bx+c=0").scale(1.1)
        quad.shift(UP * 2.15)
        d = MathTex(r"D=b^2-4ac").scale(1.2)
        d.next_to(quad, DOWN, buff=0.3)
        self.play(Write(quad), run_time=0.7)
        self.play(Write(d), run_time=0.7)
        self.hold(0.6)
        self.quad, self.d = quad, d

    def _axes(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=5.4,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        )
        axes.shift(DOWN * 0.55 + LEFT * 1.6)
        return axes

    def _case(self, fn, color, caption_jp, caption_math):
        axes = self._axes()
        graph = axes.plot(fn, x_range=[-2.6, 2.6], color=color, stroke_width=4)
        x_axis = axes.get_x_axis()
        cap = VGroup(
            self.ja_text(caption_jp, font_size=26),
            MathTex(caption_math, font_size=32),
        ).arrange(DOWN, buff=0.18)
        cap.to_edge(RIGHT, buff=0.55).shift(DOWN * 0.2)
        group = VGroup(axes, graph, cap)
        return group

    def show_three_cases(self):
        # 最後を D=0（接する）で止めて、結論と絵が一致するようにする
        cases = [
            (lambda x: 0.45 * x * x - 1.6, BLUE, "2つの実数解", r"D>0"),
            (lambda x: 0.45 * x * x + 1.3, ORANGE, "実数解なし", r"D<0"),
            (lambda x: 0.45 * (x - 0.2) ** 2, GREEN, "重解（接する）", r"D=0"),
        ]
        current = None
        for fn, color, jp, math in cases:
            nxt = self._case(fn, color, jp, math)
            if current is None:
                self.play(FadeIn(nxt), run_time=0.8)
            else:
                self.play(FadeOut(current), FadeIn(nxt), run_time=0.8)
            current = nxt
            self.hold(1.0)
        note = self.ja_text("D=0 ⇔ グラフが x 軸に接する", font_size=26)
        note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.5)
        self.hold(1.2)
