from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ChapmanKolmogorov(PacedScene):
    """#339 チャップマン・コロモゴロフ：遷移の合成（約45秒）"""

    def construct(self):
        self.show_heading("チャップマン・コロモゴロフ")
        self.draw_states()
        self.compose()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_states(self):
        self.nodes = VGroup()
        labels = ["i", "k", "j"]
        positions = [LEFT * 3.0 + UP * 0.3, ORIGIN + UP * 0.3, RIGHT * 3.0 + UP * 0.3]
        for lab, pos in zip(labels, positions):
            c = Circle(radius=0.45, color=BLUE, stroke_width=3).move_to(pos)
            t = MathTex(lab, font_size=34).move_to(pos)
            self.nodes.add(VGroup(c, t))
        self.play(LaggedStart(*[FadeIn(n) for n in self.nodes], lag_ratio=0.15), run_time=1.3)
        note = self.ja_text("状態", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compose(self):
        a1 = Arrow(self.nodes[0].get_right(), self.nodes[1].get_left(), buff=0.08, color=ORANGE, stroke_width=4)
        a2 = Arrow(self.nodes[1].get_right(), self.nodes[2].get_left(), buff=0.08, color=ORANGE, stroke_width=4)
        a3 = ArcBetweenPoints(self.nodes[0].get_top() + UP * 0.05, self.nodes[2].get_top() + UP * 0.05, angle=-0.8, color=YELLOW, stroke_width=4)
        cap = self.ja_text("経由して行く", font_size=24).move_to(self.note)
        self.play(GrowArrow(a1), GrowArrow(a2), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("合成が直通", font_size=24).move_to(self.note)
        self.play(Create(a3), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"p_{ij}(s+t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"p_{ij}(s+t)=\sum_k p_{ik}(s)p_{kj}(t)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"p_{ij}(s+t)=\sum_k p_{ik}(s)p_{kj}(t)").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
