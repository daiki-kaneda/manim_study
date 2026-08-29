from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Multigrid(PacedScene):
    """#538 多グリッド：粗い格子で誤差を消す（約45秒）"""

    def construct(self):
        self.show_heading("多グリッド")
        self.draw_levels()
        self.v_cycle()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_levels(self):
        levels = VGroup(*[
            VGroup(*[Dot(LEFT * 2.5 + RIGHT * j * (3.0 / max(n - 1, 1)) + UP * (1.2 - i * 0.9), color=BLUE, radius=0.08) for j in range(n)])
            for i, n in enumerate([7, 4, 2])
        ])
        self.play(LaggedStart(*[FadeIn(lv) for lv in levels], lag_ratio=0.2), run_time=1.4)
        note = self.ja_text("細→粗", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def v_cycle(self):
        path = VMobject(color=ORANGE, stroke_width=4)
        path.set_points_as_corners([LEFT * 2.5 + UP * 1.2, LEFT * 0.5 + DOWN * 0.6, RIGHT * 2.5 + UP * 1.2])
        cap = self.ja_text("Vサイクル", font_size=24).move_to(self.note)
        self.play(Create(path), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("平滑化＋補正", font_size=24).move_to(self.note)
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
        formula = self.ja_text("多グリッド：粗い格子で長波長誤差を消す", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
