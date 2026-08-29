from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HolderInequality(PacedScene):
    """#258 ヘルダー：積の和はノルムの積以下（約45秒）"""

    def construct(self):
        self.show_heading("ヘルダーの不等式")
        self.draw_bars()
        self.compare()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_bars(self):
        self.a = VGroup()
        self.b = VGroup()
        heights_a = [1.6, 1.1, 0.7]
        heights_b = [0.9, 1.4, 1.2]
        for i, (ha, hb) in enumerate(zip(heights_a, heights_b)):
            ba = Rectangle(width=0.55, height=ha, color=BLUE, fill_opacity=0.55, stroke_width=2)
            bb = Rectangle(width=0.55, height=hb, color=TEAL, fill_opacity=0.55, stroke_width=2)
            ba.move_to(LEFT * 3.2 + RIGHT * i * 0.75 + UP * (ha / 2 - 0.8))
            bb.move_to(LEFT * 0.4 + RIGHT * i * 0.75 + UP * (hb / 2 - 0.8))
            self.a.add(ba)
            self.b.add(bb)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.2) for x in self.a], lag_ratio=0.1), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.2) for x in self.b], lag_ratio=0.1), run_time=1.2)
        note = self.ja_text("2 つの列", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compare(self):
        # product bars
        prods = VGroup()
        for i, (ba, bb) in enumerate(zip(self.a, self.b)):
            h = 0.55 * ba.height * bb.height
            p = Rectangle(width=0.55, height=h, color=ORANGE, fill_opacity=0.6, stroke_width=2)
            p.move_to(RIGHT * 2.2 + RIGHT * i * 0.75 + UP * (h / 2 - 0.8))
            prods.add(p)
        cap = self.ja_text("項ごとの積", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(p) for p in prods], lag_ratio=0.12), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("ノルムで押さえる", font_size=24).move_to(self.note)
        box = SurroundingRectangle(prods, color=YELLOW, buff=0.15)
        self.play(Create(box), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"\sum|a_ib_i|\le\|a\|_p\|b\|_q").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sum|a_ib_i|\le\|a\|_p\|b\|_q").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sum|a_ib_i|\le\|a\|_p\|b\|_q").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
