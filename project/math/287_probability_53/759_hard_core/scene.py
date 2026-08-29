from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HardCoreProcess(PacedScene):
    """#759 ハードコア過程：最小距離を強制する点過程（約45秒）"""

    def construct(self):
        self.show_heading("ハードコア過程")
        self.draw()
        self.mid()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        import random
        random.seed(8)
        pts = []
        for _ in range(40):
            x, y = random.uniform(-2.6, 2.6), random.uniform(-1.2, 1.2)
            if all((x - p[0]) ** 2 + (y - p[1]) ** 2 >= 0.55 ** 2 for p in pts):
                pts.append((x, y))
        dots = VGroup(*[Dot([x, y, 0], radius=0.08, color=BLUE) for x, y in pts])
        rings = VGroup(*[Circle(radius=0.28, color=ORANGE, stroke_width=1.5).move_to([x, y, 0]) for x, y in pts[:8]])
        self.play(FadeIn(dots), LaggedStart(*[Create(r) for r in rings], lag_ratio=0.05), run_time=1.5)
        note = self.ja_text("最小距離 R", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("禁制球", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("パッキング型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.75)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"P(\|X_i-X_j\|<R)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"P(\|X_i-X_j\|<R)=0").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"P(\|X_i-X_j\|<R)=0").scale(0.75)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
