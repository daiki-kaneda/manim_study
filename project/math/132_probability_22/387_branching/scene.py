from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BranchingProcess(PacedScene):
    """#387 分岐過程：各個体が独立に子を生む（約45秒）"""

    def construct(self):
        self.show_heading("分岐過程")
        self.draw_tree()
        self.extinction()
        self.show_formula()
        self.read(1.4)

    def draw_tree(self):
        # generation 0
        root = Dot(UP * 1.8, color=BLUE, radius=0.12)
        # gen 1
        g1 = VGroup(*[Dot(UP * 0.7 + RIGHT * x, color=TEAL, radius=0.1) for x in [-1.6, 0.0, 1.6]])
        e1 = VGroup(*[Line(root.get_center(), d.get_center(), color=GREY, stroke_width=2) for d in g1])
        # gen 2 (some branches)
        g2_pos = [-2.2, -1.2, -0.3, 0.3, 1.4, 2.2]
        g2 = VGroup(*[Dot(DOWN * 0.5 + RIGHT * x, color=ORANGE, radius=0.09) for x in g2_pos])
        parents = [0, 0, 1, 1, 2, 2]
        e2 = VGroup(*[
            Line(g1[p].get_center(), g2[i].get_center(), color=GREY, stroke_width=2)
            for i, p in enumerate(parents)
        ])
        self.play(FadeIn(root, scale=0.5), run_time=0.6)
        self.play(LaggedStart(*[Create(e) for e in e1], lag_ratio=0.1), FadeIn(g1), run_time=1.2)
        note = self.ja_text("世代ごと増殖", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.play(LaggedStart(*[Create(e) for e in e2], lag_ratio=0.08), FadeIn(g2), run_time=1.3)
        self.read(0.3)
        self.note = note
        self.root = root

    def extinction(self):
        # fade some leaves to suggest extinction risk
        fade_box = SurroundingRectangle(
            VGroup(*[Dot(DOWN * 0.5 + RIGHT * x, radius=0.01) for x in [-2.2, -1.2]]),
            color=RED, buff=0.35,
        )
        fade_box.set_opacity(0)
        cap = self.ja_text("絶滅の確率", font_size=24).move_to(self.note)
        cross = MathTex(r"\eta", color=RED, font_size=48).next_to(self.root, LEFT, buff=0.5)
        self.play(Transform(self.note, cap), FadeIn(cross), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("平均で決まる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\eta=f(\eta),\quad f(s)=\mathbb{E}[s^{X}]").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
