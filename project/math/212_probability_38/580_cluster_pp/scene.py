from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ClusterPointProcess(PacedScene):
    """#580 クラスター点過程：親点が子点を生む（約45秒）"""

    def construct(self):
        self.show_heading("クラスター点過程")
        self.draw_parents()
        self.offspring()
        self.show_formula()
        self.read(1.4)

    def draw_parents(self):
        parents = VGroup(*[
            Dot(p, color=ORANGE, radius=0.14)
            for p in [LEFT * 2.5 + UP * 0.5, ORIGIN + UP * 0.8, RIGHT * 2.2 + UP * 0.3]
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in parents], lag_ratio=0.15), run_time=1.1)
        note = self.ja_text("親点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.parents = parents

    def offspring(self):
        kids = VGroup()
        for p in self.parents:
            for dx, dy in [(-0.4, -0.5), (0.35, -0.55), (0.05, -0.9)]:
                kids.add(Dot(p.get_center() + RIGHT * dx + UP * dy, color=BLUE, radius=0.08))
        cap = self.ja_text("子点が集まる", font_size=24).move_to(self.note)
        self.play(FadeIn(kids), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("ネイマン・スコット", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("親過程＋子孫核でクラスター", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
