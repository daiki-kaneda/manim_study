from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Stirling(PacedScene):
    """#173 スターリング第二種：集合の分割（約45秒）"""

    def construct(self):
        self.show_heading("スターリング数")
        self.draw_elements()
        self.partition()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_elements(self):
        self.dots = VGroup()
        labels = VGroup()
        for i, name in enumerate("ABCDE"):
            p = LEFT * 3.2 + RIGHT * (i * 1.35) + UP * 1.55
            d = Dot(p, radius=0.14, color=WHITE)
            lab = MathTex(name, font_size=28).next_to(d, UP, buff=0.12)
            self.dots.add(d)
            labels.add(lab)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in self.dots], lag_ratio=0.12), run_time=1.6)
        self.play(FadeIn(labels), run_time=0.5)
        note = self.ja_text("5 個", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note
        self.labels = labels

    def partition(self):
        # 3 nonempty blocks
        groups = [
            (0, 1, BLUE),
            (2, 2, YELLOW),
            (3, 4, GREEN),
        ]
        circles = VGroup()
        for i0, i1, col in groups:
            pts = [self.dots[i].get_center() for i in range(i0, i1 + 1)]
            if len(pts) == 1:
                c = Circle(radius=0.42, color=col, stroke_width=4).move_to(pts[0])
            else:
                mid = (pts[0] + pts[-1]) / 2
                c = Ellipse(width=abs(pts[-1][0] - pts[0][0]) + 0.7, height=0.9, color=col, stroke_width=4).move_to(mid)
            circles.add(c)
            for i in range(i0, i1 + 1):
                self.dots[i].set_color(col)
        cap = self.ja_text("3 グループ", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.2), Transform(self.note, cap), run_time=1.8)
        self.read(0.35)
        # rearrange briefly by indicating
        self.play(*[Indicate(c, color=WHITE) for c in circles], run_time=1.0)
        cap2 = self.ja_text("空なし", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"S(n,k)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"S(n,k)=\frac{1}{k!}\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j}j^{n}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"S(n,k)=\frac{1}{k!}\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j}j^{n}").scale(0.7)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.1)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
