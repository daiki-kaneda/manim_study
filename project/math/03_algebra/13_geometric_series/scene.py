from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class GeometricSeries(JapaneseScene):
    """#13 等比数列の和：1/2+1/4+…=1（約90秒）"""

    def construct(self):
        self.side = 3.2
        self.origin = LEFT * 4.4 + DOWN * 1.9
        self.show_heading("等比数列の和")
        self.show_series()
        self.fill_square()
        self.show_formula()
        self.hold(1.2)

    def show_series(self):
        series = MathTex(r"\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\cdots=?").scale(1.05)
        series.to_edge(UP, buff=1.15)
        self.play(Write(series), run_time=0.9)
        self.hold(0.6)
        self.series = series

    def fill_square(self):
        s = self.side
        frame = Square(side_length=s, color=WHITE, stroke_width=2)
        frame.move_to(self.origin + RIGHT * (s / 2) + UP * (s / 2))
        self.play(Create(frame), run_time=0.6)
        colors = [BLUE, GREEN, ORANGE, YELLOW, TEAL]
        labels = [r"1/2", r"1/4", r"1/8", r"1/16", r"1/32"]
        # Standard geometric filling of the unit square:
        # 1/2: left half; 1/4: bottom-right; 1/8: above that, etc.
        regions = []
        x0, y0 = self.origin[0], self.origin[1]
        # left half
        r0 = Rectangle(width=s / 2, height=s, color=colors[0], fill_opacity=0.75, stroke_width=1)
        r0.move_to([x0 + s / 4, y0 + s / 2, 0])
        regions.append((r0, labels[0], s / 2 > 0.7))
        # remaining right column, successively halved from the bottom
        height = s / 2
        y = y0
        x = x0 + 3 * s / 4
        for i in range(1, 5):
            rect = Rectangle(
                width=s / 2, height=height, color=colors[i], fill_opacity=0.75, stroke_width=1
            )
            rect.move_to([x, y + height / 2, 0])
            regions.append((rect, labels[i], height > 0.35))
            y += height
            height /= 2

        for rect, lab, show_lab in regions:
            self.play(FadeIn(rect, scale=0.9), run_time=0.4)
            if show_lab:
                t = MathTex(lab, font_size=26).move_to(rect)
                self.play(FadeIn(t), run_time=0.2)
            self.hold(0.25)
        self.hold(0.6)

    def show_formula(self):
        eq = MathTex(r"\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\cdots=1").scale(1.1)
        eq.to_edge(RIGHT, buff=0.5).shift(UP * 0.8)
        self.play(Write(eq), run_time=0.9)
        self.hold(0.7)
        gen = MathTex(r"S=\frac{a}{1-r}\quad(|r|<1)").scale(0.95)
        gen.next_to(eq, DOWN, aligned_edge=RIGHT, buff=0.4)
        note = self.ja_text("公比 r の無限等比", font_size=24)
        note.next_to(gen, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(FadeIn(gen), FadeIn(note), run_time=0.7)
        self.play(Indicate(eq, color=BLUE), run_time=0.7)
        self.hold(1.3)
