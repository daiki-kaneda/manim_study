from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class TriangleArea(JapaneseScene):
    """#2 三角形の面積：平行四辺形から導く（約90秒）"""

    def construct(self):
        self.base = 4.0
        self.height = 3.0
        self.show_title()
        self.show_triangle()
        self.form_parallelogram()
        self.derive_formula()
        self.wait(0.8)

    def show_title(self):
        title = self.ja_text("三角形の面積", font_size=44)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(0.25)
        self.play(title.animate.scale(0.55).to_edge(UP), run_time=0.4)
        self.title = title

    def show_triangle(self):
        self.A = LEFT * (self.base / 2) + UP * 0.2
        self.B = RIGHT * (self.base / 2) + UP * 0.2
        self.C = LEFT * 0.5 + UP * (0.2 + self.height)
        self.mid_ab = (self.A + self.B) / 2
        self.C_prime = 2 * self.mid_ab - self.C

        self.triangle = Polygon(
            self.A,
            self.B,
            self.C,
            color=BLUE,
            fill_opacity=0.7,
            stroke_width=2,
        )
        self.play(Create(self.triangle), run_time=0.7)

        foot = self.C.copy()
        foot[1] = self.A[1]
        height_line = DashedLine(self.C, foot, color=YELLOW, stroke_width=2)
        base_brace = Brace(Line(self.A, self.B), DOWN, buff=0.12)
        label_a = MathTex("a").next_to(base_brace, DOWN, buff=0.12)
        label_h = MathTex("h").next_to(height_line, RIGHT, buff=0.12)

        self.play(
            Create(height_line),
            GrowFromCenter(base_brace),
            FadeIn(label_a),
            FadeIn(label_h),
            run_time=0.6,
        )
        self.wait(0.35)
        self.guides = VGroup(height_line, base_brace, label_a, label_h)

    def form_parallelogram(self):
        self.play(FadeOut(self.guides), run_time=0.3)
        copy = self.triangle.copy().set_color(ORANGE)
        self.play(FadeIn(copy), run_time=0.35)
        self.play(Rotate(copy, PI, about_point=self.mid_ab), run_time=0.8)

        parallelogram = Polygon(
            self.A,
            self.B,
            self.C_prime,
            self.C,
            color=GREEN,
            fill_opacity=0,
            stroke_width=3,
        )
        self.play(Create(parallelogram), run_time=0.5)
        self.wait(0.25)

        self.copy_triangle = copy
        self.parallelogram = parallelogram

        caption = self.ja_text("平行四辺形", font_size=28).to_edge(DOWN)
        self.play(FadeIn(caption), run_time=0.35)
        self.wait(0.35)
        self.play(FadeOut(caption), run_time=0.25)

    def derive_formula(self):
        para_area = MathTex(r"ah").scale(1.2)
        para_label = self.ja_text("面積  =", font_size=28)
        row1 = VGroup(para_label, para_area).arrange(RIGHT, buff=0.2)
        row1.next_to(self.title, DOWN, buff=0.35).to_edge(RIGHT, buff=0.8)

        self.play(Write(row1), run_time=0.6)
        self.wait(0.4)

        half = self.ja_text("三角形は半分", font_size=26)
        half.next_to(row1, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(FadeIn(half), run_time=0.4)
        self.play(Indicate(self.triangle), run_time=0.5)
        self.wait(0.3)

        formula = MathTex(r"S = \frac{1}{2} ah").scale(1.4)
        formula.next_to(half, DOWN, buff=0.4).align_to(row1, RIGHT)
        self.play(FadeOut(half), TransformMatchingTex(para_area.copy(), formula), run_time=0.7)
        self.play(Indicate(formula, color=BLUE), run_time=0.5)

        example = MathTex(r"a=4,\ h=3 \ \Rightarrow\ S=6").scale(0.85)
        example.next_to(formula, DOWN, buff=0.35).align_to(formula, RIGHT)
        self.play(FadeIn(example), run_time=0.45)
        self.wait(0.6)
