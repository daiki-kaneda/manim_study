from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class RootedTrees(PacedScene):
    """#581 根付き木：根を指定した木の数え上げ（約45秒）"""

    def construct(self):
        self.show_heading("根付き木")
        self.draw_tree()
        self.root()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_tree(self):
        root = Dot(UP * 1.6, color=ORANGE, radius=0.14)
        mid = [LEFT * 1.5 + UP * 0.3, RIGHT * 1.5 + UP * 0.3]
        leaves = [LEFT * 2.3 + DOWN * 1.1, LEFT * 0.7 + DOWN * 1.1, RIGHT * 0.7 + DOWN * 1.1, RIGHT * 2.3 + DOWN * 1.1]
        dots = VGroup(root, *[Dot(p, color=BLUE, radius=0.1) for p in mid + leaves])
        edges = VGroup(
            Line(UP * 1.6, mid[0], color=GREY, stroke_width=3),
            Line(UP * 1.6, mid[1], color=GREY, stroke_width=3),
            Line(mid[0], leaves[0], color=GREY, stroke_width=3),
            Line(mid[0], leaves[1], color=GREY, stroke_width=3),
            Line(mid[1], leaves[2], color=GREY, stroke_width=3),
            Line(mid[1], leaves[3], color=GREY, stroke_width=3),
        )
        self.play(Create(edges), FadeIn(dots), run_time=1.4)
        note = self.ja_text("根を決める", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def root(self):
        cap = self.ja_text("向きが付く", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ケイリーは n^{n-1}", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"n^{n-1}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"n^{n-1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"n^{n-1}").scale(1.1)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
