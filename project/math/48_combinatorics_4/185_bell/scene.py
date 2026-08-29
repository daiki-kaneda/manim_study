from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BellNumbers(PacedScene):
    """#185 ベル数はすべての分割の数（約45秒）"""

    def construct(self):
        self.show_heading("ベル数")
        self.draw_elements()
        self.show_partitions()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_elements(self):
        self.dots = VGroup()
        labs = VGroup()
        for i, name in enumerate("ABCD"):
            p = LEFT * 2.7 + RIGHT * (i * 1.5) + UP * 1.7
            d = Dot(p, radius=0.13, color=WHITE)
            lab = MathTex(name, font_size=28).next_to(d, UP, buff=0.1)
            self.dots.add(d)
            labs.add(lab)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in self.dots], lag_ratio=0.12), run_time=1.5)
        self.play(FadeIn(labs), run_time=0.45)
        note = self.ja_text("4 個", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def _group(self, indices, color):
        pts = [self.dots[i].get_center() for i in indices]
        for i in indices:
            self.dots[i].set_color(color)
        if len(pts) == 1:
            return Circle(radius=0.4, color=color, stroke_width=3).move_to(pts[0])
        mid = sum(pts) / len(pts)
        w = abs(pts[-1][0] - pts[0][0]) + 0.65
        return Ellipse(width=w, height=0.85, color=color, stroke_width=3).move_to(mid)

    def show_partitions(self):
        # show three different partitions of 4 elements, counting toward B4=15
        configs = [
            ([(0, 1, 2, 3)], [BLUE], "1 通り"),
            ([(0, 1), (2, 3)], [YELLOW, GREEN], "いくつか"),
            ([(0,), (1,), (2,), (3,)], [BLUE, TEAL, YELLOW, ORANGE], "全部単独"),
        ]
        shown = VGroup()
        for parts, colors, label in configs:
            new = VGroup()
            for idxs, col in zip(parts, colors):
                # reset colors first somehow - just draw groups
                g = self._group(idxs, col)
                new.add(g)
            cap = self.ja_text(label, font_size=24).move_to(self.note)
            if len(shown) == 0:
                self.play(LaggedStart(*[Create(g) for g in new], lag_ratio=0.15), Transform(self.note, cap), run_time=1.4)
                shown = new
            else:
                self.play(FadeOut(shown), LaggedStart(*[Create(g) for g in new], lag_ratio=0.12), Transform(self.note, cap), run_time=1.5)
                shown = new
            self.read(0.3)
        cap = self.ja_text("全部で 15", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.7)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"B_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"B_n=\sum_{k=0}^{n}S(n,k)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"B_n=\sum_{k=0}^{n}S(n,k)").scale(1.0)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
