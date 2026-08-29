from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HeartOfTStructure(PacedScene):
    """#740 t構造の心：導来圏からアーベル圏を切り出す（約45秒）"""

    def construct(self):
        self.show_heading("t構造の心")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        big = RoundedRectangle(width=5.5, height=2.2, corner_radius=0.12, color=BLUE, stroke_width=3).shift(UP * 0.15)
        heart = RoundedRectangle(width=2.4, height=1.2, corner_radius=0.1, color=ORANGE, stroke_width=3, fill_opacity=0.2).shift(UP * 0.15)
        self.play(Create(big), Create(heart),
                  FadeIn(MathTex(r"D", font_size=28).next_to(big, UL, buff=0.1)),
                  FadeIn(MathTex(r"\mathcal{A}", font_size=28).move_to(heart)), run_time=1.4)
        note = self.ja_text("t構造", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("心はアーベル", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("安定性の舞台", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathcal{A}=\mathrm{Heart}(D)").scale(0.8)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
