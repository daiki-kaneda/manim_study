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
        self.derive()
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

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"x\sim\mathcal{N}(m_k,\sigma_k^2 C_k)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x\sim\mathcal{N}(m_k,\sigma_k^2 C_k)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x\sim\mathcal{N}(m_k,\sigma_k^2 C_k)").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
