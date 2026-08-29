from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class GibbsProcess(PacedScene):
    """#591 ギッブス過程：エネルギーで点配置を決める（約45秒）"""

    def construct(self):
        self.show_heading("ギッブス過程")
        self.draw_config()
        self.energy()
        self.show_formula()
        self.read(1.4)

    def draw_config(self):
        dots = VGroup(*[
            Dot(LEFT * 2.2 + RIGHT * (i % 4) * 1.1 + UP * (0.9 - (i // 4) * 1.1), color=BLUE, radius=0.11)
            for i in range(8)
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.05), run_time=1.3)
        note = self.ja_text("点配置", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def energy(self):
        cap = self.ja_text("相互作用エネルギー", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("密度が e^{-U}", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"p(x)\propto e^{-U(x)}\,\lambda(dx)").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
