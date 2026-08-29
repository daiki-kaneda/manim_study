from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CMAES(PacedScene):
    """#501 CMA-ES：共分散を適応する進化戦略（約45秒）"""

    def construct(self):
        self.show_heading("CMA-ES")
        self.draw_cloud()
        self.adapt()
        self.show_formula()
        self.read(1.4)

    def draw_cloud(self):
        ell = Ellipse(width=3.2, height=1.6, color=BLUE, stroke_width=3).shift(LEFT * 1.5 + UP * 0.2)
        dots = VGroup(*[
            Dot(LEFT * 1.5 + RIGHT * (i % 3 - 1) * 0.55 + UP * (0.2 + (i // 3 - 1) * 0.4), color=YELLOW, radius=0.08)
            for i in range(9)
        ])
        self.play(Create(ell), FadeIn(dots), run_time=1.3)
        note = self.ja_text("正規分布サンプル", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.ell = ell

    def adapt(self):
        ell2 = Ellipse(width=2.0, height=2.4, color=ORANGE, stroke_width=3).shift(RIGHT * 1.8 + UP * 0.2)
        cap = self.ja_text("共分散を更新", font_size=24).move_to(self.note)
        self.play(Transform(self.ell, ell2), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("平均も移動", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x\sim\mathcal{N}(m_k,\sigma_k^2 C_k)").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
