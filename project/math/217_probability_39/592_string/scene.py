from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class StringProcess(PacedScene):
    """#592 ストリング過程：区間のランダムな並び（約45秒）"""

    def construct(self):
        self.show_heading("ストリング過程")
        self.draw_intervals()
        self.overlap()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_intervals(self):
        segs = VGroup(*[
            Line(LEFT * 3 + RIGHT * i * 0.3 + UP * (0.8 - j * 0.7),
                 LEFT * 1.5 + RIGHT * i * 0.3 + UP * (0.8 - j * 0.7),
                 color=c, stroke_width=8)
            for j, (i, c) in enumerate([(0, BLUE), (2, ORANGE), (1, TEAL), (3, YELLOW)])
        ])
        # simpler horizontal segments on a line
        line = NumberLine(x_range=[0, 6, 1], length=7, include_numbers=False).shift(UP * 0.2)
        bars = VGroup(
            Line(line.n2p(0.5), line.n2p(2.0), color=BLUE, stroke_width=10).shift(UP * 0.35),
            Line(line.n2p(1.5), line.n2p(3.5), color=ORANGE, stroke_width=10).shift(UP * 0.55),
            Line(line.n2p(3.0), line.n2p(5.2), color=TEAL, stroke_width=10).shift(UP * 0.35),
        )
        self.play(Create(line), LaggedStart(*[Create(b) for b in bars], lag_ratio=0.15), run_time=1.5)
        note = self.ja_text("区間の集まり", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def overlap(self):
        cap = self.ja_text("重なりを許す模型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("線分過程の一種", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("ストリング：ランダムな区間の点過程", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
