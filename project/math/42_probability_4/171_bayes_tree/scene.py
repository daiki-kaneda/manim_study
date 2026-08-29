from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ProbabilityTree(PacedScene):
    """#171 確率の木は分岐をかけていく（約45秒）"""

    def construct(self):
        self.show_heading("確率の木")
        self.draw_tree()
        self.multiply_path()
        self.show_formula()
        self.read(1.4)

    def draw_tree(self):
        root = LEFT * 4.2 + UP * 0.1
        y1 = root + RIGHT * 2.6 + UP * 1.35
        n1 = root + RIGHT * 2.6 + DOWN * 1.35
        yy = y1 + RIGHT * 2.8 + UP * 0.7
        yn = y1 + RIGHT * 2.8 + DOWN * 0.7
        ny = n1 + RIGHT * 2.8 + UP * 0.7
        nn = n1 + RIGHT * 2.8 + DOWN * 0.7
        self.nodes = {
            "r": Dot(root, color=WHITE, radius=0.09),
            "y1": Dot(y1, color=YELLOW, radius=0.09),
            "n1": Dot(n1, color=BLUE, radius=0.09),
            "yy": Dot(yy, color=YELLOW, radius=0.08),
            "yn": Dot(yn, color=GREY, radius=0.08),
            "ny": Dot(ny, color=GREY, radius=0.08),
            "nn": Dot(nn, color=BLUE, radius=0.08),
        }
        edges1 = VGroup(
            Line(root, y1, color=YELLOW, stroke_width=4),
            Line(root, n1, color=BLUE, stroke_width=4),
        )
        edges2 = VGroup(
            Line(y1, yy, color=YELLOW, stroke_width=3),
            Line(y1, yn, color=GREY, stroke_width=3),
            Line(n1, ny, color=GREY, stroke_width=3),
            Line(n1, nn, color=BLUE, stroke_width=3),
        )
        self.play(FadeIn(self.nodes["r"]), run_time=0.4)
        self.play(Create(edges1), FadeIn(self.nodes["y1"]), FadeIn(self.nodes["n1"]), run_time=1.4)
        p1 = MathTex(r"\tfrac{2}{3}", color=YELLOW, font_size=26).next_to(edges1[0], UP, buff=0.05)
        p2 = MathTex(r"\tfrac{1}{3}", color=BLUE, font_size=26).next_to(edges1[1], DOWN, buff=0.05)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.6)
        note = self.ja_text("分岐", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.read(0.3)
        self.play(Create(edges2), *[FadeIn(self.nodes[k]) for k in ("yy", "yn", "ny", "nn")], run_time=1.6)
        self.read(0.35)
        self.note = note
        self.path_edge = edges1[0]
        self.path_edge2 = edges2[0]
        self.yy = yy

    def multiply_path(self):
        glow = VGroup(self.path_edge.copy().set_stroke(ORANGE, width=8), self.path_edge2.copy().set_stroke(ORANGE, width=8))
        cap = self.ja_text("道を掛ける", font_size=24).move_to(self.note)
        self.play(FadeIn(glow), Transform(self.note, cap), run_time=1.2)
        prod = MathTex(r"\tfrac{2}{3}\cdot\tfrac{1}{2}=\tfrac{1}{3}", color=ORANGE, font_size=34)
        prod.next_to(self.yy, RIGHT, buff=0.25)
        self.play(FadeIn(prod, shift=RIGHT * 0.1), run_time=1.1)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"P(A\cap B)=P(A)P(B\mid A)").scale(0.88)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
