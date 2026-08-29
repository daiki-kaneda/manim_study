from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Percolation(PacedScene):
    """#352 パーコレーション：開いた辺が巨大連結を作る（約45秒）"""

    def construct(self):
        self.show_heading("パーコレーション")
        self.draw_grid()
        self.open_edges()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_grid(self):
        self.dots = VGroup()
        for i in range(4):
            for j in range(3):
                self.dots.add(Dot(LEFT * 2.4 + RIGHT * i * 1.2 + UP * 1.0 + DOWN * j * 1.0, color=GREY, radius=0.08))
        self.play(LaggedStart(*[FadeIn(d) for d in self.dots], lag_ratio=0.03), run_time=1.2)
        note = self.ja_text("格子", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def open_edges(self):
        # open some edges forming a spanning path
        pairs = [(0, 1), (1, 2), (2, 5), (5, 6), (6, 9), (9, 10), (4, 5), (8, 9)]
        edges = VGroup()
        for a, b in pairs:
            edges.add(Line(self.dots[a].get_center(), self.dots[b].get_center(), color=ORANGE, stroke_width=4))
        cap = self.ja_text("開いた辺", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.08), Transform(self.note, cap), run_time=1.6)
        self.read(0.25)
        cap2 = self.ja_text("巨大連結", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(edges, color=YELLOW), run_time=1.1)
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
        formula = self.ja_text("臨界を超えると巨大連結", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
